from __future__ import annotations

import gzip
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi import (  # noqa: E402
    LingxingOpenAPIClient,
    RawResponse,
    TokenBundle,
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
        self.request_bodies: list[dict] = []

    def _build_public_query(self, business_params: dict) -> dict[str, str]:  # noqa: ANN001
        return {
            "access_token": "token-123",
            "app_key": self.app_id,
            "timestamp": "1700000000",
            "sign": "signed",
        }

    def _request(self, request, *, endpoint: str) -> dict:  # noqa: ANN001
        self.last_request = request
        if request.data:
            self.request_bodies.append(json.loads(request.data.decode("utf-8")))
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

    def test_business_requests_use_bearer_and_preserve_signing(self) -> None:
        business_params = {"sid": 1, "offset": 0, "filters": {"status": [1, 2]}, "empty": "", "none": None}
        for method in ("get_json", "post_json"):
            with self.subTest(method=method):
                client = StubClient()
                params = dict(business_params)
                if method == "get_json":
                    params["access_token"] = "stale-query-token"
                with (
                    patch.object(StubClient, "_build_public_query", LingxingOpenAPIClient._build_public_query),
                    patch.object(client, "ensure_access_token", return_value=TokenBundle("token-123", "refresh-123", 1800000000)) as token_getter,
                    patch("lib.lingxing_openapi.client.time.time", return_value=1700000000),
                    patch("lib.lingxing_openapi.client.generate_sign", wraps=generate_sign) as signer,
                ):
                    getattr(client, method)("/probe", params)
                request = client.last_request
                query = parse_qs(urlsplit(request.full_url).query, keep_blank_values=True)
                self.assertNotIn("access_token", query)
                self.assertEqual(request.get_header("Authorization"), "Bearer token-123")
                signed_params = {**business_params, "access_token": "token-123", "app_key": client.app_id, "timestamp": "1700000000"}
                signer.assert_called_once_with(signed_params, client.app_id)
                token_getter.assert_called_once_with()
                self.assertEqual(query["sign"], [generate_sign(signed_params, client.app_id)])
                self.assertEqual(query["app_key"], [client.app_id])
                self.assertEqual(query["timestamp"], ["1700000000"])
                if method == "post_json":
                    self.assertEqual(json.loads(request.data), business_params)
                else:
                    self.assertEqual(query["sid"], ["1"])
                    self.assertEqual(query["offset"], ["0"])
                    self.assertEqual(json.loads(query["filters"][0]), business_params["filters"])
                    self.assertEqual(params["access_token"], "stale-query-token")

    def test_post_json_extra_headers_cannot_override_bearer(self) -> None:
        for header_name in ("Authorization", "authorization", "AUTHORIZATION"):
            with self.subTest(header_name=header_name):
                client = StubClient()
                client.post_json("/probe", {}, extra_headers={header_name: "Bearer stale", "X-API-VERSION": "2"})
                headers = client.last_request.header_items()
                self.assertEqual([value for key, value in headers if key.lower() == "authorization"], ["Bearer token-123"])
                self.assertEqual(client.last_request.get_header("X-api-version"), "2")

    def test_token_endpoints_keep_multipart_authentication(self) -> None:
        for method, args, field in (("fetch_access_token", [], b'appSecret'), ("refresh_access_token", ["refresh-123"], b'refreshToken')):
            with self.subTest(method=method):
                client = StubClient()
                payload = {"code": 0, "data": {"access_token": "token-123", "refresh_token": "refresh-123", "expires_in": 3600}}
                with patch.object(client, "_write_token_cache"), patch.object(client, "_request", return_value=payload) as requester:
                    getattr(client, method)(*args)
                request = requester.call_args.args[0]
                self.assertIsNone(request.get_header("Authorization"))
                self.assertEqual(urlsplit(request.full_url).query, "")
                self.assertTrue(request.get_header("Content-type").startswith("multipart/form-data;"))
                self.assertIn(field, request.data)

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

    def test_paged_post_detailed_supports_page_number_pagination(self) -> None:
        client = StubClient()
        client.page_responses = [
            {"code": 0, "data": [{"id": 1}, {"id": 2}], "total": 3},
            {"code": 0, "data": [{"id": 3}], "total": 3},
        ]
        page = client.paged_post_detailed(
            "/erp/sc/routing/wms/order/wmsOrderList",
            {"page": 1, "page_size": 2},
            page_size=2,
            pagination_mode="page",
        )

        self.assertEqual([row["id"] for row in page.rows], [1, 2, 3])
        self.assertEqual(page.page_count, 2)
        self.assertEqual(page.total, 3)
        self.assertEqual(client.request_bodies, [
            {"page": 1, "page_size": 2},
            {"page": 2, "page_size": 2},
        ])

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
