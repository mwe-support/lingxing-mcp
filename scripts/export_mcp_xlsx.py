#!/usr/bin/env python3
"""Call one Lingxing MCP report tool and write its full result to XLSX."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tomllib
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.xlsx_export import write_records_xlsx  # noqa: E402


SUPPORTED_TOOLS = {
    "lingxing_shipment_settlement_report": "shipment_settlement",
    "lingxing_profit_report_order_list": "profit_report_order_transaction",
    "lingxing_sales_outbound_orders": "sales_outbound_orders",
}
RESERVED_ARGUMENTS = {"start_date", "end_date", "response_mode", "sids", "amazon_seller_ids"}


def _load_codex_server(config_path: Path, server_name: str) -> tuple[str, dict[str, str]]:
    if not config_path.exists():
        return "", {}
    with config_path.open("rb") as stream:
        config = tomllib.load(stream)
    server = (config.get("mcp_servers") or {}).get(server_name) or {}
    url = str(server.get("url") or "").strip()
    headers = {
        str(key): str(value)
        for source_name in ("http_headers", "headers")
        for key, value in (server.get(source_name) or {}).items()
    }
    return url, headers


def _connection(args: argparse.Namespace) -> tuple[str, dict[str, str]]:
    config_url, headers = _load_codex_server(args.codex_config, args.mcp_server)
    url = str(args.url or os.getenv("LINGXING_MCP_URL") or config_url).strip()
    if not url:
        raise RuntimeError("缺少 MCP URL；请设置 LINGXING_MCP_URL 或配置 Codex MCP server URL")
    bearer = os.getenv("LINGXING_MCP_BEARER_TOKEN", "").strip()
    mcp_key = os.getenv("LINGXING_MCP_KEY", "").strip()
    if bearer:
        headers["Authorization"] = f"Bearer {bearer}"
    if mcp_key:
        headers["X-Mcp-Key"] = mcp_key
    headers["Accept"] = "application/json, text/event-stream"
    headers["Content-Type"] = "application/json"
    headers.setdefault("User-Agent", "Codex-Lingxing-MCP-Exporter/1.0")
    return url, headers


def _call_tool(url: str, headers: dict[str, str], tool_name: str, arguments: dict[str, Any]) -> dict[str, Any]:
    request_body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments},
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(url, data=request_body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read(500).decode("utf-8", errors="replace")
        raise RuntimeError(f"MCP HTTP {exc.code}: {detail}") from exc
    if payload.get("error"):
        raise RuntimeError(str(payload["error"]))
    result = payload.get("result") or {}
    structured = result.get("structuredContent") or {}
    if result.get("isError") or not structured.get("ok"):
        raise RuntimeError(json.dumps(structured.get("error") or structured, ensure_ascii=False))
    return structured


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="通过 MCP 一次调用导出领星报表为 XLSX，不向终端输出明细 JSON。")
    parser.add_argument("--tool", required=True, choices=sorted(SUPPORTED_TOOLS))
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--sid", type=int, action="append", dest="sids")
    parser.add_argument("--seller-id", action="append", dest="seller_ids")
    parser.add_argument("--arguments-json", default="{}", help="附加工具参数 JSON；不能覆盖日期和 response_mode。")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--url")
    parser.add_argument("--mcp-server", default="lingxing_mcp")
    parser.add_argument(
        "--codex-config",
        type=Path,
        default=Path.home() / ".codex" / "config.toml",
    )
    return parser


def _build_arguments(args: argparse.Namespace, extra: dict[str, Any]) -> dict[str, Any]:
    reserved = sorted(RESERVED_ARGUMENTS.intersection(extra))
    if reserved:
        raise RuntimeError(f"--arguments-json 不能包含保留参数: {', '.join(reserved)}")
    arguments = dict(extra)
    arguments.update(
        {
            "start_date": args.start_date,
            "end_date": args.end_date,
            "response_mode": "full",
        }
    )
    if args.sids:
        arguments["sids"] = args.sids
    if args.seller_ids:
        if args.tool == "lingxing_profit_report_order_list":
            raise RuntimeError("利润报表 Transaction 接口仅支持 --sid，不支持 --seller-id")
        arguments["amazon_seller_ids"] = args.seller_ids
    return arguments


def main() -> int:
    args = _parser().parse_args()
    extra = json.loads(args.arguments_json)
    if not isinstance(extra, dict):
        raise RuntimeError("--arguments-json 必须是 JSON 对象")
    arguments = _build_arguments(args, extra)

    url, headers = _connection(args)
    result = _call_tool(url, headers, args.tool, arguments)
    data = result.get("data") or {}
    records = data.get("records") or []
    if data.get("truncated") or int(data.get("returned_count") or 0) != int(data.get("record_count") or 0):
        raise RuntimeError("MCP 未返回完整记录，已拒绝生成不完整 Excel")

    output = args.output
    if output is None:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output = Path.cwd() / f"{args.tool}-{args.start_date}-{args.end_date}-{stamp}.xlsx"
    summary = write_records_xlsx(records, output, profile=SUPPORTED_TOOLS[args.tool])
    summary.update(
        {
            "ok": True,
            "tool": args.tool,
            "store_scope": (result.get("meta") or {}).get("store_scope"),
            "page_count": (result.get("meta") or {}).get("page_count"),
        }
    )
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
