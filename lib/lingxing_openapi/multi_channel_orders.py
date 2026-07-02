"""Multi-channel Amazon order query helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Protocol

from .client import PagedRows, extract_path_value
from .errors import LingxingConfigError


MCF_ORDER_LIST_ENDPOINT = "/order/amzod/api/orderList"
MCF_PRODUCT_ENDPOINT = "/order/amzod/api/orderDetails/productInformation"
MCF_LOGISTICS_ENDPOINT = "/order/amzod/api/orderDetails/logisticsInformation"
MCF_RETURN_ENDPOINT = "/order/amzod/api/orderDetails/returnInformation"
MCF_TRANSACTION_ENDPOINT = "/basicOpen/openapi/salesOrder/multi-channel/list/transaction"
MCF_DETAIL_BATCH_SIZE = 200
MCF_MAX_PAGE_SIZE = 1000
MCF_MAX_RECORDS = 5000


class MultiChannelOrderClient(Protocol):
    def post_json(
        self,
        path: str,
        json_body: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> dict[str, Any]: ...


@dataclass(frozen=True, slots=True)
class MultiChannelOrderQuery:
    sids: list[int]
    start_date: str
    end_date: str
    date_type: int = 1
    order_status: list[str] | None = None
    amazon_order_id: str | None = None
    seller_fulfillment_order_id: str | None = None
    include_product_detail: bool = False
    include_logistics_detail: bool = False
    include_transaction_detail: bool = False
    include_return_detail: bool = False
    page_size: int = 200
    max_records: int = 1000


def query_multi_channel_orders(client: MultiChannelOrderClient, query: MultiChannelOrderQuery) -> dict[str, Any]:
    _validate_query(query)
    page = _fetch_order_list(client, query)
    records = _normalize_records(page.rows)
    records, filter_warnings = _filter_exact_ids(records, query)
    warnings = list(filter_warnings)
    if page.total is not None and len(page.rows) < page.total:
        warnings.append("结果已按 max_records 截断；请缩小日期范围或提高 max_records 后分批查询。")

    requested_endpoints = [MCF_ORDER_LIST_ENDPOINT]
    order_infos = _order_infos(records)
    if order_infos:
        if query.include_product_detail:
            _attach_batch_detail(client, records, order_infos, MCF_PRODUCT_ENDPOINT, "product_detail")
            requested_endpoints.append(MCF_PRODUCT_ENDPOINT)
        if query.include_logistics_detail:
            _attach_batch_detail(client, records, order_infos, MCF_LOGISTICS_ENDPOINT, "logistics_detail")
            requested_endpoints.append(MCF_LOGISTICS_ENDPOINT)
        if query.include_return_detail:
            _attach_batch_detail(client, records, order_infos, MCF_RETURN_ENDPOINT, "return_detail")
            requested_endpoints.append(MCF_RETURN_ENDPOINT)
        if query.include_transaction_detail:
            _attach_transaction_detail(client, records)
            requested_endpoints.append(MCF_TRANSACTION_ENDPOINT)
    elif _detail_requested(query):
        warnings.append("当前列表结果缺少 sid + seller_fulfillment_order_id，未执行商品/物流/退换货详情补充。")

    return {
        "ok": True,
        "data": {
            "records": records,
            "count": len(records),
            "total": page.total,
        },
        "meta": {
            "endpoint": MCF_ORDER_LIST_ENDPOINT,
            "endpoints": _unique_strings(requested_endpoints),
            "page_count": page.page_count,
            "request_ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sid": None,
            "sids": query.sids,
            "date_range": f"{query.start_date}~{query.end_date}",
            "date_type": query.date_type,
            "page_size": query.page_size,
            "max_records": query.max_records,
            "docs_path": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_MCFOrderList.md",
            "detail_docs": {
                "product": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_ProductInformation.md",
                "logistics": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_LogisticsInformation.md",
                "return": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_ReturnInfomation.md",
                "transaction": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_MutilChannelTransactionDetail.md",
            },
        },
        "warnings": warnings,
    }


def _validate_query(query: MultiChannelOrderQuery) -> None:
    if not query.sids:
        raise LingxingConfigError("缺少必要参数: sids")
    if not query.start_date or not query.end_date:
        raise LingxingConfigError("缺少必要参数: start_date/end_date；为避免默认拉取最近 6 个月，多渠道订单工具必须显式传日期范围。")
    if query.page_size < 1 or query.page_size > MCF_MAX_PAGE_SIZE:
        raise LingxingConfigError(f"page_size 必须在 1 到 {MCF_MAX_PAGE_SIZE} 之间")
    if query.max_records < 1 or query.max_records > MCF_MAX_RECORDS:
        raise LingxingConfigError(f"max_records 必须在 1 到 {MCF_MAX_RECORDS} 之间")


def _fetch_order_list(client: MultiChannelOrderClient, query: MultiChannelOrderQuery) -> PagedRows:
    body: dict[str, Any] = {
        "sids": query.sids,
        "start_date": query.start_date,
        "end_date": query.end_date,
        "date_type": query.date_type,
    }
    if query.order_status:
        body["order_status"] = query.order_status

    offset = 0
    rows: list[dict[str, Any]] = []
    total: int | None = None
    page_count = 0
    while offset < query.max_records:
        page_length = min(query.page_size, query.max_records - offset)
        payload = client.post_json(MCF_ORDER_LIST_ENDPOINT, {**body, "offset": offset, "length": page_length})
        data = extract_path_value(payload, "data.records") or []
        if not isinstance(data, list):
            raise LingxingConfigError(f"{MCF_ORDER_LIST_ENDPOINT} 返回 data.records 不是数组")
        rows.extend(dict(row) if isinstance(row, dict) else {"value": row} for row in data)
        page_count += 1
        total_raw = extract_path_value(payload, "data.total")
        total = int(total_raw) if total_raw not in (None, "") else len(rows)
        offset += len(data)
        if not data or offset >= total:
            break
    return PagedRows(rows=rows, page_count=page_count, total=total)


def _normalize_records(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for row in rows:
        record = dict(row)
        record.setdefault("items", record.get("listing_info") or [])
        records.append(record)
    return records


def _filter_exact_ids(records: list[dict[str, Any]], query: MultiChannelOrderQuery) -> tuple[list[dict[str, Any]], list[str]]:
    filtered = records
    warnings: list[str] = []
    if query.amazon_order_id:
        filtered = [row for row in filtered if str(row.get("amazon_order_id") or "").strip() == query.amazon_order_id]
    if query.seller_fulfillment_order_id:
        filtered = [
            row
            for row in filtered
            if str(row.get("seller_fulfillment_order_id") or "").strip() == query.seller_fulfillment_order_id
        ]
    if len(filtered) != len(records):
        warnings.append("amazon_order_id / seller_fulfillment_order_id 是列表结果后的精确过滤；领星列表接口本身不支持按订单号搜索。")
    return filtered, warnings


def _detail_requested(query: MultiChannelOrderQuery) -> bool:
    return query.include_product_detail or query.include_logistics_detail or query.include_return_detail


def _order_infos(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    infos: list[dict[str, Any]] = []
    seen: set[str] = set()
    for record in records:
        sid = record.get("sid")
        seller_order_id = str(record.get("seller_fulfillment_order_id") or "").strip()
        if sid in (None, "") or not seller_order_id:
            continue
        key = _order_key(sid, seller_order_id)
        if key in seen:
            continue
        seen.add(key)
        infos.append({"sid": int(sid), "seller_fulfillment_order_id": seller_order_id})
    return infos


def _attach_batch_detail(
    client: MultiChannelOrderClient,
    records: list[dict[str, Any]],
    order_infos: list[dict[str, Any]],
    endpoint: str,
    field_name: str,
) -> None:
    detail_by_key: dict[str, dict[str, Any]] = {}
    for index in range(0, len(order_infos), MCF_DETAIL_BATCH_SIZE):
        batch = order_infos[index:index + MCF_DETAIL_BATCH_SIZE]
        payload = client.post_json(endpoint, {"order_info": batch})
        data = payload.get("data") or []
        if not isinstance(data, list):
            raise LingxingConfigError(f"{endpoint} 返回 data 不是数组")
        for detail in data:
            if isinstance(detail, dict):
                key = _order_key(detail.get("sid"), detail.get("seller_fulfillment_order_id"))
                detail_by_key[key] = detail
    for record in records:
        record[field_name] = detail_by_key.get(_order_key(record.get("sid"), record.get("seller_fulfillment_order_id")))


def _attach_transaction_detail(client: MultiChannelOrderClient, records: list[dict[str, Any]]) -> None:
    for record in records:
        amazon_order_id = str(record.get("amazon_order_id") or "").strip()
        sid = record.get("sid")
        if not amazon_order_id or sid in (None, ""):
            record["transaction_detail"] = None
            continue
        payload = client.post_json(MCF_TRANSACTION_ENDPOINT, {"sid": int(sid), "amazonOrderId": amazon_order_id})
        record["transaction_detail"] = payload.get("data") or {}


def _order_key(sid: Any, seller_fulfillment_order_id: Any) -> str:
    return f"{sid}|{str(seller_fulfillment_order_id or '').strip()}"


def _unique_strings(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result
