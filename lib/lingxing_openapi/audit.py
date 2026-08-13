"""Compact, privacy-conscious audit logging for HTTP MCP requests."""

from __future__ import annotations

import json
import os
import sys
import threading
from datetime import datetime, timezone
from typing import Any, TextIO

from .auth import AuthMatch


AUDIT_EVENT = "mcp_audit"
MAX_ARGUMENT_KEYS = 32
MAX_LIST_SIZE_FIELDS = 16
MAX_TEXT_LENGTH = 128
MAX_AUDIT_BODY_BYTES = 1024 * 1024


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() not in {"0", "false", "no", "off"}


def _bounded_text(value: Any) -> str:
    text = str(value or "")[:MAX_TEXT_LENGTH]
    return "".join(character if character.isalnum() or character in "._:/@-" else "?" for character in text)


def _request_metadata(body: bytes) -> dict[str, Any]:
    if len(body) > MAX_AUDIT_BODY_BYTES:
        return {"mcp_method": "oversized_request"}
    try:
        request = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return {"mcp_method": "invalid_json"}
    if not isinstance(request, dict):
        return {"mcp_method": "invalid_request"}

    method = _bounded_text(request.get("method")) or "unknown"
    metadata: dict[str, Any] = {"mcp_method": method}
    params = request.get("params")
    if not isinstance(params, dict):
        return metadata
    if method != "tools/call":
        return metadata

    metadata["tool"] = _bounded_text(params.get("name")) or "unknown"
    arguments = params.get("arguments")
    if not isinstance(arguments, dict):
        return metadata

    bounded_arguments = list(arguments.items())[:MAX_ARGUMENT_KEYS]
    argument_keys = sorted(_bounded_text(key) for key, _ in bounded_arguments)
    metadata["argument_key_count"] = len(arguments)
    if argument_keys:
        metadata["argument_keys"] = argument_keys

    list_sizes = {
        _bounded_text(key): len(value)
        for key, value in bounded_arguments[:MAX_LIST_SIZE_FIELDS]
        if isinstance(value, list)
    }
    if list_sizes:
        metadata["list_argument_sizes"] = dict(list(list_sizes.items())[:MAX_LIST_SIZE_FIELDS])

    for flag in ("confirm", "dry_run"):
        if isinstance(arguments.get(flag), bool):
            metadata[flag] = arguments[flag]
    response_mode = arguments.get("response_mode")
    if response_mode in {"summary", "full"}:
        metadata["response_mode"] = response_mode
    return metadata


def _response_metadata(status: int, payload: dict[str, Any]) -> dict[str, Any]:
    metadata: dict[str, Any] = {"outcome": "ok"}
    if status == 401:
        metadata["outcome"] = "auth_denied"
    elif status >= 400:
        metadata["outcome"] = "http_error"

    top_error = payload.get("error")
    if top_error:
        metadata["outcome"] = "rpc_error" if isinstance(top_error, dict) else metadata["outcome"]
        if isinstance(top_error, dict):
            metadata["error_code"] = _bounded_text(top_error.get("code"))
        else:
            metadata["error_code"] = _bounded_text(top_error)

    result = payload.get("result")
    if not isinstance(result, dict):
        return metadata
    if result.get("isError") is True:
        metadata["outcome"] = "tool_error"
    structured = result.get("structuredContent")
    if not isinstance(structured, dict):
        tools = result.get("tools")
        if isinstance(tools, list):
            metadata["tool_count"] = len(tools)
        return metadata

    error = structured.get("error")
    if isinstance(error, dict):
        error_code = error.get("code") or error.get("type")
        if error_code:
            metadata["error_code"] = _bounded_text(error_code)
    data = structured.get("data")
    if isinstance(data, dict):
        for name in ("record_count", "returned_count"):
            value = data.get(name)
            if isinstance(value, int) and not isinstance(value, bool):
                metadata[name] = value
    return metadata


def build_audit_event(
    *,
    audit_id: str,
    auth_match: AuthMatch | None,
    body: bytes,
    status: int,
    payload: dict[str, Any],
    duration_ms: float,
    response_bytes: int,
    delivered: bool,
) -> dict[str, Any]:
    event: dict[str, Any] = {
        "ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
        "event": AUDIT_EVENT,
        "audit_id": _bounded_text(audit_id),
        "auth_mode": auth_match.mode if auth_match else "none",
        "token_id": _bounded_text(auth_match.token_id) if auth_match else None,
        "role": _bounded_text(auth_match.role or "minimal") if auth_match else None,
        "http_status": int(status),
        "duration_ms": round(max(0.0, duration_ms), 1),
        "request_bytes": len(body),
        "response_bytes": max(0, int(response_bytes)),
    }
    event.update(_request_metadata(body))
    event.update(_response_metadata(status, payload))
    if not delivered:
        event["outcome"] = "client_disconnected"
    return event


class MCPAuditLogger:
    def __init__(self, *, enabled: bool | None = None, stream: TextIO | None = None) -> None:
        self.enabled = _env_bool("LINGXING_MCP_AUDIT_ENABLED", True) if enabled is None else enabled
        self.stream = stream
        self._lock = threading.Lock()

    def emit(self, event: dict[str, Any]) -> bool:
        if not self.enabled:
            return False
        stream = self.stream or sys.stdout
        line = json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n"
        try:
            with self._lock:
                stream.write(line)
                stream.flush()
            return True
        except (OSError, ValueError):
            return False
