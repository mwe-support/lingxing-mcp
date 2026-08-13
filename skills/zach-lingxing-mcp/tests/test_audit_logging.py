from __future__ import annotations

import io
import json
import sys
import threading
import unittest
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.audit import MCPAuditLogger, build_audit_event  # noqa: E402
from lib.lingxing_openapi.auth import AuthMatch  # noqa: E402
from lib.lingxing_openapi.mcp import create_http_server  # noqa: E402


class LingxingMCPAuditTests(unittest.TestCase):
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
