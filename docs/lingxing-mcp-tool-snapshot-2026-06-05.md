# Lingxing MCP Tool Snapshot

- Generated at: `2026-06-05 18:15:09`
- Source: `LingxingMCPApplication.list_tools()`
- Tool count: `89`

## 当前生产最小 allowlist

- `lingxing_health_check`
- `lingxing_seller_lists`
- `lingxing_marketplaces`
- `lingxing_order_details`
- `lingxing_asin_product_snapshot`
- `lingxing_fba_warehouse_detail`
- `lingxing_local_product_costs`
- `lingxing_product_performance`
- `lingxing_finance_report_asin`

## 工具总览

| # | Tool | Registered by | Category | Required args | Optional args | Endpoint | Description |
|---:|---|---|---|---|---|---|---|
| 1 | `lingxing_health_check` | `manual` | `manual` | - | - | - | 检查领星环境变量、token 状态和基础连通性，不拉业务数据。 |
| 2 | `lingxing_seller_lists` | `manual` | `manual` | - | `status`, `marketplace` | - | 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。 |
| 3 | `lingxing_marketplaces` | `manual` | `manual` | - | - | - | 返回领星市场列表，并补充站点时区映射。 |
| 4 | `lingxing_store_sales` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | - | 按店铺和日期范围拉取 StoreSales，并自动合并分页。 |
| 5 | `lingxing_asin_daily_lists` | `manual` | `manual` | `sid`, `event_date`, `metric_type` | `asin_type` | - | 按店铺、日期和指标类型拉取 AsinDailyLists。 |
| 6 | `lingxing_order_lists` | `manual` | `manual` | `sid`, `start_date`, `end_date` | `date_type` | - | 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。 |
| 7 | `lingxing_order_details` | `manual` | `manual` | - | `order_id`, `order_ids` | - | 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。 |
| 8 | `lingxing_promotion_listing` | `manual` | `manual` | `sid`, `site_date`, `start_time`, `end_time` | `status`, `product_status`, `promotion_category` | - | 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。 |
| 9 | `lingxing_promotion_sec_kill` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | - | 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。 |
| 10 | `lingxing_promotion_manage` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | - | 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。 |
| 11 | `lingxing_promotion_vip_discount` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | - | 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。 |
| 12 | `lingxing_promotion_coupon` | `manual` | `manual` | `sid`, `start_date`, `end_date` | - | - | 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。 |
| 13 | `lingxing_resolve_daily_promotions` | `manual` | `manual` | `sid`, `target_date` | `lookback_days` | - | 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。 |
| 14 | `lingxing_asin_product_snapshot` | `manual` | `manual` | `sid`, `asin` | `start_date`, `end_date` | - | 按店铺 sid 和 ASIN 查询产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。 |
| 15 | `lingxing_local_product_costs` | `manual` | `manual` | - | `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`, `page_size`, `include_supplier_quotes`, `include_raw` | - | 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。 |
| 16 | `lingxing_smoke_check` | `manual` | `manual` | - | `sid`, `date` | - | 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。 |
| 17 | `lingxing_ad_accounts` | `manual` | `manual` | - | `type`, `sid`, `profile_id`, `country_code`, `status` | - | 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。 |
| 18 | `lingxing_report_export_create` | `manual` | `manual` | `sid`, `report_type` | `data_start_time`, `data_end_time`, `marketplace_ids`, `region`, `seller_id` | - | 创建亚马逊报告导出任务。 |
| 19 | `lingxing_report_export_query` | `manual` | `manual` | `task_id` | `sid`, `region`, `seller_id` | - | 查询亚马逊报告导出任务结果。 |
| 20 | `lingxing_report_export_refresh_url` | `manual` | `manual` | `report_document_id` | `sid`, `region`, `seller_id` | - | 续期亚马逊报告下载链接。 |
| 21 | `lingxing_report_export_download` | `manual` | `manual` | - | `url`, `sid`, `task_id`, `report_document_id`, `region`, `seller_id` | - | 下载并解析亚马逊报告导出文件。 |
| 22 | `lingxing_asin_ads_daily_rollup` | `manual` | `manual` | `sid`, `asin`, `start_date`, `end_date` | `attribution_policy` | - | 按 ASIN 汇总每日广告指标，采用 balanced 归因。 |
| 23 | `lingxing_asin_weekly_rollup` | `manual` | `manual` | `sid`, `asin`, `start_date`, `end_date` | - | - | 按周汇总 ASIN 的总销量、广告指标和促销标签。 |
| 24 | `lingxing_ads_sp_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spCampaignReports` | SP 广告活动日报。 |
| 25 | `lingxing_ads_sp_product_ad_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spProductAdReports` | SP 广告商品日报，可直接按 ASIN 聚合。 |
| 26 | `lingxing_ads_sp_keyword_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spKeywordReports` | SP 关键词日报。 |
| 27 | `lingxing_ads_sp_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spTargetReports` | SP 商品定位日报。 |
| 28 | `lingxing_ads_sp_search_term_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail`, `target_type` | `/pb/openapi/newad/queryWordReports` | SP 用户搜索词日报。 |
| 29 | `lingxing_ads_sd_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdCampaignReports` | SD 广告活动日报。 |
| 30 | `lingxing_ads_sd_product_ad_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdProductAdReports` | SD 广告商品日报，可直接按 ASIN 聚合。 |
| 31 | `lingxing_ads_sd_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdTargetReports` | SD 商品定位日报。 |
| 32 | `lingxing_ads_sb_campaign_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaCampaignReports` | SB 广告活动日报。 |
| 33 | `lingxing_ads_sb_creative_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaProductAdReport` | SB 广告创意日报。 |
| 34 | `lingxing_ads_sb_purchased_asin_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id` | `/pb/openapi/newad/hsaPurchasedAsinReports` | SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。 |
| 35 | `lingxing_ads_sp_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spCampaignHourData` | SP 广告活动小时数据。 |
| 36 | `lingxing_ads_sp_placement_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdPlacementHourData` | SP 广告位小时数据。 |
| 37 | `lingxing_ads_sp_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdGroupHourData` | SP 广告组小时数据。 |
| 38 | `lingxing_ads_sp_advertise_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdvertiseHourData` | SP 广告小时数据。 |
| 39 | `lingxing_ads_sp_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spTargetHourData` | SP 投放小时数据。 |
| 40 | `lingxing_ads_sb_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbCampaignHourData` | SB 广告活动小时数据。 |
| 41 | `lingxing_ads_sb_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbAdGroupHourData` | SB 广告组小时数据。 |
| 42 | `lingxing_ads_sb_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbTargetHourData` | SB 投放小时数据。 |
| 43 | `lingxing_ads_sb_placement_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sbAdPlacementHourData` | SB 广告位小时数据。 |
| 44 | `lingxing_ads_sd_campaign_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdCampaignHourData` | SD 广告活动小时数据。 |
| 45 | `lingxing_ads_sd_ad_group_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdGroupHourData` | SD 广告组小时数据。 |
| 46 | `lingxing_ads_sd_advertise_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdvertiseHourData` | SD 广告小时数据。 |
| 47 | `lingxing_ads_sd_target_hourly` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdTargetHourData` | SD 投放小时数据。 |
| 48 | `lingxing_ads_portfolios` | `endpoint_spec` | `ad_base` | `sid` | `profile_id` | `/pb/openapi/newad/portfolios` | 广告组合列表。 |
| 49 | `lingxing_ads_sp_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spCampaigns` | SP 广告活动基础数据。 |
| 50 | `lingxing_ads_sp_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spAdGroups` | SP 广告组基础数据。 |
| 51 | `lingxing_ads_sp_product_ads` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spProductAds` | SP 广告商品基础数据。 |
| 52 | `lingxing_ads_sp_keywords` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spKeywords` | SP 关键词基础数据。 |
| 53 | `lingxing_ads_sp_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/spTargets` | SP 商品定位基础数据。 |
| 54 | `lingxing_ads_sd_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdCampaigns` | SD 广告活动基础数据。 |
| 55 | `lingxing_ads_sd_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdAdGroups` | SD 广告组基础数据。 |
| 56 | `lingxing_ads_sd_product_ads` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdProductAds` | SD 广告商品基础数据。 |
| 57 | `lingxing_ads_sd_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sdTargets` | SD 商品定位基础数据。 |
| 58 | `lingxing_ads_sb_campaigns` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/hsaCampaigns` | SB 广告活动基础数据。 |
| 59 | `lingxing_ads_sb_ad_groups` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/hsaAdGroups` | SB 广告组基础数据。 |
| 60 | `lingxing_ads_sb_creatives` | `endpoint_spec` | `ad_base` | `sid` | `profile_id` | `/pb/openapi/newad/hsaProductAds` | SB 广告创意基础数据。 |
| 61 | `lingxing_ads_sb_targets` | `endpoint_spec` | `ad_base` | `sid` | `profile_id`, `state` | `/pb/openapi/newad/sbTargeting` | SB 投放基础数据。 |
| 62 | `lingxing_profit_seller` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value`, `monthly_query` | `/bd/profit/statistics/open/seller/list` | 店铺维度利润统计。 |
| 63 | `lingxing_profit_asin` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value` | `/bd/profit/statistics/open/asin/list` | ASIN 维度利润统计。 |
| 64 | `lingxing_profit_parent_asin` | `endpoint_spec` | `profit` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value` | `/bd/profit/statistics/open/parent/asin/list` | 父 ASIN 维度利润统计。 |
| 65 | `lingxing_fba_warehouse_detail` | `endpoint_spec` | `warehouse` | `sid` | `search_field`, `search_value`, `cid`, `bid`, `attribute`, `asin_principal`, `status`, `senior_search_list`, `fulfillment_channel_type`, `is_hide_zero_stock`, `is_parant_asin_merge`, `is_contain_del_ls`, `query_fba_storage_quantity_list` | `/basicOpen/openapi/storage/fbaWarehouseDetail` | 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。 |
| 66 | `lingxing_local_products` | `endpoint_spec` | `product` | - | `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end` | `/erp/sc/routing/data/local_inventory/productList` | 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。 |
| 67 | `lingxing_product_performance` | `endpoint_spec` | `source` | `sid`, `start_date`, `end_date` | `search_field`, `search_value`, `summary_field`, `mid`, `currency_code`, `is_recently_enum`, `purchase_status`, `sort_field`, `sort_type` | `/bd/productPerformance/openApi/asinList` | 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。 |
| 68 | `lingxing_source_all_orders` | `endpoint_spec` | `source` | `sid`, `start_date`, `end_date` | `date_type` | `/erp/sc/data/mws_report/allOrders` | 亚马逊源表所有订单。 |
| 69 | `lingxing_source_manage_inventory` | `endpoint_spec` | `source` | `sid` | - | `/erp/sc/data/mws_report/manageInventory` | 亚马逊源表 FBA 库存。 |
| 70 | `lingxing_source_daily_inventory` | `endpoint_spec` | `source` | `sid`, `event_date` | - | `/erp/sc/data/mws_report/dailyInventory` | 亚马逊源表每日库存。 |
| 71 | `lingxing_source_reserved_inventory` | `endpoint_spec` | `source` | `sid` | - | `/erp/sc/data/mws_report/reservedInventory` | 亚马逊源表预留库存。 |
| 72 | `lingxing_source_transaction` | `endpoint_spec` | `source` | `sid`, `event_date` | - | `/erp/sc/data/mws_report/transaction` | 亚马逊源表交易明细。 |
| 73 | `lingxing_fba_stock_aggregate` | `endpoint_spec` | `stock` | `sid`, `start_month`, `end_month` | - | `/cost/center/openApi/fba/gather/query` | FBA 库存新报表汇总。 |
| 74 | `lingxing_fba_stock_detail` | `endpoint_spec` | `stock` | `sid`, `start_month`, `end_month` | - | `/cost/center/openApi/fba/detail/query` | FBA 库存新报表明细。 |
| 75 | `lingxing_replenishment_summary` | `endpoint_spec` | `replenishment_summary` | `sid` | `asin`, `mode` | `/erp/sc/routing/restocking/analysis/getSummaryList` | 补货建议列表。 |
| 76 | `lingxing_replenishment_asin_info` | `endpoint_spec` | `replenishment_info` | `sid`, `asin` | `mode` | `/erp/sc/routing/fbaSug/asin/getInfo` | 补货建议 ASIN 明细。 |
| 77 | `lingxing_exp_ads_sp_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/campaignPlacementReports` | 实验层：SP 广告位日报。 |
| 78 | `lingxing_exp_ads_sp_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/spAdGroupReports` | 实验层：SP 广告组日报。 |
| 79 | `lingxing_exp_ads_sp_purchased_asin_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/asinReports` | 实验层：SP 已购买 ASIN 报表。 |
| 80 | `lingxing_exp_ads_sb_campaign_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaCampaignPlacementReports` | 实验层：SB 广告位日报。 |
| 81 | `lingxing_exp_ads_sb_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaAdGroupReports` | 实验层：SB 广告组日报。 |
| 82 | `lingxing_exp_ads_sb_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaTargetingReport` | 实验层：SB 投放日报。 |
| 83 | `lingxing_exp_ads_sb_search_term_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/hsaQueryWordReports` | 实验层：SB 用户搜索词日报。 |
| 84 | `lingxing_exp_ads_sb_keyword_placement_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/listHsaKeywordPlacementReport` | 实验层：SB 关键词广告位日报。 |
| 85 | `lingxing_exp_ads_sd_ad_group_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdAdGroupReports` | 实验层：SD 广告组日报。 |
| 86 | `lingxing_exp_ads_sd_match_target_report` | `endpoint_spec` | `ad_report` | `sid`, `report_date` | `profile_id`, `show_detail` | `/pb/openapi/newad/sdMatchTargetReports` | 实验层：SD 匹配目标日报。 |
| 87 | `lingxing_exp_ads_aba_report` | `endpoint_spec` | `ad_report` | `country`, `data_start_time` | - | `/pb/openapi/newad/abaReport` | 实验层：ABA 搜索词周报下载信息。 |
| 88 | `lingxing_finance_report_asin` | `endpoint_spec` | `profit_report` | `sid`, `start_date`, `end_date` | `currency_code`, `search_value`, `monthly_query`, `summary_enabled`, `order_status` | `/bd/profit/report/open/report/asin/list` | 结算利润报表 ASIN 视角。 |
| 89 | `lingxing_exp_finance_report_seller` | `endpoint_spec` | `profit_report` | `sid`, `start_date`, `end_date` | `currency_code`, `monthly_query`, `order_status` | `/bd/profit/report/open/report/seller/list` | 实验层：结算利润报表店铺视角。 |

## 工具详情

### 1. `lingxing_health_check`

- Description: 检查领星环境变量、token 状态和基础连通性，不拉业务数据。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: -

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 2. `lingxing_seller_lists`

- Description: 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `status`, `marketplace`

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

### 3. `lingxing_marketplaces`

- Description: 返回领星市场列表，并补充站点时区映射。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: -

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 4. `lingxing_store_sales`

- Description: 按店铺和日期范围拉取 StoreSales，并自动合并分页。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -

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

### 5. `lingxing_asin_daily_lists`

- Description: 按店铺、日期和指标类型拉取 AsinDailyLists。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `event_date`, `metric_type`
- Optional args: `asin_type`

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

### 6. `lingxing_order_lists`

- Description: 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `date_type`

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

### 7. `lingxing_order_details`

- Description: 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `order_id`, `order_ids`

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

### 8. `lingxing_promotion_listing`

- Description: 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `site_date`, `start_time`, `end_time`
- Optional args: `status`, `product_status`, `promotion_category`

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

### 9. `lingxing_promotion_sec_kill`

- Description: 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -

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

### 10. `lingxing_promotion_manage`

- Description: 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -

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

### 11. `lingxing_promotion_vip_discount`

- Description: 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -

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

### 12. `lingxing_promotion_coupon`

- Description: 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `start_date`, `end_date`
- Optional args: -

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

### 13. `lingxing_resolve_daily_promotions`

- Description: 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `target_date`
- Optional args: `lookback_days`

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

### 14. `lingxing_asin_product_snapshot`

- Output notes: sales.volume 是产品表现销量/销售件数，来源 productPerformance.volume。快照工具暂不输出 FBA/FBM 订单数量；订单类分析请单独使用订单相关工具并按业务口径过滤。

- Description: 按店铺 sid 和 ASIN 查询产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `asin`
- Optional args: `start_date`, `end_date`

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

### 15. `lingxing_local_product_costs`

- Description: 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`, `page_size`, `include_supplier_quotes`, `include_raw`

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

### 16. `lingxing_smoke_check`

- Description: 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `sid`, `date`

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

### 17. `lingxing_ad_accounts`

- Description: 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `type`, `sid`, `profile_id`, `country_code`, `status`

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

### 18. `lingxing_report_export_create`

- Description: 创建亚马逊报告导出任务。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `report_type`
- Optional args: `data_start_time`, `data_end_time`, `marketplace_ids`, `region`, `seller_id`

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

### 19. `lingxing_report_export_query`

- Description: 查询亚马逊报告导出任务结果。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `task_id`
- Optional args: `sid`, `region`, `seller_id`

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

### 20. `lingxing_report_export_refresh_url`

- Description: 续期亚马逊报告下载链接。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `report_document_id`
- Optional args: `sid`, `region`, `seller_id`

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

### 21. `lingxing_report_export_download`

- Description: 下载并解析亚马逊报告导出文件。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: -
- Optional args: `url`, `sid`, `task_id`, `report_document_id`, `region`, `seller_id`

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

### 22. `lingxing_asin_ads_daily_rollup`

- Description: 按 ASIN 汇总每日广告指标，采用 balanced 归因。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `asin`, `start_date`, `end_date`
- Optional args: `attribution_policy`

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

### 23. `lingxing_asin_weekly_rollup`

- Description: 按周汇总 ASIN 的总销量、广告指标和促销标签。
- Registered by: `manual`
- Category: `manual`
- Endpoint: -
- Docs path: -
- Required args: `sid`, `asin`, `start_date`, `end_date`
- Optional args: -

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

### 24. `lingxing_ads_sp_campaign_report`

- Description: SP 广告活动日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spCampaignReports`
- Docs path: `docs/newAd/report/spCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 25. `lingxing_ads_sp_product_ad_report`

- Description: SP 广告商品日报，可直接按 ASIN 聚合。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spProductAdReports`
- Docs path: `docs/newAd/report/spProductAdReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 26. `lingxing_ads_sp_keyword_report`

- Description: SP 关键词日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spKeywordReports`
- Docs path: `docs/newAd/report/spKeywordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 27. `lingxing_ads_sp_target_report`

- Description: SP 商品定位日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spTargetReports`
- Docs path: `docs/newAd/report/spTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 28. `lingxing_ads_sp_search_term_report`

- Description: SP 用户搜索词日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/queryWordReports`
- Docs path: `docs/newAd/report/queryWordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`, `target_type`

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

### 29. `lingxing_ads_sd_campaign_report`

- Description: SD 广告活动日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdCampaignReports`
- Docs path: `docs/newAd/report/sdCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 30. `lingxing_ads_sd_product_ad_report`

- Description: SD 广告商品日报，可直接按 ASIN 聚合。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdProductAdReports`
- Docs path: `docs/newAd/report/sdProductAdReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 31. `lingxing_ads_sd_target_report`

- Description: SD 商品定位日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdTargetReports`
- Docs path: `docs/newAd/report/sdTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 32. `lingxing_ads_sb_campaign_report`

- Description: SB 广告活动日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/hsaCampaignReports`
- Docs path: `docs/newAd/report/hsaCampaignReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 33. `lingxing_ads_sb_creative_report`

- Description: SB 广告创意日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/listHsaProductAdReport`
- Docs path: `docs/newAd/report/listHsaProductAdReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 34. `lingxing_ads_sb_purchased_asin_report`

- Description: SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/hsaPurchasedAsinReports`
- Docs path: `docs/newAd/report/hsaPurchasedAsinReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`

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

### 35. `lingxing_ads_sp_campaign_hourly`

- Description: SP 广告活动小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spCampaignHourData`
- Docs path: `docs/newAd/report/spCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 36. `lingxing_ads_sp_placement_hourly`

- Description: SP 广告位小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spAdPlacementHourData`
- Docs path: `docs/newAd/report/spAdPlacementHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 37. `lingxing_ads_sp_ad_group_hourly`

- Description: SP 广告组小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spAdGroupHourData`
- Docs path: `docs/newAd/report/spAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 38. `lingxing_ads_sp_advertise_hourly`

- Description: SP 广告小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spAdvertiseHourData`
- Docs path: `docs/newAd/report/spAdvertiseHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 39. `lingxing_ads_sp_target_hourly`

- Description: SP 投放小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spTargetHourData`
- Docs path: `docs/newAd/report/spTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 40. `lingxing_ads_sb_campaign_hourly`

- Description: SB 广告活动小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sbCampaignHourData`
- Docs path: `docs/newAd/report/sbCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 41. `lingxing_ads_sb_ad_group_hourly`

- Description: SB 广告组小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sbAdGroupHourData`
- Docs path: `docs/newAd/report/sbAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 42. `lingxing_ads_sb_target_hourly`

- Description: SB 投放小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sbTargetHourData`
- Docs path: `docs/newAd/report/sbTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 43. `lingxing_ads_sb_placement_hourly`

- Description: SB 广告位小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sbAdPlacementHourData`
- Docs path: `docs/newAd/report/sbAdPlacementHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 44. `lingxing_ads_sd_campaign_hourly`

- Description: SD 广告活动小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdCampaignHourData`
- Docs path: `docs/newAd/report/sdCampaignHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 45. `lingxing_ads_sd_ad_group_hourly`

- Description: SD 广告组小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdAdGroupHourData`
- Docs path: `docs/newAd/report/sdAdGroupHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 46. `lingxing_ads_sd_advertise_hourly`

- Description: SD 广告小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdAdvertiseHourData`
- Docs path: `docs/newAd/report/sdAdvertiseHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 47. `lingxing_ads_sd_target_hourly`

- Description: SD 投放小时数据。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdTargetHourData`
- Docs path: `docs/newAd/report/sdTargetHourData.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 48. `lingxing_ads_portfolios`

- Description: 广告组合列表。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/portfolios`
- Docs path: `docs/newAd/baseData/portfolios.md`
- Required args: `sid`
- Optional args: `profile_id`

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

### 49. `lingxing_ads_sp_campaigns`

- Description: SP 广告活动基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/spCampaigns`
- Docs path: `docs/newAd/baseData/spCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 50. `lingxing_ads_sp_ad_groups`

- Description: SP 广告组基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/spAdGroups`
- Docs path: `docs/newAd/baseData/spAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 51. `lingxing_ads_sp_product_ads`

- Description: SP 广告商品基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/spProductAds`
- Docs path: `docs/newAd/baseData/spProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 52. `lingxing_ads_sp_keywords`

- Description: SP 关键词基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/spKeywords`
- Docs path: `docs/newAd/baseData/spKeywords.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 53. `lingxing_ads_sp_targets`

- Description: SP 商品定位基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/spTargets`
- Docs path: `docs/newAd/baseData/spTargets.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 54. `lingxing_ads_sd_campaigns`

- Description: SD 广告活动基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/sdCampaigns`
- Docs path: `docs/newAd/baseData/sdCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 55. `lingxing_ads_sd_ad_groups`

- Description: SD 广告组基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/sdAdGroups`
- Docs path: `docs/newAd/baseData/sdAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 56. `lingxing_ads_sd_product_ads`

- Description: SD 广告商品基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/sdProductAds`
- Docs path: `docs/newAd/baseData/sdProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 57. `lingxing_ads_sd_targets`

- Description: SD 商品定位基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/sdTargets`
- Docs path: `docs/newAd/baseData/sdTargets.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 58. `lingxing_ads_sb_campaigns`

- Description: SB 广告活动基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/hsaCampaigns`
- Docs path: `docs/newAd/baseData/hsaCampaigns.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 59. `lingxing_ads_sb_ad_groups`

- Description: SB 广告组基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/hsaAdGroups`
- Docs path: `docs/newAd/baseData/hsaAdGroups.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 60. `lingxing_ads_sb_creatives`

- Description: SB 广告创意基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/hsaProductAds`
- Docs path: `docs/newAd/baseData/sbAdHasProductAds.md`
- Required args: `sid`
- Optional args: `profile_id`

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

### 61. `lingxing_ads_sb_targets`

- Description: SB 投放基础数据。
- Registered by: `endpoint_spec`
- Category: `ad_base`
- Endpoint: `/pb/openapi/newad/sbTargeting`
- Docs path: `docs/newAd/baseData/sbTargeting.md`
- Required args: `sid`
- Optional args: `profile_id`, `state`

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

### 62. `lingxing_profit_seller`

- Description: 店铺维度利润统计。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoint: `/bd/profit/statistics/open/seller/list`
- Docs path: `docs/Statistics/statisticsOpenSeller.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`, `monthly_query`

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

### 63. `lingxing_profit_asin`

- Description: ASIN 维度利润统计。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoint: `/bd/profit/statistics/open/asin/list`
- Docs path: `docs/Statistics/statisticsOpenASIN.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`

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

### 64. `lingxing_profit_parent_asin`

- Description: 父 ASIN 维度利润统计。
- Registered by: `endpoint_spec`
- Category: `profit`
- Endpoint: `/bd/profit/statistics/open/parent/asin/list`
- Docs path: `docs/Statistics/statisticsOpenParent.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`

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

### 65. `lingxing_fba_warehouse_detail`

- Description: 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。
- Registered by: `endpoint_spec`
- Category: `warehouse`
- Endpoint: `/basicOpen/openapi/storage/fbaWarehouseDetail`
- Docs path: `docs/Warehouse/FBAStock_v2.md`
- Required args: `sid`
- Optional args: `search_field`, `search_value`, `cid`, `bid`, `attribute`, `asin_principal`, `status`, `senior_search_list`, `fulfillment_channel_type`, `is_hide_zero_stock`, `is_parant_asin_merge`, `is_contain_del_ls`, `query_fba_storage_quantity_list`

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

### 66. `lingxing_local_products`

- Description: 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。
- Registered by: `endpoint_spec`
- Category: `product`
- Endpoint: `/erp/sc/routing/data/local_inventory/productList`
- Docs path: `docs/Product/ProductLists.md`
- Required args: -
- Optional args: `sku_list`, `sku_identifier_list`, `update_time_start`, `update_time_end`, `create_time_start`, `create_time_end`

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

### 67. `lingxing_product_performance`

- Description: 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/bd/productPerformance/openApi/asinList`
- Docs path: `docs/Statistics/AsinListNew.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `search_field`, `search_value`, `summary_field`, `mid`, `currency_code`, `is_recently_enum`, `purchase_status`, `sort_field`, `sort_type`

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

### 68. `lingxing_source_all_orders`

- Description: 亚马逊源表所有订单。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/erp/sc/data/mws_report/allOrders`
- Docs path: `docs/SourceData/AllOrders.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `date_type`

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

### 69. `lingxing_source_manage_inventory`

- Description: 亚马逊源表 FBA 库存。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/erp/sc/data/mws_report/manageInventory`
- Docs path: `docs/SourceData/ManageInventory.md`
- Required args: `sid`
- Optional args: -

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

### 70. `lingxing_source_daily_inventory`

- Description: 亚马逊源表每日库存。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/erp/sc/data/mws_report/dailyInventory`
- Docs path: `docs/SourceData/DailyInventory.md`
- Required args: `sid`, `event_date`
- Optional args: -

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

### 71. `lingxing_source_reserved_inventory`

- Description: 亚马逊源表预留库存。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/erp/sc/data/mws_report/reservedInventory`
- Docs path: `docs/SourceData/ReservedInventory.md`
- Required args: `sid`
- Optional args: -

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

### 72. `lingxing_source_transaction`

- Description: 亚马逊源表交易明细。
- Registered by: `endpoint_spec`
- Category: `source`
- Endpoint: `/erp/sc/data/mws_report/transaction`
- Docs path: `docs/SourceData/Transaction.md`
- Required args: `sid`, `event_date`
- Optional args: -

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

### 73. `lingxing_fba_stock_aggregate`

- Description: FBA 库存新报表汇总。
- Registered by: `endpoint_spec`
- Category: `stock`
- Endpoint: `/cost/center/openApi/fba/gather/query`
- Docs path: `docs/Statistics/FbaStockAggregateListNew.md`
- Required args: `sid`, `start_month`, `end_month`
- Optional args: -

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

### 74. `lingxing_fba_stock_detail`

- Description: FBA 库存新报表明细。
- Registered by: `endpoint_spec`
- Category: `stock`
- Endpoint: `/cost/center/openApi/fba/detail/query`
- Docs path: `docs/Statistics/FbaStockDetailListNew.md`
- Required args: `sid`, `start_month`, `end_month`
- Optional args: -

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

### 75. `lingxing_replenishment_summary`

- Description: 补货建议列表。
- Registered by: `endpoint_spec`
- Category: `replenishment_summary`
- Endpoint: `/erp/sc/routing/restocking/analysis/getSummaryList`
- Docs path: `docs/FBASug/GetSummaryList.md`
- Required args: `sid`
- Optional args: `asin`, `mode`

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

### 76. `lingxing_replenishment_asin_info`

- Description: 补货建议 ASIN 明细。
- Registered by: `endpoint_spec`
- Category: `replenishment_info`
- Endpoint: `/erp/sc/routing/fbaSug/asin/getInfo`
- Docs path: `docs/FBASug/InfoASIN.md`
- Required args: `sid`, `asin`
- Optional args: `mode`

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

### 77. `lingxing_exp_ads_sp_placement_report`

- Description: 实验层：SP 广告位日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/campaignPlacementReports`
- Docs path: `docs/newAd/report/campaignPlacementReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 78. `lingxing_exp_ads_sp_ad_group_report`

- Description: 实验层：SP 广告组日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/spAdGroupReports`
- Docs path: `docs/newAd/report/spAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 79. `lingxing_exp_ads_sp_purchased_asin_report`

- Description: 实验层：SP 已购买 ASIN 报表。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/asinReports`
- Docs path: `docs/newAd/report/asinReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 80. `lingxing_exp_ads_sb_campaign_placement_report`

- Description: 实验层：SB 广告位日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/hsaCampaignPlacementReports`
- Docs path: `docs/newAd/report/hsaCampaignPlacementReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 81. `lingxing_exp_ads_sb_ad_group_report`

- Description: 实验层：SB 广告组日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/hsaAdGroupReports`
- Docs path: `docs/newAd/report/hsaAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 82. `lingxing_exp_ads_sb_target_report`

- Description: 实验层：SB 投放日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/listHsaTargetingReport`
- Docs path: `docs/newAd/report/listHsaTargetingReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 83. `lingxing_exp_ads_sb_search_term_report`

- Description: 实验层：SB 用户搜索词日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/hsaQueryWordReports`
- Docs path: `docs/newAd/report/hsaQueryWordReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 84. `lingxing_exp_ads_sb_keyword_placement_report`

- Description: 实验层：SB 关键词广告位日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/listHsaKeywordPlacementReport`
- Docs path: `docs/newAd/report/listHsaKeywordPlacementReport.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 85. `lingxing_exp_ads_sd_ad_group_report`

- Description: 实验层：SD 广告组日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdAdGroupReports`
- Docs path: `docs/newAd/report/sdAdGroupReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 86. `lingxing_exp_ads_sd_match_target_report`

- Description: 实验层：SD 匹配目标日报。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/sdMatchTargetReports`
- Docs path: `docs/newAd/report/sdMatchTargetReports.md`
- Required args: `sid`, `report_date`
- Optional args: `profile_id`, `show_detail`

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

### 87. `lingxing_exp_ads_aba_report`

- Description: 实验层：ABA 搜索词周报下载信息。
- Registered by: `endpoint_spec`
- Category: `ad_report`
- Endpoint: `/pb/openapi/newad/abaReport`
- Docs path: `docs/newAd/reportDownload/abaReport.md`
- Required args: `country`, `data_start_time`
- Optional args: -

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

### 88. `lingxing_finance_report_asin`

- Description: 结算利润报表 ASIN 视角。
- Registered by: `endpoint_spec`
- Category: `profit_report`
- Endpoint: `/bd/profit/report/open/report/asin/list`
- Docs path: `docs/Finance/bdASIN.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `search_value`, `monthly_query`, `summary_enabled`, `order_status`

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

### 89. `lingxing_exp_finance_report_seller`

- Description: 实验层：结算利润报表店铺视角。
- Registered by: `endpoint_spec`
- Category: `profit_report`
- Endpoint: `/bd/profit/report/open/report/seller/list`
- Docs path: `docs/Finance/bdSeller.md`
- Required args: `sid`, `start_date`, `end_date`
- Optional args: `currency_code`, `monthly_query`, `order_status`

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
