#!/usr/bin/env python3
"""Verify live HTTP MCP audit logging without printing credentials or business data."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any


def _active_token(tokens_file: Path, role: str) -> str:
    payload = json.loads(tokens_file.read_text(encoding="utf-8"))
    for item in payload.get("tokens") or []:
        if item.get("role") == role and item.get("status") == "active" and item.get("token"):
            return str(item["token"])
    raise RuntimeError(f"没有找到有效的 {role} 成员令牌")


def _call(url: str, token: str, payload: dict[str, Any]) -> tuple[int, str, dict[str, Any], int]:
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    for attempt in range(20):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                raw = response.read()
                return (
                    response.status,
                    str(response.headers.get("X-Mcp-Audit-Id") or ""),
                    json.loads(raw),
                    len(raw),
                )
        except urllib.error.URLError:
            if attempt == 19:
                raise
            time.sleep(0.5)
    raise RuntimeError("MCP 服务未就绪")


def _recent_events(namespace: str, service: str, audit_ids: set[str]) -> list[dict[str, Any]]:
    output = subprocess.check_output(
        [
            "journalctl",
            f"--namespace={namespace}",
            "-u",
            service,
            "--since",
            "5 minutes ago",
            "-o",
            "cat",
            "--no-pager",
        ],
        text=True,
    )
    events: list[dict[str, Any]] = []
    for line in output.splitlines():
        if '"event":"mcp_audit"' not in line:
            continue
        event = json.loads(line)
        if event.get("audit_id") in audit_ids:
            events.append(event)
    return events


def main() -> int:
    parser = argparse.ArgumentParser(description="验证 MCP 审计日志，不输出令牌、参数值或业务响应。")
    parser.add_argument("--url", default="http://127.0.0.1:8099/mcp")
    parser.add_argument("--tokens-file", type=Path, default=Path("/etc/lingxing-mcp/tokens.json"))
    parser.add_argument("--role", default="operations")
    parser.add_argument("--namespace", default="lingxing-mcp")
    parser.add_argument("--service", default="lingxing-mcp.service")
    parser.add_argument("--expected-tool-count", type=int)
    args = parser.parse_args()

    token = _active_token(args.tokens_file, args.role)
    list_status, list_audit, list_payload, list_bytes = _call(
        args.url,
        token,
        {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
    )
    call_status, call_audit, call_payload, call_bytes = _call(
        args.url,
        token,
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": "lingxing_rate_limit_policy",
                "arguments": {"tool_name": "lingxing_health_check"},
            },
        },
    )
    time.sleep(0.5)
    events = _recent_events(args.namespace, args.service, {list_audit, call_audit})
    tool_count = len(list_payload["result"]["tools"])

    if list_status != 200 or call_status != 200:
        raise RuntimeError("MCP HTTP 验证失败")
    if args.expected_tool_count is not None and tool_count != args.expected_tool_count:
        raise RuntimeError(f"工具数量不匹配: {tool_count} != {args.expected_tool_count}")
    if not call_payload["result"]["structuredContent"]["ok"]:
        raise RuntimeError("本地限流策略工具调用失败")
    if len(events) != 2 or any(event.get("outcome") != "ok" for event in events):
        raise RuntimeError("没有找到两条成功的审计事件")

    safe_fields = (
        "event",
        "audit_id",
        "auth_mode",
        "token_id",
        "role",
        "mcp_method",
        "tool",
        "argument_key_count",
        "argument_keys",
        "outcome",
        "http_status",
        "duration_ms",
        "request_bytes",
        "response_bytes",
        "tool_count",
    )
    safe_events = [{key: event[key] for key in safe_fields if key in event} for event in events]
    print(
        json.dumps(
            {
                "ok": True,
                "tools_list": {
                    "status": list_status,
                    "audit_id": list_audit,
                    "tool_count": tool_count,
                    "response_bytes": list_bytes,
                },
                "tools_call": {
                    "status": call_status,
                    "audit_id": call_audit,
                    "response_bytes": call_bytes,
                },
                "audit_events": safe_events,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
