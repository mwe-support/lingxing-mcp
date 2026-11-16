from __future__ import annotations

from datetime import datetime, timedelta
import importlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.ad_management import AD_MANAGEMENT_TOOL_SPECS, AD_MANAGEMENT_BATCH_LIMITS
from lib.lingxing_openapi.client import PagedRows
from lib.lingxing_openapi.endpoint_specs import ALL_ENDPOINT_SPECS
from lib.lingxing_openapi.errors import LingxingConfigError
from lib.lingxing_openapi.mcp import LingxingMCPApplication
from lib.lingxing_openapi.services import LingxingOpenAPIService

FakeClient = importlib.import_module("skills.zach-lingxing-openapi-client.tests.test_lingxing_services").FakeClient


class RecordingClient(FakeClient):
    def paged_post_detailed(self, path, body, *, page_size, **kwargs):
        self.post_calls.append((path, body, kwargs))
        return PagedRows(rows=[], page_count=1, total=0)

    def post_json(self, path, json_body=None, query_params=None, extra_headers=None):
        self.post_json_calls.append((path, json_body or {}, extra_headers))
        return {"code": 0, "data": []}


class OfficialAPIContractTests(unittest.TestCase):
    def setUp(self):
        self.client = RecordingClient()
        self.service = LingxingOpenAPIService(self.client)

    def test_every_endpoint_spec_sends_only_official_request_fields(self):
        contracts = json.loads((ROOT / "docs/official-api-contracts-2026-11-16.json").read_text(encoding="utf-8"))
        by_path = {row["endpoint"]: row for row in contracts["contracts"]}
        self.assertEqual(len(by_path), 109)
        for spec in ALL_ENDPOINT_SPECS:
            with self.subTest(tool=spec.tool_name):
                today = datetime.now().date()
                args = {}
                for arg in spec.args:
                    if not arg.required:
                        continue
                    if arg.enum:
                        value = arg.enum[0]
                    elif arg.arg_type == "integer":
                        value = 101
                    elif arg.arg_type == "array_integer":
                        value = [101]
                    elif arg.arg_type == "array_string":
                        value = ["probe"]
                    elif "month" in arg.name:
                        value = today.strftime("%Y-%m")
                    elif "date" in arg.name.lower():
                        value = today.isoformat()
                    else:
                        value = "probe"
                    args[arg.name] = value
                if any(arg.name == "profile_id" for arg in spec.args):
                    args["profile_id"] = 321
                if spec.tool_name == "lingxing_exp_ads_aba_report":
                    args.update(country="US", data_start_time=(today - timedelta(days=(today.weekday() + 1) % 7)).isoformat())
                if spec.tool_name == "lingxing_ads_sp_target_hourly":
                    args["campaign_ids"] = [101]
                self.client.post_calls.clear()
                self.client.post_json_calls.clear()
                self.service.run_endpoint_spec(spec.tool_name, args)
                calls = [(path, body) for path, body, _ in self.client.post_calls + self.client.post_json_calls if path == spec.endpoint]
                self.assertTrue(calls)
                fields = {row["name"] for row in by_path[spec.endpoint]["request_fields"]}
                self.assertTrue(fields, spec.docs_path)
                for _, body in calls:
                    self.assertFalse(set(body) - fields, f"Undocumented outbound fields: {set(body) - fields}")

    def test_advertising_selectors_and_cursor_requests(self):
        cases = {
            "lingxing_ads_sb_targets": {"ads_type": "ALL", "targeting_type": "ALL"},
            "lingxing_exp_ads_sb_target_report": {"sponsored_type": "ALL", "target_type": "ALL"},
            "lingxing_exp_ads_sb_keyword_placement_report": {"sponsored_type": "ALL", "target_type": "keyword"},
        }
        for name, expected in cases.items():
            with self.subTest(tool=name):
                self.service.run_endpoint_spec(name, {"sid": 101, "profile_id": 321, "report_date": "2026-11-15"})
                _, body, options = self.client.post_calls[-1]
                self.assertTrue(expected.items() <= body.items())
                self.assertNotIn("offset", body)
                self.assertEqual(options["pagination_mode"], "next_token")
                self.assertEqual(options["extra_headers"], {"X-API-VERSION": "2"})
        self.client.post_calls.clear()
        self.service.run_endpoint_spec("lingxing_ads_sp_negative_targets_or_keywords", {"sid": 101, "profile_id": 321})
        self.assertEqual([body["target_type"] for _, body, _ in self.client.post_calls], ["keyword", "target"])

    def test_hourly_report_uses_campaign_ids_and_single_request(self):
        self.service.run_endpoint_spec("lingxing_ads_sp_target_hourly", {
            "report_date": datetime.now().date().isoformat(), "campaign_id": 10,
            "campaign_ids": [10, 11], "agg_dimension": "all_ad_target_placement",
        })
        self.assertEqual(self.client.get_calls, [])
        self.assertEqual(self.client.post_calls, [])
        path, body, _ = self.client.post_json_calls[-1]
        self.assertTrue(path.endswith("/spTargetHourData"))
        self.assertEqual(body["campaign_ids"], [10, 11])
        self.assertNotIn("profile_id", body)
        self.assertNotIn("offset", body)

    def test_official_input_limits_fail_before_network(self):
        cases = [
            ("lingxing_amazon_listing", {"sid": 101, "search_value": ["probe"] * 11}),
            ("lingxing_product_performance", {"sid": 101, "start_date": "2026-11-01", "end_date": "2026-11-15", "search_value": ["probe"] * 51}),
            ("lingxing_product_performance", {"sid": 101, "start_date": "2026-01-01", "end_date": "2026-11-15"}),
            ("lingxing_product_performance", {"sid": 101}),
            ("lingxing_profit_seller", {"sid": 101, "start_date": "2026-11-01", "end_date": "2026-11-15"}),
            ("lingxing_finance_report_asin", {"sid": 101, "start_date": "2026-10", "end_date": "2026-11", "monthly_query": True}),
            ("lingxing_profit_report_order_list", {"start_date": "2026-01-01", "end_date": "2026-01-02", "order_status": "Deferred"}),
            ("lingxing_return_analysis", {"startDate": "2024-01-01", "endDate": "2026-11-15", "asinType": "asin", "dateType": 0}),
            ("lingxing_ads_sp_target_hourly", {"report_date": datetime.now().date().isoformat(), "agg_dimension": "target"}),
        ]
        for name, args in cases:
            with self.subTest(tool=name), self.assertRaises(LingxingConfigError):
                self.service.run_endpoint_spec(name, args)
        with self.assertRaises(LingxingConfigError):
            self.service.resolve_daily_promotions(101, "2026-11-15", 365)
        with self.assertRaises(LingxingConfigError):
            self.service.orders(101, "2026-11-01", "2026-11-15", date_type=3)
        self.assertEqual(self.client.post_calls + self.client.post_json_calls + self.client.get_calls, [])

    def test_sp_target_hourly_limits_unique_ids_after_deduplication(self):
        args = {"report_date": datetime.now().date().isoformat(), "agg_dimension": "target"}
        self.service.run_endpoint_spec("lingxing_ads_sp_target_hourly", {**args, "campaign_ids": [101] * 51})
        self.assertEqual(self.client.post_json_calls[-1][1]["campaign_ids"], [101])
        count = len(self.client.post_json_calls)
        with self.assertRaises(LingxingConfigError):
            self.service.run_endpoint_spec("lingxing_ads_sp_target_hourly", {**args, "campaign_ids": list(range(1, 52))})
        self.assertEqual(len(self.client.post_json_calls), count)

    def test_official_sid_sort_month_and_source_warning_mappings(self):
        self.service.run_endpoint_spec("lingxing_amazon_listing", {"sid": 101, "search_value": ["probe"]})
        self.assertEqual(self.client.post_calls[-1][1]["sid"], "101")
        self.service.run_endpoint_spec("lingxing_product_performance", {"sid": 101, "start_date": "2026-11-01", "end_date": "2026-11-15"})
        self.assertEqual(self.client.post_calls[-1][1]["sid"], "101")
        self.service.run_endpoint_spec("lingxing_return_analysis", {"startDate": "2026-11-01", "endDate": "2026-11-15", "asinType": "asin", "dateType": 0, "sortType": "DESC", "storeId": [101]})
        _, body, _ = self.client.post_calls[-1]
        self.assertEqual(body["sortType"], "desc")
        self.assertEqual(body["sortField"], "curReturnGoodsCount")
        self.assertEqual(body["storeId"], [101])
        self.assertEqual(body["length"], 200)
        self.service.run_endpoint_spec("lingxing_finance_report_asin", {"sid": 101, "start_date": "2026-11", "end_date": "2026-11", "monthly_query": True})
        self.assertEqual(self.client.post_calls[-1][1]["startDate"], "2026-11")
        warning = self.service.run_endpoint_spec("lingxing_source_daily_inventory", {"sid": 101, "event_date": "2023-11-30"})
        self.assertIn("2023-12-01", warning["warnings"][0])

    def test_all_ad_write_tools_keep_strict_confirmation_and_official_profile_keys(self):
        app = LingxingMCPApplication(self.service)
        examples = {
            "campaigns": {"campaignId": 10, "isBaseValue": 0}, "ad_groups": {"adGroupId": 10, "isBaseValue": 0},
            "lingxing_ads_update_sp_keyword": {"keywordId": 10, "isBaseValue": 0, "state": "paused"},
            "targeting_clauses": {"targetId": 10, "isBaseValue": 0, "bid": 1},
            "product_ads": {"adId": 10, "state": "paused"},
            "lingxing_ads_add_sp_keywords": {"campaignId": "10", "adGroupId": "11", "keyword": "probe", "matchType": "EXACT", "state": "PAUSED", "bid": 1},
            "negative_keywords": {"campaignId": "10", "keyword": "probe", "matchType": "negativeExact", "state": "PAUSED"},
            "asins": {"campaignId": "10", "adGroupId": "11", "asin": "B0TEST", "state": "PAUSED"},
        }
        for spec in AD_MANAGEMENT_TOOL_SPECS:
            with self.subTest(tool=spec.tool_name):
                args = {"profile_id": 321}
                if spec.item_arg:
                    item = examples.get(spec.tool_name, examples.get(spec.item_arg))
                    args[spec.item_arg] = [item]
                else:
                    args["targetIds"] = ["10"]
                result = app._run_ad_management_tool(spec, args)
                self.assertFalse(result["data"]["executed"])
                profile_key = "profile_id" if spec.tool_name in {"lingxing_ads_update_sp_ad_group", "lingxing_ads_update_sp_product_ads"} else "profileId"
                self.assertEqual(result["data"]["request_body"][profile_key], 321)
                for invalid in ({"dry_run": "preview", "confirm": True}, {"dry_run": False, "confirm": "yes"}, {"dry_run": 0, "confirm": 1}):
                    with self.assertRaises(LingxingConfigError):
                        app._run_ad_management_tool(spec, {**args, **invalid})
                if spec.item_arg:
                    with self.assertRaises(LingxingConfigError):
                        app._run_ad_management_tool(spec, {"sid": 101, spec.item_arg: [{}]})
                if spec.tool_name in AD_MANAGEMENT_BATCH_LIMITS:
                    key = spec.item_arg or "targetIds"
                    with self.assertRaises(LingxingConfigError):
                        app._run_ad_management_tool(spec, {**args, key: args[key] * 1001})
        self.assertEqual(self.client.post_json_calls, [])

    def test_ad_write_validation_rejects_invalid_items_and_allows_typed_confirmation(self):
        app = LingxingMCPApplication(self.service)
        spec = next(item for item in AD_MANAGEMENT_TOOL_SPECS if item.tool_name == "lingxing_ads_update_sp_keyword")
        valid = {"keywordId": 10, "isBaseValue": 0, "state": "paused"}
        for invalid in (
            {**valid, "state": "PAUSED"}, {**valid, "keywordId": "10"},
            {**valid, "bid": float("nan")}, {"keywordId": 10, "isBaseValue": 0},
            {**valid, "isBaseValue": 1, "baseType": 1},
        ):
            with self.subTest(item=invalid), self.assertRaises(LingxingConfigError):
                app._run_ad_management_tool(spec, {"sid": 101, "keywords": [invalid], "dry_run": False, "confirm": True})
        self.assertEqual(self.client.post_json_calls, [])
        result = app._run_ad_management_tool(spec, {"sid": 101, "keywords": [valid], "dry_run": False, "confirm": True})
        self.assertTrue(result["data"]["executed"])
        self.assertEqual(len(self.client.post_json_calls), 1)


if __name__ == "__main__":
    unittest.main()
