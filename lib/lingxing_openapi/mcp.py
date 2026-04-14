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

from .auth import BearerAuthConfig, load_bearer_auth_config
from .endpoint_specs import ALL_ENDPOINT_SPECS
from .errors import LingxingClientError, LingxingConfigError
from .services import LingxingOpenAPIService


SERVER_NAME = "lingxing-openapi"
SERVER_VERSION = "0.3.0"
PROTOCOL_VERSION = "2024-11-05"


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


@dataclass
class ToolDefinition:
    name: str
    description: str
    input_schema: dict[str, Any]
    handler: Callable[[dict[str, Any]], dict[str, Any]]

    def as_mcp_tool(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.input_schema,
        }


class LingxingMCPApplication:
    """Tool registry and JSON-RPC dispatcher."""

    def __init__(self, service: LingxingOpenAPIService | None = None) -> None:
        self.service = service or LingxingOpenAPIService()
        self.tools = self._build_tools()

    def _build_tools(self) -> dict[str, ToolDefinition]:
        tools = {
            "lingxing_health_check": ToolDefinition(
                name="lingxing_health_check",
                description="检查领星环境变量、token 状态和基础连通性，不拉业务数据。",
                input_schema={"type": "object", "properties": {}, "additionalProperties": False},
                handler=lambda _: self.service.health_check(),
            ),
            "lingxing_seller_lists": ToolDefinition(
                name="lingxing_seller_lists",
                description="返回领星店铺列表，可按 status 或 marketplace 过滤。",
                input_schema={
                    "type": "object",
                    "properties": {
                        "status": {"type": "integer"},
                        "marketplace": {"type": "string"},
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
            "lingxing_orders": ToolDefinition(
                name="lingxing_orders",
                description="按店铺与时间窗口拉取 Orderlists，并自动合并分页。",
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
            )
        return tools

    def list_tools(self) -> list[dict[str, Any]]:
        return [tool.as_mcp_tool() for tool in self.tools.values()]

    def call_tool(self, name: str, arguments: dict[str, Any] | None) -> dict[str, Any]:
        tool = self.tools.get(name)
        if tool is None:
            raise LingxingConfigError(f"未知工具: {name}")
        return tool.handler(arguments or {})

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

    def dispatch(self, request: dict[str, Any]) -> dict[str, Any] | None:
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
            return self._jsonrpc_result(request_id, {"tools": self.list_tools()})
        if method == "resources/list":
            return self._jsonrpc_result(request_id, {"resources": []})
        if method == "prompts/list":
            return self._jsonrpc_result(request_id, {"prompts": []})
        if method == "tools/call":
            try:
                name = str(params.get("name") or "").strip()
                arguments = params.get("arguments") or {}
                result = self.call_tool(name, arguments)
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
            },
        }
    if method == "POST":
        try:
            request = json.loads((body or b"").decode("utf-8"))
        except json.JSONDecodeError:
            return HTTPStatus.BAD_REQUEST, {"error": "invalid_json"}
        response = app.dispatch(request)
        if response is None:
            return HTTPStatus.ACCEPTED, {"ok": True}
        return HTTPStatus.OK, response
    if method == "OPTIONS":
        return HTTPStatus.NO_CONTENT, {}
    return HTTPStatus.METHOD_NOT_ALLOWED, {"error": "method_not_allowed"}


def _build_http_handler(app: LingxingMCPApplication, auth: BearerAuthConfig) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        server_version = "LingxingMCP/1.0"

        def _send_json(self, status: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
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
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
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
