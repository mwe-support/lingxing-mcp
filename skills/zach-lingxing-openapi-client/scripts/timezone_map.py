"""Compatibility wrapper around the shared marketplace timezone helpers."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.timezones import MARKETPLACE_TIMEZONES, get_timezone, get_timezone_name  # noqa: E402,F401

