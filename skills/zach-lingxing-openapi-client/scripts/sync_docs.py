#!/usr/bin/env python3
"""Sync LingXing OpenAPI docs discovered from the official sidebar."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.doc_catalog import (  # noqa: E402
    build_index,
    discover_doc_catalog,
    exchange_doc_token,
    fetch_markdown,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="同步领星 OpenAPI 文档目录与只读接口页面")
    parser.add_argument(
        "--doc-access-key",
        default=os.getenv("LINGXING_DOC_ACCESS_KEY", ""),
        help="领星文档密钥，默认读取环境变量 LINGXING_DOC_ACCESS_KEY",
    )
    parser.add_argument(
        "--output-dir",
        default=str(Path(__file__).resolve().parent.parent / "references" / "openapi_docs"),
        help="文档输出目录",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    doc_access_key = args.doc_access_key.strip()
    doc_token: str | None = None
    warnings: list[str] = []
    if doc_access_key:
        try:
            doc_token = exchange_doc_token(doc_access_key)
        except RuntimeError as exc:
            warnings.append(f"文档密钥校验失败，改为匿名抓取: {exc}")

    catalog, catalog_warnings = discover_doc_catalog(doc_token)
    warnings.extend(catalog_warnings)

    manifest = []
    for entry in catalog:
        try:
            content = fetch_markdown(entry.remote_path, doc_token)
        except Exception as exc:
            warnings.append(f"{entry.remote_path}: {exc}")
            continue
        (output_dir / entry.local_file).write_text(content, encoding="utf-8")
        manifest.append(entry.to_manifest())

    (output_dir / "README.md").write_text(build_index(catalog, warnings), encoding="utf-8")
    (output_dir / "doc_catalog.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / "index.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"synced_docs: {output_dir}")
    print(f"doc_count: {len(manifest)}")
    if warnings:
        print(f"warnings: {len(warnings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
