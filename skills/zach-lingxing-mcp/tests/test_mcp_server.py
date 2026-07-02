from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.auth import load_bearer_auth_config  # noqa: E402
from lib.lingxing_openapi.mcp import LingxingMCPApplication, process_http_request  # noqa: E402


STDIO_SERVER = ROOT / "mcp-servers" / "lingxing-openapi" / "server.py"


def _read_message(stream) -> dict:
    headers = {}
    while True:
        line = stream.readline()
        if not line:
            raise EOFError("server closed stdout")
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()
    length = int(headers.get("content-length", "0"))
    body = stream.read(length)
    return json.loads(body.decode("utf-8"))


def _write_message(stream, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\nContent-Type: application/json\r\n\r\n".encode("ascii")
    stream.write(header)
    stream.write(body)
    stream.flush()


class LingxingMCPTests(unittest.TestCase):
    def test_stdio_can_list_tools_and_call_health_check(self) -> None:
        process = subprocess.Popen(
            [sys.executable, str(STDIO_SERVER)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert process.stdin is not None
        assert process.stdout is not None
        try:
            _write_message(
                process.stdin,
                {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}},
            )
            init = _read_message(process.stdout)
            self.assertEqual(init["result"]["serverInfo"]["name"], "lingxing-openapi")

            _write_message(process.stdin, {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
            tools = _read_message(process.stdout)
            tool_names = {item["name"] for item in tools["result"]["tools"]}
            self.assertIn("lingxing_health_check", tool_names)
            self.assertIn("lingxing_amazon_listing", tool_names)

            _write_message(
                process.stdin,
                {
                    "jsonrpc": "2.0",
                    "id": 3,
                    "method": "tools/call",
                    "params": {"name": "lingxing_health_check", "arguments": {}},
                },
            )
            health = _read_message(process.stdout)
            structured = health["result"]["structuredContent"]
            self.assertIn("ok", structured)
            self.assertIn("data", structured)
            self.assertIn("meta", structured)
            self.assertIn("warnings", structured)
        finally:
            process.stdin.close()
            process.terminate()
            process.wait(timeout=5)
            if process.stdout is not None:
                process.stdout.close()
            if process.stderr is not None:
                process.stderr.close()

    def test_http_rejects_missing_bearer_and_accepts_authorized_call(self) -> None:
        app = LingxingMCPApplication()
        auth = load_bearer_auth_config(bootstrap_token="unit-test-token")
        status, payload = process_http_request(
            app,
            auth=auth,
            method="GET",
            path="/mcp",
            headers={},
        )
        self.assertEqual(status, 401)
        self.assertEqual(payload["error"], "missing_or_invalid_bearer")

        status, payload = process_http_request(
            app,
            auth=auth,
            method="POST",
            path="/mcp",
            headers={"Authorization": "Bearer unit-test-token"},
            body=json.dumps(
                {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "lingxing_health_check", "arguments": {}}}
            ).encode("utf-8"),
        )
        self.assertEqual(status, 200)
        structured = payload["result"]["structuredContent"]
        self.assertIn("ok", structured)
        self.assertEqual(structured["meta"]["endpoint"], "/api/auth-server/oauth/access-token")

    def test_http_accepts_member_token_from_tokens_file(self) -> None:
        app = LingxingMCPApplication()
        with tempfile.TemporaryDirectory() as temp_dir:
            tokens_file = Path(temp_dir) / "tokens.json"
            tokens_file.write_text(
                json.dumps(
                    {
                        "version": 1,
                        "tokens": [
                            {"id": "alice", "description": "Alice", "token": "alice-token", "status": "active"},
                            {"id": "bob", "description": "Bob", "token": "bob-token", "status": "revoked"},
                        ],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            auth = load_bearer_auth_config(tokens_file=str(tokens_file))
            ok_status, ok_payload = process_http_request(
                app,
                auth=auth,
                method="GET",
                path="/mcp",
                headers={"Authorization": "Bearer alice-token"},
            )
            self.assertEqual(ok_status, 200)
            self.assertEqual(ok_payload["auth"]["token_id"], "alice")

            denied_status, denied_payload = process_http_request(
                app,
                auth=auth,
                method="GET",
                path="/mcp",
                headers={"Authorization": "Bearer bob-token"},
            )
            self.assertEqual(denied_status, 401)
            self.assertEqual(denied_payload["error"], "missing_or_invalid_bearer")


if __name__ == "__main__":
    unittest.main()
