"""Shared LingXing OpenAPI client with token caching and official signing."""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import os
import subprocess
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any
import zipfile

from .errors import (
    LingxingClientError,
    LingxingConfigError,
    LingxingRequestError,
    LingxingSignError,
    LingxingTransportError,
    hint_for_business_error,
)


DEFAULT_TOKEN_CACHE = Path("runtime/lingxing/token_cache.json")
AUTH_BASE_URL = "https://openapi.lingxing.com"
DOC_BASE_URL = "https://apidoc.lingxing.com"
SUCCESS_CODES = {0, "0", 1, "1", 200, "200"}


@dataclass(frozen=True)
class RateLimitRule:
    rate_per_second: float
    burst: int
    source: str = "default"


KNOWN_RATE_LIMIT_RULES: dict[str, RateLimitRule] = {
    # Capacity-1 endpoints in the current production allowlist.
    "/erp/sc/data/seller/lists": RateLimitRule(1.0, 1, "openapi_docs"),
    "/erp/sc/data/seller/allMarketplace": RateLimitRule(1.0, 1, "openapi_docs"),
    "/erp/sc/data/mws/orders": RateLimitRule(1.0, 1, "openapi_docs"),
    "/erp/sc/data/mws/orderDetail": RateLimitRule(1.0, 1, "openapi_docs"),
    "/bd/productPerformance/openApi/asinList": RateLimitRule(1.0, 1, "openapi_docs"),
    "/basicOpen/finance/profitReport/order/transcation/list": RateLimitRule(1.0, 1, "openapi_docs"),
    # Capacity-10 endpoints in the current production allowlist.
    "/bd/profit/report/open/report/asin/list": RateLimitRule(10.0, 10, "openapi_docs"),
    "/erp/sc/data/mws_report/allOrders": RateLimitRule(10.0, 10, "openapi_docs"),
    # Production endpoints without local capacity docs use a conservative queue.
    "/basicOpen/openapi/storage/fbaWarehouseDetail": RateLimitRule(1.0, 1, "conservative"),
    "/erp/sc/routing/data/local_inventory/productList": RateLimitRule(1.0, 1, "conservative"),
}


_RATE_LIMIT_BUCKETS: dict[str, "_TokenBucket"] = {}
_RATE_LIMIT_BUCKETS_LOCK = threading.Lock()


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None or raw.strip() == "":
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off"}


def _env_float(name: str, default: float) -> float:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        return default


def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name, "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _normalize_endpoint(path: str) -> str:
    return f"/{str(path).lstrip('/')}"


def normalize_rate_limit_endpoint(path: str) -> str:
    """Return the canonical endpoint key used by local rate limiting."""
    return _normalize_endpoint(path)


def _parse_rate_limit_overrides(raw: str) -> dict[str, RateLimitRule]:
    rules: dict[str, RateLimitRule] = {}
    for item in raw.split(","):
        item = item.strip()
        if not item or "=" not in item:
            continue
        endpoint, spec = item.split("=", 1)
        endpoint = _normalize_endpoint(endpoint.strip())
        parts = [part.strip() for part in spec.split(":", 1)]
        try:
            rate = float(parts[0])
            burst = int(parts[1]) if len(parts) > 1 and parts[1] else max(1, int(rate))
        except ValueError:
            continue
        rules[endpoint] = RateLimitRule(rate, max(1, burst), "env")
    return rules


def _rate_limit_rule_for_endpoint(endpoint: str) -> RateLimitRule:
    endpoint = _normalize_endpoint(endpoint)
    overrides = _parse_rate_limit_overrides(os.getenv("LINGXING_OPENAPI_RATE_LIMIT_OVERRIDES", ""))
    if endpoint in overrides:
        return overrides[endpoint]
    if endpoint in KNOWN_RATE_LIMIT_RULES:
        return KNOWN_RATE_LIMIT_RULES[endpoint]
    return RateLimitRule(
        _env_float("LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_RPS", 1.0),
        max(1, _env_int("LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_BURST", 1)),
        "default",
    )


def rate_limit_rule_for_endpoint(endpoint: str) -> RateLimitRule:
    """Return the effective rate-limit rule for an OpenAPI endpoint."""
    return _rate_limit_rule_for_endpoint(endpoint)


def rate_limit_runtime_settings() -> dict[str, Any]:
    """Return process runtime settings that affect local OpenAPI throttling."""
    return {
        "enabled": _env_bool("LINGXING_OPENAPI_RATE_LIMIT_ENABLED", True),
        "default_rate_per_second": _env_float("LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_RPS", 1.0),
        "default_burst": max(1, _env_int("LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_BURST", 1)),
        "wait_timeout_seconds": _env_float("LINGXING_OPENAPI_RATE_LIMIT_WAIT_TIMEOUT", 60.0),
        "override_count": len(_parse_rate_limit_overrides(os.getenv("LINGXING_OPENAPI_RATE_LIMIT_OVERRIDES", ""))),
    }


def rate_limit_policy_for_endpoint(endpoint: str) -> dict[str, Any]:
    """Return a machine-readable throttling policy for one endpoint."""
    normalized = _normalize_endpoint(endpoint)
    rule = _rate_limit_rule_for_endpoint(normalized)
    settings = rate_limit_runtime_settings()
    if not settings["enabled"]:
        guidance = "服务端本地限流当前关闭；客户端仍应避免并发打爆领星 OpenAPI。"
    elif rule.rate_per_second <= 1.0 and rule.burst <= 1:
        guidance = "该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。"
    else:
        guidance = f"该 endpoint 允许较高吞吐；客户端并发不应超过 burst={rule.burst}，长期速率不应超过 {rule.rate_per_second:g} req/s。"
    return {
        "endpoint": normalized,
        "rate_per_second": rule.rate_per_second,
        "burst": rule.burst,
        "source": rule.source,
        "enabled": settings["enabled"],
        "wait_timeout_seconds": settings["wait_timeout_seconds"],
        "client_guidance": guidance,
    }


class _TokenBucket:
    def __init__(self, rule: RateLimitRule) -> None:
        self.rate_per_second = max(0.0, float(rule.rate_per_second))
        self.capacity = max(1, int(rule.burst))
        self.tokens = float(self.capacity)
        self.updated_at = time.monotonic()
        self.condition = threading.Condition()

    def update(self, rule: RateLimitRule) -> None:
        with self.condition:
            self._refill(time.monotonic())
            self.rate_per_second = max(0.0, float(rule.rate_per_second))
            self.capacity = max(1, int(rule.burst))
            self.tokens = min(float(self.capacity), self.tokens)
            self.condition.notify_all()

    def _refill(self, now: float) -> None:
        if self.rate_per_second <= 0:
            self.updated_at = now
            return
        elapsed = max(0.0, now - self.updated_at)
        if elapsed:
            self.tokens = min(float(self.capacity), self.tokens + elapsed * self.rate_per_second)
            self.updated_at = now

    def acquire(self, timeout: float) -> float | None:
        if self.rate_per_second <= 0:
            return 0.0
        started_at = time.monotonic()
        deadline = started_at + timeout if timeout > 0 else started_at
        with self.condition:
            while True:
                now = time.monotonic()
                self._refill(now)
                if self.tokens >= 1.0:
                    self.tokens -= 1.0
                    return now - started_at
                remaining = deadline - now
                if remaining <= 0:
                    return None
                seconds_until_token = (1.0 - self.tokens) / self.rate_per_second
                self.condition.wait(min(remaining, max(0.01, seconds_until_token)))


def _get_rate_limit_bucket(endpoint: str, rule: RateLimitRule) -> _TokenBucket:
    endpoint = _normalize_endpoint(endpoint)
    with _RATE_LIMIT_BUCKETS_LOCK:
        bucket = _RATE_LIMIT_BUCKETS.get(endpoint)
        if bucket is None:
            bucket = _TokenBucket(rule)
            _RATE_LIMIT_BUCKETS[endpoint] = bucket
        else:
            bucket.update(rule)
        return bucket


@dataclass
class TokenBundle:
    access_token: str
    refresh_token: str
    expires_at: int

    def is_valid(self, lead_seconds: int = 60) -> bool:
        return bool(self.access_token) and self.expires_at > int(time.time()) + lead_seconds


@dataclass
class PagedRows:
    rows: list[dict[str, Any]]
    page_count: int
    total: int | None
    next_token: str | None = None


@dataclass
class DownloadedFile:
    url: str
    final_url: str
    filename: str | None
    content_type: str | None
    content_encoding: str | None
    size: int
    parsed_format: str | None
    data: Any
    warnings: list[str]


@dataclass
class RawResponse:
    body: bytes
    headers: dict[str, str]
    final_url: str


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def extract_path_value(payload: Any, path: str | None) -> Any:
    if not path:
        return payload
    current = payload
    for part in path.split("."):
        if not part:
            continue
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def _multipart_form_data(fields: dict[str, str]) -> tuple[bytes, str]:
    boundary = f"----LingxingBoundary{uuid.uuid4().hex}"
    lines: list[bytes] = []
    for name, value in fields.items():
        lines.append(f"--{boundary}".encode("utf-8"))
        disposition = f'Content-Disposition: form-data; name="{name}"'
        lines.append(disposition.encode("utf-8"))
        lines.append(b"")
        lines.append(str(value).encode("utf-8"))
    lines.append(f"--{boundary}--".encode("utf-8"))
    body = b"\r\n".join(lines) + b"\r\n"
    return body, f"multipart/form-data; boundary={boundary}"


def _stringify_sign_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (dict, list)):
        return _json_dumps(value)
    return str(value)


def build_sign_payload(params: dict[str, Any]) -> str:
    pairs: list[str] = []
    for key in sorted(params.keys()):
        value = params[key]
        rendered = _stringify_sign_value(value)
        if rendered == "":
            continue
        pairs.append(f"{key}={rendered}")
    return "&".join(pairs)


def _run_openssl_aes_ecb(plaintext: str, key: str) -> str:
    key_bytes = key.encode("utf-8")
    if len(key_bytes) not in {16, 24, 32}:
        raise LingxingSignError("appId 不是合法的 AES key 长度（需要 16/24/32 字节）")
    command = [
        "openssl",
        "enc",
        f"-aes-{len(key_bytes) * 8}-ecb",
        "-K",
        key_bytes.hex(),
        "-nosalt",
        "-base64",
        "-A",
    ]
    result = subprocess.run(
        command,
        input=plaintext.encode("utf-8"),
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="ignore").strip()
        raise LingxingSignError(f"openssl 生成 sign 失败: {stderr or '未知错误'}")
    return result.stdout.decode("utf-8").strip()


def generate_sign(params: dict[str, Any], app_key: str) -> str:
    payload = build_sign_payload(params)
    md5_upper = hashlib.md5(payload.encode("utf-8")).hexdigest().upper()
    return _run_openssl_aes_ecb(md5_upper, app_key)


def env_or_raise(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise LingxingConfigError(f"缺少环境变量: {name}")
    return value


class LingxingOpenAPIClient:
    """Thin wrapper around LingXing OpenAPI."""

    def __init__(
        self,
        app_id: str | None = None,
        app_secret: str | None = None,
        token_cache_file: str | Path | None = None,
        base_url: str = AUTH_BASE_URL,
        timeout: int = 30,
    ) -> None:
        self.app_id = app_id or env_or_raise("LINGXING_APP_ID")
        self.app_secret = app_secret or env_or_raise("LINGXING_APP_SECRET")
        cache_path = token_cache_file or os.getenv("LINGXING_TOKEN_CACHE_FILE") or DEFAULT_TOKEN_CACHE
        self.token_cache_file = Path(cache_path)
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get_cached_token(self) -> TokenBundle | None:
        if not self.token_cache_file.exists():
            return None
        try:
            payload = json.loads(self.token_cache_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return None
        access_token = str(payload.get("access_token") or "")
        refresh_token = str(payload.get("refresh_token") or "")
        expires_at = int(payload.get("expires_at") or 0)
        if not access_token or not refresh_token or not expires_at:
            return None
        return TokenBundle(access_token=access_token, refresh_token=refresh_token, expires_at=expires_at)

    def _write_token_cache(self, bundle: TokenBundle) -> None:
        self.token_cache_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "access_token": bundle.access_token,
            "refresh_token": bundle.refresh_token,
            "expires_at": bundle.expires_at,
            "updated_at": int(time.time()),
        }
        self.token_cache_file.write_text(_json_dumps(payload), encoding="utf-8")

    def _request_bytes(self, request: urllib.request.Request, *, endpoint: str) -> RawResponse:
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = response.read()
                headers = {str(key): str(value) for key, value in response.info().items()}
                final_url = str(response.geturl() or request.full_url)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="ignore")
            raise LingxingTransportError(
                f"HTTP {exc.code}: {detail or '空响应'}",
                endpoint=endpoint,
                code=exc.code,
                hint=hint_for_business_error(exc.code, detail, endpoint),
            ) from exc
        except urllib.error.URLError as exc:
            raise LingxingTransportError(
                f"网络请求失败: {exc}",
                endpoint=endpoint,
                hint=hint_for_business_error(None, str(exc), endpoint),
            ) from exc
        return RawResponse(body=body, headers=headers, final_url=final_url)

    def _request(self, request: urllib.request.Request, *, endpoint: str) -> dict[str, Any]:
        raw_response = self._request_bytes(request, endpoint=endpoint)
        raw = raw_response.body.decode("utf-8", errors="ignore")
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise LingxingTransportError(
                f"响应不是合法 JSON: {raw[:200]}",
                endpoint=endpoint,
            ) from exc

    def _token_bundle_from_payload(self, payload: dict[str, Any]) -> TokenBundle:
        self._ensure_success(payload, "token")
        data = payload.get("data") or {}
        access_token = str(data.get("access_token") or "")
        refresh_token = str(data.get("refresh_token") or "")
        expires_in = int(data.get("expires_in") or 0)
        if not access_token or not refresh_token or not expires_in:
            raise LingxingRequestError("Token 响应缺少字段", endpoint="token", details={"payload": payload})
        return TokenBundle(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=int(time.time()) + max(expires_in - 120, 60),
        )

    def fetch_access_token(self) -> TokenBundle:
        endpoint = "/api/auth-server/oauth/access-token"
        body, content_type = _multipart_form_data(
            {
                "appId": self.app_id,
                "appSecret": self.app_secret,
            }
        )
        request = urllib.request.Request(
            url=f"{self.base_url}{endpoint}",
            data=body,
            method="POST",
            headers={"Content-Type": content_type},
        )
        payload = self._request(request, endpoint=endpoint)
        bundle = self._token_bundle_from_payload(payload)
        self._write_token_cache(bundle)
        return bundle

    def refresh_access_token(self, refresh_token: str) -> TokenBundle:
        endpoint = "/api/auth-server/oauth/refresh"
        body, content_type = _multipart_form_data(
            {
                "appId": self.app_id,
                "refreshToken": refresh_token,
            }
        )
        request = urllib.request.Request(
            url=f"{self.base_url}{endpoint}",
            data=body,
            method="POST",
            headers={"Content-Type": content_type},
        )
        payload = self._request(request, endpoint=endpoint)
        bundle = self._token_bundle_from_payload(payload)
        self._write_token_cache(bundle)
        return bundle

    def ensure_access_token(self) -> TokenBundle:
        cached = self.get_cached_token()
        if cached and cached.is_valid():
            return cached
        if cached and cached.refresh_token:
            try:
                refreshed = self.refresh_access_token(cached.refresh_token)
                if refreshed.is_valid(lead_seconds=0):
                    return refreshed
            except LingxingClientError:
                pass
        return self.fetch_access_token()

    def _build_public_query(self, business_params: dict[str, Any]) -> dict[str, str]:
        token_bundle = self.ensure_access_token()
        timestamp = str(int(time.time()))
        params_for_sign = dict(business_params)
        params_for_sign.update(
            {
                "access_token": token_bundle.access_token,
                "app_key": self.app_id,
                "timestamp": timestamp,
            }
        )
        sign = generate_sign(params_for_sign, self.app_id)
        return {
            "access_token": token_bundle.access_token,
            "app_key": self.app_id,
            "timestamp": timestamp,
            "sign": sign,
        }

    def _ensure_success(self, payload: dict[str, Any], endpoint: str) -> None:
        code = payload.get("code")
        if code not in SUCCESS_CODES:
            message = payload.get("message") or payload.get("msg") or "未知错误"
            raise LingxingRequestError(
                str(message),
                endpoint=endpoint,
                code=code,
                hint=hint_for_business_error(code, str(message), endpoint),
                details={"payload": payload},
            )

    def _apply_rate_limit(self, endpoint: str) -> None:
        if not _env_bool("LINGXING_OPENAPI_RATE_LIMIT_ENABLED", True):
            return
        endpoint = _normalize_endpoint(endpoint)
        rule = _rate_limit_rule_for_endpoint(endpoint)
        if rule.rate_per_second <= 0:
            return
        timeout = max(0.0, _env_float("LINGXING_OPENAPI_RATE_LIMIT_WAIT_TIMEOUT", 60.0))
        waited = _get_rate_limit_bucket(endpoint, rule).acquire(timeout)
        if waited is None:
            raise LingxingRequestError(
                "等待领星 OpenAPI 限流令牌超时，请稍后重试或调低客户端并发。",
                endpoint=endpoint,
                code="local_rate_limit_timeout",
                details={
                    "rate_per_second": rule.rate_per_second,
                    "burst": rule.burst,
                    "rule_source": rule.source,
                    "wait_timeout": timeout,
                },
            )

    def get_json(self, path: str, query_params: dict[str, Any] | None = None) -> dict[str, Any]:
        path = f"/{path.lstrip('/')}"
        query_params = dict(query_params or {})
        public_query = self._build_public_query(query_params)
        merged_query = {**public_query, **{key: _stringify_sign_value(value) for key, value in query_params.items()}}
        query = urllib.parse.urlencode(merged_query)
        request = urllib.request.Request(url=f"{self.base_url}{path}?{query}", method="GET")
        self._apply_rate_limit(path)
        payload = self._request(request, endpoint=path)
        self._ensure_success(payload, path)
        return payload

    def post_json(
        self,
        path: str,
        json_body: dict[str, Any] | None = None,
        query_params: dict[str, Any] | None = None,
        extra_headers: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        path = f"/{path.lstrip('/')}"
        json_body = dict(json_body or {})
        query_params = dict(query_params or {})
        sign_params = dict(json_body)
        sign_params.update(query_params)
        public_query = self._build_public_query(sign_params)
        query = urllib.parse.urlencode(public_query)
        headers = {"Content-Type": "application/json"}
        if extra_headers:
            headers.update({str(key): str(value) for key, value in extra_headers.items()})
        request = urllib.request.Request(
            url=f"{self.base_url}{path}?{query}",
            data=_json_dumps(json_body).encode("utf-8"),
            method="POST",
            headers=headers,
        )
        self._apply_rate_limit(path)
        payload = self._request(request, endpoint=path)
        self._ensure_success(payload, path)
        return payload

    def paged_post_detailed(
        self,
        path: str,
        body: dict[str, Any],
        *,
        page_size: int,
        data_path: str = "data",
        total_path: str | None = "total",
        next_token_path: str | None = "next_token",
        pagination_mode: str = "offset",
        extra_headers: dict[str, str] | None = None,
    ) -> PagedRows:
        results: list[dict[str, Any]] = []
        page_count = 0
        total: int | None = None
        next_token: str | None = None
        if pagination_mode == "next_token":
            while True:
                page_count += 1
                page_body = dict(body)
                page_body["length"] = page_size
                if next_token:
                    page_body["next_token"] = next_token
                payload = self.post_json(path, page_body, extra_headers=extra_headers)
                data = extract_path_value(payload, data_path) or []
                if not isinstance(data, list):
                    raise LingxingRequestError(
                        f"{path} 返回 {data_path} 不是数组",
                        endpoint=path,
                        details={"payload": payload},
                    )
                results.extend(data)
                total_raw = extract_path_value(payload, total_path)
                total = int(total_raw) if total_raw not in (None, "") else total
                new_next_token = extract_path_value(payload, next_token_path)
                if not new_next_token or str(new_next_token) == str(next_token or ""):
                    next_token = str(new_next_token or "") or None
                    break
                next_token = str(new_next_token)
            return PagedRows(rows=results, page_count=page_count, total=total, next_token=next_token)

        offset = int(body.get("offset") or 0)
        while True:
            page_count += 1
            page_body = dict(body)
            page_body["offset"] = offset
            page_body["length"] = page_size
            payload = self.post_json(path, page_body, extra_headers=extra_headers)
            data = extract_path_value(payload, data_path) or []
            if not isinstance(data, list):
                raise LingxingRequestError(
                    f"{path} 返回 {data_path} 不是数组",
                    endpoint=path,
                    details={"payload": payload},
                )
            results.extend(data)
            total_raw = extract_path_value(payload, total_path)
            total = int(total_raw) if total_raw not in (None, "") else len(results)
            offset += len(data)
            if not data or offset >= total:
                break
        return PagedRows(rows=results, page_count=page_count, total=total, next_token=None)

    def paged_post(
        self,
        path: str,
        body: dict[str, Any],
        *,
        page_size: int,
        data_path: str = "data",
        total_path: str | None = "total",
        next_token_path: str | None = "next_token",
        pagination_mode: str = "offset",
        extra_headers: dict[str, str] | None = None,
    ) -> list[dict[str, Any]]:
        return self.paged_post_detailed(
            path,
            body,
            page_size=page_size,
            data_path=data_path,
            total_path=total_path,
            next_token_path=next_token_path,
            pagination_mode=pagination_mode,
            extra_headers=extra_headers,
        ).rows

    def download_file(self, url: str, *, extra_headers: dict[str, str] | None = None) -> DownloadedFile:
        request = urllib.request.Request(url=url, method="GET", headers=extra_headers or {})
        raw_response = self._request_bytes(request, endpoint=url)
        return self._parse_download_response(url, raw_response)

    def _parse_download_response(self, url: str, raw_response: RawResponse) -> DownloadedFile:
        body = raw_response.body
        headers = raw_response.headers
        warnings: list[str] = []
        content_type = headers.get("Content-Type") or headers.get("content-type")
        content_encoding = headers.get("Content-Encoding") or headers.get("content-encoding")
        filename = None
        disposition = headers.get("Content-Disposition") or headers.get("content-disposition") or ""
        if "filename=" in disposition:
            filename = disposition.split("filename=", 1)[1].strip().strip('"')
        parsed_format: str | None = None
        data: Any = None

        lower_url = raw_response.final_url.lower()
        lower_filename = (filename or "").lower()
        is_gzip = content_encoding == "gzip" or lower_url.endswith(".gz") or lower_filename.endswith(".gz")
        if is_gzip:
            body = gzip.decompress(body)
            parsed_format = "gzip"
            if filename and filename.lower().endswith(".gz"):
                filename = filename[:-3]
            if lower_url.endswith(".gz"):
                lower_url = lower_url[:-3]

        is_zip = lower_url.endswith(".zip") or lower_filename.endswith(".zip") or body[:4] == b"PK\x03\x04"
        if is_zip:
            files: list[dict[str, Any]] = []
            with zipfile.ZipFile(io.BytesIO(body)) as archive:
                for member in archive.namelist():
                    file_bytes = archive.read(member)
                    parsed_member, member_format = self._parse_table_or_text(member, file_bytes)
                    files.append({"name": member, "format": member_format, "data": parsed_member})
            parsed_format = "zip"
            data = files
        elif content_type and "json" in content_type.lower():
            data = json.loads(body.decode("utf-8", errors="ignore"))
            parsed_format = "json"
        else:
            parse_name = filename or raw_response.final_url
            if str(parse_name).lower().endswith(".gz"):
                parse_name = str(parse_name)[:-3]
            data, member_format = self._parse_table_or_text(str(parse_name), body)
            parsed_format = parsed_format or member_format
            if member_format is None:
                warnings.append("未识别下载文件格式，按文本返回。")

        return DownloadedFile(
            url=url,
            final_url=raw_response.final_url,
            filename=filename,
            content_type=content_type,
            content_encoding=content_encoding,
            size=len(raw_response.body),
            parsed_format=parsed_format,
            data=data,
            warnings=warnings,
        )

    def _parse_table_or_text(self, name: str, body: bytes) -> tuple[Any, str | None]:
        lower_name = (name or "").lower()
        text = body.decode("utf-8", errors="ignore")
        if lower_name.endswith(".json"):
            return json.loads(text), "json"
        if lower_name.endswith(".csv"):
            return list(csv.DictReader(io.StringIO(text))), "csv"
        if lower_name.endswith(".tsv") or ("\t" in text and "\n" in text):
            return list(csv.DictReader(io.StringIO(text), delimiter="\t")), "tsv"
        return text, "text"
