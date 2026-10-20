from __future__ import annotations

import http.client
import io
import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.audit import MCPAuditLogger  # noqa: E402
from lib.lingxing_openapi.auth import load_bearer_auth_config  # noqa: E402
from lib.lingxing_openapi.mcp import LingxingMCPApplication, create_http_server, process_http_request  # noqa: E402


HEADER_NAMES = ("Authorization", "authorization", "AUTHORIZATION", "aUtHoRiZaTiOn")


class LingxingHTTPHeaderCaseTests(unittest.TestCase):
    def test_bootstrap_auth_is_case_insensitive_for_get_and_post(self) -> None:
        app = LingxingMCPApplication()
        auth = load_bearer_auth_config(bootstrap_token="case-test-bootstrap")
        body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize"}).encode()
        for header in HEADER_NAMES:
            for method in ("GET", "POST"):
                for token, expected_status in (("case-test-bootstrap", 200), ("invalid", 401)):
                    with self.subTest(header=header, method=method, expected_status=expected_status):
                        status, _ = process_http_request(
                            app, auth=auth, method=method, path="/mcp",
                            headers={header: f"Bearer {token}"}, body=body,
                        )
                        self.assertEqual(status, expected_status)

    def test_member_auth_preserves_permissions_and_audit_identity_over_http(self) -> None:
        stream = io.StringIO()
        logger = MCPAuditLogger(enabled=True, stream=stream)
        audit_ready = threading.Event()
        original_emit = logger.emit

        def emit(event):
            result = original_emit(event)
            audit_ready.set()
            return result

        with tempfile.TemporaryDirectory() as temp_dir:
            tokens_file = Path(temp_dir) / "tokens.json"
            tokens_file.write_text(json.dumps({"version": 1, "tokens": [
                {"id": "member", "token": "case-test-member", "status": "active", "role": "minimal"},
                {"id": "revoked", "token": "case-test-revoked", "status": "revoked", "role": "minimal"},
            ]}), encoding="utf-8")
            app = LingxingMCPApplication()
            auth = load_bearer_auth_config(tokens_file=str(tokens_file))
            match = auth.authenticate_header("Bearer case-test-member")
            expected_tools = {tool["name"] for tool in app.list_tools(match)}
            server = create_http_server(
                "127.0.0.1", 0, tokens_file=str(tokens_file), app=app, audit_logger=logger,
            )
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}).encode()
            with patch.object(logger, "emit", side_effect=emit):
                thread.start()
                try:
                    for header in HEADER_NAMES:
                        for token, expected_status in (
                            ("case-test-member", 200), ("case-test-revoked", 401), (None, 401),
                        ):
                            with self.subTest(header=header, expected_status=expected_status, missing=token is None):
                                audit_ready.clear()
                                headers = {header: f"Bearer {token}"} if token is not None else {}
                                connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
                                try:
                                    connection.request("POST", "/mcp", body, headers=headers)
                                    response = connection.getresponse()
                                    payload = json.loads(response.read())
                                    audit_id = response.getheader("X-Mcp-Audit-Id")
                                finally:
                                    connection.close()
                                self.assertTrue(audit_ready.wait(5))
                                event = json.loads(stream.getvalue().splitlines()[-1])
                                self.assertEqual(response.status, expected_status)
                                self.assertEqual(event["audit_id"], audit_id)
                                self.assertEqual(event["http_status"], expected_status)
                                if expected_status == 200:
                                    self.assertEqual({tool["name"] for tool in payload["result"]["tools"]}, expected_tools)
                                    self.assertEqual(event["token_id"], "member")
                                    self.assertEqual(event["role"], "minimal")
                                    self.assertEqual(event["mcp_method"], "tools/list")
                                else:
                                    self.assertEqual(payload["error"], "missing_or_invalid_bearer")
                                    self.assertIsNone(event["token_id"])
                                    self.assertEqual(event["mcp_method"], "unauthenticated")
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=5)
        self.assertEqual(len(stream.getvalue().splitlines()), 12)
        self.assertNotIn("case-test-member", stream.getvalue())
        self.assertNotIn("case-test-revoked", stream.getvalue())

    def test_duplicate_authorization_headers_are_rejected_for_get_and_post(self) -> None:
        stream = io.StringIO()
        logger = MCPAuditLogger(enabled=True, stream=stream)
        audit_ready = threading.Event()
        original_emit = logger.emit

        def emit(event):
            result = original_emit(event)
            audit_ready.set()
            return result

        with tempfile.TemporaryDirectory() as temp_dir:
            tokens_file = Path(temp_dir) / "tokens.json"
            tokens_file.write_text(json.dumps({"version": 1, "tokens": [
                {"id": "member", "token": "case-test-member", "status": "active", "role": "operations"},
            ]}), encoding="utf-8")
            server = create_http_server(
                "127.0.0.1", 0, tokens_file=str(tokens_file),
                audit_logger=logger,
            )
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            with patch.object(logger, "emit", side_effect=emit):
                thread.start()
                try:
                    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/list"}).encode()
                    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
                    connection.putrequest("POST", "/mcp")
                    connection.putheader("Authorization", "Bearer invalid-first")
                    connection.putheader("authorization", "Bearer case-test-member")
                    connection.putheader("Content-Type", "application/json")
                    connection.putheader("Content-Length", str(len(body)))
                    connection.endheaders(body)
                    response = connection.getresponse()
                    payload = json.loads(response.read())
                    connection.close()

                    self.assertTrue(audit_ready.wait(5))
                    event = json.loads(stream.getvalue().strip())
                    self.assertEqual(response.status, 400)
                    self.assertEqual(payload["error"], "multiple_authorization_headers")
                    self.assertIsNone(event["token_id"])
                    self.assertIsNone(event["role"])
                    self.assertEqual(event["mcp_method"], "unauthenticated")
                    self.assertEqual(event["error_code"], "multiple_authorization_headers")

                    audit_ready.clear()
                    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
                    connection.putrequest("POST", "/mcp")
                    connection.putheader("Authorization", "Bearer invalid-first")
                    connection.putheader("authorization", "Bearer case-test-member")
                    connection.putheader("Content-Length", "99999999")
                    connection.endheaders()
                    response = connection.getresponse()
                    payload = json.loads(response.read())
                    connection.close()
                    self.assertEqual(response.status, 400)
                    self.assertEqual(payload["error"], "multiple_authorization_headers")
                    self.assertTrue(audit_ready.wait(5))
                    event = json.loads(stream.getvalue().splitlines()[-1])
                    self.assertEqual(event["error_code"], "multiple_authorization_headers")

                    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
                    connection.putrequest("GET", "/mcp")
                    connection.putheader("Authorization", "Bearer invalid-first")
                    connection.putheader("authorization", "Bearer case-test-member")
                    connection.endheaders()
                    response = connection.getresponse()
                    payload = json.loads(response.read())
                    connection.close()
                    self.assertEqual(response.status, 400)
                    self.assertEqual(payload["error"], "multiple_authorization_headers")
                finally:
                    server.shutdown()
                    server.server_close()
                    thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
