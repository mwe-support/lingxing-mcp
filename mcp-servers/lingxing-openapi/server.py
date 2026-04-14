#!/usr/bin/env python3
"""LingXing MCP stdio entrypoint."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.mcp import run_stdio_server  # noqa: E402


if __name__ == "__main__":
    raise SystemExit(run_stdio_server())

