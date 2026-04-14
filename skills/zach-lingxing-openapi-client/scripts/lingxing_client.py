#!/usr/bin/env python3
"""Compatibility wrapper around the shared LingXing OpenAPI client."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi import (  # noqa: E402,F401
    AUTH_BASE_URL,
    DEFAULT_TOKEN_CACHE,
    DOC_BASE_URL,
    SUCCESS_CODES,
    LingxingClientError,
    LingxingConfigError,
    LingxingOpenAPIClient,
    LingxingRequestError,
    LingxingSignError,
    LingxingTransportError,
    PagedRows,
    TokenBundle,
    build_sign_payload,
    env_or_raise,
    generate_sign,
)

