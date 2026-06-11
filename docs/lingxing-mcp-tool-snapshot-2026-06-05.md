# Lingxing MCP Tool Snapshot

- Generated at: `2026-06-11 15:31:02`
- Source: `LingxingMCPApplication` tool registry plus built-in role allowlists and rate-limit metadata
- Tool count: `90`

## Built-in Role Tool Sets

Role allowlists are the MCP tool visibility boundary. The deprecated global `LINGXING_MCP_ENABLED_TOOLS` allowlist is no longer used. Every role always includes `lingxing_health_check`, `lingxing_smoke_check`, and `lingxing_rate_limit_policy`.

### `minimal` default role

- Tool count: `12`
- `lingxing_asin_product_snapshot`
- `lingxing_fba_warehouse_detail`
- `lingxing_finance_report_asin`
- `lingxing_health_check`
- `lingxing_local_product_costs`
- `lingxing_marketplaces`
- `lingxing_order_details`
- `lingxing_order_lists`
- `lingxing_product_performance`
- `lingxing_rate_limit_policy`
- `lingxing_seller_lists`
- `lingxing_smoke_check`

### `operations` role

- Tool count: `11`
- `lingxing_asin_product_snapshot`
- `lingxing_fba_warehouse_detail`
- `lingxing_health_check`
- `lingxing_local_product_costs`
- `lingxing_marketplaces`
- `lingxing_order_details`
- `lingxing_order_lists`
- `lingxing_product_performance`
- `lingxing_rate_limit_policy`
- `lingxing_seller_lists`
- `lingxing_smoke_check`

### `finance` role

- Tool count: `15`
- `lingxing_exp_finance_report_seller`
- `lingxing_fba_stock_aggregate`
- `lingxing_fba_stock_detail`
- `lingxing_fba_warehouse_detail`
- `lingxing_finance_report_asin`
- `lingxing_health_check`
- `lingxing_local_product_costs`
- `lingxing_order_details`
- `lingxing_profit_asin`
- `lingxing_profit_seller`
- `lingxing_rate_limit_policy`
- `lingxing_seller_lists`
- `lingxing_smoke_check`
- `lingxing_source_transaction`
- `lingxing_store_sales`

## Rate Limit Visibility

- Every registered MCP tool description includes a `限流：` line generated from tool endpoint metadata.
- Simple `EndpointSpec` tools inherit their endpoint automatically. Handwritten aggregate tools list every endpoint they may call.
- Clients should group calls by endpoint, not by tool name. Capacity-1 endpoints should be called serially at about 1 request/second.
- Use `lingxing_rate_limit_policy` for machine-readable policy before running large or parallel jobs.

Runtime settings:

```json
{
  "enabled": true,
  "default_rate_per_second": 1.0,
  "default_burst": 1,
  "wait_timeout_seconds": 60.0,
  "override_count": 0
}
```

## Tool Overview

| # | Tool | Registered by | Category | Required args | Optional args | Endpoints | Rate limit | Description |
|---:|---|---|---|---|---|---|---|---|
| 1 | `lingxing_health_check` | `manual` | `manual` | - | - | `/api/auth-server/oauth/access-token` | 限流：endpoint /api/auth-server/oauth/access-token，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 检查领星环境变量、token 状态和基础连通性，不拉业务数据。 |
| 2 | `lingxing_rate_limit_policy` | `manual` | `manual` | - | `tool_name` | - | 限流：本工具不直接调用领星业务 OpenAPI，或仅返回本地网关策略；客户端可并发调用，但不应把它作为业务查询循环。 | 返回当前 MCP 工具到领星 OpenAPI endpoint 的限流政策，供客户端 agent 在调用前按 endpoint 自主排队。 |
| 3 | `lingxing_seller_lists` | `manual` | `manual` | - | `status`, `marketplace` | `/erp/sc/data/seller/lists`<br>`/erp/sc/data/seller/allMarketplace` | 限流：聚合工具，涉及 2 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。 |
| 4 | `lingxing_marketplaces` | `manual` | `manual` | - | - | `/erp/sc/data/seller/allMarketplace` | 限流：endpoint /erp/sc/data/seller/allMarketplace，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 返回领星市场列表，并补充站点时区映射。 |
| 5 | `lingxing_store_sales` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | `/erp/sc/data/sales_report/sales` | 限流：endpoint /erp/sc/data/sales_report/sales，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺和日期范围拉取 StoreSales，并自动合并分页。 |
| 6 | `lingxing_asin_daily_lists` | `manual` | `manual` | `sid`, `event_date`, `metric_type` | `asin_type` | `/erp/sc/data/sales_report/asinDailyLists` | 限流：endpoint /erp/sc/data/sales_report/asinDailyLists，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺、日期和指标类型拉取 AsinDailyLists。 |
| 7 | `lingxing_order_lists` | `manual` | `manual` | `sid`, `start_date`, `end_date` | `date_type` | `/erp/sc/data/mws/orders` | 限流：endpoint /erp/sc/data/mws/orders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。 |
| 8 | `lingxing_order_details` | `manual` | `manual` | - | `order_id`, `order_ids` | `/erp/sc/data/mws/orderDetail`<br>`/erp/sc/data/seller/lists`<br>`/erp/sc/data/seller/allMarketplace` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/mws/orderDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。 |
| 9 | `lingxing_promotion_listing` | `manual` | `manual` | `sid`, `site_date`, `start_time`, `end_time` | `status`, `product_status`, `promotion_category` | `/basicOpen/promotion/listingList` | 限流：endpoint /basicOpen/promotion/listingList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。 |
| 10 | `lingxing_promotion_sec_kill` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | `/basicOpen/promotionalActivities/secKill/list` | 限流：endpoint /basicOpen/promotionalActivities/secKill/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。 |
| 11 | `lingxing_promotion_manage` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | `/basicOpen/promotionalActivities/manage/list` | 限流：endpoint /basicOpen/promotionalActivities/manage/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。 |
| 12 | `lingxing_promotion_vip_discount` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | `/basicOpen/promotionalActivities/vipDiscount/list` | 限流：endpoint /basicOpen/promotionalActivities/vipDiscount/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。 |
| 13 | `lingxing_promotion_coupon` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | `/basicOpen/promotionalActivities/coupon/list` | 限流：endpoint /basicOpen/promotionalActivities/coupon/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。 |
| 14 | `lingxing_resolve_daily_promotions` | `manual` | `manual` | `sid`, `target_date` | `lookback_days` | `/basicOpen/promotion/listingList`<br>`/basicOpen/promotionalActivities/secKill/list`<br>`/basicOpen/promotionalActivities/manage/list`<br>`/basicOpen/promotionalActivities/vipDiscount/list`<br>`/basicOpen/promotionalActivities/coupon/list` | 限流：聚合工具，涉及 5 个 endpoint；最严格为 /basicOpen/promotion/listingList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。 |
| 15 | `lingxing_asin_product_snapshot` | `manual` | `manual` | `sid`, `asin` | `start_date`, `end_date` | `/basicOpen/openapi/storage/fbaWarehouseDetail`<br>`/bd/productPerformance/openApi/asinList`<br>`/erp/sc/routing/data/local_inventory/productList` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /basicOpen/openapi/storage/fbaWarehouseDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按店铺 sid 和 ASIN 查询产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。 |
| 16 | `lingxing_local_product_costs` | `manual` | `manual` | - | `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`, `page_size`, `include_supplier_quotes`, `include_raw` | `/erp/sc/routing/data/local_inventory/productList` | 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。 |
| 17 | `lingxing_smoke_check` | `manual` | `manual` | - | `sid`, `date` | `/erp/sc/data/seller/lists`<br>`/erp/sc/data/seller/allMarketplace`<br>`/erp/sc/data/sales_report/sales`<br>`/erp/sc/data/mws/orders`<br>`/basicOpen/promotion/listingList`<br>`/basicOpen/baseData/account/list`<br>`/pb/openapi/newad/spProductAdReports`<br>`/pb/openapi/newad/sdProductAdReports`<br>`/pb/openapi/newad/hsaPurchasedAsinReports`<br>`/bd/profit/statistics/open/seller/list`<br>`/erp/sc/data/mws_report/allOrders`<br>`/erp/sc/data/mws_report/manageInventory` | 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。 |
| 18 | `lingxing_ad_accounts` | `manual` | `manual` | - | `type`, `sid`, `profile_id`, `country_code`, `status` | `/basicOpen/baseData/account/list` | 限流：endpoint /basicOpen/baseData/account/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。 |
| 19 | `lingxing_report_export_create` | `manual` | `manual` | `sid`, `report_type` | `data_start_time`, `data_end_time`, `marketplace_ids`, `region`, `seller_id` | `/basicOpen/report/create/reportExportTask` | 限流：endpoint /basicOpen/report/create/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 创建亚马逊报告导出任务。 |
| 20 | `lingxing_report_export_query` | `manual` | `manual` | `task_id` | `sid`, `region`, `seller_id` | `/basicOpen/report/query/reportExportTask` | 限流：endpoint /basicOpen/report/query/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询亚马逊报告导出任务结果。 |
| 21 | `lingxing_report_export_refresh_url` | `manual` | `manual` | `report_document_id` | `sid`, `region`, `seller_id` | `/basicOpen/report/amazonReportExportTask` | 限流：endpoint /basicOpen/report/amazonReportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 续期亚马逊报告下载链接。 |
| 22 | `lingxing_report_export_download` | `manual` | `manual` | - | `url`, `sid`, `task_id`, `report_document_id`, `region`, `seller_id` | `/basicOpen/report/query/reportExportTask`<br>`/basicOpen/report/amazonReportExportTask` | 限流：聚合工具，涉及 2 个 endpoint；最严格为 /basicOpen/report/query/reportExportTask 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 下载并解析亚马逊报告导出文件。 |
| 23 | `lingxing_asin_ads_daily_rollup` | `manual` | `manual` | `sid`, `asin`, `start_date`, `end_date` | `attribution_policy` | `/basicOpen/baseData/account/list`<br>`/pb/openapi/newad/hsaProductAds`<br>`/pb/openapi/newad/spProductAdReports`<br>`/pb/openapi/newad/sdProductAdReports`<br>`/pb/openapi/newad/hsaPurchasedAsinReports`<br>`/pb/openapi/newad/listHsaProductAdReport` | 限流：聚合工具，涉及 6 个 endpoint；最严格为 /basicOpen/baseData/account/list 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按 ASIN 汇总每日广告指标，采用 balanced 归因。 |
| 24 | `lingxing_asin_weekly_rollup` | `manual` | `manual` | `sid`, `asin`, `start_date`, `end_date` | - | `/erp/sc/data/sales_report/sales`<br>`/basicOpen/baseData/account/list`<br>`/pb/openapi/newad/hsaProductAds`<br>`/pb/openapi/newad/spProductAdReports`<br>`/pb/openapi/newad/sdProductAdReports`<br>`/pb/openapi/newad/hsaPurchasedAsinReports`<br>`/pb/openapi/newad/listHsaProductAdReport`<br>`/basicOpen/promotion/listingList`<br>`/basicOpen/promotionalActivities/secKill/list`<br>`/basicOpen/promotionalActivities/manage/list`<br>`/basicOpen/promotionalActivities/vipDiscount/list`<br>`/basicOpen/promotionalActivities/coupon/list` | 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/sales_report/sales 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按周汇总 ASIN 的总销量、广告指标和促销标签。 |
| 25 | `lingxing_ads_sp_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spCampaignReports` | 限流：endpoint /pb/openapi/newad/spCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动日报。 |
| 26 | `lingxing_ads_sp_product_ad_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spProductAdReports` | 限流：endpoint /pb/openapi/newad/spProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告商品日报，可直接按 ASIN 聚合。 |
| 27 | `lingxing_ads_sp_keyword_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spKeywordReports` | 限流：endpoint /pb/openapi/newad/spKeywordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 关键词日报。 |
| 28 | `lingxing_ads_sp_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spTargetReports` | 限流：endpoint /pb/openapi/newad/spTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 商品定位日报。 |
| 29 | `lingxing_ads_sp_search_term_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail`, `target_type` | `/pb/openapi/newad/queryWordReports` | 限流：endpoint /pb/openapi/newad/queryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 用户搜索词日报。 |
| 30 | `lingxing_ads_sd_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdCampaignReports` | 限流：endpoint /pb/openapi/newad/sdCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动日报。 |
| 31 | `lingxing_ads_sd_product_ad_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdProductAdReports` | 限流：endpoint /pb/openapi/newad/sdProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告商品日报，可直接按 ASIN 聚合。 |
| 32 | `lingxing_ads_sd_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdTargetReports` | 限流：endpoint /pb/openapi/newad/sdTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 商品定位日报。 |
| 33 | `lingxing_ads_sb_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaCampaignReports` | 限流：endpoint /pb/openapi/newad/hsaCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动日报。 |
| 34 | `lingxing_ads_sb_creative_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaProductAdReport` | 限流：endpoint /pb/openapi/newad/listHsaProductAdReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告创意日报。 |
| 35 | `lingxing_ads_sb_purchased_asin_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id` | `/pb/openapi/newad/hsaPurchasedAsinReports` | 限流：endpoint /pb/openapi/newad/hsaPurchasedAsinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。 |
| 36 | `lingxing_ads_sp_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spCampaignHourData` | 限流：endpoint /pb/openapi/newad/spCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动小时数据。 |
| 37 | `lingxing_ads_sp_placement_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdPlacementHourData` | 限流：endpoint /pb/openapi/newad/spAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告位小时数据。 |
| 38 | `lingxing_ads_sp_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdGroupHourData` | 限流：endpoint /pb/openapi/newad/spAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告组小时数据。 |
| 39 | `lingxing_ads_sp_advertise_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdvertiseHourData` | 限流：endpoint /pb/openapi/newad/spAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告小时数据。 |
| 40 | `lingxing_ads_sp_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spTargetHourData` | 限流：endpoint /pb/openapi/newad/spTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 投放小时数据。 |
| 41 | `lingxing_ads_sb_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbCampaignHourData` | 限流：endpoint /pb/openapi/newad/sbCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动小时数据。 |
| 42 | `lingxing_ads_sb_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbAdGroupHourData` | 限流：endpoint /pb/openapi/newad/sbAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告组小时数据。 |
| 43 | `lingxing_ads_sb_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbTargetHourData` | 限流：endpoint /pb/openapi/newad/sbTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 投放小时数据。 |
| 44 | `lingxing_ads_sb_placement_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbAdPlacementHourData` | 限流：endpoint /pb/openapi/newad/sbAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告位小时数据。 |
| 45 | `lingxing_ads_sd_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdCampaignHourData` | 限流：endpoint /pb/openapi/newad/sdCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动小时数据。 |
| 46 | `lingxing_ads_sd_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdGroupHourData` | 限流：endpoint /pb/openapi/newad/sdAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告组小时数据。 |
| 47 | `lingxing_ads_sd_advertise_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdvertiseHourData` | 限流：endpoint /pb/openapi/newad/sdAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告小时数据。 |
| 48 | `lingxing_ads_sd_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdTargetHourData` | 限流：endpoint /pb/openapi/newad/sdTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 投放小时数据。 |
| 49 | `lingxing_ads_portfolios` | `endpoint_spec` | `ad_base` | `sid` | `profile_id` | `/pb/openapi/newad/portfolios` | 限流：endpoint /pb/openapi/newad/portfolios，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 广告组合列表。 |
| 50 | `lingxing_ads_sp_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spCampaigns` | 限流：endpoint /pb/openapi/newad/spCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动基础数据。 |
| 51 | `lingxing_ads_sp_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spAdGroups` | 限流：endpoint /pb/openapi/newad/spAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告组基础数据。 |
| 52 | `lingxing_ads_sp_product_ads` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spProductAds` | 限流：endpoint /pb/openapi/newad/spProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告商品基础数据。 |
| 53 | `lingxing_ads_sp_keywords` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spKeywords` | 限流：endpoint /pb/openapi/newad/spKeywords，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 关键词基础数据。 |
| 54 | `lingxing_ads_sp_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spTargets` | 限流：endpoint /pb/openapi/newad/spTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 商品定位基础数据。 |
| 55 | `lingxing_ads_sd_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdCampaigns` | 限流：endpoint /pb/openapi/newad/sdCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动基础数据。 |
| 56 | `lingxing_ads_sd_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdAdGroups` | 限流：endpoint /pb/openapi/newad/sdAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告组基础数据。 |
| 57 | `lingxing_ads_sd_product_ads` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdProductAds` | 限流：endpoint /pb/openapi/newad/sdProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告商品基础数据。 |
| 58 | `lingxing_ads_sd_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdTargets` | 限流：endpoint /pb/openapi/newad/sdTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 商品定位基础数据。 |
| 59 | `lingxing_ads_sb_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/hsaCampaigns` | 限流：endpoint /pb/openapi/newad/hsaCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动基础数据。 |
| 60 | `lingxing_ads_sb_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/hsaAdGroups` | 限流：endpoint /pb/openapi/newad/hsaAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告组基础数据。 |
| 61 | `lingxing_ads_sb_creatives` | `endpoint_spec` | `ad_base` | `sid` | `profile_id` | `/pb/openapi/newad/hsaProductAds` | 限流：endpoint /pb/openapi/newad/hsaProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告创意基础数据。 |
| 62 | `lingxing_ads_sb_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sbTargeting` | 限流：endpoint /pb/openapi/newad/sbTargeting，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 投放基础数据。 |
| 63 | `lingxing_profit_seller` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value`, `monthly_query` | `/bd/profit/statistics/open/seller/list` | 限流：endpoint /bd/profit/statistics/open/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 店铺维度利润统计。 |
| 64 | `lingxing_profit_asin` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value` | `/bd/profit/statistics/open/asin/list` | 限流：endpoint /bd/profit/statistics/open/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | ASIN 维度利润统计。 |
| 65 | `lingxing_profit_parent_asin` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value` | `/bd/profit/statistics/open/parent/asin/list` | 限流：endpoint /bd/profit/statistics/open/parent/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 父 ASIN 维度利润统计。 |
| 66 | `lingxing_fba_warehouse_detail` | `endpoint_spec` | `warehouse` | `sid` | `search_field`, `search_value`, `cid`, `bid`, `attribute`, `asin_principal`, `status`, `senior_search_list`, `fulfillment_channel_type`, `is_hide_zero_stock`, `is_parant_asin_merge`, `is_contain_del_ls`, `query_fba_storage_quantity_list` | `/basicOpen/openapi/storage/fbaWarehouseDetail` | 限流：endpoint /basicOpen/openapi/storage/fbaWarehouseDetail，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。 |
| 67 | `lingxing_local_products` | `endpoint_spec` | `product` | - | `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end` | `/erp/sc/routing/data/local_inventory/productList` | 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。 |
| 68 | `lingxing_product_performance` | `endpoint_spec` | `source` | `sid`, `start_date`, `end_date` | `search_field`, `search_value`, `summary_field`, `mid`, `currency_code`, `is_recently_enum`, `purchase_status`, `sort_field`, `sort_type` | `/bd/productPerformance/openApi/asinList` | 限流：endpoint /bd/productPerformance/openApi/asinList，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。 |
| 69 | `lingxing_source_all_orders` | `endpoint_spec` | `source` | `sid`, `start_date`, `end_date` | `date_type` | `/erp/sc/data/mws_report/allOrders` | 限流：endpoint /erp/sc/data/mws_report/allOrders，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。 | 亚马逊源表所有订单。 |
| 70 | `lingxing_source_manage_inventory` | `endpoint_spec` | `source` | `sid` | - | `/erp/sc/data/mws_report/manageInventory` | 限流：endpoint /erp/sc/data/mws_report/manageInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表 FBA 库存。 |
| 71 | `lingxing_source_daily_inventory` | `endpoint_spec` | `source` | `sid`, `event_date` | - | `/erp/sc/data/mws_report/dailyInventory` | 限流：endpoint /erp/sc/data/mws_report/dailyInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表每日库存。 |
| 72 | `lingxing_source_reserved_inventory` | `endpoint_spec` | `source` | `sid` | - | `/erp/sc/data/mws_report/reservedInventory` | 限流：endpoint /erp/sc/data/mws_report/reservedInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表预留库存。 |
| 73 | `lingxing_source_transaction` | `endpoint_spec` | `source` | `sid`, `event_date` | - | `/erp/sc/data/mws_report/transaction` | 限流：endpoint /erp/sc/data/mws_report/transaction，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表交易明细。 |
| 74 | `lingxing_fba_stock_aggregate` | `endpoint_spec` | `stock` | `sid`, `start_month`, `end_month` | - | `/cost/center/openApi/fba/gather/query` | 限流：endpoint /cost/center/openApi/fba/gather/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | FBA 库存新报表汇总。 |
| 75 | `lingxing_fba_stock_detail` | `endpoint_spec` | `stock` | `sid`, `start_month`, `end_month` | - | `/cost/center/openApi/fba/detail/query` | 限流：endpoint /cost/center/openApi/fba/detail/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | FBA 库存新报表明细。 |
| 76 | `lingxing_replenishment_summary` | `endpoint_spec` | `replenishment_summary` | `sid` | `asin`, `mode` | `/erp/sc/routing/restocking/analysis/getSummaryList` | 限流：endpoint /erp/sc/routing/restocking/analysis/getSummaryList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 补货建议列表。 |
| 77 | `lingxing_replenishment_asin_info` | `endpoint_spec` | `replenishment_info` | `sid`, `asin` | `mode` | `/erp/sc/routing/fbaSug/asin/getInfo` | 限流：endpoint /erp/sc/routing/fbaSug/asin/getInfo，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 补货建议 ASIN 明细。 |
| 78 | `lingxing_exp_ads_sp_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/campaignPlacementReports` | 限流：endpoint /pb/openapi/newad/campaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 广告位日报。 |
| 79 | `lingxing_exp_ads_sp_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdGroupReports` | 限流：endpoint /pb/openapi/newad/spAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 广告组日报。 |
| 80 | `lingxing_exp_ads_sp_purchased_asin_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/asinReports` | 限流：endpoint /pb/openapi/newad/asinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 已购买 ASIN 报表。 |
| 81 | `lingxing_exp_ads_sb_campaign_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaCampaignPlacementReports` | 限流：endpoint /pb/openapi/newad/hsaCampaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 广告位日报。 |
| 82 | `lingxing_exp_ads_sb_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaAdGroupReports` | 限流：endpoint /pb/openapi/newad/hsaAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 广告组日报。 |
| 83 | `lingxing_exp_ads_sb_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaTargetingReport` | 限流：endpoint /pb/openapi/newad/listHsaTargetingReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 投放日报。 |
| 84 | `lingxing_exp_ads_sb_search_term_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaQueryWordReports` | 限流：endpoint /pb/openapi/newad/hsaQueryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 用户搜索词日报。 |
| 85 | `lingxing_exp_ads_sb_keyword_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaKeywordPlacementReport` | 限流：endpoint /pb/openapi/newad/listHsaKeywordPlacementReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 关键词广告位日报。 |
| 86 | `lingxing_exp_ads_sd_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdGroupReports` | 限流：endpoint /pb/openapi/newad/sdAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SD 广告组日报。 |
| 87 | `lingxing_exp_ads_sd_match_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdMatchTargetReports` | 限流：endpoint /pb/openapi/newad/sdMatchTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SD 匹配目标日报。 |
| 88 | `lingxing_exp_ads_aba_report` | `endpoint_spec` | `ad_report` | `country`, `data_start_time` | - | `/pb/openapi/newad/abaReport` | 限流：endpoint /pb/openapi/newad/abaReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：ABA 搜索词周报下载信息。 |
| 89 | `lingxing_finance_report_asin` | `endpoint_spec` | `profit_report` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value`, `monthly_query`, `summary_enabled`, `order_status` | `/bd/profit/report/open/report/asin/list` | 限流：endpoint /bd/profit/report/open/report/asin/list，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。 | 结算利润报表 ASIN 视角。 |
| 90 | `lingxing_exp_finance_report_seller` | `endpoint_spec` | `profit_report` | `sid`, `start_date`, `end_date` | `currency_code`, `monthly_query`, `order_status` | `/bd/profit/report/open/report/seller/list` | 限流：endpoint /bd/profit/report/open/report/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：结算利润报表店铺视角。 |

## Tool Details

### 1. `lingxing_health_check`

- Description: 检查领星环境变量、token 状态和基础连通性，不拉业务数据。
- Rate limit: 限流：endpoint /api/auth-server/oauth/access-token，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/api/auth-server/oauth/access-token`
- Docs path: -
- Required args: -
- Optional args: -
- Endpoint policies:
  - `/api/auth-server/oauth/access-token`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 2. `lingxing_rate_limit_policy`

- Description: 返回当前 MCP 工具到领星 OpenAPI endpoint 的限流政策，供客户端 agent 在调用前按 endpoint 自主排队。
- Rate limit: 限流：本工具不直接调用领星业务 OpenAPI，或仅返回本地网关策略；客户端可并发调用，但不应把它作为业务查询循环。
- Registered by: `manual`
- Category: `manual`
- Endpoints: -
- Docs path: -
- Required args: -
- Optional args: `tool_name`

```json
{
  "type": "object",
  "properties": {
    "tool_name": {
      "type": "string",
      "description": "可选；只查询某一个 MCP 工具的限流策略。"
    }
  },
  "additionalProperties": false
}
```

### 3. `lingxing_seller_lists`

- Description: 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。
- Rate limit: 限流：聚合工具，涉及 2 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/seller/lists`, `/erp/sc/data/seller/allMarketplace`
- Docs path: -
- Required args: -
- Optional args: `status`, `marketplace`
- Endpoint policies:
  - `/erp/sc/data/seller/lists`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/data/seller/allMarketplace`: 1 req/s, burst `1`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "integer",
      "description": "店铺状态过滤，按领星 seller/lists 返回的 status 值匹配。"
    },
    "marketplace": {
      "type": "string",
      "description": "站点代码过滤，例如 US、UK、DE、JP。"
    }
  },
  "additionalProperties": false
}
```

### 4. `lingxing_marketplaces`

- Description: 返回领星市场列表，并补充站点时区映射。
- Rate limit: 限流：endpoint /erp/sc/data/seller/allMarketplace，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/seller/allMarketplace`
- Docs path: -
- Required args: -
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/seller/allMarketplace`: 1 req/s, burst `1`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 5. `lingxing_store_sales`

- Description: 按店铺和日期范围拉取 StoreSales，并自动合并分页。
- Rate limit: 限流：endpoint /erp/sc/data/sales_report/sales，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/sales_report/sales`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/sales_report/sales`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 6. `lingxing_asin_daily_lists`

- Description: 按店铺、日期和指标类型拉取 AsinDailyLists。
- Rate limit: 限流：endpoint /erp/sc/data/sales_report/asinDailyLists，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/sales_report/asinDailyLists`
- Docs path: -
- Required args: `sid`, `event_date`, `metric_type`
- Optional args: `asin_type`
- Endpoint policies:
  - `/erp/sc/data/sales_report/asinDailyLists`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "event_date": {
      "type": "string"
    },
    "metric_type": {
      "type": "integer"
    },
    "asin_type": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "event_date",
    "metric_type"
  ],
  "additionalProperties": false
}
```

### 7. `lingxing_order_lists`

- Description: 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。
- Rate limit: 限流：endpoint /erp/sc/data/mws/orders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/mws/orders`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `date_type`
- Endpoint policies:
  - `/erp/sc/data/mws/orders`: 1 req/s, burst `1`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "date_type": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 8. `lingxing_order_details`

- Description: 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/mws/orderDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/mws/orderDetail`, `/erp/sc/data/seller/lists`, `/erp/sc/data/seller/allMarketplace`
- Docs path: -
- Required args: -
- Optional args: `order_id`, `order_ids`
- Endpoint policies:
  - `/erp/sc/data/mws/orderDetail`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/data/seller/lists`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/data/seller/allMarketplace`: 1 req/s, burst `1`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "order_id": {
      "type": "string",
      "description": "单个亚马逊订单号；也可用英文逗号、中文逗号、分号或换行分隔多个订单号。"
    },
    "order_ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "亚马逊订单号列表。"
    }
  },
  "additionalProperties": false
}
```

### 9. `lingxing_promotion_listing`

- Description: 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。
- Rate limit: 限流：endpoint /basicOpen/promotion/listingList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotion/listingList`
- Docs path: -
- Required args: `sid`, `site_date`, `start_time`, `end_time`
- Optional args: `status`, `product_status`, `promotion_category`
- Endpoint policies:
  - `/basicOpen/promotion/listingList`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "site_date": {
      "type": "string"
    },
    "start_time": {
      "type": "string"
    },
    "end_time": {
      "type": "string"
    },
    "status": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "product_status": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "promotion_category": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    }
  },
  "required": [
    "sid",
    "site_date",
    "start_time",
    "end_time"
  ],
  "additionalProperties": false
}
```

### 10. `lingxing_promotion_sec_kill`

- Description: 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/secKill/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotionalActivities/secKill/list`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/basicOpen/promotionalActivities/secKill/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 11. `lingxing_promotion_manage`

- Description: 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/manage/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotionalActivities/manage/list`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/basicOpen/promotionalActivities/manage/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 12. `lingxing_promotion_vip_discount`

- Description: 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/vipDiscount/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotionalActivities/vipDiscount/list`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/basicOpen/promotionalActivities/vipDiscount/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 13. `lingxing_promotion_coupon`

- Description: 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/coupon/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotionalActivities/coupon/list`
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/basicOpen/promotionalActivities/coupon/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 14. `lingxing_resolve_daily_promotions`

- Description: 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。
- Rate limit: 限流：聚合工具，涉及 5 个 endpoint；最严格为 /basicOpen/promotion/listingList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/promotion/listingList`, `/basicOpen/promotionalActivities/secKill/list`, `/basicOpen/promotionalActivities/manage/list`, `/basicOpen/promotionalActivities/vipDiscount/list`, `/basicOpen/promotionalActivities/coupon/list`
- Docs path: -
- Required args: `sid`, `target_date`
- Optional args: `lookback_days`
- Endpoint policies:
  - `/basicOpen/promotion/listingList`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/secKill/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/manage/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/vipDiscount/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/coupon/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "target_date": {
      "type": "string"
    },
    "lookback_days": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "target_date"
  ],
  "additionalProperties": false
}
```

### 15. `lingxing_asin_product_snapshot`

- Description: 按店铺 sid 和 ASIN 查询产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /basicOpen/openapi/storage/fbaWarehouseDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/openapi/storage/fbaWarehouseDetail`, `/bd/productPerformance/openApi/asinList`, `/erp/sc/routing/data/local_inventory/productList`
- Docs path: -
- Required args: `sid`, `asin`
- Optional args: `start_date`, `end_date`
- Endpoint policies:
  - `/basicOpen/openapi/storage/fbaWarehouseDetail`: 1 req/s, burst `1`, source `conservative`
  - `/bd/productPerformance/openApi/asinList`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/routing/data/local_inventory/productList`: 1 req/s, burst `1`, source `conservative`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "asin": {
      "type": "string"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "asin"
  ],
  "additionalProperties": false
}
```

### 16. `lingxing_local_product_costs`

- Description: 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。
- Rate limit: 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/routing/data/local_inventory/productList`
- Docs path: -
- Required args: -
- Optional args: `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`, `page_size`, `include_supplier_quotes`, `include_raw`
- Endpoint policies:
  - `/erp/sc/routing/data/local_inventory/productList`: 1 req/s, burst `1`, source `conservative`

```json
{
  "type": "object",
  "properties": {
    "sku_list": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "sku_identifier_list": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "update_time_start": {
      "type": "integer"
    },
    "update_time_end": {
      "type": "integer"
    },
    "create_time_start": {
      "type": "integer"
    },
    "create_time_end": {
      "type": "integer"
    },
    "page_size": {
      "type": "integer"
    },
    "include_supplier_quotes": {
      "type": "boolean"
    },
    "include_raw": {
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```

### 17. `lingxing_smoke_check`

- Description: 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。
- Rate limit: 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/seller/lists`, `/erp/sc/data/seller/allMarketplace`, `/erp/sc/data/sales_report/sales`, `/erp/sc/data/mws/orders`, `/basicOpen/promotion/listingList`, `/basicOpen/baseData/account/list`, `/pb/openapi/newad/spProductAdReports`, `/pb/openapi/newad/sdProductAdReports`, `/pb/openapi/newad/hsaPurchasedAsinReports`, `/bd/profit/statistics/open/seller/list`, `/erp/sc/data/mws_report/allOrders`, `/erp/sc/data/mws_report/manageInventory`
- Docs path: -
- Required args: -
- Optional args: `sid`, `date`
- Endpoint policies:
  - `/erp/sc/data/seller/lists`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/data/seller/allMarketplace`: 1 req/s, burst `1`, source `openapi_docs`
  - `/erp/sc/data/sales_report/sales`: 1 req/s, burst `1`, source `default`
  - `/erp/sc/data/mws/orders`: 1 req/s, burst `1`, source `openapi_docs`
  - `/basicOpen/promotion/listingList`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/baseData/account/list`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/spProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/sdProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/hsaPurchasedAsinReports`: 1 req/s, burst `1`, source `default`
  - `/bd/profit/statistics/open/seller/list`: 1 req/s, burst `1`, source `default`
  - `/erp/sc/data/mws_report/allOrders`: 10 req/s, burst `10`, source `openapi_docs`
  - `/erp/sc/data/mws_report/manageInventory`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "date": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

### 18. `lingxing_ad_accounts`

- Description: 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。
- Rate limit: 限流：endpoint /basicOpen/baseData/account/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/baseData/account/list`
- Docs path: -
- Required args: -
- Optional args: `type`, `sid`, `profile_id`, `country_code`, `status`
- Endpoint policies:
  - `/basicOpen/baseData/account/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "type": {
      "type": "string"
    },
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "country_code": {
      "type": "string"
    },
    "status": {
      "type": "integer"
    }
  },
  "additionalProperties": false
}
```

### 19. `lingxing_report_export_create`

- Description: 创建亚马逊报告导出任务。
- Rate limit: 限流：endpoint /basicOpen/report/create/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/report/create/reportExportTask`
- Docs path: -
- Required args: `sid`, `report_type`
- Optional args: `data_start_time`, `data_end_time`, `marketplace_ids`, `region`, `seller_id`
- Endpoint policies:
  - `/basicOpen/report/create/reportExportTask`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_type": {
      "type": "string"
    },
    "data_start_time": {
      "type": "string"
    },
    "data_end_time": {
      "type": "string"
    },
    "marketplace_ids": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "region": {
      "type": "string"
    },
    "seller_id": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "report_type"
  ],
  "additionalProperties": false
}
```

### 20. `lingxing_report_export_query`

- Description: 查询亚马逊报告导出任务结果。
- Rate limit: 限流：endpoint /basicOpen/report/query/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/report/query/reportExportTask`
- Docs path: -
- Required args: `task_id`
- Optional args: `sid`, `region`, `seller_id`
- Endpoint policies:
  - `/basicOpen/report/query/reportExportTask`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "task_id": {
      "type": "string"
    },
    "region": {
      "type": "string"
    },
    "seller_id": {
      "type": "string"
    }
  },
  "required": [
    "task_id"
  ],
  "additionalProperties": false
}
```

### 21. `lingxing_report_export_refresh_url`

- Description: 续期亚马逊报告下载链接。
- Rate limit: 限流：endpoint /basicOpen/report/amazonReportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/report/amazonReportExportTask`
- Docs path: -
- Required args: `report_document_id`
- Optional args: `sid`, `region`, `seller_id`
- Endpoint policies:
  - `/basicOpen/report/amazonReportExportTask`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_document_id": {
      "type": "string"
    },
    "region": {
      "type": "string"
    },
    "seller_id": {
      "type": "string"
    }
  },
  "required": [
    "report_document_id"
  ],
  "additionalProperties": false
}
```

### 22. `lingxing_report_export_download`

- Description: 下载并解析亚马逊报告导出文件。
- Rate limit: 限流：聚合工具，涉及 2 个 endpoint；最严格为 /basicOpen/report/query/reportExportTask 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/report/query/reportExportTask`, `/basicOpen/report/amazonReportExportTask`
- Docs path: -
- Required args: -
- Optional args: `url`, `sid`, `task_id`, `report_document_id`, `region`, `seller_id`
- Endpoint policies:
  - `/basicOpen/report/query/reportExportTask`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/report/amazonReportExportTask`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "url": {
      "type": "string"
    },
    "sid": {
      "type": "integer"
    },
    "task_id": {
      "type": "string"
    },
    "report_document_id": {
      "type": "string"
    },
    "region": {
      "type": "string"
    },
    "seller_id": {
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

### 23. `lingxing_asin_ads_daily_rollup`

- Description: 按 ASIN 汇总每日广告指标，采用 balanced 归因。
- Rate limit: 限流：聚合工具，涉及 6 个 endpoint；最严格为 /basicOpen/baseData/account/list 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/basicOpen/baseData/account/list`, `/pb/openapi/newad/hsaProductAds`, `/pb/openapi/newad/spProductAdReports`, `/pb/openapi/newad/sdProductAdReports`, `/pb/openapi/newad/hsaPurchasedAsinReports`, `/pb/openapi/newad/listHsaProductAdReport`
- Docs path: -
- Required args: `sid`, `asin`, `start_date`, `end_date`
- Optional args: `attribution_policy`
- Endpoint policies:
  - `/basicOpen/baseData/account/list`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/hsaProductAds`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/spProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/sdProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/hsaPurchasedAsinReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/listHsaProductAdReport`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "asin": {
      "type": "string"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "attribution_policy": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "asin",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 24. `lingxing_asin_weekly_rollup`

- Description: 按周汇总 ASIN 的总销量、广告指标和促销标签。
- Rate limit: 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/sales_report/sales 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Registered by: `manual`
- Category: `manual`
- Endpoints: `/erp/sc/data/sales_report/sales`, `/basicOpen/baseData/account/list`, `/pb/openapi/newad/hsaProductAds`, `/pb/openapi/newad/spProductAdReports`, `/pb/openapi/newad/sdProductAdReports`, `/pb/openapi/newad/hsaPurchasedAsinReports`, `/pb/openapi/newad/listHsaProductAdReport`, `/basicOpen/promotion/listingList`, `/basicOpen/promotionalActivities/secKill/list`, `/basicOpen/promotionalActivities/manage/list`, `/basicOpen/promotionalActivities/vipDiscount/list`, `/basicOpen/promotionalActivities/coupon/list`
- Docs path: -
- Required args: `sid`, `asin`, `start_date`, `end_date`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/sales_report/sales`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/baseData/account/list`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/hsaProductAds`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/spProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/sdProductAdReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/hsaPurchasedAsinReports`: 1 req/s, burst `1`, source `default`
  - `/pb/openapi/newad/listHsaProductAdReport`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotion/listingList`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/secKill/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/manage/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/vipDiscount/list`: 1 req/s, burst `1`, source `default`
  - `/basicOpen/promotionalActivities/coupon/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "asin": {
      "type": "string"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "asin",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 25. `lingxing_ads_sp_campaign_report`

- Description: SP 广告活动日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spCampaignReports`
- Docs path: `docs/newAd/report/spCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spCampaignReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 26. `lingxing_ads_sp_product_ad_report`

- Description: SP 广告商品日报，可直接按 ASIN 聚合。
- Rate limit: 限流：endpoint /pb/openapi/newad/spProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spProductAdReports`
- Docs path: `docs/newAd/report/spProductAdReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spProductAdReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 27. `lingxing_ads_sp_keyword_report`

- Description: SP 关键词日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/spKeywordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spKeywordReports`
- Docs path: `docs/newAd/report/spKeywordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spKeywordReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 28. `lingxing_ads_sp_target_report`

- Description: SP 商品定位日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spTargetReports`
- Docs path: `docs/newAd/report/spTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spTargetReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 29. `lingxing_ads_sp_search_term_report`

- Description: SP 用户搜索词日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/queryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/queryWordReports`
- Docs path: `docs/newAd/report/queryWordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`, `target_type`
- Endpoint policies:
  - `/pb/openapi/newad/queryWordReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    },
    "target_type": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 30. `lingxing_ads_sd_campaign_report`

- Description: SD 广告活动日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdCampaignReports`
- Docs path: `docs/newAd/report/sdCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdCampaignReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 31. `lingxing_ads_sd_product_ad_report`

- Description: SD 广告商品日报，可直接按 ASIN 聚合。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdProductAdReports`
- Docs path: `docs/newAd/report/sdProductAdReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdProductAdReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 32. `lingxing_ads_sd_target_report`

- Description: SD 商品定位日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdTargetReports`
- Docs path: `docs/newAd/report/sdTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdTargetReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 33. `lingxing_ads_sb_campaign_report`

- Description: SB 广告活动日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/hsaCampaignReports`
- Docs path: `docs/newAd/report/hsaCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/hsaCampaignReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 34. `lingxing_ads_sb_creative_report`

- Description: SB 广告创意日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaProductAdReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/listHsaProductAdReport`
- Docs path: `docs/newAd/report/listHsaProductAdReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/listHsaProductAdReport`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 35. `lingxing_ads_sb_purchased_asin_report`

- Description: SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaPurchasedAsinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/hsaPurchasedAsinReports`
- Docs path: `docs/newAd/report/hsaPurchasedAsinReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`
- Endpoint policies:
  - `/pb/openapi/newad/hsaPurchasedAsinReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 36. `lingxing_ads_sp_campaign_hourly`

- Description: SP 广告活动小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spCampaignHourData`
- Docs path: `docs/newAd/report/spCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spCampaignHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 37. `lingxing_ads_sp_placement_hourly`

- Description: SP 广告位小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spAdPlacementHourData`
- Docs path: `docs/newAd/report/spAdPlacementHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spAdPlacementHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 38. `lingxing_ads_sp_ad_group_hourly`

- Description: SP 广告组小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spAdGroupHourData`
- Docs path: `docs/newAd/report/spAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spAdGroupHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 39. `lingxing_ads_sp_advertise_hourly`

- Description: SP 广告小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spAdvertiseHourData`
- Docs path: `docs/newAd/report/spAdvertiseHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spAdvertiseHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 40. `lingxing_ads_sp_target_hourly`

- Description: SP 投放小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spTargetHourData`
- Docs path: `docs/newAd/report/spTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spTargetHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 41. `lingxing_ads_sb_campaign_hourly`

- Description: SB 广告活动小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sbCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sbCampaignHourData`
- Docs path: `docs/newAd/report/sbCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sbCampaignHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 42. `lingxing_ads_sb_ad_group_hourly`

- Description: SB 广告组小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sbAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sbAdGroupHourData`
- Docs path: `docs/newAd/report/sbAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sbAdGroupHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 43. `lingxing_ads_sb_target_hourly`

- Description: SB 投放小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sbTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sbTargetHourData`
- Docs path: `docs/newAd/report/sbTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sbTargetHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 44. `lingxing_ads_sb_placement_hourly`

- Description: SB 广告位小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sbAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sbAdPlacementHourData`
- Docs path: `docs/newAd/report/sbAdPlacementHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sbAdPlacementHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 45. `lingxing_ads_sd_campaign_hourly`

- Description: SD 广告活动小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdCampaignHourData`
- Docs path: `docs/newAd/report/sdCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdCampaignHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 46. `lingxing_ads_sd_ad_group_hourly`

- Description: SD 广告组小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdAdGroupHourData`
- Docs path: `docs/newAd/report/sdAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdAdGroupHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 47. `lingxing_ads_sd_advertise_hourly`

- Description: SD 广告小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdAdvertiseHourData`
- Docs path: `docs/newAd/report/sdAdvertiseHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdAdvertiseHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 48. `lingxing_ads_sd_target_hourly`

- Description: SD 投放小时数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdTargetHourData`
- Docs path: `docs/newAd/report/sdTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdTargetHourData`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 49. `lingxing_ads_portfolios`

- Description: 广告组合列表。
- Rate limit: 限流：endpoint /pb/openapi/newad/portfolios，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/portfolios`
- Docs path: `docs/newAd/baseData/portfolios.md`
- Required args: `sid`
- Optional args: `profile_id`
- Endpoint policies:
  - `/pb/openapi/newad/portfolios`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 50. `lingxing_ads_sp_campaigns`

- Description: SP 广告活动基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/spCampaigns`
- Docs path: `docs/newAd/baseData/spCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/spCampaigns`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 51. `lingxing_ads_sp_ad_groups`

- Description: SP 广告组基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/spAdGroups`
- Docs path: `docs/newAd/baseData/spAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/spAdGroups`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 52. `lingxing_ads_sp_product_ads`

- Description: SP 广告商品基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/spProductAds`
- Docs path: `docs/newAd/baseData/spProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/spProductAds`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 53. `lingxing_ads_sp_keywords`

- Description: SP 关键词基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spKeywords，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/spKeywords`
- Docs path: `docs/newAd/baseData/spKeywords.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/spKeywords`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 54. `lingxing_ads_sp_targets`

- Description: SP 商品定位基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/spTargets`
- Docs path: `docs/newAd/baseData/spTargets.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/spTargets`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 55. `lingxing_ads_sd_campaigns`

- Description: SD 广告活动基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/sdCampaigns`
- Docs path: `docs/newAd/baseData/sdCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/sdCampaigns`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 56. `lingxing_ads_sd_ad_groups`

- Description: SD 广告组基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/sdAdGroups`
- Docs path: `docs/newAd/baseData/sdAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/sdAdGroups`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 57. `lingxing_ads_sd_product_ads`

- Description: SD 广告商品基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/sdProductAds`
- Docs path: `docs/newAd/baseData/sdProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/sdProductAds`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 58. `lingxing_ads_sd_targets`

- Description: SD 商品定位基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/sdTargets`
- Docs path: `docs/newAd/baseData/sdTargets.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/sdTargets`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 59. `lingxing_ads_sb_campaigns`

- Description: SB 广告活动基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/hsaCampaigns`
- Docs path: `docs/newAd/baseData/hsaCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/hsaCampaigns`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 60. `lingxing_ads_sb_ad_groups`

- Description: SB 广告组基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/hsaAdGroups`
- Docs path: `docs/newAd/baseData/hsaAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/hsaAdGroups`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 61. `lingxing_ads_sb_creatives`

- Description: SB 广告创意基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/hsaProductAds`
- Docs path: `docs/newAd/baseData/sbAdHasProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`
- Endpoint policies:
  - `/pb/openapi/newad/hsaProductAds`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 62. `lingxing_ads_sb_targets`

- Description: SB 投放基础数据。
- Rate limit: 限流：endpoint /pb/openapi/newad/sbTargeting，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoints: `/pb/openapi/newad/sbTargeting`
- Docs path: `docs/newAd/baseData/sbTargeting.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`
- Endpoint policies:
  - `/pb/openapi/newad/sbTargeting`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "profile_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 63. `lingxing_profit_seller`

- Description: 店铺维度利润统计。
- Rate limit: 限流：endpoint /bd/profit/statistics/open/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoints: `/bd/profit/statistics/open/seller/list`
- Docs path: `docs/Statistics/statisticsOpenSeller.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`, `monthly_query`
- Endpoint policies:
  - `/bd/profit/statistics/open/seller/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "currency_code": {
      "type": "string"
    },
    "search_value": {
      "type": "string"
    },
    "monthly_query": {
      "type": "boolean"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 64. `lingxing_profit_asin`

- Description: ASIN 维度利润统计。
- Rate limit: 限流：endpoint /bd/profit/statistics/open/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoints: `/bd/profit/statistics/open/asin/list`
- Docs path: `docs/Statistics/statisticsOpenASIN.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`
- Endpoint policies:
  - `/bd/profit/statistics/open/asin/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "currency_code": {
      "type": "string"
    },
    "search_value": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 65. `lingxing_profit_parent_asin`

- Description: 父 ASIN 维度利润统计。
- Rate limit: 限流：endpoint /bd/profit/statistics/open/parent/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoints: `/bd/profit/statistics/open/parent/asin/list`
- Docs path: `docs/Statistics/statisticsOpenParent.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`
- Endpoint policies:
  - `/bd/profit/statistics/open/parent/asin/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "currency_code": {
      "type": "string"
    },
    "search_value": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 66. `lingxing_fba_warehouse_detail`

- Description: 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。
- Rate limit: 限流：endpoint /basicOpen/openapi/storage/fbaWarehouseDetail，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `warehouse`
- Endpoints: `/basicOpen/openapi/storage/fbaWarehouseDetail`
- Docs path: `docs/Warehouse/FBAStock_v2.md`
- Required args: `sid`
- Optional args: `search_field`, `search_value`, `cid`, `bid`, `attribute`, `asin_principal`, `status`, `senior_search_list`, `fulfillment_channel_type`, `is_hide_zero_stock`, `is_parant_asin_merge`, `is_contain_del_ls`, `query_fba_storage_quantity_list`
- Endpoint policies:
  - `/basicOpen/openapi/storage/fbaWarehouseDetail`: 1 req/s, burst `1`, source `conservative`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "search_field": {
      "type": "string"
    },
    "search_value": {
      "type": "string"
    },
    "cid": {
      "type": "string"
    },
    "bid": {
      "type": "string"
    },
    "attribute": {
      "type": "string"
    },
    "asin_principal": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "senior_search_list": {
      "type": "string"
    },
    "fulfillment_channel_type": {
      "type": "string"
    },
    "is_hide_zero_stock": {
      "type": "string"
    },
    "is_parant_asin_merge": {
      "type": "string"
    },
    "is_contain_del_ls": {
      "type": "string"
    },
    "query_fba_storage_quantity_list": {
      "type": "boolean"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 67. `lingxing_local_products`

- Description: 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。
- Rate limit: 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `product`
- Endpoints: `/erp/sc/routing/data/local_inventory/productList`
- Docs path: `docs/Product/ProductLists.md`
- Required args: -
- Optional args: `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`
- Endpoint policies:
  - `/erp/sc/routing/data/local_inventory/productList`: 1 req/s, burst `1`, source `conservative`

```json
{
  "type": "object",
  "properties": {
    "sku_list": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "sku_identifier_list": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "update_time_start": {
      "type": "integer"
    },
    "update_time_end": {
      "type": "integer"
    },
    "create_time_start": {
      "type": "integer"
    },
    "create_time_end": {
      "type": "integer"
    }
  },
  "required": [],
  "additionalProperties": false
}
```

### 68. `lingxing_product_performance`

- Description: 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。
- Rate limit: 限流：endpoint /bd/productPerformance/openApi/asinList，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/bd/productPerformance/openApi/asinList`
- Docs path: `docs/Statistics/AsinListNew.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `search_field`, `search_value`, `summary_field`, `mid`, `currency_code`, `is_recently_enum`, `purchase_status`, `sort_field`, `sort_type`
- Endpoint policies:
  - `/bd/productPerformance/openApi/asinList`: 1 req/s, burst `1`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "search_field": {
      "type": "string"
    },
    "search_value": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "summary_field": {
      "type": "string"
    },
    "mid": {
      "type": "integer"
    },
    "currency_code": {
      "type": "string"
    },
    "is_recently_enum": {
      "type": "boolean"
    },
    "purchase_status": {
      "type": "integer"
    },
    "sort_field": {
      "type": "string"
    },
    "sort_type": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 69. `lingxing_source_all_orders`

- Description: 亚马逊源表所有订单。
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/allOrders，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/erp/sc/data/mws_report/allOrders`
- Docs path: `docs/SourceData/AllOrders.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `date_type`
- Endpoint policies:
  - `/erp/sc/data/mws_report/allOrders`: 10 req/s, burst `10`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "date_type": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 70. `lingxing_source_manage_inventory`

- Description: 亚马逊源表 FBA 库存。
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/manageInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/erp/sc/data/mws_report/manageInventory`
- Docs path: `docs/SourceData/ManageInventory.md`
- Required args: `sid`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/mws_report/manageInventory`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 71. `lingxing_source_daily_inventory`

- Description: 亚马逊源表每日库存。
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/dailyInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/erp/sc/data/mws_report/dailyInventory`
- Docs path: `docs/SourceData/DailyInventory.md`
- Required args: `sid`, `event_date`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/mws_report/dailyInventory`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "event_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "event_date"
  ],
  "additionalProperties": false
}
```

### 72. `lingxing_source_reserved_inventory`

- Description: 亚马逊源表预留库存。
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/reservedInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/erp/sc/data/mws_report/reservedInventory`
- Docs path: `docs/SourceData/ReservedInventory.md`
- Required args: `sid`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/mws_report/reservedInventory`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 73. `lingxing_source_transaction`

- Description: 亚马逊源表交易明细。
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/transaction，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoints: `/erp/sc/data/mws_report/transaction`
- Docs path: `docs/SourceData/Transaction.md`
- Required args: `sid`, `event_date`
- Optional args: -
- Endpoint policies:
  - `/erp/sc/data/mws_report/transaction`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "event_date": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "event_date"
  ],
  "additionalProperties": false
}
```

### 74. `lingxing_fba_stock_aggregate`

- Description: FBA 库存新报表汇总。
- Rate limit: 限流：endpoint /cost/center/openApi/fba/gather/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `stock`
- Endpoints: `/cost/center/openApi/fba/gather/query`
- Docs path: `docs/Statistics/FbaStockAggregateListNew.md`
- Required args: `sid`, `start_month`, `end_month`
- Optional args: -
- Endpoint policies:
  - `/cost/center/openApi/fba/gather/query`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_month": {
      "type": "string"
    },
    "end_month": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_month",
    "end_month"
  ],
  "additionalProperties": false
}
```

### 75. `lingxing_fba_stock_detail`

- Description: FBA 库存新报表明细。
- Rate limit: 限流：endpoint /cost/center/openApi/fba/detail/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `stock`
- Endpoints: `/cost/center/openApi/fba/detail/query`
- Docs path: `docs/Statistics/FbaStockDetailListNew.md`
- Required args: `sid`, `start_month`, `end_month`
- Optional args: -
- Endpoint policies:
  - `/cost/center/openApi/fba/detail/query`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_month": {
      "type": "string"
    },
    "end_month": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_month",
    "end_month"
  ],
  "additionalProperties": false
}
```

### 76. `lingxing_replenishment_summary`

- Description: 补货建议列表。
- Rate limit: 限流：endpoint /erp/sc/routing/restocking/analysis/getSummaryList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `replenishment_summary`
- Endpoints: `/erp/sc/routing/restocking/analysis/getSummaryList`
- Docs path: `docs/FBASug/GetSummaryList.md`
- Required args: `sid`
- Optional args: `asin`, `mode`
- Endpoint policies:
  - `/erp/sc/routing/restocking/analysis/getSummaryList`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "asin": {
      "type": "string"
    },
    "mode": {
      "type": "integer"
    }
  },
  "required": [
    "sid"
  ],
  "additionalProperties": false
}
```

### 77. `lingxing_replenishment_asin_info`

- Description: 补货建议 ASIN 明细。
- Rate limit: 限流：endpoint /erp/sc/routing/fbaSug/asin/getInfo，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `replenishment_info`
- Endpoints: `/erp/sc/routing/fbaSug/asin/getInfo`
- Docs path: `docs/FBASug/InfoASIN.md`
- Required args: `sid`, `asin`
- Optional args: `mode`
- Endpoint policies:
  - `/erp/sc/routing/fbaSug/asin/getInfo`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "asin": {
      "type": "string"
    },
    "mode": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "asin"
  ],
  "additionalProperties": false
}
```

### 78. `lingxing_exp_ads_sp_placement_report`

- Description: 实验层：SP 广告位日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/campaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/campaignPlacementReports`
- Docs path: `docs/newAd/report/campaignPlacementReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/campaignPlacementReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 79. `lingxing_exp_ads_sp_ad_group_report`

- Description: 实验层：SP 广告组日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/spAdGroupReports`
- Docs path: `docs/newAd/report/spAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/spAdGroupReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 80. `lingxing_exp_ads_sp_purchased_asin_report`

- Description: 实验层：SP 已购买 ASIN 报表。
- Rate limit: 限流：endpoint /pb/openapi/newad/asinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/asinReports`
- Docs path: `docs/newAd/report/asinReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/asinReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 81. `lingxing_exp_ads_sb_campaign_placement_report`

- Description: 实验层：SB 广告位日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/hsaCampaignPlacementReports`
- Docs path: `docs/newAd/report/hsaCampaignPlacementReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/hsaCampaignPlacementReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 82. `lingxing_exp_ads_sb_ad_group_report`

- Description: 实验层：SB 广告组日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/hsaAdGroupReports`
- Docs path: `docs/newAd/report/hsaAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/hsaAdGroupReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 83. `lingxing_exp_ads_sb_target_report`

- Description: 实验层：SB 投放日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaTargetingReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/listHsaTargetingReport`
- Docs path: `docs/newAd/report/listHsaTargetingReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/listHsaTargetingReport`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 84. `lingxing_exp_ads_sb_search_term_report`

- Description: 实验层：SB 用户搜索词日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaQueryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/hsaQueryWordReports`
- Docs path: `docs/newAd/report/hsaQueryWordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/hsaQueryWordReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 85. `lingxing_exp_ads_sb_keyword_placement_report`

- Description: 实验层：SB 关键词广告位日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaKeywordPlacementReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/listHsaKeywordPlacementReport`
- Docs path: `docs/newAd/report/listHsaKeywordPlacementReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/listHsaKeywordPlacementReport`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 86. `lingxing_exp_ads_sd_ad_group_report`

- Description: 实验层：SD 广告组日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdAdGroupReports`
- Docs path: `docs/newAd/report/sdAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdAdGroupReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 87. `lingxing_exp_ads_sd_match_target_report`

- Description: 实验层：SD 匹配目标日报。
- Rate limit: 限流：endpoint /pb/openapi/newad/sdMatchTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/sdMatchTargetReports`
- Docs path: `docs/newAd/report/sdMatchTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`
- Endpoint policies:
  - `/pb/openapi/newad/sdMatchTargetReports`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "report_date": {
      "type": "string"
    },
    "profile_id": {
      "type": "integer"
    },
    "show_detail": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "report_date"
  ],
  "additionalProperties": false
}
```

### 88. `lingxing_exp_ads_aba_report`

- Description: 实验层：ABA 搜索词周报下载信息。
- Rate limit: 限流：endpoint /pb/openapi/newad/abaReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoints: `/pb/openapi/newad/abaReport`
- Docs path: `docs/newAd/reportDownload/abaReport.md`
- Required args: `country`, `data_start_time`
- Optional args: -
- Endpoint policies:
  - `/pb/openapi/newad/abaReport`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "country": {
      "type": "string"
    },
    "data_start_time": {
      "type": "string"
    }
  },
  "required": [
    "country",
    "data_start_time"
  ],
  "additionalProperties": false
}
```

### 89. `lingxing_finance_report_asin`

- Description: 结算利润报表 ASIN 视角。
- Rate limit: 限流：endpoint /bd/profit/report/open/report/asin/list，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。
- Registered by: `endpoint_spec`
- Category: `profit_report`
- Endpoints: `/bd/profit/report/open/report/asin/list`
- Docs path: `docs/Finance/bdASIN.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`, `monthly_query`, `summary_enabled`, `order_status`
- Endpoint policies:
  - `/bd/profit/report/open/report/asin/list`: 10 req/s, burst `10`, source `openapi_docs`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "currency_code": {
      "type": "string"
    },
    "search_value": {
      "type": "string"
    },
    "monthly_query": {
      "type": "boolean"
    },
    "summary_enabled": {
      "type": "boolean"
    },
    "order_status": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 90. `lingxing_exp_finance_report_seller`

- Description: 实验层：结算利润报表店铺视角。
- Rate limit: 限流：endpoint /bd/profit/report/open/report/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Registered by: `endpoint_spec`
- Category: `profit_report`
- Endpoints: `/bd/profit/report/open/report/seller/list`
- Docs path: `docs/Finance/bdSeller.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `monthly_query`, `order_status`
- Endpoint policies:
  - `/bd/profit/report/open/report/seller/list`: 1 req/s, burst `1`, source `default`

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "currency_code": {
      "type": "string"
    },
    "monthly_query": {
      "type": "boolean"
    },
    "order_status": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```
