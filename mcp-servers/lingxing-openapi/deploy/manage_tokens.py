#!/usr/bin/env python3
"""Manage LingXing MCP member tokens for shared HTTP gateway."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi import (  # noqa: E402
    LingxingConfigError,
    init_tokens_file,
    load_tokens_file,
    revoke_token,
    rotate_token,
    set_token_role,
    upsert_token,
)


def _print_json(payload: object) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage Lingxing MCP team member tokens")
    parser.add_argument("--tokens-file", required=True, help="Token file path, for example /etc/lingxing-mcp/tokens.json")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_cmd = subparsers.add_parser("init", help="Initialize the token file and create the first admin token")
    init_cmd.add_argument("--id", default="admin", help="First token ID, default admin")
    init_cmd.add_argument("--description", default="Gateway admin bootstrap token", help="Token description")
    init_cmd.add_argument("--token", default="", help="Custom token value; generated automatically when omitted")
    init_cmd.add_argument("--role", default="minimal", help="Member role, default minimal; recommended values: minimal, operations, finance")

    list_cmd = subparsers.add_parser("list", help="List tokens")
    list_cmd.add_argument("--show-token", action="store_true", help="Show full token values; default only shows masked previews")

    add_cmd = subparsers.add_parser("add", help="Add a member token; overwrites the token if ID already exists")
    add_cmd.add_argument("--id", required=True, help="Member token ID, for example alice-mac")
    add_cmd.add_argument("--description", default="", help="Member description")
    add_cmd.add_argument("--token", default="", help="Custom token value; generated automatically when omitted")
    add_cmd.add_argument("--role", default="minimal", help="Member role, default minimal; recommended values: minimal, operations, finance")

    revoke_cmd = subparsers.add_parser("revoke", help="Revoke a member token")
    revoke_cmd.add_argument("--id", required=True, help="Member token ID")

    rotate_cmd = subparsers.add_parser("rotate", help="Rotate a member token")
    rotate_cmd.add_argument("--id", required=True, help="Member token ID")
    rotate_cmd.add_argument("--token", default="", help="Custom new token; generated automatically when omitted")

    role_cmd = subparsers.add_parser("set-role", help="Change member role without rotating the token")
    role_cmd.add_argument("--id", required=True, help="Member token ID")
    role_cmd.add_argument("--role", required=True, help="Member role; recommended values: minimal, operations, finance")

    return parser


def main() -> int:
    args = build_parser().parse_args()
    tokens_file = args.tokens_file
    try:
        if args.command == "init":
            path, token = init_tokens_file(
                tokens_file,
                token_id=args.id,
                description=args.description,
                token=args.token or None,
                role=args.role or None,
            )
            _print_json(
                {
                    "ok": True,
                    "action": "init",
                    "tokens_file": str(path),
                    "token_id": args.id,
                    "role": args.role or "minimal",
                    "token": token,
                    "next_step": "把该令牌发给管理员客户端，并在接入完成后新增其他成员令牌。",
                }
            )
            return 0

        if args.command == "list":
            rows = []
            for record in load_tokens_file(tokens_file):
                payload = record.to_public_dict()
                if args.show_token:
                    payload["token"] = record.token
                rows.append(payload)
            _print_json({"ok": True, "tokens_file": str(Path(tokens_file).expanduser()), "tokens": rows})
            return 0

        if args.command == "add":
            token = upsert_token(
                tokens_file,
                token_id=args.id,
                description=args.description,
                token=args.token or None,
                role=args.role or None,
            )
            _print_json(
                {
                    "ok": True,
                    "action": "add",
                    "token_id": args.id,
                    "role": args.role or "minimal",
                    "token": token,
                    "message": "新增成功，请把该令牌单独发给对应成员。",
                }
            )
            return 0

        if args.command == "revoke":
            changed = revoke_token(tokens_file, token_id=args.id)
            _print_json({"ok": changed, "action": "revoke", "token_id": args.id})
            return 0 if changed else 1

        if args.command == "rotate":
            token = rotate_token(tokens_file, token_id=args.id, token=args.token or None)
            _print_json(
                {
                    "ok": True,
                    "action": "rotate",
                    "token_id": args.id,
                    "token": token,
                    "message": "轮换成功，请通知成员更新本机配置。",
                }
            )
            return 0

        if args.command == "set-role":
            changed = set_token_role(tokens_file, token_id=args.id, role=args.role or None)
            _print_json({"ok": changed, "action": "set-role", "token_id": args.id, "role": args.role or "minimal"})
            return 0 if changed else 1
    except LingxingConfigError as exc:
        _print_json({"ok": False, "error": exc.to_dict()})
        return 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
