from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.client import PagedRows  # noqa: E402
from lib.lingxing_openapi.ad_management import AdManagementRequest  # noqa: E402
from lib.lingxing_openapi.services import LingxingOpenAPIService  # noqa: E402


class FakeClient:
    def __init__(self) -> None:
        self.get_calls: list[tuple[str, dict | None]] = []
        self.post_calls: list[tuple[str, dict, dict]] = []
        self.post_json_calls: list[tuple[str, dict, dict | None]] = []

    def get_cached_token(self):  # noqa: ANN001, D401
        return None

    def ensure_access_token(self):  # noqa: ANN001, D401
        raise AssertionError("health_check should not call ensure_access_token in this test")

    def get_json(self, path: str, query_params: dict | None = None) -> dict:
        self.get_calls.append((path, query_params))
        if path == "/erp/sc/data/seller/allMarketplace":
            return {"code": 0, "data": [{"mid": 1, "code": "US", "marketplace_id": "ATVPDKIKX0DER"}]}
        if path == "/erp/sc/data/seller/lists":
            return {
                "code": 0,
                "data": [
                    {
                        "sid": 101,
                        "mid": 1,
                        "name": "US Store",
                        "status": 1,
                        "seller_id": "A1SELLER",
                        "marketplace_id": "ATVPDKIKX0DER",
                    },
                    {
                        "sid": 202,
                        "mid": 1,
                        "name": "Paused Store",
                        "status": 0,
                        "seller_id": "A2SELLER",
                        "marketplace_id": "A1PAUSEDMARKET",
                    },
                ],
            }
        raise AssertionError(f"unexpected get_json path: {path}")

    def paged_post_detailed(self, path: str, body: dict, *, page_size: int, **kwargs) -> PagedRows:  # noqa: ARG002
        self.post_calls.append((path, body, kwargs))
        if path == "/erp/sc/data/sales_report/sales":
            return PagedRows(
                rows=[
                    {"asin": "B0TARGET", "r_date": "2026-03-20", "volume": 3, "amount": 120, "order_items": 2},
                    {"asin": "B0OTHER", "r_date": "2026-03-20", "volume": 1, "amount": 20, "order_items": 1},
                ],
                page_count=2,
                total=2,
            )
        if path == "/erp/sc/data/mws/orders":
            return PagedRows(rows=[{"amazon_order_id": "ORDER-1"}], page_count=1, total=1)
        if path == "/order/amzod/api/orderList":
            return PagedRows(rows=[], page_count=1, total=0)
        if path == "/basicOpen/promotion/listingList":
            return PagedRows(
                rows=[
                    {
                        "asin": "B0TEST",
                        "seller_sku": "SKU-1",
                        "item_name": "Demo Product",
                        "promotion_list": [
                            {
                                "promotion_id": "promo-1",
                                "category": "2",
                                "category_text": "秒杀",
                                "promotion_type_text": "Lightning Deal",
                                "promotion_start_time": "2026-03-20 00:00:00",
                                "promotion_end_time": "2026-03-20 23:59:00",
                            }
                        ],
                    }
                ],
                page_count=1,
                total=1,
            )
        if path == "/basicOpen/promotionalActivities/secKill/list":
            return PagedRows(rows=[{"promotion_id": "promo-1", "promotion_type": 2}], page_count=1, total=1)
        if path in {
            "/basicOpen/promotionalActivities/manage/list",
            "/basicOpen/promotionalActivities/vipDiscount/list",
            "/basicOpen/promotionalActivities/coupon/list",
        }:
            return PagedRows(rows=[], page_count=1, total=0)
        if path == "/basicOpen/baseData/account/list":
            return PagedRows(
                rows=[
                    {"sid": 101, "profile_id": 321, "country_code": "US", "status": 1},
                    {"sid": 999, "profile_id": 654, "country_code": "CA", "status": 0},
                ],
                page_count=1,
                total=2,
            )
        if path == "/bd/profit/statistics/open/seller/list":
            return PagedRows(rows=[{"sid": 101, "profit": 12.5}], page_count=2, total=1)
        if path == "/erp/sc/data/mws_report/allOrders":
            return PagedRows(rows=[{"amazon_order_id": "ALL-1"}], page_count=1, total=1)
        if path == "/basicOpen/customerService/voiceOfBuyer/list":
            return PagedRows(
                rows=[
                    {
                        "sid": "101",
                        "asin": "B0TARGET",
                        "msku": "MSKU-1",
                        "sku": "SKU-1",
                        "fulfillment_channel": "FBA",
                        "ncx_rate": "0.9000",
                        "ncx_count": 3,
                        "order_count": 5,
                        "pcx_health_text": "良好",
                    }
                ],
                page_count=1,
                total=1,
            )
        if path == "/cost/center/api/settlement/report":
            return PagedRows(
                rows=[{"sid": 101, "amazonOrderId": "ORDER-SETTLED-1"}],
                page_count=2,
                total=1,
            )
        if path == "/basicOpen/finance/profitReport/order/transcation/list":
            return PagedRows(
                rows=[{"sid": "101", "orderId": "ORDER-TX-1", "productSales": 12.5}],
                page_count=2,
                total=1,
            )
        if path == "/erp/sc/routing/wms/order/wmsOrderList":
            return PagedRows(
                rows=[{"sid": 101, "wo_number": "WO-1"}],
                page_count=2,
                total=1,
            )
        if path == "/erp/sc/data/mws_report/manageInventory":
            return PagedRows(rows=[{"asin": "B0TARGET", "available": 9}], page_count=1, total=1)
        if path == "/pb/openapi/newad/spProductAdReports":
            return PagedRows(
                rows=[{"asin": "B0TARGET", "impressions": 10, "clicks": 1, "cost": 2, "orders": 1, "sales": 20, "units": 1}],
                page_count=1,
                total=1,
            )
        if path == "/pb/openapi/newad/sdProductAdReports":
            return PagedRows(
                rows=[{"asin": "B0TARGET", "impressions": 5, "clicks": 2, "cost": 1, "orders": 1, "sales": 10, "units": 2}],
                page_count=1,
                total=1,
            )
        if path == "/pb/openapi/newad/hsaPurchasedAsinReports":
            return PagedRows(
                rows=[{"asin": "B0TARGET", "orders14d": 3, "sales14d": 30, "units_sold14d": 4}],
                page_count=1,
                total=1,
            )
        if path == "/pb/openapi/newad/listHsaProductAdReport":
            return PagedRows(
                rows=[{"ad_creative_id": "creative-1", "impressions": 100, "clicks": 5, "cost": 9}],
                page_count=1,
                total=1,
            )
        if path == "/pb/openapi/newad/hsaProductAds":
            return PagedRows(rows=[{"ad_creative_id": "creative-1", "asin": ["B0TARGET"]}], page_count=1, total=1)
        raise AssertionError(f"unexpected paged_post_detailed path: {path}")

    def post_json(self, path: str, json_body: dict | None = None, query_params: dict | None = None, extra_headers: dict | None = None) -> dict:  # noqa: ARG002
        self.post_json_calls.append((path, json_body or {}, extra_headers))
        if path == "/basicOpen/report/create/reportExportTask":
            return {"code": 0, "data": {"task_id": "task-1"}}
        if path == "/basicOpen/report/query/reportExportTask":
            return {"code": 0, "data": {"url": "https://example.com/report.csv"}}
        if path == "/basicOpen/report/amazonReportExportTask":
            return {"code": 0, "data": {"url": "https://example.com/report.csv"}}
        if path == "/order/amzod/api/orderList":
            return {
                "code": 0,
                "data": {
                    "total": 1,
                    "records": [
                        {
                            "sid": 101,
                            "store_name": "US Store",
                            "country": "美国",
                            "amazon_order_id": "S01-TEST",
                            "seller_fulfillment_order_id": "SELLER-ORDER-1",
                            "order_status": "COMPLETE",
                            "purchase_date_local": "2026-06-20 10:00:00",
                            "listing_info": [{"asin": "B0TARGET", "msku": "MSKU-1", "quantity": 2}],
                        }
                    ],
                },
            }
        if path == "/order/amzod/api/orderDetails/productInformation":
            return {
                "code": 0,
                "data": [
                    {
                        "sid": 101,
                        "amazon_order_id": "S01-TEST",
                        "seller_fulfillment_order_id": "SELLER-ORDER-1",
                        "listing_detail_info": [{"asin": "B0TARGET", "fba_fee": "-3.20"}],
                    }
                ],
            }
        if path == "/order/amzod/api/orderDetails/logisticsInformation":
            return {
                "code": 0,
                "data": [
                    {
                        "sid": 101,
                        "amazon_order_id": "S01-TEST",
                        "seller_fulfillment_order_id": "SELLER-ORDER-1",
                        "shipment_info": [{"amazon_shipment_id": "SHIP-1"}],
                    }
                ],
            }
        if path == "/basicOpen/openapi/salesOrder/multi-channel/list/transaction":
            return {
                "code": 0,
                "data": {
                    "list": [{"sellerSku": "MSKU-1", "totalCurrencyAmount": "$-3.20"}],
                    "totalCurrencyAmounts": "$-3.20",
                },
            }
        if path == "/basicOpen/adReport/manage/putSpKeyword":
            return {"code": 1, "success": True, "data": {"apiResult": [{"code": "SUCCESS", "keywordId": "K-1"}]}}
        if path == "/pb/openapi/newad/apiLogStandard":
            return {"code": 0, "data": {"list": [{"operate_type": "keywords"}], "total": 1}}
        raise AssertionError(f"unexpected post_json path: {path}")


class LingxingServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.service = LingxingOpenAPIService(client=FakeClient())

    def test_seller_lists_enriches_marketplace_timezone_and_filters(self) -> None:
        result = self.service.seller_lists(status=1, marketplace="US")
        self.assertTrue(result["ok"])
        self.assertEqual(len(result["data"]), 1)
        self.assertEqual(result["data"][0]["marketplace_code"], "US")
        self.assertEqual(result["data"][0]["timezone"], "America/Los_Angeles")

    def test_store_sales_keeps_page_count_in_meta(self) -> None:
        result = self.service.store_sales(101, "2026-03-20", "2026-03-20")
        self.assertEqual(result["meta"]["page_count"], 2)
        self.assertEqual(result["data"][0]["asin"], "B0TARGET")

    def test_resolve_daily_promotions_merges_listing_and_secondary_maps(self) -> None:
        result = self.service.resolve_daily_promotions(101, "2026-03-20")
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"][0]["asin"], "B0TEST")
        self.assertEqual(result["data"][0]["promotion_labels"], ["deal.lightning_deal"])

    def test_ad_accounts_filters_by_sid_and_status(self) -> None:
        result = self.service.ad_accounts(sid=101, status=1)
        self.assertTrue(result["ok"])
        self.assertEqual(len(result["data"]), 1)
        self.assertEqual(result["data"][0]["profile_id"], 321)

    def test_ads_management_apply_dry_run_does_not_call_write_endpoint(self) -> None:
        result = self.service.ads_management_apply(
            AdManagementRequest(
                tool_name="lingxing_ads_update_sp_keyword",
                endpoint="/basicOpen/adReport/manage/putSpKeyword",
                docs_path="docs/newAd/adReportManagePutSpKeyword",
                body={"sid": 101, "keywords": [{"keywordId": 1, "state": "paused", "isBaseValue": 0}]},
                dry_run=True,
                confirm=False,
            )
        )
        self.assertTrue(result["ok"])
        self.assertFalse(result["data"]["executed"])
        self.assertNotIn("/basicOpen/adReport/manage/putSpKeyword", [call[0] for call in self.service.client.post_json_calls])

    def test_ads_management_apply_calls_write_endpoint_when_confirmed(self) -> None:
        result = self.service.ads_management_apply(
            AdManagementRequest(
                tool_name="lingxing_ads_update_sp_keyword",
                endpoint="/basicOpen/adReport/manage/putSpKeyword",
                docs_path="docs/newAd/adReportManagePutSpKeyword",
                body={"sid": 101, "keywords": [{"keywordId": 1, "state": "paused", "isBaseValue": 0}]},
                dry_run=False,
                confirm=True,
            )
        )
        self.assertTrue(result["ok"])
        self.assertTrue(result["data"]["executed"])
        self.assertEqual(self.service.client.post_json_calls[-1][0], "/basicOpen/adReport/manage/putSpKeyword")

    def test_ads_operation_logs_uses_official_endpoint_and_version_header(self) -> None:
        result = self.service.ads_operation_logs(
            sid=101,
            log_source="erp",
            sponsored_type="sp",
            operate_type="keywords",
            start_date="2026-06-01",
            end_date="2026-06-30",
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"]["total"], 1)
        path, body, headers = self.service.client.post_json_calls[-1]
        self.assertEqual(path, "/pb/openapi/newad/apiLogStandard")
        self.assertEqual(body["sid"], 101)
        self.assertEqual(headers, {"X-API-VERSION": "2"})

    def test_run_endpoint_spec_supports_profit_catalog(self) -> None:
        result = self.service.run_endpoint_spec(
            "lingxing_profit_seller",
            {"sid": 101, "start_date": "2026-03-20", "end_date": "2026-03-20"},
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"][0]["profit"], 12.5)
        self.assertEqual(result["meta"]["page_count"], 2)

    def test_run_endpoint_spec_supports_voice_of_buyer_filters(self) -> None:
        result = self.service.run_endpoint_spec(
            "lingxing_voice_of_buyer",
            {
                "sids": [101],
                "fulfillment_channel": "FBA",
                "pxc_health": ["3"],
                "search_field": "msku",
                "search_value": ["MSKU-1"],
                "return_badge": ["Yes", "At_Risk"],
            },
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"][0]["asin"], "B0TARGET")
        path, body, kwargs = self.service.client.post_calls[-1]
        self.assertEqual(path, "/basicOpen/customerService/voiceOfBuyer/list")
        self.assertEqual(body["length"], 200)
        self.assertEqual(body["sids"], [101])
        self.assertEqual(body["pxc_health"], ["3"])
        self.assertEqual(body["search_value"], ["MSKU-1"])
        self.assertEqual(body["return_badge"], ["Yes", "At_Risk"])
        self.assertEqual(kwargs["data_path"], "data")
        self.assertEqual(kwargs["total_path"], "total")

    def test_shipment_settlement_report_uses_active_sellers_when_sids_are_omitted(self) -> None:
        result = self.service.shipment_settlement_report(
            start_date="2026-06-01",
            end_date="2026-06-30",
        )

        self.assertTrue(result["ok"])
        self.assertEqual(result["meta"]["response_mode"], "summary")
        self.assertEqual(result["data"]["record_count"], 1)
        self.assertEqual(result["data"]["returned_count"], 1)
        self.assertFalse(result["data"]["truncated"])
        self.assertEqual(result["meta"]["store_scope"], "all")
        self.assertEqual(result["meta"]["selected_store_count"], 1)
        self.assertEqual(result["meta"]["selected_store_status"], "active")
        path, body, kwargs = self.service.client.post_calls[-1]
        self.assertEqual(path, "/cost/center/api/settlement/report")
        self.assertEqual(body["sids"], [101])
        self.assertEqual(body["amazonSellerIds"], ["A1SELLER"])
        self.assertEqual(body["timeType"], "04")
        self.assertEqual(body["filterBeginDate"], "2026-06-01")
        self.assertEqual(body["filterEndDate"], "2026-06-30")
        self.assertEqual(kwargs["data_path"], "data.records")
        self.assertEqual(kwargs["total_path"], "data.total")

    def test_shipment_settlement_report_full_mode_returns_all_records(self) -> None:
        result = self.service.shipment_settlement_report(
            start_date="2026-06-01",
            end_date="2026-06-30",
            response_mode="full",
        )

        self.assertEqual(result["meta"]["response_mode"], "full")
        self.assertEqual(result["data"]["record_count"], 1)
        self.assertEqual(result["data"]["records"], [{"sid": 101, "amazonOrderId": "ORDER-SETTLED-1"}])
        self.assertFalse(result["data"]["truncated"])

    def test_shipment_settlement_report_resolves_sid_or_seller_id_filters(self) -> None:
        cases = [
            ({"sids": [101]}, [101], ["A1SELLER"]),
            ({"amazon_seller_ids": ["A2SELLER"]}, [202], ["A2SELLER"]),
        ]
        for filters, expected_sids, expected_seller_ids in cases:
            with self.subTest(filters=filters):
                service = LingxingOpenAPIService(client=FakeClient())
                service.shipment_settlement_report(
                    start_date="2026-06-01",
                    end_date="2026-06-30",
                    **filters,
                )
                _, body, _ = service.client.post_calls[-1]
                self.assertEqual(body["sids"], expected_sids)
                self.assertEqual(body["amazonSellerIds"], expected_seller_ids)

    def test_shipment_settlement_report_skips_inactive_incomplete_store_for_all_scope(self) -> None:
        class IncompleteSellerClient(FakeClient):
            def get_json(self, path: str, query_params: dict | None = None) -> dict:
                payload = super().get_json(path, query_params)
                if path == "/erp/sc/data/seller/lists":
                    payload["data"].append({"sid": 303, "name": "Missing Seller ID", "status": 0})
                return payload

        service = LingxingOpenAPIService(client=IncompleteSellerClient())
        result = service.shipment_settlement_report(
            start_date="2026-06-01",
            end_date="2026-06-30",
        )
        self.assertTrue(result["ok"])
        _, body, _ = service.client.post_calls[-1]
        self.assertEqual(body["sids"], [101])

    def test_shipment_settlement_report_allows_explicit_inactive_store(self) -> None:
        self.service.shipment_settlement_report(
            start_date="2026-06-01",
            end_date="2026-06-30",
            sids=[202],
        )
        _, body, _ = self.service.client.post_calls[-1]
        self.assertEqual(body["sids"], [202])

    def test_shipment_settlement_report_groups_cross_marketplace_stores_server_side(self) -> None:
        class CrossMarketplaceClient(FakeClient):
            def get_json(self, path: str, query_params: dict | None = None) -> dict:
                payload = super().get_json(path, query_params)
                if path == "/erp/sc/data/seller/allMarketplace":
                    payload["data"].append({"mid": 2, "code": "DE", "marketplace_id": "A1PAUSEDMARKET"})
                if path == "/erp/sc/data/seller/lists":
                    payload["data"][1]["mid"] = 2
                    payload["data"][1]["status"] = 1
                return payload

        service = LingxingOpenAPIService(client=CrossMarketplaceClient())
        result = service.shipment_settlement_report(
            start_date="2026-06-01",
            end_date="2026-06-30",
            response_mode="full",
        )

        calls = [call for call in service.client.post_calls if call[0] == "/cost/center/api/settlement/report"]
        self.assertEqual(len(calls), 2)
        self.assertEqual([call[1]["sids"] for call in calls], [[202], [101]])
        self.assertEqual(result["meta"]["store_group_count"], 2)
        self.assertEqual(result["meta"]["page_count"], 4)
        self.assertEqual(result["data"]["record_count"], 2)

    def test_sales_outbound_orders_omits_sid_filter_for_all_store_export(self) -> None:
        result = self.service.sales_outbound_orders(
            start_date="2026-06-01",
            end_date="2026-06-30",
        )

        self.assertTrue(result["ok"])
        self.assertEqual(result["meta"]["response_mode"], "summary")
        self.assertEqual(result["data"]["record_count"], 1)
        self.assertEqual(result["meta"]["store_scope"], "all")
        path, body, kwargs = self.service.client.post_calls[-1]
        self.assertEqual(path, "/erp/sc/routing/wms/order/wmsOrderList")
        self.assertNotIn("sid_arr", body)
        self.assertEqual(body["time_type"], "stock_delivered_at")
        self.assertEqual(body["start_date"], "2026-06-01")
        self.assertEqual(body["end_date"], "2026-06-30")
        self.assertEqual(kwargs["pagination_mode"], "page")
        self.assertEqual(kwargs["data_path"], "data")
        self.assertEqual(kwargs["total_path"], "total")

    def test_large_report_response_mode_is_validated(self) -> None:
        with self.assertRaisesRegex(Exception, "response_mode"):
            self.service.sales_outbound_orders(
                start_date="2026-06-01",
                end_date="2026-06-30",
                response_mode="raw",
            )
        self.assertEqual(self.service.client.get_calls, [])
        self.assertEqual(self.service.client.post_calls, [])

    def test_sales_outbound_orders_resolves_sid_or_seller_id_filters(self) -> None:
        cases = [
            ({"sids": [101]}, [101]),
            ({"amazon_seller_ids": ["A2SELLER"]}, [202]),
        ]
        for filters, expected_sids in cases:
            with self.subTest(filters=filters):
                service = LingxingOpenAPIService(client=FakeClient())
                service.sales_outbound_orders(
                    start_date="2026-06-01",
                    end_date="2026-06-30",
                    **filters,
                )
                _, body, _ = service.client.post_calls[-1]
                self.assertEqual(body["sid_arr"], expected_sids)

    def test_profit_report_order_defaults_to_summary_and_supports_full_export(self) -> None:
        summary = self.service.run_endpoint_spec(
            "lingxing_profit_report_order_list",
            {"start_date": "2026-06-01", "end_date": "2026-06-30", "preview_limit": 0},
        )
        self.assertEqual(summary["meta"]["response_mode"], "summary")
        self.assertEqual(summary["data"]["record_count"], 1)
        self.assertEqual(summary["data"]["returned_count"], 0)
        self.assertNotIn("orderId", summary["data"])
        self.assertTrue(any("摘要模式" in warning for warning in summary["warnings"]))

        full = self.service.run_endpoint_spec(
            "lingxing_profit_report_order_list",
            {
                "start_date": "2026-06-01",
                "end_date": "2026-06-30",
                "response_mode": "full",
            },
        )
        self.assertEqual(full["meta"]["response_mode"], "full")
        self.assertEqual(full["data"]["records"][0]["orderId"], "ORDER-TX-1")

    def test_multi_channel_orders_enriches_optional_details(self) -> None:
        from lib.lingxing_openapi.multi_channel_orders import MultiChannelOrderQuery

        result = self.service.multi_channel_orders(
            MultiChannelOrderQuery(
                sids=[101],
                start_date="2026-06-20",
                end_date="2026-06-20",
                include_product_detail=True,
                include_logistics_detail=True,
                include_transaction_detail=True,
            )
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["data"]["count"], 1)
        row = result["data"]["records"][0]
        self.assertEqual(row["items"][0]["asin"], "B0TARGET")
        self.assertEqual(row["product_detail"]["listing_detail_info"][0]["fba_fee"], "-3.20")
        self.assertEqual(row["logistics_detail"]["shipment_info"][0]["amazon_shipment_id"], "SHIP-1")
        self.assertEqual(row["transaction_detail"]["totalCurrencyAmounts"], "$-3.20")
        self.assertIn("/order/amzod/api/orderList", result["meta"]["endpoints"])

    def test_asin_ads_daily_rollup_balanced_combines_sp_sd_and_sb(self) -> None:
        result = self.service.asin_ads_daily_rollup(101, "B0TARGET", "2026-03-20", "2026-03-20")
        self.assertTrue(result["ok"])
        row = result["data"][0]
        self.assertEqual(row["impressions"], 115.0)
        self.assertEqual(row["clicks"], 8.0)
        self.assertEqual(row["cost"], 12.0)
        self.assertEqual(row["ad_orders"], 5.0)
        self.assertEqual(row["ad_sales"], 60.0)
        self.assertEqual(row["ad_units"], 7.0)

    def test_smoke_check_includes_extended_read_only_surfaces(self) -> None:
        result = self.service.smoke_check(sid=101, site_date="2026-03-20")
        self.assertTrue(result["ok"])
        self.assertTrue(result["data"]["ad_accounts_ok"])
        self.assertTrue(result["data"]["sp_product_ad_report_ok"])
        self.assertTrue(result["data"]["profit_seller_ok"])
        self.assertTrue(result["data"]["source_manage_inventory_ok"])


if __name__ == "__main__":
    unittest.main()
