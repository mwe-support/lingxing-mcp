"""Marketplace timezone helpers for LingXing-backed Amazon stores."""

from __future__ import annotations

from zoneinfo import ZoneInfo


MARKETPLACE_TIMEZONES = {
    "US": "America/Los_Angeles",
    "CA": "America/Toronto",
    "MX": "America/Mexico_City",
    "UK": "Europe/London",
    "DE": "Europe/Berlin",
    "FR": "Europe/Paris",
    "IT": "Europe/Rome",
    "ES": "Europe/Madrid",
    "JP": "Asia/Tokyo",
    "AU": "Australia/Sydney",
    "AE": "Asia/Dubai",
    "SG": "Asia/Singapore",
    "BR": "America/Sao_Paulo",
    "SE": "Europe/Stockholm",
    "PL": "Europe/Warsaw",
    "TR": "Europe/Istanbul",
    "BE": "Europe/Brussels",
    "SA": "Asia/Riyadh",
    "NL": "Europe/Amsterdam",
    "IN": "Asia/Kolkata",
}


def get_timezone_name(marketplace_code: str | None) -> str:
    if not marketplace_code:
        return "UTC"
    return MARKETPLACE_TIMEZONES.get(str(marketplace_code).upper(), "UTC")


def get_timezone(marketplace_code: str | None) -> ZoneInfo:
    return ZoneInfo(get_timezone_name(marketplace_code))

