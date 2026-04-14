from __future__ import annotations

import gzip
import io
import sys
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi import (  # noqa: E402
    LingxingOpenAPIClient,
    RawResponse,
    build_sign_payload,
    extract_path_value,
    generate_sign,
    hint_for_business_error,
)


class StubClient(LingxingOpenAPIClient):
    def __init__(self) -> None:
        super().__init__(
            app_id="1234567890123456",
            app_secret="demo-secret",
            token_cache_file=ROOT / "runtime" / "tests" / "token_cache.json",
            base_url="https://example.com",
        )
        self.last_request = None
        self.page_responses: list[dict] = []

    def _build_public_query(self, business_params: dict) -> dict[str, str]:  # noqa: ANN001
        return {
            "access_token": "token-123",
            "app_key": self.app_id,
            "timestamp": "1700000000",
            "sign": "signed",
        }

    def _request(self, request, *, endpoint: str) -> dict:  # noqa: ANN001
        self.last_request = request
        if self.page_responses:
            return self.page_responses.pop(0)
        return {"code": 0, "data": []}


class LingxingClientTests(unittest.TestCase):
    def test_build_sign_payload_skips_empty_string_but_keeps_null(self) -> None:
        payload = build_sign_payload(
            {
                "name": "kobe",
                "empty": "",
                "none_field": None,
                "list_field": [1, 2],
            }
        )
        self.assertEqual(payload, 'list_field=[1,2]&name=kobe&none_field=null')

    def test_build_sign_payload_stringifies_nested_json(self) -> None:
        payload = build_sign_payload(
            {
                "offset": 0,
                "filters": {
                    "status": [1, 2],
                    "keyword": "deal",
                },
            }
        )
        self.assertEqual(payload, 'filters={"status":[1,2],"keyword":"deal"}&offset=0')

    def test_generate_sign_is_stable(self) -> None:
        params = {
            "access_token": "token-123",
            "app_key": "demo-app-key-123",
            "timestamp": "1720429074",
            "offset": 0,
            "length": 100,
        }
        sign = generate_sign(params, "demo-app-key-123")
        self.assertEqual(sign, "KC77jyLYZjZe0yprCYzwCH7fEQMPz/eTmAE+7zVo5SYRi5DRRHDUOBlFHu41v2If")

    def test_hint_for_403_mentions_auth_and_ip(self) -> None:
        hint = hint_for_business_error(403, "授权失效，请更新授权有效期或检查权限", "/erp/sc/data/seller/lists")
        self.assertIn("授权有效期", hint or "")
        self.assertIn("IP", hint or "")

    def test_extract_path_value_supports_nested_paths(self) -> None:
        payload = {"data": {"records": [{"asin": "B0TEST"}]}}
        self.assertEqual(extract_path_value(payload, "data.records"), [{"asin": "B0TEST"}])
        self.assertIsNone(extract_path_value(payload, "data.total"))

    def test_post_json_merges_extra_headers(self) -> None:
        client = StubClient()
        client.post_json("/pb/openapi/newad/demo", {"sid": 1}, extra_headers={"X-API-VERSION": "2"})
        header_items = dict(client.last_request.header_items())
        self.assertEqual(header_items["Content-type"], "application/json")
        self.assertEqual(header_items["X-api-version"], "2")

    def test_paged_post_detailed_supports_nested_offset_pagination(self) -> None:
        client = StubClient()
        client.page_responses = [
            {"code": 0, "data": {"records": [{"id": 1}, {"id": 2}], "total": 3}},
            {"code": 0, "data": {"records": [{"id": 3}], "total": 3}},
        ]
        page = client.paged_post_detailed(
            "/bd/profit/statistics/open/seller/list",
            {"sid": 1, "offset": 0, "length": 2},
            page_size=2,
            data_path="data.records",
            total_path="data.total",
        )
        self.assertEqual([row["id"] for row in page.rows], [1, 2, 3])
        self.assertEqual(page.page_count, 2)
        self.assertEqual(page.total, 3)

    def test_paged_post_detailed_supports_next_token_pagination(self) -> None:
        client = StubClient()
        client.page_responses = [
            {"code": 0, "data": [{"id": 1}], "next_token": "page-2"},
            {"code": 0, "data": [{"id": 2}], "next_token": ""},
        ]
        page = client.paged_post_detailed(
            "/pb/openapi/newad/spCampaigns",
            {"sid": 1},
            page_size=100,
            pagination_mode="next_token",
        )
        self.assertEqual([row["id"] for row in page.rows], [1, 2])
        self.assertEqual(page.page_count, 2)
        self.assertIsNone(page.next_token)

    def test_parse_download_response_handles_gzip_csv(self) -> None:
        client = StubClient()
        csv_bytes = "asin,clicks\nB0TEST,3\n".encode("utf-8")
        raw_response = RawResponse(
            body=gzip.compress(csv_bytes),
            headers={"Content-Type": "text/csv", "Content-Encoding": "gzip"},
            final_url="https://example.com/report.csv.gz",
        )
        downloaded = client._parse_download_response("https://example.com/report.csv.gz", raw_response)
        self.assertEqual(downloaded.parsed_format, "gzip")
        self.assertEqual(downloaded.data[0]["asin"], "B0TEST")
        self.assertEqual(downloaded.data[0]["clicks"], "3")

    def test_parse_download_response_handles_zip_tsv(self) -> None:
        client = StubClient()
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("report.tsv", "asin\torders\nB0ZIP\t7\n")
        raw_response = RawResponse(
            body=buffer.getvalue(),
            headers={"Content-Type": "application/zip"},
            final_url="https://example.com/report.zip",
        )
        downloaded = client._parse_download_response("https://example.com/report.zip", raw_response)
        self.assertEqual(downloaded.parsed_format, "zip")
        self.assertEqual(downloaded.data[0]["name"], "report.tsv")
        self.assertEqual(downloaded.data[0]["data"][0]["asin"], "B0ZIP")


if __name__ == "__main__":
    unittest.main()
