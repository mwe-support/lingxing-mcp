from __future__ import annotations

import io
import http.client
import json
import sys
import threading
import unittest
import urllib.error
import urllib.request
from contextlib import redirect_stderr
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.audit import MCPAuditLogger, build_audit_event, should_emit_audit_event  # noqa: E402
from lib.lingxing_openapi.auth import AuthMatch  # noqa: E402
from lib.lingxing_openapi.mcp import LingxingMCPApplication, _send_json_response, create_http_server  # noqa: E402


class LingxingMCPAuditTests(unittest.TestCase):
    def test_successful_routine_messages_are_suppressed_but_errors_are_not(self) -> None:
        routine = {"mcp_method": "ping", "outcome": "ok"}
        failed = {"mcp_method": "ping", "outcome": "client_disconnected"}

        self.assertFalse(should_emit_audit_event(routine))
        self.assertTrue(should_emit_audit_event(failed))

    def test_send_json_response_handles_broken_pipe(self) -> None:
        class BrokenWriter:
            def write(self, body: bytes) -> None:
                raise BrokenPipeError(32, "broken pipe")

        class FakeHandler:
            wfile = BrokenWriter()

            def send_response(self, status: int) -> None:
                return None

            def send_header(self, name: str, value: str) -> None:
                return None

            def _send_cors_headers(self) -> None:
                return None

            def end_headers(self) -> None:
                return None

        status, payload, response_bytes, delivered = _send_json_response(
            FakeHandler(), 200, {"ok": True}, audit_id="audit-broken"
        )

        self.assertEqual(status, 200)
        self.assertEqual(payload, {"ok": True})
        self.assertGreater(response_bytes, 0)
        self.assertFalse(delivered)

    def test_malformed_request_gets_audit_id_and_event(self) -> None:
        stream = io.StringIO()
        server = create_http_server(
            "127.0.0.1",
            0,
            bearer_token="unit-test-token",
            audit_logger=MCPAuditLogger(enabled=True, stream=stream),
        )
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
            connection.putrequest("POST", "/mcp")
            connection.putheader("Authorization", "Bearer unit-test-token")
            connection.putheader("Content-Length", "invalid")
            connection.endheaders()
            response = connection.getresponse()
            response.read()
            audit_id = response.getheader("X-Mcp-Audit-Id")
            connection.close()

            event = json.loads(stream.getvalue().strip())
            self.assertEqual(response.status, 400)
            self.assertEqual(event["audit_id"], audit_id)
            self.assertEqual(event["error_code"], "invalid_content_length")
            self.assertEqual(event["outcome"], "http_error")
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

    def test_dispatch_exception_still_gets_audited(self) -> None:
        class BrokenApp(LingxingMCPApplication):
            def dispatch(self, request, auth_match=None):
                raise RuntimeError("must not leak")

        stream = io.StringIO()
        server = create_http_server(
            "127.0.0.1",
            0,
            bearer_token="unit-test-token",
            app=BrokenApp(),
            audit_logger=MCPAuditLogger(enabled=True, stream=stream),
        )
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}).encode()
            request = urllib.request.Request(
                f"http://127.0.0.1:{server.server_port}/mcp",
                data=body,
                headers={"Authorization": "Bearer unit-test-token", "Content-Type": "application/json"},
            )
            with self.assertRaises(urllib.error.HTTPError) as caught:
                urllib.request.urlopen(request, timeout=5)
            caught.exception.read()
            event = json.loads(stream.getvalue().strip())

            self.assertEqual(caught.exception.code, 500)
            self.assertEqual(event["error_code"], "internal_server_error")
            self.assertNotIn("must not leak", stream.getvalue())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

    def test_audit_event_keeps_metadata_without_argument_values(self) -> None:
        body = json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": "lingxing_sales_outbound_orders",
                    "arguments": {
                        "sids": [7787, 7789],
                        "search_value": "DO-NOT-LOG-THIS",
                        "dry_run": True,
                        "response_mode": "full",
                    },
                },
            }
        ).encode()
        payload = {
            "result": {
                "structuredContent": {
                    "ok": True,
                    "data": {"record_count": 123, "returned_count": 123},
                }
            }
        }

        event = build_audit_event(
            audit_id="audit-1",
            auth_match=AuthMatch(mode="multi", token_id="mark", description="Mark", role="operations"),
            body=body,
            status=200,
            payload=payload,
            duration_ms=12.34,
            response_bytes=456,
            delivered=True,
        )

        serialized = json.dumps(event, ensure_ascii=False)
        self.assertNotIn("DO-NOT-LOG-THIS", serialized)
        self.assertNotIn("7787", serialized)
        self.assertEqual(event["tool"], "lingxing_sales_outbound_orders")
        self.assertEqual(event["argument_key_count"], 4)
        self.assertEqual(event["list_argument_sizes"], {"sids": 2})
        self.assertTrue(event["dry_run"])
        self.assertEqual(event["response_mode"], "full")
        self.assertEqual(event["record_count"], 123)
        self.assertEqual(event["outcome"], "ok")

    def test_client_disconnect_overrides_response_outcome(self) -> None:
        event = build_audit_event(
            audit_id="audit-2",
            auth_match=None,
            body=b'{"method":"tools/list"}',
            status=200,
            payload={"result": {"tools": []}},
            duration_ms=5,
            response_bytes=10,
            delivered=False,
        )

        self.assertEqual(event["outcome"], "client_disconnected")

    def test_unauthenticated_request_body_does_not_supply_audit_metadata(self) -> None:
        body = b'{"method":"attackerMethod","params":{"name":"attackerTool","arguments":{"secretKey":"value"}}}'
        event = build_audit_event(
            audit_id="audit-unauthenticated",
            auth_match=None,
            body=body,
            status=401,
            payload={"error": "unauthorized"},
            duration_ms=1,
            response_bytes=10,
            delivered=True,
        )

        serialized = json.dumps(event)
        self.assertEqual(event["mcp_method"], "unauthenticated")
        self.assertNotIn("attackerMethod", serialized)
        self.assertNotIn("attackerTool", serialized)
        self.assertNotIn("secretKey", serialized)

    def test_failed_primary_audit_write_emits_metadata_only_health_event(self) -> None:
        class FailingStream:
            def write(self, value: str) -> None:
                raise OSError("audit stream unavailable")

            def flush(self) -> None:
                return None

        server = create_http_server(
            "127.0.0.1",
            0,
            bearer_token="unit-test-token",
            audit_logger=MCPAuditLogger(enabled=True, stream=FailingStream()),
        )
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        fallback = io.StringIO()
        try:
            body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}).encode()
            request = urllib.request.Request(
                f"http://127.0.0.1:{server.server_port}/mcp",
                data=body,
                headers={"Authorization": "Bearer unit-test-token", "Content-Type": "application/json"},
            )
            with redirect_stderr(fallback):
                with urllib.request.urlopen(request, timeout=5) as response:
                    response.read()
                    audit_id = response.headers.get("X-Mcp-Audit-Id")

            event = json.loads(fallback.getvalue().strip())
            self.assertEqual(event["event"], "mcp_audit_write_failed")
            self.assertEqual(event["audit_id"], audit_id)
            self.assertNotIn("unit-test-token", fallback.getvalue())
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

    def test_http_request_gets_audit_header_and_one_compact_log_line(self) -> None:
        stream = io.StringIO()
        logger = MCPAuditLogger(enabled=True, stream=stream)
        server = create_http_server(
            "127.0.0.1",
            0,
            bearer_token="unit-test-token",
            audit_logger=logger,
        )
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}).encode()
            request = urllib.request.Request(
                f"http://127.0.0.1:{server.server_port}/mcp",
                data=body,
                headers={"Authorization": "Bearer unit-test-token", "Content-Type": "application/json"},
            )
            with urllib.request.urlopen(request, timeout=5) as response:
                response.read()
                audit_id = response.headers.get("X-Mcp-Audit-Id")
            event = json.loads(stream.getvalue().strip())

            self.assertEqual(event["audit_id"], audit_id)
            self.assertEqual(event["mcp_method"], "tools/list")
            self.assertEqual(event["token_id"], "bootstrap")
            self.assertEqual(event["outcome"], "ok")
            self.assertGreater(event["tool_count"], 0)
            self.assertNotIn("unit-test-token", stream.getvalue())
            self.assertEqual(len(stream.getvalue().splitlines()), 1)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
