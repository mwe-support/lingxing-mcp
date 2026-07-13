from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from xml.etree import ElementTree
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

    def test_settlement_profile_keeps_web_headers_when_no_rows_are_returned(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "settlement.xlsx"
            summary = write_records_xlsx([], output, profile="shipment_settlement")

            self.assertEqual(summary["row_count"], 0)
            self.assertEqual(summary["column_count"], 52)
            with zipfile.ZipFile(output) as archive:
                workbook = archive.read("xl/workbook.xml").decode("utf-8")
                sheet = archive.read("xl/worksheets/sheet1.xml").decode("utf-8")
            self.assertIn('name="结算差异报告"', workbook)
            self.assertIn("店铺名称", sheet)
            self.assertIn("含税订单毛利率", sheet)
            self.assertNotIn("autoFilter", sheet)

    def test_transaction_profile_matches_two_row_web_export_layout(self) -> None:
        rows = [
            {
                "storeName": "拓惠美亚马逊-US",
                "country": "美国",
                "currencyCode": "USD",
                "orderId": "114-9493218-6950624",
                "settlementId": "26761815271",
                "productSales": 549,
                "settlementGrossProfitRate": 0.2424,
            }
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "transaction.xlsx"
            summary = write_records_xlsx(rows, output, profile="profit_report_order_transaction")

            self.assertEqual(summary["row_count"], 1)
            self.assertEqual(summary["column_count"], 56)
            with zipfile.ZipFile(output) as archive:
                sheet = archive.read("xl/worksheets/sheet1.xml").decode("utf-8")
            self.assertIn('<mergeCell ref="A1:BD1"/>', sheet)
            self.assertIn("基础信息", sheet)
            self.assertIn("Settlement Id", sheet)
            self.assertIn("24.24%", sheet)
            self.assertIn('r="J3" t="inlineStr"', sheet)

    def test_outbound_profile_explodes_products_and_preserves_long_ids_as_text(self) -> None:
        rows = [
            {
                "wo_number": "WO103710765523995137",
                "order_number": "103710166681993321",
                "status_name": "已出库",
                "seller_name": "易贝优-UK",
                "product_info": [
                    {"sku": "SKU-1", "seller_sku": "MSKU-1", "product_name": "产品一", "count": 1},
                    {"sku": "SKU-2", "seller_sku": "MSKU-2", "product_name": "产品二", "count": 2},
                ],
            }
        ]
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "outbound.xlsx"
            summary = write_records_xlsx(rows, output, profile="sales_outbound_orders")

            self.assertEqual(summary["source_record_count"], 1)
            self.assertEqual(summary["row_count"], 2)
            self.assertEqual(summary["column_count"], 68)
            with zipfile.ZipFile(output) as archive:
                sheet = archive.read("xl/worksheets/sheet1.xml").decode("utf-8")
                ElementTree.fromstring(sheet)
            self.assertIn('<mergeCell ref="A2:A3"/>', sheet)
            self.assertIn('r="B2" t="inlineStr"', sheet)
            self.assertIn("103710166681993321", sheet)
            self.assertIn("SKU-1", sheet)
            self.assertIn("SKU-2", sheet)


if __name__ == "__main__":
    unittest.main()
