"""Business-oriented LingXing service layer shared by scripts and MCP."""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from .client import DEFAULT_TOKEN_CACHE, LingxingOpenAPIClient, DownloadedFile, extract_path_value
from .endpoint_specs import ENDPOINT_SPECS_BY_NAME, EndpointSpec
from .errors import LingxingClientError, LingxingConfigError
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
        if spec.category in {"profit", "profit_report"}:
            return self._run_profit_like_spec(spec, args)
        if spec.category == "source":
            return self._run_source_spec(spec, args)
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
