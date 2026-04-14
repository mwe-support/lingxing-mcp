#!/usr/bin/env python3
"""LingXing MCP HTTP entrypoint."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.mcp import build_http_arg_parser, run_http_server  # noqa: E402


def main() -> int:
    args = build_http_arg_parser().parse_args()
    return run_http_server(args.host, args.port, bearer_token=args.bearer_token, tokens_file=args.tokens_file)


if __name__ == "__main__":
    raise SystemExit(main())
