"""Promotion normalization helpers shared by monitor and MCP."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def parse_datetime(value: str) -> datetime:
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError(f"无法解析时间: {value}")


def daterange(start: date, end: date) -> list[date]:
    days: list[date] = []
    cursor = start
    while cursor <= end:
        days.append(cursor)
        cursor += timedelta(days=1)
    return days


def safe_int(value: Any, default: int = 0) -> int:
    if value in (None, ""):
        return default
    if isinstance(value, bool):
        return int(value)
    try:
        return int(float(str(value).replace(",", "")))
    except ValueError:
        return default


def normalize_text(value: Any) -> str:
    return str(value or "").strip().lower()


def pick_coupon_label(promotion_type_text: Any) -> str:
    text = normalize_text(promotion_type_text)
    if any(token in text for token in ["percent", "百分"]):
        return "coupon.percent_off"
    if any(token in text for token in ["amount", "金额", "money", "固定", "save", "$", "¥", "€", "£"]):
        return "coupon.amount_off"
    return "coupon.generic"


def pick_manage_label(promotion_type: Any) -> str:
    mapping = {
        3: "manage.buy_one_get_one",
        4: "manage.purchase_discount",
        5: "manage.fixed_price",
        8: "manage.social_media",
    }
    return mapping.get(safe_int(promotion_type), "manage.generic")


def pick_discount_label(customer_target: Any) -> str:
    target = normalize_text(customer_target).replace(" ", "_")
    if target == "prime_exclusive":
        return "discount.prime_exclusive"
    if target == "all_customers":
        return "discount.all_customers"
    return "discount.generic"


def pick_deal_label(promotion_type: Any) -> str:
    mapping = {
        1: "deal.best_deal",
        2: "deal.lightning_deal",
    }
    return mapping.get(safe_int(promotion_type), "deal.generic")


def classify_coupon_activity(row: dict[str, Any]) -> str:
    for key in ("promotion_type_text", "coupon_type_text", "discount_type_text", "type_text"):
        value = row.get(key)
        if value:
            return pick_coupon_label(value)
    return "coupon.generic"


def classify_promotion(
    promotion: dict[str, Any],
    sec_kill_map: dict[str, dict[str, Any]],
    manage_map: dict[str, dict[str, Any]],
    discount_map: dict[str, dict[str, Any]],
) -> str:
    category = safe_int(promotion.get("category"))
    promotion_id = str(promotion.get("promotion_id") or promotion.get("promotionId") or "")
    if category == 1:
        return pick_coupon_label(promotion.get("promotion_type_text"))
    if category == 2:
        return pick_deal_label((sec_kill_map.get(promotion_id) or {}).get("promotion_type"))
    if category == 3:
        return pick_manage_label((manage_map.get(promotion_id) or {}).get("promotion_type"))
    if category == 4:
        return pick_discount_label((discount_map.get(promotion_id) or {}).get("customer_target"))
    return "promotion.unknown"


@dataclass
class PromotionWindow:
    promotion_id: str
    label: str
    start_at: datetime
    end_at: datetime
    category_text: str
    promotion_type_text: str

    @property
    def start_date(self) -> date:
        return self.start_at.date()

    @property
    def end_date(self) -> date:
        return self.end_at.date()

    def covers_date(self, target: date) -> bool:
        return self.start_date <= target <= self.end_date

    def covers_datetime(self, target: datetime) -> bool:
        return self.start_at <= target <= self.end_at


def build_promotion_windows(
    listing_records: list[dict[str, Any]],
    sec_kill_map: dict[str, dict[str, Any]],
    manage_map: dict[str, dict[str, Any]],
    discount_map: dict[str, dict[str, Any]],
) -> tuple[dict[str, list[PromotionWindow]], dict[str, dict[str, Any]]]:
    windows_by_asin: dict[str, list[PromotionWindow]] = defaultdict(list)
    asin_meta: dict[str, dict[str, Any]] = {}
    for row in listing_records:
        asin = str(row.get("asin") or "")
        if not asin:
            continue
        asin_meta.setdefault(
            asin,
            {
                "asin": asin,
                "seller_sku": str(row.get("seller_sku") or ""),
                "item_name": str(row.get("item_name") or ""),
                "store_name": str(row.get("store_name") or ""),
                "region_name": str(row.get("region_name") or ""),
            },
        )
        for promotion in row.get("promotion_list") or []:
            promotion_id = str(promotion.get("promotion_id") or "")
            start_at = parse_datetime(str(promotion.get("promotion_start_time")))
            end_at = parse_datetime(str(promotion.get("promotion_end_time")))
            windows_by_asin[asin].append(
                PromotionWindow(
                    promotion_id=promotion_id,
                    label=classify_promotion(promotion, sec_kill_map, manage_map, discount_map),
                    start_at=start_at,
                    end_at=end_at,
                    category_text=str(promotion.get("category_text") or ""),
                    promotion_type_text=str(promotion.get("promotion_type_text") or ""),
                )
            )
    return windows_by_asin, asin_meta


def promotion_dates_by_asin(windows_by_asin: dict[str, list[PromotionWindow]]) -> dict[str, set[str]]:
    output: dict[str, set[str]] = defaultdict(set)
    for asin, windows in windows_by_asin.items():
        for window in windows:
            for day in daterange(window.start_date, window.end_date):
                output[asin].add(day.isoformat())
    return output


def active_promotions_for_target(
    windows: list[PromotionWindow],
    target_date: date,
    current_site_datetime: datetime,
    historical_mode: bool,
) -> list[PromotionWindow]:
    if historical_mode:
        return [window for window in windows if window.covers_date(target_date)]
    return [window for window in windows if window.covers_datetime(current_site_datetime)]


def serialize_promotion_window(window: PromotionWindow) -> dict[str, Any]:
    return {
        "promotion_id": window.promotion_id,
        "label": window.label,
        "start_at": window.start_at.strftime("%Y-%m-%d %H:%M:%S"),
        "end_at": window.end_at.strftime("%Y-%m-%d %H:%M:%S"),
        "category_text": window.category_text,
        "promotion_type_text": window.promotion_type_text,
    }

