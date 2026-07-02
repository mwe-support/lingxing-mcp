#!/usr/bin/env python3
"""Validate Lingxing MCP role-based tool visibility without calling Lingxing APIs."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.auth import AuthMatch  # noqa: E402
from lib.lingxing_openapi.mcp import LingxingMCPApplication  # noqa: E402

BASE_TOOLS = {"lingxing_health_check", "lingxing_smoke_check", "lingxing_rate_limit_policy"}
EXPECTED_MINIMAL = BASE_TOOLS | {
    "lingxing_seller_lists",
    "lingxing_marketplaces",
    "lingxing_order_details",
    "lingxing_order_lists",
    "lingxing_asin_product_snapshot",
    "lingxing_fba_warehouse_detail",
    "lingxing_amazon_listing",
    "lingxing_local_product_costs",
    "lingxing_product_performance",
    "lingxing_finance_report_asin",
}
EXPECTED_OPERATIONS = BASE_TOOLS | {
    "lingxing_seller_lists",
    "lingxing_marketplaces",
    "lingxing_order_details",
    "lingxing_order_lists",
    "lingxing_asin_product_snapshot",
    "lingxing_fba_warehouse_detail",
    "lingxing_local_product_costs",
    "lingxing_product_performance",
    "lingxing_profit_report_order_list",
    "lingxing_multi_channel_orders",
}
EXPECTED_FINANCE = BASE_TOOLS | {
    "lingxing_store_sales",
    "lingxing_profit_seller",
    "lingxing_profit_asin",
    "lingxing_finance_report_asin",
    "lingxing_local_product_costs",
    "lingxing_fba_stock_aggregate",
    "lingxing_exp_finance_report_seller",
    "lingxing_seller_lists",
    "lingxing_order_details",
    "lingxing_fba_warehouse_detail",
    "lingxing_fba_stock_detail",
    "lingxing_source_transaction",
}


def tool_names(app: LingxingMCPApplication, role: str | None) -> set[str]:
    match = AuthMatch(mode="test", token_id=role or "default", description="test", role=role) if role else None
    response = app.dispatch({"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}, auth_match=match)
    return {tool["name"] for tool in response["result"]["tools"]}


def assert_equal(name: str, actual: set[str], expected: set[str]) -> None:
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    if missing or extra:
        raise AssertionError(f"{name} mismatch: missing={missing}, extra={extra}")


def main() -> int:
    os.environ.pop("LINGXING_MCP_ROLE_TOOLS", None)
    app = LingxingMCPApplication()
    assert_equal("default/minimal tools", tool_names(app, None), EXPECTED_MINIMAL)
    assert_equal("minimal tools", tool_names(app, "minimal"), EXPECTED_MINIMAL)
    assert_equal("operations tools", tool_names(app, "operations"), EXPECTED_OPERATIONS)
    assert_equal("finance tools", tool_names(app, "finance"), EXPECTED_FINANCE)

    for role in ["minimal", "operations", "finance"]:
        names = tool_names(app, role)
        if not BASE_TOOLS.issubset(names):
            raise AssertionError(f"{role} missing base tools: {sorted(BASE_TOOLS - names)}")

    all_tools = app.list_tools(AuthMatch(mode="test", token_id="minimal", description="test", role="minimal"))
    limit_marker = "\\u9650\\u6d41\\uff1a".encode("ascii").decode("unicode_escape")
    all_registered_tools = [tool.as_mcp_tool() for tool in app.tools.values()]
    missing_rate_limit = [
        tool["name"]
        for tool in all_registered_tools
        if limit_marker not in str(tool.get("description") or "")
    ]
    if missing_rate_limit:
        raise AssertionError(f"tools missing visible rate-limit policy: {missing_rate_limit}")
    if "lingxing_rate_limit_policy" not in {tool["name"] for tool in all_tools}:
        raise AssertionError("minimal role cannot see lingxing_rate_limit_policy")

    finance = AuthMatch(mode="test", token_id="finance", description="test", role="finance")
    denied = app.dispatch(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {"name": "lingxing_product_performance", "arguments": {}},
        },
        auth_match=finance,
    )
    if denied["result"].get("isError") is not True:
        raise AssertionError("finance role unexpectedly called lingxing_product_performance")

    os.environ["LINGXING_MCP_ROLE_TOOLS"] = json.dumps({"custom": ["lingxing_seller_lists"]})
    override_app = LingxingMCPApplication()
    assert_equal("custom override includes base tools", tool_names(override_app, "custom"), BASE_TOOLS | {"lingxing_seller_lists"})

    print(
        json.dumps(
            {
                "ok": True,
                "minimal_count": len(EXPECTED_MINIMAL),
                "operations_count": len(EXPECTED_OPERATIONS),
                "finance_count": len(EXPECTED_FINANCE),
                "base_tools": sorted(BASE_TOOLS),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
