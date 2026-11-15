"""Token-based HTTP auth helpers for LingXing MCP."""

from __future__ import annotations

import json
import secrets
from dataclasses import dataclass, replace
from datetime import datetime
from pathlib import Path
from typing import Any

from .errors import LingxingConfigError


TOKENS_FILE_VERSION = 1


def _now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def generate_member_token() -> str:
    return secrets.token_urlsafe(32)


def _mask_token(token: str) -> str:
    if len(token) <= 10:
        return "*" * len(token)
    return f"{token[:4]}...{token[-4:]}"


@dataclass(frozen=True)
class AuthTokenRecord:
    token_id: str
    token: str
    description: str
    status: str
    created_at: str
    updated_at: str
    revoked_at: str | None = None
    role: str | None = None
    lingxing_uid: int | None = None
    allowed_sids: tuple[int, ...] = ()
    allowed_profile_ids: tuple[int, ...] = ()

    @property
    def is_active(self) -> bool:
        return self.status == "active" and bool(self.token)

    def to_public_dict(self) -> dict[str, Any]:
        return {
            "id": self.token_id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "revoked_at": self.revoked_at,
            "role": self.role or "minimal",
            "lingxing_uid": self.lingxing_uid,
            "allowed_sid_count": len(self.allowed_sids),
            "allowed_profile_id_count": len(self.allowed_profile_ids),
            "token_preview": _mask_token(self.token),
        }


@dataclass(frozen=True)
class AuthMatch:
    mode: str
    token_id: str
    description: str
    role: str | None = None
    lingxing_uid: int | None = None
    allowed_sids: tuple[int, ...] = ()
    allowed_profile_ids: tuple[int, ...] = ()


@dataclass(frozen=True)
class BearerAuthConfig:
    bootstrap_token: str | None
    tokens_file: Path | None
    records: tuple[AuthTokenRecord, ...]

    def has_any(self) -> bool:
        return bool(self.bootstrap_token) or any(record.is_active for record in self.records)

    def auth_modes(self) -> list[str]:
        modes: list[str] = []
        if self.bootstrap_token:
            modes.append("single")
        if any(record.is_active for record in self.records):
            modes.append("multi")
        return modes

    def authenticate_header(self, authorization: str) -> AuthMatch | None:
        normalized = str(authorization or "").strip()
        if not normalized.startswith("Bearer "):
            return None
        token = normalized[len("Bearer ") :].strip()
        if not token:
            return None
        if self.bootstrap_token and secrets.compare_digest(token, self.bootstrap_token):
            return AuthMatch(mode="single", token_id="bootstrap", description="bootstrap", role=None)
        for record in self.records:
            if record.is_active and secrets.compare_digest(token, record.token):
                return AuthMatch(
                    mode="multi",
                    token_id=record.token_id,
                    description=record.description,
                    role=record.role,
                    lingxing_uid=record.lingxing_uid,
                    allowed_sids=record.allowed_sids,
                    allowed_profile_ids=record.allowed_profile_ids,
                )
        return None

    def summary(self) -> dict[str, Any]:
        return {
            "modes": self.auth_modes(),
            "bootstrap_enabled": bool(self.bootstrap_token),
            "tokens_file": str(self.tokens_file) if self.tokens_file else None,
            "active_member_tokens": len([record for record in self.records if record.is_active]),
        }


def _record_to_file_dict(record: AuthTokenRecord) -> dict[str, Any]:
    payload = {
        "id": record.token_id,
        "description": record.description,
        "token": record.token,
        "status": record.status,
        "created_at": record.created_at,
        "updated_at": record.updated_at,
        "revoked_at": record.revoked_at,
    }
    if record.role:
        payload["role"] = record.role
    if record.lingxing_uid is not None:
        payload["lingxing_uid"] = record.lingxing_uid
        payload["allowed_sids"] = list(record.allowed_sids)
        payload["allowed_profile_ids"] = list(record.allowed_profile_ids)
    return payload


def build_tokens_payload(records: list[AuthTokenRecord]) -> dict[str, Any]:
    return {
        "version": TOKENS_FILE_VERSION,
        "tokens": [_record_to_file_dict(record) for record in records],
    }


def _parse_positive_ints(value: Any, field_name: str) -> tuple[int, ...]:
    if value in (None, ""):
        return ()
    if not isinstance(value, list):
        raise LingxingConfigError(f"令牌字段 {field_name} 必须是整数数组")
    try:
        normalized = sorted({int(item) for item in value})
    except (TypeError, ValueError) as exc:
        raise LingxingConfigError(f"令牌字段 {field_name} 必须是整数数组") from exc
    if any(item <= 0 for item in normalized):
        raise LingxingConfigError(f"令牌字段 {field_name} 只能包含正整数")
    return tuple(normalized)


def _parse_record(raw: dict[str, Any], index: int) -> AuthTokenRecord:
    token_id = str(raw.get("id") or f"token-{index + 1}").strip()
    token = str(raw.get("token") or "").strip()
    description = str(raw.get("description") or "").strip()
    status = str(raw.get("status") or "").strip().lower() or "active"
    created_at = str(raw.get("created_at") or "").strip() or _now_iso()
    updated_at = str(raw.get("updated_at") or "").strip() or created_at
    revoked_at = str(raw.get("revoked_at") or "").strip() or None
    role = str(raw.get("role") or "").strip() or None
    lingxing_uid_raw = raw.get("lingxing_uid")
    try:
        lingxing_uid = int(lingxing_uid_raw) if lingxing_uid_raw not in (None, "") else None
    except (TypeError, ValueError) as exc:
        raise LingxingConfigError("令牌字段 lingxing_uid 必须是正整数") from exc
    if lingxing_uid is not None and lingxing_uid <= 0:
        raise LingxingConfigError("令牌字段 lingxing_uid 必须是正整数")
    allowed_sids = _parse_positive_ints(raw.get("allowed_sids"), "allowed_sids")
    allowed_profile_ids = _parse_positive_ints(raw.get("allowed_profile_ids"), "allowed_profile_ids")
    enabled = raw.get("enabled")
    if enabled is False and status == "active":
        status = "disabled"
    return AuthTokenRecord(
        token_id=token_id,
        token=token,
        description=description,
        status=status,
        created_at=created_at,
        updated_at=updated_at,
        revoked_at=revoked_at,
        role=role,
        lingxing_uid=lingxing_uid,
        allowed_sids=allowed_sids,
        allowed_profile_ids=allowed_profile_ids,
    )


def load_tokens_file(tokens_file: str | Path) -> tuple[AuthTokenRecord, ...]:
    path = Path(tokens_file).expanduser()
    if not path.exists():
        raise LingxingConfigError(f"令牌文件不存在: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LingxingConfigError(f"令牌文件不是合法 JSON: {path}") from exc
    raw_tokens = payload.get("tokens")
    if not isinstance(raw_tokens, list):
        raise LingxingConfigError(f"令牌文件缺少 tokens 数组: {path}")
    return tuple(_parse_record(item or {}, index) for index, item in enumerate(raw_tokens))


def load_bearer_auth_config(*, bootstrap_token: str = "", tokens_file: str = "") -> BearerAuthConfig:
    normalized_bootstrap = bootstrap_token.strip() or None
    normalized_file = tokens_file.strip()
    records: tuple[AuthTokenRecord, ...] = ()
    path: Path | None = None
    if normalized_file:
        path = Path(normalized_file).expanduser()
        if path.exists():
            records = load_tokens_file(path)
        elif not normalized_bootstrap:
            raise LingxingConfigError(f"令牌文件不存在: {path}")
    config = BearerAuthConfig(
        bootstrap_token=normalized_bootstrap,
        tokens_file=path,
        records=records,
    )
    if not config.has_any():
        raise LingxingConfigError("HTTP MCP 至少需要一个单令牌或一个有效的多人令牌文件。")
    return config


def init_tokens_file(
    tokens_file: str | Path,
    *,
    token_id: str,
    description: str,
    token: str | None = None,
    role: str | None = None,
) -> tuple[Path, str]:
    path = Path(tokens_file).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise LingxingConfigError(f"令牌文件已存在: {path}")
    value = token or generate_member_token()
    now = _now_iso()
    records = [
        AuthTokenRecord(
            token_id=token_id,
            token=value,
            description=description,
            status="active",
            created_at=now,
            updated_at=now,
            role=role.strip() or None if role else None,
        )
    ]
    path.write_text(json.dumps(build_tokens_payload(records), ensure_ascii=False, indent=2), encoding="utf-8")
    return path, value


def upsert_token(
    tokens_file: str | Path,
    *,
    token_id: str,
    description: str,
    token: str | None = None,
    role: str | None = None,
) -> str:
    path = Path(tokens_file).expanduser()
    existing = list(load_tokens_file(path))
    value = token or generate_member_token()
    now = _now_iso()
    normalized_role = role.strip() or None if role else None
    replaced = False
    for index, record in enumerate(existing):
        if record.token_id == token_id:
            existing[index] = replace(
                record,
                token=value,
                description=description or record.description,
                status="active",
                updated_at=now,
                role=normalized_role if role is not None else record.role,
                revoked_at=None,
            )
            replaced = True
            break
    if not replaced:
        existing.append(
            AuthTokenRecord(
                token_id=token_id,
                token=value,
                description=description,
                status="active",
                created_at=now,
                updated_at=now,
                role=normalized_role,
            )
        )
    path.write_text(json.dumps(build_tokens_payload(existing), ensure_ascii=False, indent=2), encoding="utf-8")
    return value


def revoke_token(tokens_file: str | Path, *, token_id: str) -> bool:
    path = Path(tokens_file).expanduser()
    existing = list(load_tokens_file(path))
    now = _now_iso()
    changed = False
    for index, record in enumerate(existing):
        if record.token_id == token_id and record.status != "revoked":
            existing[index] = replace(
                record,
                status="revoked",
                updated_at=now,
                revoked_at=now,
            )
            changed = True
            break
    if changed:
        path.write_text(json.dumps(build_tokens_payload(existing), ensure_ascii=False, indent=2), encoding="utf-8")
    return changed


def rotate_token(tokens_file: str | Path, *, token_id: str, token: str | None = None) -> str:
    path = Path(tokens_file).expanduser()
    existing = list(load_tokens_file(path))
    now = _now_iso()
    value = token or generate_member_token()
    for index, record in enumerate(existing):
        if record.token_id == token_id:
            existing[index] = replace(
                record,
                token=value,
                status="active",
                updated_at=now,
                revoked_at=None,
            )
            path.write_text(json.dumps(build_tokens_payload(existing), ensure_ascii=False, indent=2), encoding="utf-8")
            return value
    raise LingxingConfigError(f"未找到令牌 ID: {token_id}")


def set_token_role(tokens_file: str | Path, *, token_id: str, role: str | None) -> bool:
    path = Path(tokens_file).expanduser()
    existing = list(load_tokens_file(path))
    now = _now_iso()
    normalized_role = role.strip() or None if role else None
    changed = False
    for index, record in enumerate(existing):
        if record.token_id == token_id:
            existing[index] = replace(
                record,
                updated_at=now,
                role=normalized_role,
            )
            changed = True
            break
    if changed:
        path.write_text(json.dumps(build_tokens_payload(existing), ensure_ascii=False, indent=2), encoding="utf-8")
    return changed
