"""Shared LingXing error types and hints."""

from __future__ import annotations

from typing import Any


def hint_for_business_error(code: Any, message: str, endpoint: str | None = None) -> str | None:
    text = str(message or "").strip()
    endpoint_text = str(endpoint or "").strip()
    code_text = str(code or "").strip()
    combined = f"{code_text} {text} {endpoint_text}".lower()

    if "403" in combined or "授权失效" in text or "权限" in text:
        return "请检查领星开放平台授权有效期、接口权限范围，以及调用 IP 是否在白名单内。"
    if "sign" in combined or "签名" in text:
        return "请检查 sign 生成规则、请求参数排序和 appId AES key 长度。"
    if "timeout" in combined or "超时" in text:
        return "请稍后重试，并确认当前网络是否能访问 openapi.lingxing.com。"
    if "network" in combined or "网络" in text:
        return "请检查当前机器网络、DNS 和 HTTPS 访问能力。"
    return None


class LingxingClientError(RuntimeError):
    """Base LingXing client error with structured metadata."""

    def __init__(
        self,
        message: str,
        *,
        endpoint: str | None = None,
        code: Any = None,
        hint: str | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.message = str(message)
        self.endpoint = endpoint
        self.code = code
        self.hint = hint
        self.details = details or {}
        super().__init__(self.__str__())

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "message": self.message,
        }
        if self.endpoint:
            payload["endpoint"] = self.endpoint
        if self.code not in (None, ""):
            payload["code"] = self.code
        if self.hint:
            payload["hint"] = self.hint
        if self.details:
            payload["details"] = self.details
        return payload

    def __str__(self) -> str:
        parts = []
        if self.endpoint:
            parts.append(self.endpoint)
        if self.code not in (None, ""):
            parts.append(f"code={self.code}")
        parts.append(self.message)
        if self.hint:
            parts.append(f"hint={self.hint}")
        return " | ".join(parts)


class LingxingConfigError(LingxingClientError):
    """Configuration error such as missing environment variables."""


class LingxingTransportError(LingxingClientError):
    """HTTP/network layer error."""


class LingxingSignError(LingxingClientError):
    """Signature generation error."""


class LingxingRequestError(LingxingClientError):
    """Business-level request error returned by LingXing."""

