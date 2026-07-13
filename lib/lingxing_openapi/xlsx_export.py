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

from .xlsx_profiles import ExportProfile, get_export_profile


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


def _cell_xml(reference: str, value: Any, style_id: int = 0) -> str:
    style = f' s="{style_id}"' if style_id else ""
    if isinstance(value, bool):
        return f'<c r="{reference}"{style} t="b"><v>{1 if value else 0}</v></c>'
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if not isinstance(value, float) or math.isfinite(value):
            return f'<c r="{reference}"{style}><v>{value}</v></c>'
    text = escape(_clean_text("" if value is None else value), {'"': "&quot;"})
    return f'<c r="{reference}"{style} t="inlineStr"><is><t xml:space="preserve">{text}</t></is></c>'


def _sheet_name(value: str) -> str:
    name = _INVALID_SHEET_CHARS.sub("_", value).strip().strip("'") or "Report"
    return name[:31]


def _write_sheet(
    archive: zipfile.ZipFile,
    flattened_rows: list[dict[str, Any]],
    headers: list[str],
    *,
    number_formats: list[str | None] | None = None,
    group_header: str | None = None,
    merge_order_columns: int = 0,
    web_export_layout: bool = False,
) -> None:
    header_row = 2 if group_header else 1
    first_data_row = header_row + 1
    last_column = _column_name(max(1, len(headers)))
    last_row = max(header_row, len(flattened_rows) + header_row)
    style_by_format = {"integer": 2, "decimal2": 3, "decimal4": 4}
    formats = number_formats or [None] * len(headers)
    merge_ranges: list[str] = []
    if group_header:
        merge_ranges.append(f"A1:{last_column}1")
    if merge_order_columns and flattened_rows:
        group_start = 0
        while group_start < len(flattened_rows):
            group_value = flattened_rows[group_start].get("_merge_group")
            group_end = group_start
            while (
                group_end + 1 < len(flattened_rows)
                and flattened_rows[group_end + 1].get("_merge_group") == group_value
            ):
                group_end += 1
            if group_end > group_start:
                excel_start = first_data_row + group_start
                excel_end = first_data_row + group_end
                for column_index in range(1, min(merge_order_columns, len(headers)) + 1):
                    column = _column_name(column_index)
                    merge_ranges.append(f"{column}{excel_start}:{column}{excel_end}")
            group_start = group_end + 1
    with archive.open("xl/worksheets/sheet1.xml", "w") as stream:
        stream.write(b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        stream.write(b'<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">')
        stream.write(f'<dimension ref="A1:{last_column}{last_row}"/>'.encode("utf-8"))
        if web_export_layout:
            stream.write(b'<sheetViews><sheetView workbookViewId="0"/></sheetViews>')
        else:
            stream.write(b'<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
        stream.write(b'<cols>')
        for column_index in range(1, len(headers) + 1):
            width = "20.7109375" if column_index == 1 else "13"
            stream.write(
                f'<col min="{column_index}" max="{column_index}" width="{width}" customWidth="1"/>'.encode("utf-8")
            )
        stream.write(b'</cols>')
        stream.write(b"<sheetData>")
        if group_header:
            stream.write(b'<row r="1">')
            stream.write(_cell_xml("A1", group_header, 1).encode("utf-8"))
            stream.write(b"</row>")
        stream.write(f'<row r="{header_row}">'.encode("utf-8"))
        for column_index, header in enumerate(headers, 1):
            stream.write(
                _cell_xml(f"{_column_name(column_index)}{header_row}", header, 1).encode("utf-8")
            )
        stream.write(b"</row>")
        for row_index, row in enumerate(flattened_rows, first_data_row):
            stream.write(f'<row r="{row_index}">'.encode("utf-8"))
            for column_index, header in enumerate(headers, 1):
                value = row.get(header)
                if value is None:
                    continue
                style_id = style_by_format.get(formats[column_index - 1], 0)
                stream.write(
                    _cell_xml(f"{_column_name(column_index)}{row_index}", value, style_id).encode("utf-8")
                )
            stream.write(b"</row>")
        stream.write(b"</sheetData>")
        if merge_ranges:
            stream.write(f'<mergeCells count="{len(merge_ranges)}">'.encode("utf-8"))
            for reference in merge_ranges:
                stream.write(f'<mergeCell ref="{reference}"/>'.encode("utf-8"))
            stream.write(b'</mergeCells>')
        if headers and not web_export_layout:
            stream.write(f'<autoFilter ref="A1:{last_column}{last_row}"/>'.encode("utf-8"))
        stream.write(b"</worksheet>")


def _styles_xml() -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<numFmts count="3">'
        '<numFmt numFmtId="164" formatCode="#,##0;-#,##0"/>'
        '<numFmt numFmtId="165" formatCode="#,##0.00;-#,##0.00"/>'
        '<numFmt numFmtId="166" formatCode="#,##0.0000;-#,##0.0000"/>'
        '</numFmts>'
        '<fonts count="2">'
        '<font><sz val="11"/><name val="Calibri"/></font>'
        '<font><b/><sz val="11"/><color rgb="FF000000"/><name val="Calibri"/></font>'
        '</fonts>'
        '<fills count="2"><fill><patternFill patternType="none"/></fill>'
        '<fill><patternFill patternType="gray125"/></fill></fills>'
        '<borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>'
        '<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>'
        '<cellXfs count="5">'
        '<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>'
        '<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1" applyAlignment="1">'
        '<alignment horizontal="center" vertical="center"/></xf>'
        '<xf numFmtId="164" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
        '<xf numFmtId="165" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
        '<xf numFmtId="166" fontId="0" fillId="0" borderId="0" xfId="0" applyNumberFormat="1"/>'
        '</cellXfs>'
        '<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>'
        '</styleSheet>'
    )


def write_records_xlsx(
    records: Iterable[dict[str, Any]],
    output_path: str | Path,
    *,
    sheet_name: str | None = None,
    profile: str | None = None,
) -> dict[str, Any]:
    """Write records as a flat, filterable XLSX workbook and return a compact summary."""
    source_rows = [dict(record) for record in records]
    export_profile: ExportProfile | None = get_export_profile(profile) if profile else None
    if export_profile:
        rows = export_profile.prepare_rows(source_rows)
        headers = [column.header for column in export_profile.columns]
        number_formats = [column.number_format for column in export_profile.columns]
        safe_sheet_name = _sheet_name(sheet_name or export_profile.sheet_name)
    else:
        rows = [_flatten_record(record) for record in source_rows]
        headers = []
        seen: set[str] = set()
        for row in rows:
            for key in row:
                if key not in seen:
                    seen.add(key)
                    headers.append(key)
        number_formats = [None] * len(headers)
        safe_sheet_name = _sheet_name(sheet_name or "Report")

    output = Path(output_path).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        archive.writestr(
            "[Content_Types].xml",
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
            '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
            '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
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
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
            '</Relationships>',
        )
        archive.writestr("xl/styles.xml", _styles_xml())
        _write_sheet(
            archive,
            rows,
            headers,
            number_formats=number_formats,
            group_header=export_profile.group_header if export_profile else None,
            merge_order_columns=export_profile.merge_order_columns if export_profile else 0,
            web_export_layout=export_profile is not None,
        )

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {
        "output": str(output),
        "profile": export_profile.name if export_profile else None,
        "unavailable_columns": list(export_profile.unavailable_columns) if export_profile else [],
        "source_record_count": len(source_rows),
        "row_count": len(rows),
        "column_count": len(headers),
        "size_bytes": output.stat().st_size,
        "sha256": digest,
    }
