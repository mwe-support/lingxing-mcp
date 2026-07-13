"""Business-oriented LingXing service layer shared by scripts and MCP."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .ad_management import AD_OPERATION_LOGS_ENDPOINT, AdManagementRequest
from .client import DEFAULT_TOKEN_CACHE, LingxingOpenAPIClient, DownloadedFile, extract_path_value
from .endpoint_specs import ENDPOINT_SPECS_BY_NAME, EndpointSpec
from .errors import LingxingClientError, LingxingConfigError
from .multi_channel_orders import MultiChannelOrderQuery, query_multi_channel_orders
from .promotions import (
    active_promotions_for_target,
    build_promotion_windows,
    classify_coupon_activity,
    pick_deal_label,
    pick_discount_label,
    pick_manage_label,
    serialize_promotion_window,
)
from .timezones import get_timezone, get_timezone_name


def _now_text() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def _listify_ints(values: Any) -> list[int]:
    if values in (None, ""):
        return []
    if isinstance(values, list):
        return [int(value) for value in values]
    return [int(values)]


def _listify_strings(values: Any) -> list[str]:
    if values in (None, ""):
        return []
    if isinstance(values, list):
        return [str(value) for value in values]
    return [str(values)]


REGION_CODE_MAP = {
    "US": "na",
    "CA": "na",
    "MX": "na",
    "BR": "na",
    "ES": "eu",
    "UK": "eu",
    "FR": "eu",
    "BE": "eu",
    "NL": "eu",
    "DE": "eu",
    "IT": "eu",
    "SE": "eu",
    "ZA": "eu",
    "PL": "eu",
    "EG": "eu",
    "TR": "eu",
    "SA": "eu",
    "AE": "eu",
    "IN": "eu",
    "SG": "fe",
    "AU": "fe",
    "JP": "fe",
}

ASIN_PRODUCT_SNAPSHOT_MAX_ASINS = 50


def _parse_iso_date(value: str) -> datetime.date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _iso_day_range(start_date: str, end_date: str) -> list[str]:
    start = _parse_iso_date(start_date)
    end = _parse_iso_date(end_date)
    days: list[str] = []
    current = start
    while current <= end:
        days.append(current.isoformat())
        current += timedelta(days=1)
    return days


def _week_start_text(value: str) -> str:
    day = _parse_iso_date(value)
    return (day - timedelta(days=day.weekday())).isoformat()


def _sum_number(rows: list[dict[str, Any]], key: str) -> float:
    total = 0.0
    for row in rows:
        try:
            total += float(row.get(key) or 0)
        except (TypeError, ValueError):
            continue
    return total


def _number_value(value: Any, default: float = 0.0) -> float:
    if value in (None, ""):
        return default
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _int_value(value: Any, default: int = 0) -> int:
    return int(_number_value(value, float(default)))


def _first_non_empty(*values: Any) -> Any:
    for value in values:
        if value not in (None, ""):
            return value
    return None


@dataclass
class LingxingResult:
    ok: bool
    data: Any
    meta: dict[str, Any]
    warnings: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "data": self.data,
            "meta": self.meta,
            "warnings": self.warnings,
        }


class LingxingOpenAPIService:
    """Business-oriented service layer with normalized outputs."""

    def __init__(self, client: LingxingOpenAPIClient | None = None) -> None:
        self._client = client

    @property
    def client(self) -> LingxingOpenAPIClient:
        if self._client is None:
            self._client = LingxingOpenAPIClient()
        return self._client

    def _result(
        self,
        *,
        data: Any,
        endpoint: str,
        page_count: int = 1,
        warnings: list[str] | None = None,
        sid: int | None = None,
        date_range: str | None = None,
        extra_meta: dict[str, Any] | None = None,
        ok: bool = True,
    ) -> dict[str, Any]:
        meta: dict[str, Any] = {
            "endpoint": endpoint,
            "page_count": page_count,
            "request_ts": _now_text(),
            "sid": sid,
            "date_range": date_range,
        }
        if extra_meta:
            meta.update(extra_meta)
        return LingxingResult(ok=ok, data=data, meta=meta, warnings=warnings or []).to_dict()

    def _normalize_large_report_options(self, response_mode: str, preview_limit: int) -> tuple[str, int]:
        normalized_mode = str(response_mode or "summary").strip().lower()
        if normalized_mode not in {"summary", "full"}:
            raise LingxingConfigError("response_mode 必须为 summary 或 full")
        if preview_limit < 0 or preview_limit > 100:
            raise LingxingConfigError("preview_limit 必须在 0 到 100 之间")
        return normalized_mode, preview_limit

    def _large_report_data(
        self,
        rows: list[dict[str, Any]],
        *,
        response_mode: str,
        preview_limit: int,
        warnings: list[str],
    ) -> dict[str, Any]:
        normalized_mode, preview_limit = self._normalize_large_report_options(response_mode, preview_limit)

        records = rows if normalized_mode == "full" else rows[:preview_limit]
        truncated = len(records) < len(rows)
        if truncated:
            warnings.append(
                f"摘要模式仅返回前 {len(records)} 条预览，共 {len(rows)} 条；"
                "生成 Excel 时请由本地导出器使用 response_mode=full。"
            )
        return {
            "records": records,
            "record_count": len(rows),
            "returned_count": len(records),
            "truncated": truncated,
        }

    def health_check(self) -> dict[str, Any]:
        env_status = {
            "LINGXING_APP_ID": bool(os.getenv("LINGXING_APP_ID", "").strip()),
            "LINGXING_APP_SECRET": bool(os.getenv("LINGXING_APP_SECRET", "").strip()),
            "LINGXING_TOKEN_CACHE_FILE": bool(os.getenv("LINGXING_TOKEN_CACHE_FILE", "").strip()),
            "LINGXING_MCP_BEARER_TOKEN": bool(os.getenv("LINGXING_MCP_BEARER_TOKEN", "").strip()),
            "LINGXING_DOC_ACCESS_KEY": bool(os.getenv("LINGXING_DOC_ACCESS_KEY", "").strip()),
        }
        cache_path = Path(os.getenv("LINGXING_TOKEN_CACHE_FILE", "")).expanduser() if os.getenv("LINGXING_TOKEN_CACHE_FILE", "").strip() else DEFAULT_TOKEN_CACHE
        cached_exists = cache_path.exists()
        data: dict[str, Any] = {
            "env": env_status,
            "token_cache": {
                "path": str(cache_path),
                "exists": cached_exists,
            },
            "connectivity": {
                "auth_ok": False,
                "message": "未执行",
            },
        }
        warnings: list[str] = []
        ok = env_status["LINGXING_APP_ID"] and env_status["LINGXING_APP_SECRET"]
        if ok:
            try:
                cached = self.client.get_cached_token()
                if cached:
                    data["token_cache"]["expires_at"] = cached.expires_at
                    data["token_cache"]["refresh_token_present"] = bool(cached.refresh_token)
                bundle = self.client.ensure_access_token()
                data["connectivity"] = {
                    "auth_ok": True,
                    "message": "access_token 获取成功",
                    "expires_at": bundle.expires_at,
                }
            except LingxingClientError as exc:
                ok = False
                data["connectivity"] = {
                    "auth_ok": False,
                    "message": exc.message,
                }
                data["error"] = exc.to_dict()
                warnings.append(str(exc))
        else:
            warnings.append("缺少领星 App ID 或 App Secret，无法完成鉴权连通性检查。")
        return self._result(
            data=data,
            endpoint="/api/auth-server/oauth/access-token",
            warnings=warnings,
            extra_meta={"mode": "health_check"},
            ok=ok,
        )

    def marketplaces(self) -> dict[str, Any]:
        endpoint = "/erp/sc/data/seller/allMarketplace"
        payload = self.client.get_json(endpoint)
        rows = payload.get("data") or []
        enriched: list[dict[str, Any]] = []
        for row in rows:
            item = dict(row)
            code = str(item.get("code") or "")
            item["timezone"] = get_timezone_name(code)
            enriched.append(item)
        return self._result(data=enriched, endpoint=endpoint)

    def seller_lists(self, status: int | None = None, marketplace: str | None = None) -> dict[str, Any]:
        endpoint = "/erp/sc/data/seller/lists"
        sellers = self.client.get_json(endpoint).get("data") or []
        marketplaces = {
            int(item.get("mid") or 0): item
            for item in self.marketplaces()["data"]
        }
        filtered: list[dict[str, Any]] = []
        marketplace_filter = str(marketplace or "").strip().upper()
        for row in sellers:
            item = dict(row)
            marketplace_row = marketplaces.get(int(item.get("mid") or 0), {})
            code = str(marketplace_row.get("code") or "")
            item["marketplace_code"] = code
            item["timezone"] = get_timezone_name(code)
            if status is not None and int(item.get("status") or 0) != int(status):
                continue
            if marketplace_filter and code.upper() != marketplace_filter:
                continue
            filtered.append(item)
        return self._result(
            data=filtered,
            endpoint=endpoint,
            extra_meta={"marketplace_filter": marketplace_filter or None},
        )

    def store_sales(self, sid: int, start_date: str, end_date: str) -> dict[str, Any]:
        endpoint = "/erp/sc/data/sales_report/sales"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "sid": sid,
                "start_date": start_date,
                "end_date": end_date,
                "offset": 0,
                "length": 1000,
            },
            page_size=1000,
        )
        return self._result(
            data=page.rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
        )

    def asin_daily_lists(self, sid: int, event_date: str, metric_type: int, asin_type: int = 1) -> dict[str, Any]:
        endpoint = "/erp/sc/data/sales_report/asinDailyLists"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "sid": sid,
                "event_date": event_date,
                "asin_type": asin_type,
                "type": metric_type,
                "offset": 0,
                "length": 1000,
            },
            page_size=1000,
        )
        return self._result(
            data=page.rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=event_date,
            extra_meta={"metric_type": metric_type, "asin_type": asin_type},
        )

    def orders(self, sid: int, start_date: str, end_date: str, date_type: int = 1) -> dict[str, Any]:
        endpoint = "/erp/sc/data/mws/orders"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "sid": sid,
                "start_date": start_date,
                "end_date": end_date,
                "date_type": date_type,
                "offset": 0,
                "length": 5000,
            },
            page_size=5000,
        )
        return self._result(
            data=page.rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
            extra_meta={"date_type": date_type},
        )

    def order_details(self, order_id: str | None = None, order_ids: Any = None) -> dict[str, Any]:
        endpoint = "/erp/sc/data/mws/orderDetail"
        requested_values: list[str] = []

        def collect(value: Any) -> None:
            if value in (None, ""):
                return
            if isinstance(value, list):
                for item in value:
                    collect(item)
                return
            text = str(value).replace("，", ",").replace(";", ",").replace("\n", ",")
            for part in text.split(","):
                order_text = part.strip()
                if order_text:
                    requested_values.append(order_text)

        collect(order_id)
        collect(order_ids)

        normalized_order_ids: list[str] = []
        seen: set[str] = set()
        for value in requested_values:
            if value not in seen:
                normalized_order_ids.append(value)
                seen.add(value)

        if not normalized_order_ids:
            raise LingxingConfigError("缺少必要参数: order_id 或 order_ids")
        if len(normalized_order_ids) > 1000:
            raise LingxingConfigError("order_details 单次最多查询 1000 个订单号；领星接口每批最多 200 个，服务端会自动分批")

        rows: list[dict[str, Any]] = []
        chunk_size = 200
        for index in range(0, len(normalized_order_ids), chunk_size):
            chunk = normalized_order_ids[index:index + chunk_size]
            payload = self.client.post_json(endpoint, {"order_id": ",".join(chunk)})
            data = payload.get("data") or []
            if isinstance(data, dict):
                data = [data]
            if not isinstance(data, list):
                raise LingxingConfigError(f"{endpoint} 返回 data 不是数组或对象")
            for row in data:
                rows.append(dict(row) if isinstance(row, dict) else {"value": row})

        warnings: list[str] = []
        store_by_sid: dict[int, dict[str, Any]] = {}
        order_sids = {
            int(row.get("sid"))
            for row in rows
            if isinstance(row, dict) and str(row.get("sid") or "").isdigit()
        }
        if order_sids:
            try:
                seller_rows = self.seller_lists().get("data") or []
                for seller in seller_rows:
                    sid_value = seller.get("sid")
                    if str(sid_value or "").isdigit():
                        sid_int = int(sid_value)
                        if sid_int in order_sids:
                            store_by_sid[sid_int] = dict(seller)
            except LingxingClientError as exc:
                warnings.append("订单已返回，但店铺列表查询失败，未能补充店铺名。" + f" {exc.message}")

        stores: list[dict[str, Any]] = []
        for sid_value in sorted(order_sids):
            seller = store_by_sid.get(sid_value, {})
            store_name = str(
                seller.get("name")
                or seller.get("store_name")
                or seller.get("seller_name")
                or seller.get("account_name")
                or ""
            ).strip()
            stores.append({
                "sid": sid_value,
                "store_name": store_name or None,
                "marketplace_code": seller.get("marketplace_code"),
                "timezone": seller.get("timezone"),
                "status": seller.get("status"),
            })

        for row in rows:
            if not isinstance(row, dict):
                continue
            sid_text = str(row.get("sid") or "")
            if not sid_text.isdigit():
                continue
            seller = store_by_sid.get(int(sid_text), {})
            store_name = str(
                seller.get("name")
                or seller.get("store_name")
                or seller.get("seller_name")
                or seller.get("account_name")
                or ""
            ).strip()
            row["store_name"] = store_name or None
            row["marketplace_code"] = seller.get("marketplace_code")
            row["store_timezone"] = seller.get("timezone")

        found_order_ids = {
            str(row.get("amazon_order_id") or row.get("order_id") or "").strip()
            for row in rows
            if isinstance(row, dict) and str(row.get("amazon_order_id") or row.get("order_id") or "").strip()
        }
        missing_order_ids = [order for order in normalized_order_ids if order not in found_order_ids]
        if missing_order_ids:
            warnings.append("部分订单号未在 orderDetail 返回结果中匹配。")

        return self._result(
            data={
                "requested_order_ids": normalized_order_ids,
                "found_order_ids": [order for order in normalized_order_ids if order in found_order_ids],
                "missing_order_ids": missing_order_ids,
                "found_count": len(rows),
                "stores": stores,
                "orders": rows,
            },
            endpoint=endpoint,
            page_count=(len(normalized_order_ids) + chunk_size - 1) // chunk_size,
            warnings=warnings,
            extra_meta={
                "docs_path": "skills/zach-lingxing-openapi-client/references/openapi_docs/Sale_OrderDetail.md",
                "request_chunk_size": chunk_size,
                "max_order_ids": 1000,
                "upstream_max_order_ids_per_request": 200,
            },
        )

    def multi_channel_orders(self, query: MultiChannelOrderQuery) -> dict[str, Any]:
        return query_multi_channel_orders(self.client, query)

    def promotion_listing(
        self,
        sid: int,
        site_date: str,
        start_time: str,
        end_time: str,
        *,
        status: list[int] | None = None,
        product_status: list[int] | None = None,
        promotion_category: list[int] | None = None,
    ) -> dict[str, Any]:
        endpoint = "/basicOpen/promotion/listingList"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "site_date": site_date,
                "start_time": start_time,
                "end_time": end_time,
                "offset": 0,
                "length": 200,
                "sids": [sid],
                "status": status or [0, 1, 2, 3],
                "product_status": product_status or [1],
                "promotion_category": promotion_category or [1, 2, 3, 4],
            },
            page_size=200,
        )
        return self._result(
            data=page.rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_time}~{end_time}",
            extra_meta={"site_date": site_date},
        )

    def promotion_sec_kill(self, sid: int, start_date: str, end_date: str) -> dict[str, Any]:
        endpoint = "/basicOpen/promotionalActivities/secKill/list"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "start_date": start_date,
                "end_date": end_date,
                "sids": [sid],
                "offset": 0,
                "length": 200,
            },
            page_size=200,
        )
        rows = []
        for row in page.rows:
            item = dict(row)
            item["promotion_label"] = pick_deal_label(item.get("promotion_type"))
            rows.append(item)
        return self._result(
            data=rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
        )

    def promotion_manage(self, sid: int, start_date: str, end_date: str) -> dict[str, Any]:
        endpoint = "/basicOpen/promotionalActivities/manage/list"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "start_date": start_date,
                "end_date": end_date,
                "sids": [sid],
                "offset": 0,
                "length": 200,
            },
            page_size=200,
        )
        rows = []
        for row in page.rows:
            item = dict(row)
            item["promotion_label"] = pick_manage_label(item.get("promotion_type"))
            rows.append(item)
        return self._result(
            data=rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
        )

    def promotion_vip_discount(self, sid: int, start_date: str, end_date: str) -> dict[str, Any]:
        endpoint = "/basicOpen/promotionalActivities/vipDiscount/list"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "start_date": start_date,
                "end_date": end_date,
                "sids": [sid],
                "offset": 0,
                "length": 200,
            },
            page_size=200,
        )
        rows = []
        for row in page.rows:
            item = dict(row)
            item["promotion_label"] = pick_discount_label(item.get("customer_target"))
            rows.append(item)
        return self._result(
            data=rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
        )

    def promotion_coupon(self, sid: int, start_date: str, end_date: str) -> dict[str, Any]:
        endpoint = "/basicOpen/promotionalActivities/coupon/list"
        page = self.client.paged_post_detailed(
            endpoint,
            {
                "start_date": start_date,
                "end_date": end_date,
                "sids": [sid],
                "offset": 0,
                "length": 200,
            },
            page_size=200,
        )
        rows = []
        for row in page.rows:
            item = dict(row)
            item["promotion_label"] = classify_coupon_activity(item)
            rows.append(item)
        return self._result(
            data=rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{start_date}~{end_date}",
        )

    def resolve_daily_promotions(self, sid: int, target_date: str, lookback_days: int = 90) -> dict[str, Any]:
        target = datetime.strptime(target_date, "%Y-%m-%d").date()
        window_start = (target - timedelta(days=max(1, int(lookback_days) - 1))).isoformat()
        listing = self.promotion_listing(
            sid,
            target_date,
            window_start,
            target_date,
            status=[0, 1, 2, 3],
            product_status=[1],
            promotion_category=[1, 2, 3, 4],
        )
        sec_kill = self.promotion_sec_kill(sid, window_start, target_date)
        manage = self.promotion_manage(sid, window_start, target_date)
        discount = self.promotion_vip_discount(sid, window_start, target_date)
        coupon = self.promotion_coupon(sid, window_start, target_date)

        sec_kill_map = {str(row.get("promotion_id") or ""): row for row in sec_kill["data"]}
        manage_map = {str(row.get("promotion_id") or ""): row for row in manage["data"]}
        discount_map = {str(row.get("promotion_id") or ""): row for row in discount["data"]}
        windows_by_asin, asin_meta = build_promotion_windows(
            listing["data"],
            sec_kill_map,
            manage_map,
            discount_map,
        )

        site_now = datetime.combine(target, datetime.max.time())
        rows: list[dict[str, Any]] = []
        warnings: list[str] = []
        for asin in sorted(set(asin_meta) | set(windows_by_asin)):
            active_windows = active_promotions_for_target(
                windows_by_asin.get(asin, []),
                target,
                site_now,
                True,
            )
            if not active_windows:
                continue
            labels = sorted({window.label for window in active_windows})
            if any(label.endswith(".generic") or label == "promotion.unknown" for label in labels):
                warnings.append(f"{asin} 存在无法细分的促销标签: {','.join(labels)}")
            rows.append(
                {
                    **asin_meta.get(asin, {"asin": asin}),
                    "promotion_labels": labels,
                    "promotions": [serialize_promotion_window(window) for window in active_windows],
                }
            )

        return self._result(
            data=rows,
            endpoint="resolve_daily_promotions",
            page_count=(
                int(listing["meta"]["page_count"])
                + int(sec_kill["meta"]["page_count"])
                + int(manage["meta"]["page_count"])
                + int(discount["meta"]["page_count"])
                + int(coupon["meta"]["page_count"])
            ),
            sid=sid,
            date_range=target_date,
            warnings=sorted(set(warnings)),
            extra_meta={
                "endpoints": [
                    listing["meta"]["endpoint"],
                    sec_kill["meta"]["endpoint"],
                    manage["meta"]["endpoint"],
                    discount["meta"]["endpoint"],
                    coupon["meta"]["endpoint"],
                ]
            },
        )

    def fba_warehouse_detail(
        self,
        *,
        sid: int,
        search_field: str = "asin",
        search_value: str | None = None,
        page_size: int = 200,
        cid: str | None = None,
        bid: str | None = None,
        attribute: str | None = None,
        asin_principal: str | None = None,
        status: str | None = None,
        senior_search_list: str | None = None,
        fulfillment_channel_type: str = "FBA",
        is_hide_zero_stock: str = "0",
        is_parant_asin_merge: str = "0",
        is_contain_del_ls: str = "0",
        query_fba_storage_quantity_list: bool | None = None,
    ) -> dict[str, Any]:
        endpoint = "/basicOpen/openapi/storage/fbaWarehouseDetail"
        normalized_page_size = max(20, min(int(page_size or 200), 200))
        body: dict[str, Any] = {
            "offset": 0,
            "length": normalized_page_size,
            "sid": str(sid),
            "search_field": str(search_field or "asin"),
            "fulfillment_channel_type": str(fulfillment_channel_type or "FBA"),
            "is_hide_zero_stock": str(is_hide_zero_stock if is_hide_zero_stock not in (None, "") else "0"),
            "is_parant_asin_merge": str(is_parant_asin_merge if is_parant_asin_merge not in (None, "") else "0"),
            "is_contain_del_ls": str(is_contain_del_ls if is_contain_del_ls not in (None, "") else "0"),
        }
        if search_value not in (None, ""):
            body["search_value"] = str(search_value)
        for key, value in {
            "cid": cid,
            "bid": bid,
            "attribute": attribute,
            "asin_principal": asin_principal,
            "status": status,
            "senior_search_list": senior_search_list,
        }.items():
            if value not in (None, ""):
                body[key] = str(value)
        if query_fba_storage_quantity_list is not None:
            body["query_fba_storage_quantity_list"] = bool(query_fba_storage_quantity_list)

        page = self.client.paged_post_detailed(endpoint, body, page_size=normalized_page_size)
        return self._result(
            data=page.rows,
            endpoint=endpoint,
            page_count=page.page_count,
            sid=int(sid),
            extra_meta={
                "docs_path": "docs/Warehouse/FBAStock_v2.md",
                "filters": body,
                "total": page.total,
            },
        )

    def asin_product_snapshot(
        self,
        *,
        sid: int,
        asin: str | None = None,
        asins: list[str] | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
    ) -> dict[str, Any]:
        asin_values, batch_mode = self._normalize_snapshot_asin_input(asin=asin, asins=asins)
        normalized_start_date, normalized_end_date = self._normalize_snapshot_date_range(start_date, end_date)
        items, warnings, page_count, endpoints = self._asin_product_snapshot_items(
            sid=sid,
            asins=asin_values,
            start_date=normalized_start_date,
            end_date=normalized_end_date,
        )

        if batch_mode:
            data = {
                "sid": int(sid),
                "asins": asin_values,
                "date_range": {"start_date": normalized_start_date, "end_date": normalized_end_date},
                "items": items,
                "warnings": sorted(set(warnings)),
            }
            return self._result(
                data=data,
                endpoint="asin_product_snapshot",
                page_count=page_count,
                sid=int(sid),
                date_range=f"{normalized_start_date}~{normalized_end_date}",
                warnings=sorted(set(warnings)),
                extra_meta={
                    "endpoints": endpoints,
                    "input_mode": "batch",
                    "max_asins": ASIN_PRODUCT_SNAPSHOT_MAX_ASINS,
                    "inventory_scope": "FBA only; FBM quantity is intentionally excluded.",
                    "sales_source": "productPerformance.volume",
                },
            )

        data = items[0] if items else self._empty_asin_product_snapshot_item(
            sid=int(sid),
            asin=asin_values[0],
            start_date=normalized_start_date,
            end_date=normalized_end_date,
        )
        if not data.get("per_sku"):
            warnings.append("No SKU rows were available from FBAStock_v2 or productPerformance.")
        return self._result(
            data=data,
            endpoint="asin_product_snapshot",
            page_count=page_count,
            sid=int(sid),
            date_range=f"{normalized_start_date}~{normalized_end_date}",
            warnings=sorted(set(warnings)),
            extra_meta={
                "endpoints": endpoints,
                "input_mode": "single",
                "max_asins": ASIN_PRODUCT_SNAPSHOT_MAX_ASINS,
                "inventory_scope": "FBA only; FBM quantity is intentionally excluded.",
                "sales_source": "productPerformance.volume",
            },
        )

    def _normalize_snapshot_asin_input(self, *, asin: str | None, asins: list[str] | None) -> tuple[list[str], bool]:
        has_asin = str(asin or "").strip() != ""
        asin_list = [
            str(value or "").strip().upper()
            for value in (asins or [])
            if str(value or "").strip()
        ]
        if has_asin and asin_list:
            raise LingxingConfigError("asin_product_snapshot accepts either asin or asins, not both")
        if has_asin:
            return [str(asin or "").strip().upper()], False
        if not asin_list:
            raise LingxingConfigError("asin_product_snapshot requires asin or asins")
        deduped = list(dict.fromkeys(asin_list))
        if len(deduped) > ASIN_PRODUCT_SNAPSHOT_MAX_ASINS:
            raise LingxingConfigError(
                f"asin_product_snapshot accepts at most {ASIN_PRODUCT_SNAPSHOT_MAX_ASINS} ASINs per call; "
                "split larger jobs into serial batches of 50 or fewer ASINs"
            )
        return deduped, True

    def _normalize_snapshot_date_range(self, start_date: str | None, end_date: str | None) -> tuple[str, str]:
        if end_date in (None, ""):
            end_day = datetime.now().date() - timedelta(days=1)
            normalized_end_date = end_day.isoformat()
        else:
            normalized_end_date = str(end_date).strip()
            end_day = _parse_iso_date(normalized_end_date)
        if start_date in (None, ""):
            start_day = end_day - timedelta(days=29)
            normalized_start_date = start_day.isoformat()
        else:
            normalized_start_date = str(start_date).strip()
            start_day = _parse_iso_date(normalized_start_date)
        if start_day > end_day:
            raise LingxingConfigError("start_date must be on or before end_date")
        return normalized_start_date, normalized_end_date

    def _asin_product_snapshot_items(
        self,
        *,
        sid: int,
        asins: list[str],
        start_date: str,
        end_date: str,
    ) -> tuple[list[dict[str, Any]], list[str], int, list[str | None]]:
        warnings: list[str] = []
        asin_set = set(asins)

        if len(asins) == 1:
            fba_result = self.fba_warehouse_detail(
                sid=sid,
                search_field="asin",
                search_value=asins[0],
                page_size=200,
                fulfillment_channel_type="FBA",
                is_hide_zero_stock="0",
                is_parant_asin_merge="0",
                is_contain_del_ls="0",
            )
        else:
            fba_result = self.fba_warehouse_detail(
                sid=sid,
                search_field="asin",
                page_size=200,
                senior_search_list=json.dumps(
                    [{"name": "ASIN", "search_field": "asin", "search_value": asins}],
                    ensure_ascii=False,
                ),
                fulfillment_channel_type="FBA",
                is_hide_zero_stock="0",
                is_parant_asin_merge="0",
                is_contain_del_ls="0",
            )
        fba_rows = [
            dict(row)
            for row in (fba_result.get("data") or [])
            if str(row.get("asin") or "").strip().upper() in asin_set
        ]
        fba_rows_by_asin: dict[str, list[dict[str, Any]]] = {value: [] for value in asins}
        for row in fba_rows:
            row_asin = str(row.get("asin") or "").strip().upper()
            if row_asin in fba_rows_by_asin:
                fba_rows_by_asin[row_asin].append(row)

        performance_result = self.run_endpoint_spec(
            "lingxing_product_performance",
            {
                "sid": sid,
                "start_date": start_date,
                "end_date": end_date,
                "search_field": "asin",
                "search_value": asins,
                "summary_field": "sku",
                "sort_field": "volume",
                "sort_type": "desc",
                "is_recently_enum": False,
                "purchase_status": 0,
            },
        )
        performance_rows = [dict(row) for row in (performance_result.get("data") or [])]
        performance_rows_by_asin: dict[str, list[dict[str, Any]]] = {value: [] for value in asins}
        for row in performance_rows:
            matched_asins = self._snapshot_asins_from_performance_row(row, asin_set)
            for row_asin in matched_asins:
                performance_rows_by_asin.setdefault(row_asin, []).append(row)

        local_skus = sorted(
            {
                str(row.get("sku") or row.get("local_sku") or "").strip()
                for row in [*fba_rows, *performance_rows]
                if str(row.get("sku") or row.get("local_sku") or "").strip()
            }
        )
        local_cost_by_sku: dict[str, dict[str, Any]] = {}
        if local_skus and (
            any(row.get("cg_price") in (None, "") for row in fba_rows)
            or any(row.get("cg_price") in (None, "") for row in performance_rows)
        ):
            try:
                local_cost_result = self.local_product_costs(
                    sku_list=local_skus,
                    include_supplier_quotes=True,
                    include_raw=False,
                )
                for item in local_cost_result.get("data") or []:
                    sku = str(item.get("sku") or "").strip()
                    if sku:
                        local_cost_by_sku[sku] = dict(item)
            except LingxingClientError as exc:
                warnings.append(f"local_product_costs fallback failed: {exc.message}")

        items: list[dict[str, Any]] = []
        for item_asin in asins:
            item, item_warnings = self._build_asin_product_snapshot_item(
                sid=int(sid),
                asin=item_asin,
                start_date=start_date,
                end_date=end_date,
                fba_rows=fba_rows_by_asin.get(item_asin) or [],
                performance_rows=performance_rows_by_asin.get(item_asin) or [],
                local_cost_by_sku=local_cost_by_sku,
            )
            items.append(item)
            warnings.extend(item_warnings)

        page_count = (
            int(fba_result.get("meta", {}).get("page_count") or 0)
            + int(performance_result.get("meta", {}).get("page_count") or 0)
        )
        if local_cost_by_sku:
            page_count += 1
        endpoints = [
            fba_result.get("meta", {}).get("endpoint"),
            performance_result.get("meta", {}).get("endpoint"),
        ]
        if local_cost_by_sku:
            endpoints.append("/erp/sc/routing/data/local_inventory/productList")
        return items, sorted(set(warnings)), page_count, endpoints

    def _snapshot_asins_from_performance_row(self, row: dict[str, Any], asin_set: set[str]) -> list[str]:
        values: set[str] = set()
        for key in ("asin", "seller_asin"):
            text = str(row.get(key) or "").strip().upper()
            if text in asin_set:
                values.add(text)
        for asin_item in row.get("asins") or []:
            text = str((asin_item or {}).get("asin") or "").strip().upper()
            if text in asin_set:
                values.add(text)
        return sorted(values)

    def _build_asin_product_snapshot_item(
        self,
        *,
        sid: int,
        asin: str,
        start_date: str,
        end_date: str,
        fba_rows: list[dict[str, Any]],
        performance_rows: list[dict[str, Any]],
        local_cost_by_sku: dict[str, dict[str, Any]],
    ) -> tuple[dict[str, Any], list[str]]:
        warnings: list[str] = []
        if not fba_rows:
            warnings.append(f"No FBAStock_v2 rows matched sid={sid}, asin={asin}.")
        if not performance_rows:
            warnings.append(f"No productPerformance rows matched sid={sid}, asin={asin}.")

        performance_by_local_sku: dict[str, dict[str, Any]] = {}
        performance_by_seller_sku: dict[str, dict[str, Any]] = {}
        for row in performance_rows:
            sku = str(row.get("sku") or row.get("local_sku") or "").strip()
            if sku:
                performance_by_local_sku.setdefault(sku, row)
            for price_item in row.get("price_list") or []:
                local_sku = str(price_item.get("local_sku") or "").strip()
                seller_sku = str(price_item.get("seller_sku") or "").strip()
                if local_sku:
                    performance_by_local_sku.setdefault(local_sku, row)
                if seller_sku:
                    performance_by_seller_sku.setdefault(seller_sku, row)

        def performance_for(row: dict[str, Any]) -> dict[str, Any] | None:
            local_sku = str(row.get("sku") or "").strip()
            seller_sku = str(row.get("seller_sku") or "").strip()
            return performance_by_local_sku.get(local_sku) or performance_by_seller_sku.get(seller_sku)

        def price_for(perf_row: dict[str, Any] | None, fba_row: dict[str, Any] | None = None) -> dict[str, Any] | None:
            if not perf_row:
                return None
            price_list = [dict(item) for item in (perf_row.get("price_list") or [])]
            if not price_list:
                return None
            local_sku = str((fba_row or {}).get("sku") or "").strip()
            seller_sku = str((fba_row or {}).get("seller_sku") or "").strip()
            sku_matches = [
                item for item in price_list
                if (local_sku and str(item.get("local_sku") or "").strip() == local_sku)
                or (seller_sku and str(item.get("seller_sku") or "").strip() == seller_sku)
            ]
            if sku_matches:
                return sku_matches[0]
            return price_list[0]

        def amazon_url_from(perf_row: dict[str, Any] | None) -> str | None:
            if not perf_row:
                return None
            for asin_item in perf_row.get("asins") or []:
                if str(asin_item.get("asin") or "").upper() == asin and asin_item.get("amazon_url"):
                    return str(asin_item.get("amazon_url"))
            for asin_item in perf_row.get("asins") or []:
                if asin_item.get("amazon_url"):
                    return str(asin_item.get("amazon_url"))
            return None

        sales = {
            "volume": _int_value(sum(_number_value(row.get("volume")) for row in performance_rows)),
            "source": "productPerformance.volume",
        }
        per_sku: list[dict[str, Any]] = []
        for row in fba_rows:
            perf_row = performance_for(row)
            price_item = price_for(perf_row, row)
            local_sku = str(row.get("sku") or "").strip()
            fallback_cost = (local_cost_by_sku.get(local_sku) or {}).get("purchase") or {}
            purchase_amount = _first_non_empty(row.get("cg_price"), fallback_cost.get("cg_price"))
            transport_cost = _first_non_empty(row.get("cg_transport_costs"), fallback_cost.get("cg_transport_costs"))
            inventory = self._snapshot_inventory_from_fba_row(row)
            per_sku.append(
                {
                    "sku": local_sku or None,
                    "seller_sku": row.get("seller_sku"),
                    "fnsku": row.get("fnsku"),
                    "asin": row.get("asin"),
                    "fulfillment_channel": row.get("fulfillment_channel"),
                    "product_name": _first_non_empty(row.get("product_name"), (perf_row or {}).get("local_name"), (perf_row or {}).get("item_name")),
                    "frontend_price": {
                        "amount": (price_item or {}).get("price"),
                        "currency_icon": (perf_row or {}).get("currency_icon"),
                        "source": "productPerformance.price_list.price" if price_item else None,
                    },
                    "purchase_cost": {
                        "amount": purchase_amount,
                        "currency_icon": (fallback_cost.get("primary_supplier_quote") or {}).get("cg_currency_icon") or "\N{YEN SIGN}",
                        "transport_cost": transport_cost,
                        "source": "fbaWarehouseDetail.cg_price" if row.get("cg_price") not in (None, "") else ("local_product_costs.purchase.cg_price" if fallback_cost else None),
                    },
                    "inventory": inventory,
                    "product_link": amazon_url_from(perf_row),
                }
            )

        if not per_sku:
            for perf_row in performance_rows:
                price_item = price_for(perf_row)
                local_sku = str(perf_row.get("sku") or perf_row.get("local_sku") or "").strip()
                fallback_cost = (local_cost_by_sku.get(local_sku) or {}).get("purchase") or {}
                per_sku.append(
                    {
                        "sku": perf_row.get("sku") or perf_row.get("local_sku"),
                        "seller_sku": (price_item or {}).get("seller_sku"),
                        "fnsku": None,
                        "asin": asin,
                        "fulfillment_channel": None,
                        "product_name": _first_non_empty(perf_row.get("local_name"), perf_row.get("item_name")),
                        "frontend_price": {
                            "amount": (price_item or {}).get("price"),
                            "currency_icon": perf_row.get("currency_icon"),
                            "source": "productPerformance.price_list.price" if price_item else None,
                        },
                        "purchase_cost": {
                            "amount": _first_non_empty(
                                perf_row.get("cg_price"),
                                fallback_cost.get("cg_price"),
                            ),
                            "currency_icon": perf_row.get("cg_price_currency_icon") or "\N{YEN SIGN}",
                            "transport_cost": fallback_cost.get("cg_transport_costs"),
                            "source": (
                                "productPerformance.cg_price"
                                if perf_row.get("cg_price") not in (None, "")
                                else (
                                    "local_product_costs.purchase.cg_price"
                                    if fallback_cost
                                    else None
                                )
                            ),
                        },
                        "inventory": self._empty_snapshot_inventory(),
                        "product_link": amazon_url_from(perf_row),
                    }
                )

        representative = per_sku[0] if per_sku else None
        product_link = (representative or {}).get("product_link")
        if not product_link:
            product_link = f"https://www.amazon.com/dp/{asin}"
            warnings.append("No amazon_url found in productPerformance; generated a generic amazon.com dp URL.")

        data = {
            "sid": int(sid),
            "asin": asin,
            "date_range": {"start_date": start_date, "end_date": end_date},
            "product_name": (representative or {}).get("product_name"),
            "product_link": product_link,
            "frontend_price": (representative or {}).get("frontend_price") or {"amount": None, "currency_icon": None, "source": None},
            "purchase_cost": (representative or {}).get("purchase_cost") or {"amount": None, "currency_icon": "\N{YEN SIGN}", "transport_cost": None, "source": None},
            "sales": sales,
            "inventory": self._sum_snapshot_inventory([item.get("inventory") or {} for item in per_sku]),
            "per_sku": per_sku,
        }
        if not per_sku:
            warnings.append("No SKU rows were available from FBAStock_v2 or productPerformance.")
        return data, warnings

    def _empty_asin_product_snapshot_item(
        self,
        *,
        sid: int,
        asin: str,
        start_date: str,
        end_date: str,
    ) -> dict[str, Any]:
        return {
            "sid": int(sid),
            "asin": asin,
            "date_range": {"start_date": start_date, "end_date": end_date},
            "product_name": None,
            "product_link": f"https://www.amazon.com/dp/{asin}",
            "frontend_price": {"amount": None, "currency_icon": None, "source": None},
            "purchase_cost": {"amount": None, "currency_icon": "\N{YEN SIGN}", "transport_cost": None, "source": None},
            "sales": {"volume": 0, "source": "productPerformance.volume"},
            "inventory": self._empty_snapshot_inventory(),
            "per_sku": [],
        }

    def _country_matches(self, requested: str, value: Any) -> bool:
        requested_text = str(requested or "").strip().upper()
        value_text = str(value or "").strip().upper()
        if not requested_text or not value_text:
            return False
        aliases = {
            "US": {"US", "USA", "UNITED STATES", "AMERICA"},
            "CA": {"CA", "CANADA"},
            "MX": {"MX", "MEXICO"},
            "UK": {"UK", "GB", "UNITED KINGDOM"},
            "DE": {"DE", "GERMANY"},
            "FR": {"FR", "FRANCE"},
            "IT": {"IT", "ITALY"},
            "ES": {"ES", "SPAIN"},
            "JP": {"JP", "JAPAN"},
            "AU": {"AU", "AUSTRALIA"},
        }
        requested_aliases = aliases.get(requested_text, {requested_text})
        return value_text in requested_aliases or requested_text == value_text

    def _snapshot_inventory_from_fba_row(self, row: dict[str, Any]) -> dict[str, Any]:
        fba_available = _int_value(row.get("afn_fulfillable_quantity"))
        fba_direct_inbound = _int_value(row.get("stock_up_num"))
        fba_transferring = _int_value(row.get("reserved_fc_processing"))
        fba_researching = _int_value(row.get("afn_researching_quantity"))
        return {
            "fba_available": fba_available,
            "fba_direct_inbound": fba_direct_inbound,
            "fba_transferring": fba_transferring,
            "fba_researching": fba_researching,
            "total_inventory": fba_available + fba_direct_inbound + fba_transferring + fba_researching,
            "source": "fbaWarehouseDetail",
        }

    def _empty_snapshot_inventory(self) -> dict[str, Any]:
        return {
            "fba_available": 0,
            "fba_direct_inbound": 0,
            "fba_transferring": 0,
            "fba_researching": 0,
            "total_inventory": 0,
            "source": "fbaWarehouseDetail",
        }

    def _sum_snapshot_inventory(self, inventories: list[dict[str, Any]]) -> dict[str, Any]:
        keys = ["fba_available", "fba_direct_inbound", "fba_transferring", "fba_researching"]
        totals = {key: sum(_int_value(inventory.get(key)) for inventory in inventories) for key in keys}
        return {
            **totals,
            "total_inventory": sum(totals.values()),
            "source": "fbaWarehouseDetail",
        }

    def local_product_costs(
        self,
        *,
        sku_list: list[str] | None = None,
        sku_identifier_list: list[str] | None = None,
        update_time_start: int | None = None,
        update_time_end: int | None = None,
        create_time_start: int | None = None,
        create_time_end: int | None = None,
        page_size: int = 1000,
        include_supplier_quotes: bool = True,
        include_raw: bool = False,
    ) -> dict[str, Any]:
        endpoint = "/erp/sc/routing/data/local_inventory/productList"
        sku_values = _listify_strings(sku_list)
        sku_identifier_values = _listify_strings(sku_identifier_list)
        if not sku_values and not sku_identifier_values:
            raise LingxingConfigError("local_product_costs requires sku_list or sku_identifier_list to avoid scanning the full product catalog")

        normalized_page_size = max(1, min(int(page_size or 1000), 1000))
        body: dict[str, Any] = {
            "offset": 0,
            "length": normalized_page_size,
        }
        if sku_values:
            body["sku_list"] = sku_values
        if sku_identifier_values:
            body["sku_identifier_list"] = sku_identifier_values
        for key, value in {
            "update_time_start": update_time_start,
            "update_time_end": update_time_end,
            "create_time_start": create_time_start,
            "create_time_end": create_time_end,
        }.items():
            if value not in (None, ""):
                body[key] = int(value)

        page = self.client.paged_post_detailed(endpoint, body, page_size=normalized_page_size)
        rows = [
            self._normalize_local_product_cost_row(
                row,
                include_supplier_quotes=include_supplier_quotes,
                include_raw=include_raw,
            )
            for row in page.rows
        ]
        return self._result(
            data=rows,
            endpoint=endpoint,
            page_count=page.page_count,
            extra_meta={
                "docs_path": "docs/Product/ProductLists.md",
                "filters": {
                    "sku_list": sku_values,
                    "sku_identifier_list": sku_identifier_values,
                    "update_time_start": update_time_start,
                    "update_time_end": update_time_end,
                    "create_time_start": create_time_start,
                    "create_time_end": create_time_end,
                },
                "total": page.total,
            },
        )

    def _normalize_local_product_cost_row(
        self,
        row: dict[str, Any],
        *,
        include_supplier_quotes: bool,
        include_raw: bool,
    ) -> dict[str, Any]:
        supplier_quotes = row.get("supplier_quote") or []
        if not isinstance(supplier_quotes, list):
            supplier_quotes = []
        primary_quote = next(
            (quote for quote in supplier_quotes if str(quote.get("is_primary") or "") == "1"),
            supplier_quotes[0] if supplier_quotes else None,
        )

        item: dict[str, Any] = {
            "id": row.get("id"),
            "sku": row.get("sku"),
            "sku_identifier": row.get("sku_identifier"),
            "product_name": row.get("product_name"),
            "spu": row.get("spu"),
            "category_name": row.get("category_name"),
            "brand_name": row.get("brand_name"),
            "open_status": row.get("open_status"),
            "status": row.get("status"),
            "status_text": row.get("status_text"),
            "purchase": {
                "cg_price": row.get("cg_price"),
                "cg_transport_costs": row.get("cg_transport_costs"),
                "cg_delivery": row.get("cg_delivery"),
                "purchase_remark": row.get("purchase_remark"),
                "cg_opt_uid": row.get("cg_opt_uid"),
                "cg_opt_username": row.get("cg_opt_username"),
                "primary_supplier_quote": self._normalize_supplier_quote(primary_quote) if primary_quote else None,
            },
            "create_time": row.get("create_time"),
            "update_time": row.get("update_time"),
        }
        if include_supplier_quotes:
            item["supplier_quote"] = [self._normalize_supplier_quote(quote) for quote in supplier_quotes]
        if include_raw:
            item["raw"] = row
        return item

    def _normalize_supplier_quote(self, quote: dict[str, Any]) -> dict[str, Any]:
        return {
            "psq_id": quote.get("psq_id"),
            "product_id": quote.get("product_id"),
            "supplier_id": quote.get("supplier_id"),
            "supplier_name": quote.get("supplier_name"),
            "supplier_code": quote.get("supplier_code"),
            "is_primary": quote.get("is_primary"),
            "cg_price": quote.get("cg_price"),
            "cg_currency_icon": quote.get("cg_currency_icon"),
            "supplier_product_url": quote.get("supplier_product_url") or [],
            "quote_remark": quote.get("quote_remark"),
            "quotes": quote.get("quotes") or [],
        }

    def _seller_context(self, sid: int) -> dict[str, Any]:
        seller = next(
            (item for item in self.seller_lists()["data"] if int(item.get("sid") or 0) == int(sid)),
            None,
        )
        if seller is None:
            raise LingxingConfigError(f"找不到 sid={sid} 对应的店铺")
        marketplace_code = str(seller.get("marketplace_code") or "").upper()
        region_code = REGION_CODE_MAP.get(marketplace_code)
        if not region_code:
            raise LingxingConfigError(f"无法从站点 {marketplace_code or 'unknown'} 推导 report_export 区域")
        marketplace_id = seller.get("marketplace_id")
        if not marketplace_id:
            raise LingxingConfigError(f"sid={sid} 缺少 marketplace_id，无法调用 report_export")
        seller_id = str(seller.get("seller_id") or "").strip()
        if not seller_id:
            raise LingxingConfigError(f"sid={sid} 缺少 seller_id")
        return {
            **seller,
            "region_code": region_code,
            "marketplace_code": marketplace_code,
            "marketplace_id": str(marketplace_id),
            "seller_id": seller_id,
        }

    def _select_amazon_sellers(
        self,
        *,
        sids: list[int] | None = None,
        amazon_seller_ids: list[str] | None = None,
    ) -> tuple[list[dict[str, Any]], list[str]]:
        requested_sids = list(dict.fromkeys(_listify_ints(sids)))
        requested_seller_ids = list(dict.fromkeys(_listify_strings(amazon_seller_ids)))
        sid_filter = set(requested_sids)
        seller_id_filter = set(requested_seller_ids)
        explicit_scope = bool(sid_filter or seller_id_filter)
        selected: list[dict[str, Any]] = []
        skipped_without_pair = 0
        skipped_inactive = 0
        for seller in self.seller_lists()["data"]:
            sid = int(seller.get("sid") or 0)
            seller_id = str(seller.get("seller_id") or "").strip()
            if sid_filter and sid not in sid_filter:
                continue
            if seller_id_filter and seller_id not in seller_id_filter:
                continue
            if not explicit_scope and str(seller.get("status") or "") != "1":
                skipped_inactive += 1
                continue
            if not sid or not seller_id:
                skipped_without_pair += 1
                continue
            selected.append({**seller, "sid": sid, "seller_id": seller_id})

        if not sid_filter and not seller_id_filter and skipped_without_pair:
            raise LingxingConfigError(
                "全量查询要求每个店铺同时具备 sid 和 seller_id；"
                f"当前有 {skipped_without_pair} 个店铺缺少配对标识，请修复店铺资料或改用定向筛选。"
            )

        selected_sids = {int(item["sid"]) for item in selected}
        selected_seller_ids = {str(item["seller_id"]) for item in selected}
        missing_sids = sorted(sid_filter - selected_sids)
        missing_seller_ids = sorted(seller_id_filter - selected_seller_ids)
        if missing_sids or missing_seller_ids:
            raise LingxingConfigError(
                "店铺筛选无法匹配 sid 与 seller_id 对应关系："
                f"missing_sids={missing_sids}, missing_seller_ids={missing_seller_ids}"
            )
        if not selected:
            raise LingxingConfigError("没有可用于查询的亚马逊店铺 sid/seller_id 对")

        warnings: list[str] = []
        if skipped_inactive:
            warnings.append(f"全量查询已跳过 {skipped_inactive} 个非启用店铺。")
        if skipped_without_pair:
            warnings.append(f"已跳过 {skipped_without_pair} 个缺少 sid 或 seller_id 的店铺。")
        return selected, warnings

    def shipment_settlement_report(
        self,
        start_date: str,
        end_date: str,
        *,
        sids: list[int] | None = None,
        amazon_seller_ids: list[str] | None = None,
        time_type: str = "04",
        country_codes: list[str] | None = None,
        order_numbers: list[str] | None = None,
        shipment_numbers: list[str] | None = None,
        custom_numbers: list[str] | None = None,
        mskus: list[str] | None = None,
        skus: list[str] | None = None,
        product_names: list[str] | None = None,
        track_codes: list[str] | None = None,
        fulfillment_type: str | None = None,
        response_mode: str = "summary",
        preview_limit: int = 20,
    ) -> dict[str, Any]:
        normalized_mode, preview_limit = self._normalize_large_report_options(response_mode, preview_limit)
        endpoint = "/cost/center/api/settlement/report"
        if time_type not in {"01", "02", "03", "04", "05", "06"}:
            raise LingxingConfigError("time_type 必须为 01 至 06；04 表示结算时间")
        sellers, warnings = self._select_amazon_sellers(
            sids=sids,
            amazon_seller_ids=amazon_seller_ids,
        )
        body: dict[str, Any] = {
            "timeType": time_type,
            "filterBeginDate": start_date,
            "filterEndDate": end_date,
            "offset": 0,
            "length": 1000,
        }
        array_mappings = {
            "countryCodes": country_codes,
            "orderNumbers": order_numbers,
            "shipmentNumbers": shipment_numbers,
            "customNumbers": custom_numbers,
            "mskus": mskus,
            "skus": skus,
            "productNames": product_names,
            "trackCodes": track_codes,
        }
        for body_name, values in array_mappings.items():
            normalized = _listify_strings(values)
            if normalized:
                body[body_name] = normalized
        if fulfillment_type:
            body["fulfillmentType"] = str(fulfillment_type)

        seller_groups: dict[str, list[dict[str, Any]]] = {}
        for seller in sellers:
            group_key = str(seller.get("marketplace_code") or seller.get("mid") or "unknown")
            seller_groups.setdefault(group_key, []).append(seller)
        rows: list[dict[str, Any]] = []
        page_count = 0
        for group_key in sorted(seller_groups):
            group = seller_groups[group_key]
            group_body = {
                **body,
                "amazonSellerIds": [str(item["seller_id"]) for item in group],
                "sids": [int(item["sid"]) for item in group],
            }
            page = self.client.paged_post_detailed(
                endpoint,
                group_body,
                page_size=1000,
                data_path="data.records",
                total_path="data.total",
            )
            rows.extend(page.rows)
            page_count += page.page_count
        if len(seller_groups) > 1:
            warnings.append(
                f"结算接口已按 {len(seller_groups)} 个站点分组请求并在服务端合并；客户端仍为一次 MCP 调用。"
            )
        data = self._large_report_data(
            rows,
            response_mode=normalized_mode,
            preview_limit=preview_limit,
            warnings=warnings,
        )
        return self._result(
            data=data,
            endpoint=endpoint,
            page_count=page_count,
            warnings=warnings,
            date_range=f"{start_date}~{end_date}",
            extra_meta={
                "docs_path": "docs/Finance/SettlementReport.md",
                "store_scope": "filtered" if sids or amazon_seller_ids else "all",
                "selected_store_count": len(sellers),
                "selected_store_status": "explicit" if sids or amazon_seller_ids else "active",
                "store_group_count": len(seller_groups),
                "page_size": 1000,
                "pagination_mode": "offset_by_marketplace",
                "response_mode": normalized_mode,
            },
        )

    def sales_outbound_orders(
        self,
        start_date: str,
        end_date: str,
        *,
        sids: list[int] | None = None,
        amazon_seller_ids: list[str] | None = None,
        time_type: str = "stock_delivered_at",
        status: list[int] | None = None,
        logistics_status: list[int] | None = None,
        platform_order_numbers: list[str] | None = None,
        system_order_numbers: list[str] | None = None,
        outbound_order_numbers: list[str] | None = None,
        response_mode: str = "summary",
        preview_limit: int = 20,
    ) -> dict[str, Any]:
        normalized_mode, preview_limit = self._normalize_large_report_options(response_mode, preview_limit)
        endpoint = "/erp/sc/routing/wms/order/wmsOrderList"
        if time_type not in {"create_at", "delivered_at", "stock_delivered_at", "update_at"}:
            raise LingxingConfigError(
                "time_type 必须为 create_at、delivered_at、stock_delivered_at 或 update_at"
            )
        requested_sids = list(dict.fromkeys(_listify_ints(sids)))
        if amazon_seller_ids:
            sellers, warnings = self._select_amazon_sellers(
                sids=requested_sids or None,
                amazon_seller_ids=amazon_seller_ids,
            )
            selected_sids = [int(item["sid"]) for item in sellers]
        else:
            warnings = []
            selected_sids = requested_sids

        body: dict[str, Any] = {
            "page": 1,
            "page_size": 200,
            "time_type": time_type,
            "start_date": start_date,
            "end_date": end_date,
        }
        if selected_sids:
            body["sid_arr"] = selected_sids
        integer_array_mappings = {
            "status_arr": status,
            "logistics_status_arr": logistics_status,
        }
        string_array_mappings = {
            "platform_order_no_arr": platform_order_numbers,
            "order_number_arr": system_order_numbers,
            "wo_number_arr": outbound_order_numbers,
        }
        for body_name, values in integer_array_mappings.items():
            normalized = _listify_ints(values)
            if normalized:
                body[body_name] = normalized
        for body_name, values in string_array_mappings.items():
            normalized = _listify_strings(values)
            if normalized:
                body[body_name] = normalized

        page = self.client.paged_post_detailed(
            endpoint,
            body,
            page_size=200,
            data_path="data",
            total_path="total",
            pagination_mode="page",
        )
        data = self._large_report_data(
            page.rows,
            response_mode=normalized_mode,
            preview_limit=preview_limit,
            warnings=warnings,
        )
        return self._result(
            data=data,
            endpoint=endpoint,
            page_count=page.page_count,
            warnings=warnings,
            date_range=f"{start_date}~{end_date}",
            extra_meta={
                "docs_path": "docs/Warehouse/WmsOrderList.md",
                "store_scope": "filtered" if sids or amazon_seller_ids else "all",
                "selected_store_count": len(selected_sids) if selected_sids else None,
                "page_size": 200,
                "pagination_mode": "page",
                "response_mode": normalized_mode,
            },
        )

    def _normalize_spec_value(self, value: Any) -> Any:
        if isinstance(value, list):
            return value
        return value

    def _build_spec_body(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        body = dict(spec.defaults)
        for arg in spec.args:
            value = args.get(arg.name, arg.default)
            if value in (None, ""):
                continue
            if arg.arg_type == "array_string":
                body[arg.name] = _listify_strings(value)
            elif arg.arg_type == "array_integer":
                body[arg.name] = _listify_ints(value)
            elif arg.arg_type == "integer":
                body[arg.name] = int(value)
            elif arg.arg_type == "boolean":
                body[arg.name] = bool(value)
            else:
                body[arg.name] = self._normalize_spec_value(value)
        return body

    def ad_accounts(
        self,
        account_type: str = "seller",
        *,
        sid: int | None = None,
        profile_id: int | None = None,
        country_code: str | None = None,
        status: int | None = None,
    ) -> dict[str, Any]:
        endpoint = "/basicOpen/baseData/account/list"
        page = self.client.paged_post_detailed(
            endpoint,
            {"type": account_type, "offset": 0, "length": 200},
            page_size=200,
        )
        filtered: list[dict[str, Any]] = []
        for row in page.rows:
            item = dict(row)
            if sid is not None and str(item.get("sid") or "") != str(sid):
                continue
            if profile_id is not None and str(item.get("profile_id") or "") != str(profile_id):
                continue
            if country_code and str(item.get("country_code") or "").upper() != str(country_code).upper():
                continue
            if status is not None and int(item.get("status") or 0) != int(status):
                continue
            filtered.append(item)
        return self._result(
            data=filtered,
            endpoint=endpoint,
            page_count=page.page_count,
            extra_meta={"account_type": account_type},
        )

    def ads_management_apply(self, request: AdManagementRequest) -> dict[str, Any]:
        warnings: list[str] = []
        if request.dry_run or not request.confirm:
            warnings.append("dry_run=true 或 confirm 未开启，未调用领星广告写接口。")
            return self._result(
                data={
                    "executed": False,
                    "tool_name": request.tool_name,
                    "request_body": request.body,
                },
                endpoint=request.endpoint,
                sid=int(request.body.get("sid") or 0) or None,
                warnings=warnings,
                extra_meta={"docs_path": request.docs_path, "dry_run": request.dry_run, "confirm": request.confirm},
            )

        payload = self.client.post_json(request.endpoint, request.body)
        return self._result(
            data={"executed": True, "response": payload},
            endpoint=request.endpoint,
            sid=int(request.body.get("sid") or 0) or None,
            extra_meta={"docs_path": request.docs_path, "dry_run": False, "confirm": True},
        )

    def ads_operation_logs(
        self,
        *,
        sid: int,
        log_source: str,
        sponsored_type: str,
        operate_type: str,
        start_date: str,
        end_date: str,
        offset: int = 0,
        length: int = 100,
    ) -> dict[str, Any]:
        body = {
            "sid": int(sid),
            "log_source": log_source,
            "sponsored_type": sponsored_type,
            "operate_type": operate_type,
            "start_date": start_date,
            "end_date": end_date,
            "offset": max(0, int(offset)),
            "length": max(1, min(int(length), 200)),
        }
        payload = self.client.post_json(AD_OPERATION_LOGS_ENDPOINT, body, extra_headers={"X-API-VERSION": "2"})
        return self._result(
            data=payload.get("data"),
            endpoint=AD_OPERATION_LOGS_ENDPOINT,
            sid=int(sid),
            date_range=f"{start_date}~{end_date}",
            extra_meta={
                "docs_path": "https://apidoc.lingxing.com/#/docs/newAd/apiLogStandard",
                "filters": body,
            },
        )

    def _resolve_profile_id(self, sid: int, *, profile_id: int | None = None, account_type: str = "seller") -> int:
        if profile_id is not None:
            return int(profile_id)
        accounts = self.ad_accounts(account_type=account_type, sid=sid)["data"]
        if not accounts:
            raise LingxingConfigError(f"sid={sid} 未找到 type={account_type} 的广告账号")
        value = accounts[0].get("profile_id")
        if value in (None, ""):
            raise LingxingConfigError(f"sid={sid} 的广告账号缺少 profile_id")
        return int(value)

    def _spec_result_date_range(self, body: dict[str, Any]) -> str | None:
        if "report_date" in body:
            return str(body["report_date"])
        if "event_date" in body:
            return str(body["event_date"])
        if "start_date" in body and "end_date" in body:
            return f"{body['start_date']}~{body['end_date']}"
        if "startDate" in body and "endDate" in body:
            return f"{body['startDate']}~{body['endDate']}"
        if "start_month" in body and "end_month" in body:
            return f"{body['start_month']}~{body['end_month']}"
        return None

    def _run_ad_like_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        body = self._build_spec_body(spec, args)
        sid = int(body.get("sid") or 0)
        if spec.auto_profile:
            body["profile_id"] = self._resolve_profile_id(
                sid,
                profile_id=int(body["profile_id"]) if body.get("profile_id") not in (None, "") else None,
                account_type=spec.profile_type,
            )
        if spec.result_kind == "object" or spec.pagination_mode == "none":
            payload = self.client.post_json(spec.endpoint, body, extra_headers=spec.headers)
            data = extract_path_value(payload, spec.data_path)
            return self._result(
                data=data,
                endpoint=spec.endpoint,
                sid=sid or None,
                date_range=self._spec_result_date_range(body),
                extra_meta={"docs_path": spec.docs_path, "profile_id": body.get("profile_id")},
            )
        page = self.client.paged_post_detailed(
            spec.endpoint,
            {**body, "offset": 0, "length": spec.page_size},
            page_size=spec.page_size,
            data_path=spec.data_path,
            total_path=spec.total_path,
            next_token_path=spec.next_token_path,
            pagination_mode=spec.pagination_mode,
            extra_headers=spec.headers,
        )
        return self._result(
            data=page.rows,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            sid=sid or None,
            date_range=self._spec_result_date_range(body),
            extra_meta={"docs_path": spec.docs_path, "profile_id": body.get("profile_id")},
        )

    def _run_profit_report_order_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        normalized_mode, preview_limit = self._normalize_large_report_options(
            str(args.get("response_mode") or "summary"),
            20 if args.get("preview_limit") is None else int(args["preview_limit"]),
        )
        body: dict[str, Any] = {
            "offset": 0,
            "length": spec.page_size,
            "startDate": str(args.get("start_date") or ""),
            "endDate": str(args.get("end_date") or ""),
        }
        string_mappings = {
            "search_date_field": "searchDateField",
            "currency_code": "currencyCode",
            "search_field": "searchField",
            "sort_field": "sortField",
            "sort_type": "sortType",
            "order_status": "orderStatus",
            "gmt_modified_start_date": "gmtModifiedStartDate",
            "gmt_modified_end_date": "gmtModifiedEndDate",
        }
        array_string_mappings = {
            "fee_type": "eventSource",
            "search_value": "searchValue",
            "settlement_status": "settlementStatus",
            "fund_transfer_status": "fundTransferStatus",
            "account_type": "accountType",
            "fulfillment": "fulfillment",
        }
        array_int_mappings = {
            "sids": "sids",
            "mids": "mids",
            "listing_owner": "principalUids",
            "product_developer_uids": "productDeveloperUids",
        }
        for arg_name, body_name in string_mappings.items():
            value = str(args.get(arg_name) or "").strip()
            if value:
                body[body_name] = value
        for arg_name, body_name in array_string_mappings.items():
            values = _listify_strings(args.get(arg_name))
            if values:
                body[body_name] = values
        for arg_name, body_name in array_int_mappings.items():
            values = _listify_ints(args.get(arg_name))
            if values:
                body[body_name] = values
        page = self.client.paged_post_detailed(
            spec.endpoint,
            body,
            page_size=spec.page_size,
            data_path=spec.data_path,
            total_path=spec.total_path,
        )
        warnings: list[str] = []
        data = self._large_report_data(
            page.rows,
            response_mode=normalized_mode,
            preview_limit=preview_limit,
            warnings=warnings,
        )
        return self._result(
            data=data,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            warnings=warnings,
            sid=None,
            date_range=f"{body['startDate']}~{body['endDate']}",
            extra_meta={
                "docs_path": spec.docs_path,
                "field_aliases": {
                    "fee_type": "eventSource",
                    "listing_owner": "principalUids",
                    "search_date_field": "searchDateField",
                },
                "page_size": spec.page_size,
                "pagination_mode": "offset",
                "response_mode": normalized_mode,
            },
        )

    def _run_profit_like_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        sid = int(args.get("sid") or 0)
        body: dict[str, Any] = {
            "offset": 0,
            "length": spec.page_size,
            "sids": [sid],
            "startDate": str(args.get("start_date") or ""),
            "endDate": str(args.get("end_date") or ""),
        }
        currency_code = str(args.get("currency_code") or "").strip()
        if currency_code:
            body["currencyCode"] = currency_code
        search_value = str(args.get("search_value") or "").strip()
        if search_value and spec.search_field:
            body["searchField"] = spec.search_field
            body["searchValue"] = [search_value]
        if "monthly_query" in args and args.get("monthly_query") is not None:
            body["monthlyQuery"] = bool(args.get("monthly_query"))
        if "summary_enabled" in args and args.get("summary_enabled") is not None:
            body["summaryEnabled"] = bool(args.get("summary_enabled"))
        order_status = str(args.get("order_status") or "").strip()
        if order_status:
            body["orderStatus"] = order_status
        page = self.client.paged_post_detailed(
            spec.endpoint,
            body,
            page_size=spec.page_size,
            data_path=spec.data_path,
            total_path=spec.total_path,
        )
        return self._result(
            data=page.rows,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{body['startDate']}~{body['endDate']}",
            extra_meta={"docs_path": spec.docs_path},
        )

    def _run_source_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        body = self._build_spec_body(spec, args)
        sid = int(body.get("sid") or 0)
        page = self.client.paged_post_detailed(
            spec.endpoint,
            {**body, "offset": 0, "length": spec.page_size},
            page_size=spec.page_size,
            data_path=spec.data_path,
            total_path=spec.total_path,
            next_token_path=spec.next_token_path,
            pagination_mode=spec.pagination_mode,
            extra_headers=spec.headers,
        )
        return self._result(
            data=page.rows,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=self._spec_result_date_range(body),
            extra_meta={"docs_path": spec.docs_path},
        )

    def _run_warehouse_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        body = self._build_spec_body(spec, args)
        return self.fba_warehouse_detail(
            sid=int(body.get("sid") or 0),
            search_field=str(body.get("search_field") or "asin"),
            search_value=str(body.get("search_value") or "").strip() or None,
            page_size=spec.page_size,
            cid=str(body.get("cid") or "").strip() or None,
            bid=str(body.get("bid") or "").strip() or None,
            attribute=str(body.get("attribute") or "").strip() or None,
            asin_principal=str(body.get("asin_principal") or "").strip() or None,
            status=str(body.get("status") or "").strip() or None,
            senior_search_list=str(body.get("senior_search_list") or "").strip() or None,
            fulfillment_channel_type=str(body.get("fulfillment_channel_type") or "FBA"),
            is_hide_zero_stock=str(body.get("is_hide_zero_stock") if body.get("is_hide_zero_stock") not in (None, "") else "0"),
            is_parant_asin_merge=str(body.get("is_parant_asin_merge") if body.get("is_parant_asin_merge") not in (None, "") else "0"),
            is_contain_del_ls=str(body.get("is_contain_del_ls") if body.get("is_contain_del_ls") not in (None, "") else "0"),
            query_fba_storage_quantity_list=body.get("query_fba_storage_quantity_list") if "query_fba_storage_quantity_list" in body else None,
        )

    def _run_stock_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        sid = int(args.get("sid") or 0)
        context = self._seller_context(sid)
        body = {
            "offset": 0,
            "length": spec.page_size,
            "start_date": str(args.get("start_month") or ""),
            "end_date": str(args.get("end_month") or ""),
            "seller_id": [context["seller_id"]],
        }
        page = self.client.paged_post_detailed(
            spec.endpoint,
            body,
            page_size=spec.page_size,
            data_path=spec.data_path,
            total_path=spec.total_path,
        )
        return self._result(
            data=page.rows,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=f"{body['start_date']}~{body['end_date']}",
            extra_meta={"docs_path": spec.docs_path, "seller_id": context["seller_id"]},
        )

    def _run_replenishment_summary_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        sid = int(args.get("sid") or 0)
        body = {
            "sid_list": [str(sid)],
            "data_type": 1,
            "offset": 0,
            "length": spec.page_size,
        }
        asin = str(args.get("asin") or "").strip()
        if asin:
            body["asin_list"] = [asin]
        if args.get("mode") not in (None, ""):
            body["mode"] = int(args["mode"])
        page = self.client.paged_post_detailed(spec.endpoint, body, page_size=spec.page_size)
        return self._result(
            data=page.rows,
            endpoint=spec.endpoint,
            page_count=page.page_count,
            sid=sid,
            date_range=None,
            extra_meta={"docs_path": spec.docs_path, "data_type": 1},
        )

    def _run_replenishment_info_spec(self, spec: EndpointSpec, args: dict[str, Any]) -> dict[str, Any]:
        body = self._build_spec_body(spec, args)
        sid = int(body.get("sid") or 0)
        payload = self.client.post_json(spec.endpoint, body)
        data = extract_path_value(payload, spec.data_path)
        return self._result(
            data=data,
            endpoint=spec.endpoint,
            sid=sid,
            date_range=None,
            extra_meta={"docs_path": spec.docs_path},
        )

    def run_endpoint_spec(self, tool_name: str, args: dict[str, Any]) -> dict[str, Any]:
        spec = ENDPOINT_SPECS_BY_NAME.get(tool_name)
        if spec is None:
            raise LingxingConfigError(f"未知 endpoint spec: {tool_name}")
        if spec.category in {"ad_report", "ad_base"}:
            return self._run_ad_like_spec(spec, args)
        if spec.category == "profit_report_order":
            return self._run_profit_report_order_spec(spec, args)
        if spec.category in {"profit", "profit_report"}:
            return self._run_profit_like_spec(spec, args)
        if spec.category in {"source", "product"}:
            return self._run_source_spec(spec, args)
        if spec.category == "warehouse":
            return self._run_warehouse_spec(spec, args)
        if spec.category == "stock":
            return self._run_stock_spec(spec, args)
        if spec.category == "replenishment_summary":
            return self._run_replenishment_summary_spec(spec, args)
        if spec.category == "replenishment_info":
            return self._run_replenishment_info_spec(spec, args)
        raise LingxingConfigError(f"暂不支持的 endpoint spec category: {spec.category}")

    def report_export_create(
        self,
        *,
        sid: int,
        report_type: str,
        data_start_time: str | None = None,
        data_end_time: str | None = None,
        marketplace_ids: list[str] | None = None,
        region: str | None = None,
        seller_id: str | None = None,
    ) -> dict[str, Any]:
        context = self._seller_context(sid)
        body = {
            "seller_id": seller_id or context["seller_id"],
            "report_type": report_type,
            "marketplace_ids": marketplace_ids or [context["marketplace_id"]],
            "region": region or context["region_code"],
        }
        if data_start_time:
            body["data_start_time"] = data_start_time
        if data_end_time:
            body["data_end_time"] = data_end_time
        payload = self.client.post_json("/basicOpen/report/create/reportExportTask", body)
        return self._result(
            data=payload.get("data") or {},
            endpoint="/basicOpen/report/create/reportExportTask",
            sid=sid,
            date_range=f"{data_start_time or ''}~{data_end_time or ''}".strip("~"),
            extra_meta={"report_type": report_type, "docs_path": "docs/Statistics/reportCreateReportExportTask.md"},
        )

    def report_export_query(
        self,
        *,
        task_id: str,
        sid: int | None = None,
        region: str | None = None,
        seller_id: str | None = None,
    ) -> dict[str, Any]:
        context = self._seller_context(sid) if sid is not None else None
        body = {
            "task_id": task_id,
            "seller_id": seller_id or (context or {}).get("seller_id") or "",
            "region": region or (context or {}).get("region_code") or "",
        }
        if not body["seller_id"] or not body["region"]:
            raise LingxingConfigError("report_export_query 需要 sid 或同时传 seller_id + region")
        payload = self.client.post_json("/basicOpen/report/query/reportExportTask", body)
        return self._result(
            data=payload.get("data") or {},
            endpoint="/basicOpen/report/query/reportExportTask",
            sid=sid,
            date_range=None,
            extra_meta={"docs_path": "docs/Statistics/reportQueryReportExportTask.md"},
        )

    def report_export_refresh_url(
        self,
        *,
        report_document_id: str,
        sid: int | None = None,
        region: str | None = None,
        seller_id: str | None = None,
    ) -> dict[str, Any]:
        context = self._seller_context(sid) if sid is not None else None
        body = {
            "report_document_id": report_document_id,
            "seller_id": seller_id or (context or {}).get("seller_id") or "",
            "region": region or (context or {}).get("region_code") or "",
        }
        if not body["seller_id"] or not body["region"]:
            raise LingxingConfigError("report_export_refresh_url 需要 sid 或同时传 seller_id + region")
        payload = self.client.post_json("/basicOpen/report/amazonReportExportTask", body)
        return self._result(
            data=payload.get("data") or {},
            endpoint="/basicOpen/report/amazonReportExportTask",
            sid=sid,
            date_range=None,
            extra_meta={"docs_path": "docs/Statistics/AmazonReportExportTask.md"},
        )

    def _serialize_downloaded_file(self, downloaded: DownloadedFile) -> dict[str, Any]:
        return {
            "url": downloaded.url,
            "final_url": downloaded.final_url,
            "filename": downloaded.filename,
            "content_type": downloaded.content_type,
            "content_encoding": downloaded.content_encoding,
            "size": downloaded.size,
            "parsed_format": downloaded.parsed_format,
            "data": downloaded.data,
            "warnings": downloaded.warnings,
        }

    def report_export_download(
        self,
        *,
        url: str | None = None,
        sid: int | None = None,
        task_id: str | None = None,
        report_document_id: str | None = None,
        region: str | None = None,
        seller_id: str | None = None,
    ) -> dict[str, Any]:
        resolved_url = str(url or "").strip()
        warnings: list[str] = []
        if not resolved_url and task_id:
            query_result = self.report_export_query(task_id=task_id, sid=sid, region=region, seller_id=seller_id)
            query_data = query_result.get("data") or {}
            resolved_url = str(query_data.get("url") or "").strip()
            report_document_id = report_document_id or str(query_data.get("report_document_id") or "").strip() or None
            if not resolved_url and report_document_id:
                refresh_result = self.report_export_refresh_url(
                    report_document_id=report_document_id,
                    sid=sid,
                    region=region,
                    seller_id=seller_id,
                )
                refresh_data = refresh_result.get("data") or {}
                resolved_url = str(refresh_data.get("url") or "").strip()
        if not resolved_url and report_document_id:
            refresh_result = self.report_export_refresh_url(
                report_document_id=report_document_id,
                sid=sid,
                region=region,
                seller_id=seller_id,
            )
            refresh_data = refresh_result.get("data") or {}
            resolved_url = str(refresh_data.get("url") or "").strip()
        if not resolved_url:
            raise LingxingConfigError("report_export_download 需要 url，或传 task_id / report_document_id 以解析下载链接")
        downloaded = self.client.download_file(resolved_url)
        warnings.extend(downloaded.warnings)
        return self._result(
            data=self._serialize_downloaded_file(downloaded),
            endpoint="report_export_download",
            sid=sid,
            date_range=None,
            warnings=warnings,
            extra_meta={"docs_path": "docs/Statistics/reportQueryReportExportTask.md"},
        )

    def asin_ads_daily_rollup(
        self,
        sid: int,
        asin: str,
        start_date: str,
        end_date: str,
        attribution_policy: str = "balanced",
    ) -> dict[str, Any]:
        if attribution_policy != "balanced":
            raise LingxingConfigError("当前仅支持 attribution_policy=balanced")
        profile_id = self._resolve_profile_id(sid)
        sb_creatives = self.run_endpoint_spec("lingxing_ads_sb_creatives", {"sid": sid, "profile_id": profile_id})["data"]
        sb_creative_map: dict[str, list[str]] = {}
        for row in sb_creatives:
            creative_id = str(row.get("ad_creative_id") or "")
            asins = [str(item) for item in row.get("asin") or [] if str(item)]
            if creative_id:
                sb_creative_map[creative_id] = asins

        rows: list[dict[str, Any]] = []
        warnings: list[str] = []
        for report_date in _iso_day_range(start_date, end_date):
            sp_rows = self.run_endpoint_spec(
                "lingxing_ads_sp_product_ad_report",
                {"sid": sid, "report_date": report_date, "profile_id": profile_id, "show_detail": 1},
            )["data"]
            sd_rows = self.run_endpoint_spec(
                "lingxing_ads_sd_product_ad_report",
                {"sid": sid, "report_date": report_date, "profile_id": profile_id, "show_detail": 1},
            )["data"]
            sb_purchase_rows = self.run_endpoint_spec(
                "lingxing_ads_sb_purchased_asin_report",
                {"sid": sid, "report_date": report_date, "profile_id": profile_id},
            )["data"]
            sb_creative_rows = self.run_endpoint_spec(
                "lingxing_ads_sb_creative_report",
                {"sid": sid, "report_date": report_date, "profile_id": profile_id},
            )["data"]

            sp_asin_rows = [row for row in sp_rows if str(row.get("asin") or "") == asin]
            sd_asin_rows = [row for row in sd_rows if str(row.get("asin") or "") == asin]
            sb_asin_rows = [row for row in sb_purchase_rows if str(row.get("asin") or "") == asin]

            sb_impressions = 0.0
            sb_clicks = 0.0
            sb_cost = 0.0
            skipped_sb_rows = 0
            for row in sb_creative_rows:
                creative_id = str(row.get("ad_creative_id") or "")
                creative_asins = sb_creative_map.get(creative_id, [])
                if creative_asins == [asin]:
                    sb_impressions += float(row.get("impressions") or 0)
                    sb_clicks += float(row.get("clicks") or 0)
                    sb_cost += float(row.get("cost") or 0)
                elif creative_asins and asin in creative_asins:
                    skipped_sb_rows += 1
            row_warnings: list[str] = []
            if skipped_sb_rows:
                row_warnings.append(f"SB 多 ASIN 创意 {skipped_sb_rows} 条未分摊曝光/点击/花费")

            source_breakdown = {
                "sp": {
                    "impressions": _sum_number(sp_asin_rows, "impressions"),
                    "clicks": _sum_number(sp_asin_rows, "clicks"),
                    "cost": _sum_number(sp_asin_rows, "cost"),
                    "ad_orders": _sum_number(sp_asin_rows, "orders"),
                    "ad_sales": _sum_number(sp_asin_rows, "sales"),
                    "ad_units": _sum_number(sp_asin_rows, "units"),
                },
                "sd": {
                    "impressions": _sum_number(sd_asin_rows, "impressions"),
                    "clicks": _sum_number(sd_asin_rows, "clicks"),
                    "cost": _sum_number(sd_asin_rows, "cost"),
                    "ad_orders": _sum_number(sd_asin_rows, "orders"),
                    "ad_sales": _sum_number(sd_asin_rows, "sales"),
                    "ad_units": _sum_number(sd_asin_rows, "units"),
                },
                "sb": {
                    "impressions": sb_impressions,
                    "clicks": sb_clicks,
                    "cost": sb_cost,
                    "ad_orders": _sum_number(sb_asin_rows, "orders14d"),
                    "ad_sales": _sum_number(sb_asin_rows, "sales14d"),
                    "ad_units": _sum_number(sb_asin_rows, "units_sold14d"),
                },
            }
            rows.append(
                {
                    "date": report_date,
                    "asin": asin,
                    "impressions": source_breakdown["sp"]["impressions"] + source_breakdown["sd"]["impressions"] + source_breakdown["sb"]["impressions"],
                    "clicks": source_breakdown["sp"]["clicks"] + source_breakdown["sd"]["clicks"] + source_breakdown["sb"]["clicks"],
                    "cost": source_breakdown["sp"]["cost"] + source_breakdown["sd"]["cost"] + source_breakdown["sb"]["cost"],
                    "ad_orders": source_breakdown["sp"]["ad_orders"] + source_breakdown["sd"]["ad_orders"] + source_breakdown["sb"]["ad_orders"],
                    "ad_sales": source_breakdown["sp"]["ad_sales"] + source_breakdown["sd"]["ad_sales"] + source_breakdown["sb"]["ad_sales"],
                    "ad_units": source_breakdown["sp"]["ad_units"] + source_breakdown["sd"]["ad_units"] + source_breakdown["sb"]["ad_units"],
                    "source_breakdown": source_breakdown,
                    "warnings": row_warnings,
                }
            )
            warnings.extend(row_warnings)
        return self._result(
            data=rows,
            endpoint="asin_ads_daily_rollup",
            sid=sid,
            date_range=f"{start_date}~{end_date}",
            warnings=sorted(set(warnings)),
            extra_meta={"asin": asin, "attribution_policy": attribution_policy},
        )

    def asin_weekly_rollup(self, sid: int, asin: str, start_date: str, end_date: str) -> dict[str, Any]:
        sales_rows = [row for row in self.store_sales(sid, start_date, end_date)["data"] if str(row.get("asin") or "") == asin]
        ads_daily = self.asin_ads_daily_rollup(sid, asin, start_date, end_date)["data"]
        promotion_by_date: dict[str, list[str]] = {}
        warnings: list[str] = []
        for current_date in _iso_day_range(start_date, end_date):
            try:
                rows = self.resolve_daily_promotions(sid, current_date)["data"]
                target_row = next((row for row in rows if str(row.get("asin") or "") == asin), None)
                promotion_by_date[current_date] = list(target_row.get("promotion_labels") or []) if target_row else []
            except LingxingClientError as exc:
                warnings.append(f"{current_date} 促销解析失败: {exc.message}")
                promotion_by_date[current_date] = []

        weekly: dict[str, dict[str, Any]] = {}
        for row in sales_rows:
            current_date = str(row.get("r_date") or "")
            if not current_date:
                continue
            week_start = _week_start_text(current_date)
            entry = weekly.setdefault(
                week_start,
                {
                    "week_start": week_start,
                    "week_end": (_parse_iso_date(week_start) + timedelta(days=6)).isoformat(),
                    "date_range": f"{week_start}~{(_parse_iso_date(week_start) + timedelta(days=6)).isoformat()}",
                    "asin": asin,
                    "total_sales": 0.0,
                    "total_units": 0.0,
                    "total_orders": 0.0,
                    "impressions": 0.0,
                    "clicks": 0.0,
                    "cost": 0.0,
                    "ad_orders": 0.0,
                    "ad_sales": 0.0,
                    "ad_units": 0.0,
                    "promotion_labels": set(),
                },
            )
            entry["total_sales"] += float(row.get("amount") or 0)
            entry["total_units"] += float(row.get("volume") or 0)
            entry["total_orders"] += float(row.get("order_items") or 0)
            for label in promotion_by_date.get(current_date, []):
                entry["promotion_labels"].add(label)
        for row in ads_daily:
            week_start = _week_start_text(str(row.get("date") or ""))
            entry = weekly.setdefault(
                week_start,
                {
                    "week_start": week_start,
                    "week_end": (_parse_iso_date(week_start) + timedelta(days=6)).isoformat(),
                    "date_range": f"{week_start}~{(_parse_iso_date(week_start) + timedelta(days=6)).isoformat()}",
                    "asin": asin,
                    "total_sales": 0.0,
                    "total_units": 0.0,
                    "total_orders": 0.0,
                    "impressions": 0.0,
                    "clicks": 0.0,
                    "cost": 0.0,
                    "ad_orders": 0.0,
                    "ad_sales": 0.0,
                    "ad_units": 0.0,
                    "promotion_labels": set(),
                },
            )
            entry["impressions"] += float(row.get("impressions") or 0)
            entry["clicks"] += float(row.get("clicks") or 0)
            entry["cost"] += float(row.get("cost") or 0)
            entry["ad_orders"] += float(row.get("ad_orders") or 0)
            entry["ad_sales"] += float(row.get("ad_sales") or 0)
            entry["ad_units"] += float(row.get("ad_units") or 0)
        rows = []
        for week_start in sorted(weekly):
            item = dict(weekly[week_start])
            item["promotion_labels"] = sorted(item["promotion_labels"])
            rows.append(item)
        return self._result(
            data=rows,
            endpoint="asin_weekly_rollup",
            sid=sid,
            date_range=f"{start_date}~{end_date}",
            warnings=sorted(set(warnings)),
            extra_meta={"asin": asin},
        )

    def smoke_check(self, sid: int | None = None, site_date: str | None = None) -> dict[str, Any]:
        sellers = self.seller_lists(status=1)["data"]
        if not sellers:
            raise LingxingClientError("店铺列表为空，无法继续烟测", endpoint="/erp/sc/data/seller/lists")
        seller = None
        if sid is not None:
            seller = next((item for item in sellers if int(item.get("sid") or 0) == int(sid)), None)
        if seller is None:
            seller = sellers[0]
        marketplaces = {
            int(item.get("mid") or 0): item
            for item in self.marketplaces()["data"]
        }
        marketplace = marketplaces.get(int(seller.get("mid") or 0), {})
        site_code = str(marketplace.get("code") or "UTC")
        if not site_date:
            site_date = datetime.now(get_timezone(site_code)).strftime("%Y-%m-%d")
        next_date = (datetime.strptime(site_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        sid_value = int(seller["sid"])

        store_sales = self.store_sales(sid_value, site_date, site_date)
        orders = self.orders(sid_value, f"{site_date} 00:00:00", f"{next_date} 00:00:00")
        promotions = self.promotion_listing(sid_value, site_date, site_date, site_date)
        warnings: list[str] = []
        endpoint_list = [
            "/erp/sc/data/seller/lists",
            "/erp/sc/data/sales_report/sales",
            "/erp/sc/data/mws/orders",
            "/basicOpen/promotion/listingList",
        ]

        ad_accounts_ok = False
        sp_product_ad_report_ok = False
        sd_product_ad_report_ok = False
        sb_purchased_asin_report_ok = False
        profit_seller_ok = False
        source_all_orders_ok = False
        source_manage_inventory_ok = False

        ad_profile_id: int | None = None
        sample_counts = {
            "store_sales": len(store_sales["data"] or []),
            "orders": len(orders["data"] or []),
            "promotions": len(promotions["data"] or []),
        }
        try:
            ad_accounts = self.ad_accounts(sid=sid_value)
            ad_accounts_ok = ad_accounts["ok"]
            sample_counts["ad_accounts"] = len(ad_accounts["data"] or [])
            endpoint_list.append("/basicOpen/baseData/account/list")
            first_account = next(iter(ad_accounts["data"] or []), None)
            if first_account and first_account.get("profile_id") not in (None, ""):
                ad_profile_id = int(first_account["profile_id"])
        except LingxingClientError as exc:
            warnings.append(f"ad_accounts 烟测失败: {exc.message}")

        if ad_profile_id is not None:
            for tool_name, count_key, ok_key in (
                ("lingxing_ads_sp_product_ad_report", "sp_product_ad_report", "sp_product_ad_report_ok"),
                ("lingxing_ads_sd_product_ad_report", "sd_product_ad_report", "sd_product_ad_report_ok"),
                ("lingxing_ads_sb_purchased_asin_report", "sb_purchased_asin_report", "sb_purchased_asin_report_ok"),
            ):
                try:
                    result = self.run_endpoint_spec(
                        tool_name,
                        {"sid": sid_value, "report_date": site_date, "profile_id": ad_profile_id, "show_detail": 1},
                    )
                    sample_counts[count_key] = len(result["data"] or [])
                    endpoint_list.append(str(result["meta"].get("endpoint") or tool_name))
                    if ok_key == "sp_product_ad_report_ok":
                        sp_product_ad_report_ok = result["ok"]
                    elif ok_key == "sd_product_ad_report_ok":
                        sd_product_ad_report_ok = result["ok"]
                    else:
                        sb_purchased_asin_report_ok = result["ok"]
                except LingxingClientError as exc:
                    warnings.append(f"{tool_name} 烟测失败: {exc.message}")
        else:
            warnings.append("未找到广告 profile_id，跳过广告报表烟测。")

        for tool_name, args, count_key in (
            ("lingxing_profit_seller", {"sid": sid_value, "start_date": site_date, "end_date": site_date}, "profit_seller"),
            (
                "lingxing_source_all_orders",
                {
                    "sid": sid_value,
                    "start_date": f"{site_date} 00:00:00",
                    "end_date": f"{next_date} 00:00:00",
                    "date_type": 1,
                },
                "source_all_orders",
            ),
            ("lingxing_source_manage_inventory", {"sid": sid_value}, "source_manage_inventory"),
        ):
            try:
                result = self.run_endpoint_spec(tool_name, args)
                sample_counts[count_key] = len(result["data"] or []) if isinstance(result["data"], list) else 1
                endpoint_list.append(str(result["meta"].get("endpoint") or tool_name))
                if tool_name == "lingxing_profit_seller":
                    profit_seller_ok = result["ok"]
                elif tool_name == "lingxing_source_all_orders":
                    source_all_orders_ok = result["ok"]
                else:
                    source_manage_inventory_ok = result["ok"]
            except LingxingClientError as exc:
                warnings.append(f"{tool_name} 烟测失败: {exc.message}")

        data = {
            "sid": sid_value,
            "store_name": seller.get("name"),
            "site_code": site_code,
            "site_date": site_date,
            "seller_lists_ok": True,
            "store_sales_ok": store_sales["ok"],
            "orderlists_ok": orders["ok"],
            "promotion_listing_ok": promotions["ok"],
            "ad_accounts_ok": ad_accounts_ok,
            "sp_product_ad_report_ok": sp_product_ad_report_ok,
            "sd_product_ad_report_ok": sd_product_ad_report_ok,
            "sb_purchased_asin_report_ok": sb_purchased_asin_report_ok,
            "profit_seller_ok": profit_seller_ok,
            "source_all_orders_ok": source_all_orders_ok,
            "source_manage_inventory_ok": source_manage_inventory_ok,
            "sample_counts": sample_counts,
        }
        return self._result(
            data=data,
            endpoint="smoke_check",
            sid=sid_value,
            date_range=site_date,
            warnings=warnings,
            extra_meta={
                "endpoints": endpoint_list
            },
        )
