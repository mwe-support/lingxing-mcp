#!/usr/bin/env python3
"""Run a minimal LingXing smoke check sequence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi import LingxingClientError, LingxingOpenAPIService  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="领星 OpenAPI 烟测")
    parser.add_argument("--sid", type=int, help="指定店铺 sid；默认取第一个状态正常的店铺")
    parser.add_argument("--date", help="站点日期 YYYY-MM-DD；默认自动按店铺站点当天")
    args = parser.parse_args()

    result = LingxingOpenAPIService().smoke_check(sid=args.sid, site_date=args.date)
    print(json.dumps(result["data"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except LingxingClientError as exc:
        raise SystemExit(str(exc))
