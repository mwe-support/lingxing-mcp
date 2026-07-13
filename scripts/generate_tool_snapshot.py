#!/usr/bin/env python3
"""Refresh the checked-in MCP tool and role snapshot from the registry."""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.client import rate_limit_policy_for_endpoint, rate_limit_runtime_settings  # noqa: E402
from lib.lingxing_openapi.endpoint_specs import ALL_ENDPOINT_SPECS  # noqa: E402
from lib.lingxing_openapi.mcp import (  # noqa: E402
    LingxingMCPApplication,
    _rate_limit_description,
    _unique_endpoints,
)


JSON_PATH = ROOT / "docs" / "lingxing-mcp-tool-snapshot-2026-06-05.json"
MARKDOWN_PATH = ROOT / "docs" / "lingxing-mcp-tool-snapshot-2026-06-05.md"


def _required_and_optional(schema: dict[str, Any]) -> tuple[list[str], list[str]]:
    required = list(schema.get("required") or [])
    properties = list((schema.get("properties") or {}).keys())
    return required, [name for name in properties if name not in required]


def _escape_table(value: Any) -> str:
    text = str(value if value not in (None, "") else "None")
    return text.replace("\n", " ").replace("|", "\\|")


def build_snapshot() -> dict[str, Any]:
    os.environ.pop("LINGXING_MCP_ROLE_TOOLS", None)
    app = LingxingMCPApplication()
    old = json.loads(JSON_PATH.read_text(encoding="utf-8")) if JSON_PATH.exists() else {"tools": []}
    old_by_name = {item["name"]: item for item in old.get("tools") or []}
    specs = {spec.tool_name: spec for spec in ALL_ENDPOINT_SPECS}
    tools: list[dict[str, Any]] = []
    for name in sorted(app.tools):
        definition = app.tools[name]
        schema = definition.input_schema
        required, optional = _required_and_optional(schema)
        existing = old_by_name.get(name) or {}
        spec = specs.get(name)
        endpoints = list(_unique_endpoints(definition.rate_limit_endpoints))
        tools.append(
            {
                "name": name,
                "origin": "endpoint_spec" if spec else existing.get("origin", "manual"),
                "category": spec.category if spec else existing.get("category", "manual"),
                "description": definition.description,
                "required_args": required,
                "optional_args": optional,
                "endpoint": spec.endpoint if spec else existing.get("endpoint"),
                "docs_path": spec.docs_path if spec else existing.get("docs_path"),
                "rate_limit_endpoints": endpoints,
                "rate_limit_description": _rate_limit_description(tuple(endpoints)),
                "rate_limit_policies": [rate_limit_policy_for_endpoint(endpoint) for endpoint in endpoints],
                "input_schema": schema,
            }
        )
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "generated_at": generated_at,
        "source": "LingxingMCPApplication built-in role defaults",
        "tool_count": len(tools),
        "roles": {role: sorted(names) for role, names in sorted(app.role_tool_names.items()) if role in {"finance", "minimal", "operations"}},
        "rate_limit_runtime_settings": rate_limit_runtime_settings(),
        "tools": tools,
    }


def render_markdown(snapshot: dict[str, Any]) -> str:
    lines = [
        "# Lingxing MCP Tool Snapshot",
        "",
        f"Generated: {snapshot['generated_at']}",
        f"Source: {snapshot['source']}",
        f"Registered tools: {snapshot['tool_count']}",
        "",
        "## Role Allowlists",
        "",
    ]
    for role, names in snapshot["roles"].items():
        lines.extend([f"### {role} ({len(names)})", ""])
        lines.extend(f"- `{name}`" for name in names)
        lines.append("")
    lines.extend(
        [
            "## Tool Index",
            "",
            "| # | Tool | Origin | Category | Required args | Optional args | Endpoint | Rate limit | Description |",
            "|---:|---|---|---|---|---|---|---|---|",
        ]
    )
    for index, tool in enumerate(snapshot["tools"], 1):
        required = ", ".join(tool["required_args"]) or "None"
        optional = ", ".join(tool["optional_args"]) or "None"
        endpoint = tool["endpoint"] or "Manual"
        lines.append(
            f"| {index} | `{tool['name']}` | `{tool['origin']}` | `{tool['category']}` | "
            f"{_escape_table(required)} | {_escape_table(optional)} | `{_escape_table(endpoint)}` | "
            f"{_escape_table(tool['rate_limit_description'])} | {_escape_table(tool['description'])} |"
        )
    lines.extend(["", "## Tool Details", ""])
    for index, tool in enumerate(snapshot["tools"], 1):
        required = ", ".join(tool["required_args"]) or "None"
        optional = ", ".join(tool["optional_args"]) or "None"
        endpoint = tool["endpoint"] or "Manual"
        docs_path = tool["docs_path"] or "None"
        rate_endpoints = ", ".join(tool["rate_limit_endpoints"]) or "None"
        lines.extend(
            [
                f"### {index}. `{tool['name']}`",
                "",
                f"- Origin: `{tool['origin']}`",
                f"- Category: `{tool['category']}`",
                f"- Description: {tool['description']}",
                f"- Endpoint: `{endpoint}`",
                f"- Docs path: `{docs_path}`",
                f"- Rate-limit endpoints: {rate_endpoints}",
                f"- Rate limit: {tool['rate_limit_description']}",
                f"- Required args: {required}",
                f"- Optional args: {optional}",
                "- Input schema:",
                "",
                "```json",
                json.dumps(tool["input_schema"], ensure_ascii=False, indent=2),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    snapshot = build_snapshot()
    JSON_PATH.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MARKDOWN_PATH.write_text(render_markdown(snapshot), encoding="utf-8")
    print(json.dumps({"ok": True, "tool_count": snapshot["tool_count"], "roles": {key: len(value) for key, value in snapshot["roles"].items()}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
