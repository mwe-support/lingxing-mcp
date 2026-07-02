"""Minimal MCP implementation for LingXing OpenAPI tools."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Callable

from .auth import AuthMatch, BearerAuthConfig, load_bearer_auth_config
from .client import rate_limit_policy_for_endpoint, rate_limit_runtime_settings
from .endpoint_specs import ALL_ENDPOINT_SPECS
from .errors import LingxingClientError, LingxingConfigError
from .multi_channel_orders import MultiChannelOrderQuery
from .services import LingxingOpenAPIService


SERVER_NAME = "lingxing-openapi"
SERVER_VERSION = "0.3.0"
PROTOCOL_VERSION = "2024-11-05"
ROLE_TOOL_MAP_ENV = "LINGXING_MCP_ROLE_TOOLS"
BASE_ROLE_TOOL_NAMES = {
    "lingxing_health_check",
    "lingxing_smoke_check",
    "lingxing_rate_limit_policy",
}
DEFAULT_ROLE_TOOL_NAMES: dict[str, set[str]] = {
    "minimal": BASE_ROLE_TOOL_NAMES
    | {
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
    },
    "operations": BASE_ROLE_TOOL_NAMES
    | {
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
    },
    "finance": BASE_ROLE_TOOL_NAMES
    | {
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
    },
}
ROLE_ALIASES = {
    "legacy": "minimal",
    "base": "minimal",
    "readonly": "minimal",
    "read_only": "minimal",
    "minimum": "minimal",
    "operation": "operations",
    "ops": "operations",
    "financial": "finance",
}
CORS_ALLOW_HEADERS = ", ".join(
    [
        "Authorization",
        "Content-Type",
        "Accept",
        "CF-Access-Client-Id",
        "CF-Access-Client-Secret",
        "Mcp-Session-Id",
        "Last-Event-ID",
    ]
)


MANUAL_TOOL_RATE_LIMIT_ENDPOINTS: dict[str, tuple[str, ...]] = {
    "lingxing_health_check": ("/api/auth-server/oauth/access-token",),
    "lingxing_rate_limit_policy": (),
    "lingxing_seller_lists": ("/erp/sc/data/seller/lists", "/erp/sc/data/seller/allMarketplace"),
    "lingxing_marketplaces": ("/erp/sc/data/seller/allMarketplace",),
    "lingxing_store_sales": ("/erp/sc/data/sales_report/sales",),
    "lingxing_asin_daily_lists": ("/erp/sc/data/sales_report/asinDailyLists",),
    "lingxing_order_lists": ("/erp/sc/data/mws/orders",),
    "lingxing_order_details": ("/erp/sc/data/mws/orderDetail", "/erp/sc/data/seller/lists", "/erp/sc/data/seller/allMarketplace"),
    "lingxing_multi_channel_orders": (
        "/order/amzod/api/orderList",
        "/order/amzod/api/orderDetails/productInformation",
        "/order/amzod/api/orderDetails/logisticsInformation",
        "/order/amzod/api/orderDetails/returnInformation",
        "/basicOpen/openapi/salesOrder/multi-channel/list/transaction",
    ),
    "lingxing_promotion_listing": ("/basicOpen/promotion/listingList",),
    "lingxing_promotion_sec_kill": ("/basicOpen/promotionalActivities/secKill/list",),
    "lingxing_promotion_manage": ("/basicOpen/promotionalActivities/manage/list",),
    "lingxing_promotion_vip_discount": ("/basicOpen/promotionalActivities/vipDiscount/list",),
    "lingxing_promotion_coupon": ("/basicOpen/promotionalActivities/coupon/list",),
    "lingxing_resolve_daily_promotions": (
        "/basicOpen/promotion/listingList",
        "/basicOpen/promotionalActivities/secKill/list",
        "/basicOpen/promotionalActivities/manage/list",
        "/basicOpen/promotionalActivities/vipDiscount/list",
        "/basicOpen/promotionalActivities/coupon/list",
    ),
    "lingxing_asin_product_snapshot": (
        "/basicOpen/openapi/storage/fbaWarehouseDetail",
        "/bd/productPerformance/openApi/asinList",
        "/erp/sc/routing/data/local_inventory/productList",
    ),
    "lingxing_local_product_costs": ("/erp/sc/routing/data/local_inventory/productList",),
    "lingxing_smoke_check": (
        "/erp/sc/data/seller/lists",
        "/erp/sc/data/seller/allMarketplace",
        "/erp/sc/data/sales_report/sales",
        "/erp/sc/data/mws/orders",
        "/basicOpen/promotion/listingList",
        "/basicOpen/baseData/account/list",
        "/pb/openapi/newad/spProductAdReports",
        "/pb/openapi/newad/sdProductAdReports",
        "/pb/openapi/newad/hsaPurchasedAsinReports",
        "/bd/profit/statistics/open/seller/list",
        "/erp/sc/data/mws_report/allOrders",
        "/erp/sc/data/mws_report/manageInventory",
    ),
    "lingxing_ad_accounts": ("/basicOpen/baseData/account/list",),
    "lingxing_report_export_create": ("/basicOpen/report/create/reportExportTask",),
    "lingxing_report_export_query": ("/basicOpen/report/query/reportExportTask",),
    "lingxing_report_export_refresh_url": ("/basicOpen/report/amazonReportExportTask",),
    "lingxing_report_export_download": (
        "/basicOpen/report/query/reportExportTask",
        "/basicOpen/report/amazonReportExportTask",
    ),
    "lingxing_asin_ads_daily_rollup": (
        "/basicOpen/baseData/account/list",
        "/pb/openapi/newad/hsaProductAds",
        "/pb/openapi/newad/spProductAdReports",
        "/pb/openapi/newad/sdProductAdReports",
        "/pb/openapi/newad/hsaPurchasedAsinReports",
        "/pb/openapi/newad/listHsaProductAdReport",
    ),
    "lingxing_asin_weekly_rollup": (
        "/erp/sc/data/sales_report/sales",
        "/basicOpen/baseData/account/list",
        "/pb/openapi/newad/hsaProductAds",
        "/pb/openapi/newad/spProductAdReports",
        "/pb/openapi/newad/sdProductAdReports",
        "/pb/openapi/newad/hsaPurchasedAsinReports",
        "/pb/openapi/newad/listHsaProductAdReport",
        "/basicOpen/promotion/listingList",
        "/basicOpen/promotionalActivities/secKill/list",
        "/basicOpen/promotionalActivities/manage/list",
        "/basicOpen/promotionalActivities/vipDiscount/list",
        "/basicOpen/promotionalActivities/coupon/list",
    ),
}


def _normalize_role(role: str | None) -> str:
    normalized = str(role or "").strip()
    if not normalized:
        return ""
    lowered = normalized.lower().replace("-", "_")
    return ROLE_ALIASES.get(normalized, ROLE_ALIASES.get(lowered, lowered))


def _split_tool_names(value: Any) -> set[str]:
    if isinstance(value, str):
        normalized = value.replace("\n", ",").replace(";", ",")
        return {item.strip() for item in normalized.split(",") if item.strip()}
    if isinstance(value, list):
        return {str(item).strip() for item in value if str(item).strip()}
    raise LingxingConfigError(f"{ROLE_TOOL_MAP_ENV} role value must be a list, string, or null")


def _role_tool_names_from_env() -> dict[str, set[str]]:
    mapping = {role: set(tool_names) for role, tool_names in DEFAULT_ROLE_TOOL_NAMES.items()}
    raw_value = os.getenv(ROLE_TOOL_MAP_ENV, "").strip()
    if raw_value:
        try:
            payload = json.loads(raw_value)
        except json.JSONDecodeError as exc:
            raise LingxingConfigError(f"{ROLE_TOOL_MAP_ENV} must be a JSON object") from exc
        if not isinstance(payload, dict):
            raise LingxingConfigError(f"{ROLE_TOOL_MAP_ENV} must be a JSON object")
        for role, tool_names in payload.items():
            normalized_role = _normalize_role(str(role))
            if not normalized_role:
                continue
            if tool_names is None:
                mapping[normalized_role] = BASE_ROLE_TOOL_NAMES | set(DEFAULT_ROLE_TOOL_NAMES.get(normalized_role, set()))
            else:
                mapping[normalized_role] = BASE_ROLE_TOOL_NAMES | _split_tool_names(tool_names)
    mapping.setdefault("minimal", set(DEFAULT_ROLE_TOOL_NAMES["minimal"]))
    return mapping


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True)


def _now_text() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _optional_int(args: dict[str, Any], key: str) -> int | None:
    value = args.get(key)
    if value in (None, ""):
        return None
    return int(value)


def _required_int(args: dict[str, Any], key: str) -> int:
    value = _optional_int(args, key)
    if value is None:
        raise LingxingConfigError(f"缺少必要参数: {key}")
    return value


def _optional_bool(args: dict[str, Any], key: str, default: bool = False) -> bool:
    value = args.get(key)
    if value in (None, ""):
        return default
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _required_text(args: dict[str, Any], key: str) -> str:
    value = str(args.get(key) or "").strip()
    if not value:
        raise LingxingConfigError(f"缺少必要参数: {key}")
    return value


def _list_of_ints(args: dict[str, Any], key: str) -> list[int] | None:
    value = args.get(key)
    if value in (None, ""):
        return None
    if isinstance(value, list):
        return [int(item) for item in value]
    return [int(value)]


def _listify_strings(value: Any) -> list[str]:
    if value in (None, ""):
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def _unique_endpoints(endpoints: tuple[str, ...] | list[str]) -> tuple[str, ...]:
    seen: set[str] = set()
    values: list[str] = []
    for endpoint in endpoints:
        text = str(endpoint or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        values.append(text)
    return tuple(values)


def _rate_limit_description(endpoints: tuple[str, ...]) -> str:
    endpoints = _unique_endpoints(endpoints)
    if not endpoints:
        return "限流：本工具不直接调用领星业务 OpenAPI，或仅返回本地网关策略；客户端可并发调用，但不应把它作为业务查询循环。"
    if len(endpoints) == 1:
        policy = rate_limit_policy_for_endpoint(endpoints[0])
        return (
            f"限流：endpoint {policy['endpoint']}，"
            f"{policy['rate_per_second']:g} req/s，burst {policy['burst']}，来源 {policy['source']}；"
            f"{policy['client_guidance']}"
        )
    policies = [rate_limit_policy_for_endpoint(endpoint) for endpoint in endpoints]
    strict = min(policies, key=lambda item: (float(item['rate_per_second']), int(item['burst'])))
    return (
        f"限流：聚合工具，涉及 {len(policies)} 个 endpoint；最严格为 {strict['endpoint']} "
        f"{strict['rate_per_second']:g} req/s，burst {strict['burst']}；"
        "客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。"
    )


@dataclass
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: Callable[[dict[str, Any]], dict[str, Any]]
    rate_limit_endpoints: tuple[str, ...] = ()

    def as_mcp_tool(self) -> dict[str, Any]:
        description = f"{self.description}\n{_rate_limit_description(self.rate_limit_endpoints)}"
        return {
            "name": self.name,
            "description": description,
            "inputSchema": self.input_schema,
        }


class LingxingMCPApplication:
    """Tool registry and JSON-RPC dispatcher."""

    def __init__(self, service: LingxingOpenAPIService | None = None) -> None:
        self.service = service or LingxingOpenAPIService()
        self.tools = self._build_tools()
        self.role_tool_names = _role_tool_names_from_env()

    def _build_tools(self) -> dict[str, ToolDefinition]:
        tools = {
            "lingxing_health_check": ToolDefinition(
                name="lingxing_health_check",
                description="检查领星环境变量、token 状态和基础连通性，不拉业务数据。",
                input_schema={"type": "object", "properties": {}, "additionalProperties": False},
                handler=lambda _: self.service.health_check(),
            ),
            "lingxing_rate_limit_policy": ToolDefinition(
                name="lingxing_rate_limit_policy",
                description="返回当前 MCP 工具到领星 OpenAPI endpoint 的限流政策，供客户端 agent 在调用前按 endpoint 自主排队。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "tool_name": {"type": "string", "description": "可选；只查询某一个 MCP 工具的限流策略。"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.rate_limit_policy(
                    tool_name=str(args.get("tool_name") or "").strip() or None
                ),
            ),
            "lingxing_seller_lists": ToolDefinition(
                name="lingxing_seller_lists",
                description="获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "status": {"type": "integer", "description": "店铺状态过滤，按领星 seller/lists 返回的 status 值匹配。"},
                        "marketplace": {"type": "string", "description": "站点代码过滤，例如 US、UK、DE、JP。"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.seller_lists(
                    status=_optional_int(args, "status"),
                    marketplace=str(args.get("marketplace") or "").strip() or None,
                ),
            ),
            "lingxing_marketplaces": ToolDefinition(
                name="lingxing_marketplaces",
                description="返回领星市场列表，并补充站点时区映射。",
                input_schema={"type": "object", "properties": {}, "additionalProperties": False},
                handler=lambda _: self.service.marketplaces(),
            ),
            "lingxing_store_sales": ToolDefinition(
                name="lingxing_store_sales",
                description="按店铺和日期范围拉取 StoreSales，并自动合并分页。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.store_sales(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
            "lingxing_asin_daily_lists": ToolDefinition(
                name="lingxing_asin_daily_lists",
                description="按店铺、日期和指标类型拉取 AsinDailyLists。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "event_date": {"type": "string"},
                        "metric_type": {"type": "integer"},
                        "asin_type": {"type": "integer"},
                    },
                    "required": ["sid", "event_date", "metric_type"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.asin_daily_lists(
                    _required_int(args, "sid"),
                    _required_text(args, "event_date"),
                    _required_int(args, "metric_type"),
                    asin_type=_optional_int(args, "asin_type") or 1,
                ),
            ),
            "lingxing_order_lists": ToolDefinition(
                name="lingxing_order_lists",
                description="按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "date_type": {"type": "integer"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.orders(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                    date_type=_optional_int(args, "date_type") or 1,
                ),
            ),
            "lingxing_order_details": ToolDefinition(
                name="lingxing_order_details",
                description="按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "单个亚马逊订单号；也可用英文逗号、中文逗号、分号或换行分隔多个订单号。"},
                        "order_ids": {"type": "array", "items": {"type": "string"}, "description": "亚马逊订单号列表。"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.order_details(
                    order_id=str(args.get("order_id") or "").strip() or None,
                    order_ids=_listify_strings(args.get("order_ids")),
                ),
            ),
            "lingxing_multi_channel_orders": ToolDefinition(
                name="lingxing_multi_channel_orders",
                description=(
                    "查询亚马逊多渠道订单列表，按店铺 sid、日期范围和订单状态过滤；可选补充商品、物流、交易明细、退换货详情。"
                    "为避免领星默认拉取最近 6 个月，本工具强制要求 start_date/end_date。"
                ),
                input_schema={
                    "type": "object",
                    "properties": {
                        "sids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "领星店铺 sid 列表，至少 1 个。",
                            "minItems": 1,
                        },
                        "start_date": {"type": "string", "description": "订购时间或修改时间开始日期，YYYY-MM-DD。"},
                        "end_date": {"type": "string", "description": "订购时间或修改时间结束日期，YYYY-MM-DD。"},
                        "date_type": {"type": "integer", "description": "查询日期类型：1 订购时间，2 订单修改时间；默认 1。"},
                        "order_status": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "订单状态枚举，需使用官方大写值，例如 NEW、PROCESSING、COMPLETE、CANCELLED。",
                        },
                        "amazon_order_id": {"type": "string", "description": "可选；在列表结果返回后按亚马逊订单号精确过滤。"},
                        "seller_fulfillment_order_id": {"type": "string", "description": "可选；在列表结果返回后按卖家订单号精确过滤。"},
                        "include_product_detail": {"type": "boolean", "description": "是否补充商品详情，默认 false。"},
                        "include_logistics_detail": {"type": "boolean", "description": "是否补充物流详情，默认 false。"},
                        "include_transaction_detail": {"type": "boolean", "description": "是否逐单补充交易明细，默认 false；该接口 1 req/s，订单多时会较慢。"},
                        "include_return_detail": {"type": "boolean", "description": "是否补充退换货详情，默认 false。"},
                        "page_size": {"type": "integer", "description": "分页大小，1 到 1000，默认 200。"},
                        "max_records": {"type": "integer", "description": "最多拉取记录数，1 到 5000，默认 1000。"},
                    },
                    "required": ["sids", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.multi_channel_orders(
                    MultiChannelOrderQuery(
                        sids=_list_of_ints(args, "sids") or [],
                        start_date=_required_text(args, "start_date"),
                        end_date=_required_text(args, "end_date"),
                        date_type=_optional_int(args, "date_type") or 1,
                        order_status=_listify_strings(args.get("order_status")) or None,
                        amazon_order_id=str(args.get("amazon_order_id") or "").strip() or None,
                        seller_fulfillment_order_id=str(args.get("seller_fulfillment_order_id") or "").strip() or None,
                        include_product_detail=_optional_bool(args, "include_product_detail", False),
                        include_logistics_detail=_optional_bool(args, "include_logistics_detail", False),
                        include_transaction_detail=_optional_bool(args, "include_transaction_detail", False),
                        include_return_detail=_optional_bool(args, "include_return_detail", False),
                        page_size=_optional_int(args, "page_size") or 200,
                        max_records=_optional_int(args, "max_records") or 1000,
                    )
                ),
            ),
            "lingxing_promotion_listing": ToolDefinition(
                name="lingxing_promotion_listing",
                description="拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "site_date": {"type": "string"},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                        "status": {"type": "array", "items": {"type": "integer"}},
                        "product_status": {"type": "array", "items": {"type": "integer"}},
                        "promotion_category": {"type": "array", "items": {"type": "integer"}},
                    },
                    "required": ["sid", "site_date", "start_time", "end_time"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.promotion_listing(
                    _required_int(args, "sid"),
                    _required_text(args, "site_date"),
                    _required_text(args, "start_time"),
                    _required_text(args, "end_time"),
                    status=_list_of_ints(args, "status"),
                    product_status=_list_of_ints(args, "product_status"),
                    promotion_category=_list_of_ints(args, "promotion_category"),
                ),
            ),
            "lingxing_promotion_sec_kill": ToolDefinition(
                name="lingxing_promotion_sec_kill",
                description="拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.promotion_sec_kill(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
            "lingxing_promotion_manage": ToolDefinition(
                name="lingxing_promotion_manage",
                description="拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.promotion_manage(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
            "lingxing_promotion_vip_discount": ToolDefinition(
                name="lingxing_promotion_vip_discount",
                description="拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.promotion_vip_discount(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
            "lingxing_promotion_coupon": ToolDefinition(
                name="lingxing_promotion_coupon",
                description="拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.promotion_coupon(
                    _required_int(args, "sid"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
            "lingxing_resolve_daily_promotions": ToolDefinition(
                name="lingxing_resolve_daily_promotions",
                description="输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "target_date": {"type": "string"},
                        "lookback_days": {"type": "integer"},
                    },
                    "required": ["sid", "target_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.resolve_daily_promotions(
                    _required_int(args, "sid"),
                    _required_text(args, "target_date"),
                    lookback_days=_optional_int(args, "lookback_days") or 90,
                ),
            ),
            "lingxing_asin_product_snapshot": ToolDefinition(
                name="lingxing_asin_product_snapshot",
                description=(
                    "按店铺 sid 查询 1 到 50 个 ASIN 的产品快照，返回产品名、采购成本、前台售价、"
                    "FBA 实时库存、产品表现销量 volume 和产品链接。单个 ASIN 也使用 asins 数组传入，"
                    "例如 [\"B0...\"]；超过 50 个时客户端 Agent 应自行按 50 个一批拆分并串行调用。"
                ),
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer", "description": "领星店铺 sid。"},
                        "asins": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "ASIN 列表，支持 1 到 50 个；单个 ASIN 也传数组，超过 50 个请客户端按批次串行调用。",
                            "minItems": 1,
                            "maxItems": 50,
                        },
                        "start_date": {"type": "string", "description": "销量统计开始日期，YYYY-MM-DD；不传时默认近 30 天。"},
                        "end_date": {"type": "string", "description": "销量统计结束日期，YYYY-MM-DD；不传时默认昨天。"},
                    },
                    "required": ["sid", "asins"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.asin_product_snapshot(
                    sid=_required_int(args, "sid"),
                    asins=_listify_strings(args.get("asins")),
                    start_date=str(args.get("start_date") or "").strip() or None,
                    end_date=str(args.get("end_date") or "").strip() or None,
                ),
            ),
            "lingxing_local_product_costs": ToolDefinition(
                name="lingxing_local_product_costs",
                description="按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sku_list": {"type": "array", "items": {"type": "string"}},
                        "sku_identifier_list": {"type": "array", "items": {"type": "string"}},
                        "update_time_start": {"type": "integer"},
                        "update_time_end": {"type": "integer"},
                        "create_time_start": {"type": "integer"},
                        "create_time_end": {"type": "integer"},
                        "page_size": {"type": "integer"},
                        "include_supplier_quotes": {"type": "boolean"},
                        "include_raw": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.local_product_costs(
                    sku_list=_listify_strings(args.get("sku_list")),
                    sku_identifier_list=_listify_strings(args.get("sku_identifier_list")),
                    update_time_start=_optional_int(args, "update_time_start"),
                    update_time_end=_optional_int(args, "update_time_end"),
                    create_time_start=_optional_int(args, "create_time_start"),
                    create_time_end=_optional_int(args, "create_time_end"),
                    page_size=_optional_int(args, "page_size") or 1000,
                    include_supplier_quotes=_optional_bool(args, "include_supplier_quotes", True),
                    include_raw=_optional_bool(args, "include_raw", False),
                ),
            ),
            "lingxing_smoke_check": ToolDefinition(
                name="lingxing_smoke_check",
                description="按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "date": {"type": "string"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.smoke_check(
                    sid=_optional_int(args, "sid"),
                    site_date=str(args.get("date") or "").strip() or None,
                ),
            ),
            "lingxing_ad_accounts": ToolDefinition(
                name="lingxing_ad_accounts",
                description="查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "sid": {"type": "integer"},
                        "profile_id": {"type": "integer"},
                        "country_code": {"type": "string"},
                        "status": {"type": "integer"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.ad_accounts(
                    account_type=str(args.get("type") or "seller").strip() or "seller",
                    sid=_optional_int(args, "sid"),
                    profile_id=_optional_int(args, "profile_id"),
                    country_code=str(args.get("country_code") or "").strip() or None,
                    status=_optional_int(args, "status"),
                ),
            ),
            "lingxing_report_export_create": ToolDefinition(
                name="lingxing_report_export_create",
                description="创建亚马逊报告导出任务。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "report_type": {"type": "string"},
                        "data_start_time": {"type": "string"},
                        "data_end_time": {"type": "string"},
                        "marketplace_ids": {"type": "array", "items": {"type": "string"}},
                        "region": {"type": "string"},
                        "seller_id": {"type": "string"},
                    },
                    "required": ["sid", "report_type"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.report_export_create(
                    sid=_required_int(args, "sid"),
                    report_type=_required_text(args, "report_type"),
                    data_start_time=str(args.get("data_start_time") or "").strip() or None,
                    data_end_time=str(args.get("data_end_time") or "").strip() or None,
                    marketplace_ids=_listify_strings(args.get("marketplace_ids")) or None,
                    region=str(args.get("region") or "").strip() or None,
                    seller_id=str(args.get("seller_id") or "").strip() or None,
                ),
            ),
            "lingxing_report_export_query": ToolDefinition(
                name="lingxing_report_export_query",
                description="查询亚马逊报告导出任务结果。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "task_id": {"type": "string"},
                        "region": {"type": "string"},
                        "seller_id": {"type": "string"},
                    },
                    "required": ["task_id"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.report_export_query(
                    sid=_optional_int(args, "sid"),
                    task_id=_required_text(args, "task_id"),
                    region=str(args.get("region") or "").strip() or None,
                    seller_id=str(args.get("seller_id") or "").strip() or None,
                ),
            ),
            "lingxing_report_export_refresh_url": ToolDefinition(
                name="lingxing_report_export_refresh_url",
                description="续期亚马逊报告下载链接。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "report_document_id": {"type": "string"},
                        "region": {"type": "string"},
                        "seller_id": {"type": "string"},
                    },
                    "required": ["report_document_id"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.report_export_refresh_url(
                    sid=_optional_int(args, "sid"),
                    report_document_id=_required_text(args, "report_document_id"),
                    region=str(args.get("region") or "").strip() or None,
                    seller_id=str(args.get("seller_id") or "").strip() or None,
                ),
            ),
            "lingxing_report_export_download": ToolDefinition(
                name="lingxing_report_export_download",
                description="下载并解析亚马逊报告导出文件。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "url": {"type": "string"},
                        "sid": {"type": "integer"},
                        "task_id": {"type": "string"},
                        "report_document_id": {"type": "string"},
                        "region": {"type": "string"},
                        "seller_id": {"type": "string"},
                    },
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.report_export_download(
                    url=str(args.get("url") or "").strip() or None,
                    sid=_optional_int(args, "sid"),
                    task_id=str(args.get("task_id") or "").strip() or None,
                    report_document_id=str(args.get("report_document_id") or "").strip() or None,
                    region=str(args.get("region") or "").strip() or None,
                    seller_id=str(args.get("seller_id") or "").strip() or None,
                ),
            ),
            "lingxing_asin_ads_daily_rollup": ToolDefinition(
                name="lingxing_asin_ads_daily_rollup",
                description="按 ASIN 汇总每日广告指标，采用 balanced 归因。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "asin": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "attribution_policy": {"type": "string"},
                    },
                    "required": ["sid", "asin", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.asin_ads_daily_rollup(
                    _required_int(args, "sid"),
                    _required_text(args, "asin"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                    attribution_policy=str(args.get("attribution_policy") or "balanced").strip() or "balanced",
                ),
            ),
            "lingxing_asin_weekly_rollup": ToolDefinition(
                name="lingxing_asin_weekly_rollup",
                description="按周汇总 ASIN 的总销量、广告指标和促销标签。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "sid": {"type": "integer"},
                        "asin": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                    },
                    "required": ["sid", "asin", "start_date", "end_date"],
                    "additionalProperties": False,
                },
                handler=lambda args: self.service.asin_weekly_rollup(
                    _required_int(args, "sid"),
                    _required_text(args, "asin"),
                    _required_text(args, "start_date"),
                    _required_text(args, "end_date"),
                ),
            ),
        }
        for spec in ALL_ENDPOINT_SPECS:
            tools[spec.tool_name] = ToolDefinition(
                name=spec.tool_name,
                description=spec.description,
                input_schema=spec.input_schema,
                handler=lambda args, tool_name=spec.tool_name: self.service.run_endpoint_spec(tool_name, args),
                rate_limit_endpoints=(spec.endpoint,),
            )
        for tool_name, endpoints in MANUAL_TOOL_RATE_LIMIT_ENDPOINTS.items():
            tool = tools.get(tool_name)
            if tool is not None and not tool.rate_limit_endpoints:
                tool.rate_limit_endpoints = _unique_endpoints(endpoints)
        return tools

    def _tools_for_auth(self, auth_match: AuthMatch | None = None) -> dict[str, ToolDefinition]:
        role = _normalize_role(auth_match.role if auth_match else None) or "minimal"
        allowed_names = self.role_tool_names.get(role)
        if allowed_names is None:
            return {}
        unknown_names = sorted(allowed_names.difference(self.tools))
        if unknown_names:
            sys.stderr.write(f"Ignoring unknown MCP tool names for role {role}: {', '.join(unknown_names)}\n")
        return {name: tool for name, tool in self.tools.items() if name in allowed_names}

    def list_tools(self, auth_match: AuthMatch | None = None) -> list[dict[str, Any]]:
        return [tool.as_mcp_tool() for tool in self._tools_for_auth(auth_match).values()]

    def call_tool(self, name: str, arguments: dict[str, Any] | None, auth_match: AuthMatch | None = None) -> dict[str, Any]:
        tool = self._tools_for_auth(auth_match).get(name)
        if tool is None:
            role = _normalize_role(auth_match.role if auth_match else None) or "minimal"
            raise LingxingConfigError(f"Tool is not available for this role or does not exist: {name} (role={role})")
        return tool.handler(arguments or {})

    def rate_limit_policy(self, tool_name: str | None = None) -> dict[str, Any]:
        selected_tools: dict[str, ToolDefinition]
        if tool_name:
            tool = self.tools.get(tool_name)
            if tool is None:
                raise LingxingConfigError(f"?? MCP ??: {tool_name}")
            selected_tools = {tool_name: tool}
        else:
            selected_tools = self.tools

        tool_policies: list[dict[str, Any]] = []
        for name in sorted(selected_tools):
            tool = selected_tools[name]
            endpoints = _unique_endpoints(tool.rate_limit_endpoints)
            endpoint_policies = [rate_limit_policy_for_endpoint(endpoint) for endpoint in endpoints]
            if endpoint_policies:
                client_guidance = (
                    endpoint_policies[0]["client_guidance"]
                    if len(endpoint_policies) == 1
                    else "聚合工具会串行触发多个 endpoint；客户端应按 endpoint 维度排队，避免同类查询并发。"
                )
            else:
                client_guidance = "本工具不直接调用领星业务 OpenAPI；可低风险调用，但不应在业务查询循环中高频轮询。"
            tool_policies.append(
                {
                    "tool_name": name,
                    "description": tool.description,
                    "rate_limit_description": _rate_limit_description(endpoints),
                    "endpoints": endpoints,
                    "endpoint_policies": endpoint_policies,
                    "client_guidance": client_guidance,
                }
            )

        return {
            "ok": True,
            "data": {
                "scope": "all_registered_tools" if tool_name is None else "single_tool",
                "tool_count": len(tool_policies),
                "runtime_settings": rate_limit_runtime_settings(),
                "client_rules": [
                    "调用任意业务工具前先读取 tools/list 的限流说明；复杂任务可先调用 lingxing_rate_limit_policy 获取机器可读策略。",
                    "按 endpoint 分组限流，不按工具名分组；多个工具可能共享同一个领星 endpoint。",
                    "capacity=1 的 endpoint 必须串行调用，默认 1 秒 1 次，不要并发。",
                    "聚合工具由服务端串行调用内部 endpoint；客户端不要把同一聚合查询拆成并发子调用。",
                    "收到 local_rate_limit_timeout 时缩小查询范围或降低并发，而不是立即重试。",
                ],
                "tools": tool_policies,
            },
            "meta": {
                "endpoint": "local_rate_limit_policy",
                "page_count": 1,
                "request_ts": _now_text(),
                "sid": None,
                "date_range": None,
            },
            "warnings": [],
        }

    def initialize_result(self) -> dict[str, Any]:
        return {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {
                "tools": {"listChanged": False},
            },
            "serverInfo": {
                "name": SERVER_NAME,
                "version": SERVER_VERSION,
            },
        }

    def _tool_result(self, payload: dict[str, Any], *, is_error: bool = False) -> dict[str, Any]:
        return {
            "content": [{"type": "text", "text": _json_text(payload)}],
            "structuredContent": payload,
            "isError": is_error,
        }

    def _tool_error_payload(self, exc: Exception) -> dict[str, Any]:
        if isinstance(exc, LingxingClientError):
            error = exc.to_dict()
            endpoint = exc.endpoint or "unknown"
        else:
            error = {"message": str(exc)}
            endpoint = "unknown"
        return {
            "ok": False,
            "error": error,
            "meta": {
                "endpoint": endpoint,
                "page_count": 0,
                "request_ts": _now_text(),
                "sid": None,
                "date_range": None,
            },
            "warnings": [str(exc)],
        }

    def _jsonrpc_result(self, request_id: Any, result: Any) -> dict[str, Any]:
        return {"jsonrpc": "2.0", "id": request_id, "result": result}

    def _jsonrpc_error(self, request_id: Any, code: int, message: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        payload: dict[str, Any] = {"code": code, "message": message}
        if data:
            payload["data"] = data
        return {"jsonrpc": "2.0", "id": request_id, "error": payload}

    def dispatch(self, request: dict[str, Any], auth_match: AuthMatch | None = None) -> dict[str, Any] | None:
        method = request.get("method")
        request_id = request.get("id")
        params = request.get("params") or {}

        if method == "notifications/initialized":
            return None
        if method == "initialize":
            return self._jsonrpc_result(request_id, self.initialize_result())
        if method == "ping":
            return self._jsonrpc_result(request_id, {})
        if method == "tools/list":
            return self._jsonrpc_result(request_id, {"tools": self.list_tools(auth_match)})
        if method == "resources/list":
            return self._jsonrpc_result(request_id, {"resources": []})
        if method == "prompts/list":
            return self._jsonrpc_result(request_id, {"prompts": []})
        if method == "tools/call":
            try:
                name = str(params.get("name") or "").strip()
                arguments = params.get("arguments") or {}
                result = self.call_tool(name, arguments, auth_match)
                return self._jsonrpc_result(request_id, self._tool_result(result))
            except LingxingClientError as exc:
                return self._jsonrpc_result(request_id, self._tool_result(self._tool_error_payload(exc), is_error=True))
            except Exception as exc:  # pragma: no cover - defensive guard
                return self._jsonrpc_result(request_id, self._tool_result(self._tool_error_payload(exc), is_error=True))
        if request_id is None:
            return None
        return self._jsonrpc_error(request_id, -32601, f"Method not found: {method}")


def _read_stdio_message(stream: Any) -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = stream.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        key, _, value = line.decode("utf-8").partition(":")
        headers[key.strip().lower()] = value.strip()
    content_length = int(headers.get("content-length", "0"))
    if content_length <= 0:
        return None
    body = stream.read(content_length)
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def _write_stdio_message(stream: Any, payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\nContent-Type: application/json\r\n\r\n".encode("ascii")
    stream.write(header)
    stream.write(body)
    stream.flush()


def run_stdio_server(app: LingxingMCPApplication | None = None) -> int:
    application = app or LingxingMCPApplication()
    stdin = sys.stdin.buffer
    stdout = sys.stdout.buffer
    while True:
        message = _read_stdio_message(stdin)
        if message is None:
            return 0
        response = application.dispatch(message)
        if response is not None:
            _write_stdio_message(stdout, response)


def process_http_request(
    app: LingxingMCPApplication,
    *,
    auth: BearerAuthConfig,
    method: str,
    path: str,
    headers: dict[str, str] | None = None,
    body: bytes | None = None,
) -> tuple[int, dict[str, Any]]:
    normalized_headers = {str(key): str(value) for key, value in (headers or {}).items()}
    authorization = normalized_headers.get("Authorization", "")

    if method == "GET" and path == "/healthz":
        return HTTPStatus.OK, {
            "ok": True,
            "server": SERVER_NAME,
            "version": SERVER_VERSION,
            "auth": auth.summary(),
        }
    if path != "/mcp":
        return HTTPStatus.NOT_FOUND, {"error": "not_found"}
    if method == "OPTIONS":
        return HTTPStatus.NO_CONTENT, {}
    match = auth.authenticate_header(authorization)
    if match is None:
        return HTTPStatus.UNAUTHORIZED, {
            "error": "missing_or_invalid_bearer",
            "message": "需要 Authorization: Bearer <LINGXING_MCP_BEARER_TOKEN> 或多人令牌文件中的有效成员令牌。",
        }
    if method == "GET":
        return HTTPStatus.OK, {
            "ok": True,
            "protocolVersion": PROTOCOL_VERSION,
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            "capabilities": {"tools": {"listChanged": False}},
            "auth": {
                "mode": match.mode,
                "token_id": match.token_id,
                "role": _normalize_role(match.role) or "minimal",
            },
        }
    if method == "POST":
        try:
            request = json.loads((body or b"").decode("utf-8"))
        except json.JSONDecodeError:
            return HTTPStatus.BAD_REQUEST, {"error": "invalid_json"}
        response = app.dispatch(request, auth_match=match)
        if response is None:
            return HTTPStatus.ACCEPTED, {"ok": True}
        return HTTPStatus.OK, response
    return HTTPStatus.METHOD_NOT_ALLOWED, {"error": "method_not_allowed"}


def _build_http_handler(app: LingxingMCPApplication, auth: BearerAuthConfig) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        server_version = "LingxingMCP/1.0"

        def _send_cors_headers(self) -> None:
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", CORS_ALLOW_HEADERS)
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Expose-Headers", "Mcp-Session-Id")

        def _send_json(self, status: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self._send_cors_headers()
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802
            status, payload = process_http_request(
                app,
                auth=auth,
                method="GET",
                path=self.path,
                headers={key: value for key, value in self.headers.items()},
            )
            self._send_json(status, payload)

        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers.get("Content-Length", "0"))
            status, payload = process_http_request(
                app,
                auth=auth,
                method="POST",
                path=self.path,
                headers={key: value for key, value in self.headers.items()},
                body=self.rfile.read(length),
            )
            self._send_json(status, payload)

        def do_OPTIONS(self) -> None:  # noqa: N802
            status, _ = process_http_request(
                app,
                auth=auth,
                method="OPTIONS",
                path=self.path,
                headers={key: value for key, value in self.headers.items()},
            )
            self.send_response(status)
            self._send_cors_headers()
            self.end_headers()

        def log_message(self, format: str, *args: Any) -> None:  # noqa: A003
            return

    return Handler


def create_http_server(
    host: str,
    port: int,
    *,
    bearer_token: str = "",
    tokens_file: str = "",
    app: LingxingMCPApplication | None = None,
) -> ThreadingHTTPServer:
    application = app or LingxingMCPApplication()
    auth = load_bearer_auth_config(bootstrap_token=bearer_token, tokens_file=tokens_file)
    return ThreadingHTTPServer((host, port), _build_http_handler(application, auth))


def run_http_server(
    host: str,
    port: int,
    *,
    bearer_token: str = "",
    tokens_file: str = "",
    app: LingxingMCPApplication | None = None,
) -> int:
    auth = load_bearer_auth_config(bootstrap_token=bearer_token, tokens_file=tokens_file)
    server = ThreadingHTTPServer((host, port), _build_http_handler(app or LingxingMCPApplication(), auth))
    print(
        json.dumps(
            {"host": host, "port": port, "mode": "http", "server": SERVER_NAME, "auth": auth.summary()},
            ensure_ascii=False,
        )
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


def build_http_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="领星 MCP HTTP 服务")
    parser.add_argument("--host", default=os.getenv("LINGXING_MCP_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.getenv("LINGXING_MCP_PORT", "8099")))
    parser.add_argument("--bearer-token", default=os.getenv("LINGXING_MCP_BEARER_TOKEN", ""))
    parser.add_argument("--tokens-file", default=os.getenv("LINGXING_MCP_TOKENS_FILE", ""))
    return parser
