from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.xlsx_export import write_records_xlsx  # noqa: E402


class XlsxExportTests(unittest.TestCase):
    def test_write_records_xlsx_creates_valid_ooxml_with_flattened_columns(self) -> None:
        rows = [
            {"order": "A-1", "amount": 12.5, "store": {"sid": 101}, "tags": ["FBA", "DE"]},
            {"order": "A-2", "amount": 0, "store": {"sid": 202}, "tags": []},
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "report.xlsx"
            summary = write_records_xlsx(rows, output, sheet_name="Report")

            self.assertEqual(summary["row_count"], 2)
            self.assertEqual(summary["column_count"], 4)
            self.assertGreater(summary["size_bytes"], 0)
            with zipfile.ZipFile(output) as archive:
                self.assertIn("xl/workbook.xml", archive.namelist())
                sheet = archive.read("xl/worksheets/sheet1.xml").decode("utf-8")
            self.assertIn("store.sid", sheet)
            self.assertIn("[&quot;FBA&quot;, &quot;DE&quot;]", sheet)
            self.assertIn('<c r="B2"><v>12.5</v></c>', sheet)


if __name__ == "__main__":
    unittest.main()
