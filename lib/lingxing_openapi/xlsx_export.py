"""Dependency-free XLSX writer for MCP export orchestration."""

from __future__ import annotations

import hashlib
import json
import math
import re
import zipfile
from pathlib import Path
from typing import Any, Iterable
from xml.sax.saxutils import escape


_INVALID_XML_CHARS = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
_INVALID_SHEET_CHARS = re.compile(r"[\\/*?:\[\]]")


def _flatten_record(record: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    flattened: dict[str, Any] = {}
    for key, value in record.items():
        name = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, dict):
            flattened.update(_flatten_record(value, name))
        elif isinstance(value, (list, tuple)):
            flattened[name] = json.dumps(value, ensure_ascii=False, default=str)
        else:
            flattened[name] = value
    return flattened


def _column_name(index: int) -> str:
    value = index
    letters = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        letters = chr(65 + remainder) + letters
    return letters


def _clean_text(value: Any) -> str:
    text = _INVALID_XML_CHARS.sub("", str(value))
    return text[:32767]


def _cell_xml(reference: str, value: Any) -> str:
    if isinstance(value, bool):
        return f'<c r="{reference}" t="b"><v>{1 if value else 0}</v></c>'
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if not isinstance(value, float) or math.isfinite(value):
            return f'<c r="{reference}"><v>{value}</v></c>'
    text = escape(_clean_text("" if value is None else value), {'"': "&quot;"})
    return f'<c r="{reference}" t="inlineStr"><is><t xml:space="preserve">{text}</t></is></c>'


def _sheet_name(value: str) -> str:
    name = _INVALID_SHEET_CHARS.sub("_", value).strip().strip("'") or "Report"
    return name[:31]


def _write_sheet(
    archive: zipfile.ZipFile,
    flattened_rows: list[dict[str, Any]],
    headers: list[str],
) -> None:
    last_column = _column_name(max(1, len(headers)))
    last_row = max(1, len(flattened_rows) + 1)
    with archive.open("xl/worksheets/sheet1.xml", "w") as stream:
        stream.write(b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        stream.write(b'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">')
        stream.write(f'<dimension ref="A1:{last_column}{last_row}"/>'.encode("utf-8"))
        stream.write(b'<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
        stream.write(b"<sheetData>")
        stream.write(b'<row r="1">')
        for column_index, header in enumerate(headers, 1):
            stream.write(_cell_xml(f"{_column_name(column_index)}1", header).encode("utf-8"))
        stream.write(b"</row>")
        for row_index, row in enumerate(flattened_rows, 2):
            stream.write(f'<row r="{row_index}">'.encode("utf-8"))
            for column_index, header in enumerate(headers, 1):
                stream.write(
                    _cell_xml(f"{_column_name(column_index)}{row_index}", row.get(header)).encode("utf-8")
                )
            stream.write(b"</row>")
        stream.write(b"</sheetData>")
        if headers:
            stream.write(f'<autoFilter ref="A1:{last_column}{last_row}"/>'.encode("utf-8"))
        stream.write(b"</worksheet>")


def write_records_xlsx(
    records: Iterable[dict[str, Any]],
    output_path: str | Path,
    *,
    sheet_name: str = "Report",
) -> dict[str, Any]:
    """Write records as a flat, filterable XLSX workbook and return a compact summary."""
    rows = [_flatten_record(dict(record)) for record in records]
    headers: list[str] = []
    seen: set[str] = set()
    for row in rows:
        for key in row:
            if key not in seen:
                seen.add(key)
                headers.append(key)

    output = Path(output_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    safe_sheet_name = _sheet_name(sheet_name)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            '</Types>',
        )
        archive.writestr(
            "_rels/.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>'
            '</Relationships>',
        )
        archive.writestr(
            "xl/workbook.xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            f'<sheets><sheet name="{escape(safe_sheet_name, {chr(34): "&quot;"})}" sheetId="1" r:id="rId1"/></sheets>'
            '</workbook>',
        )
        archive.writestr(
            "xl/_rels/workbook.xml.rels",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>'
            '</Relationships>',
        )
        _write_sheet(archive, rows, headers)

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {
        "output": str(output),
        "row_count": len(rows),
        "column_count": len(headers),
        "size_bytes": output.stat().st_size,
        "sha256": digest,
    }
