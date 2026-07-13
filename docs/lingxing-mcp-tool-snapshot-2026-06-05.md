# Lingxing MCP Tool Snapshot

Generated: 2026-07-13 23:32:28
Source: LingxingMCPApplication built-in role defaults
Registered tools: 112

## Role Allowlists

### finance (22)

- `lingxing_exp_finance_report_seller`
- `lingxing_fba_stock_aggregate`
- `lingxing_fba_stock_detail`
- `lingxing_fba_warehouse_detail`
- `lingxing_finance_report_asin`
- `lingxing_health_check`
- `lingxing_local_product_costs`
- `lingxing_order_details`
- `lingxing_profit_asin`
- `lingxing_profit_report_order_list`
- `lingxing_profit_seller`
- `lingxing_rate_limit_policy`
- `lingxing_report_export_create`
- `lingxing_report_export_download`
- `lingxing_report_export_query`
- `lingxing_report_export_refresh_url`
- `lingxing_sales_outbound_orders`
- `lingxing_seller_lists`
- `lingxing_shipment_settlement_report`
- `lingxing_smoke_check`
- `lingxing_source_transaction`
- `lingxing_store_sales`

### minimal (13)

- `lingxing_amazon_listing`
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

### operations (75)

- `lingxing_ad_accounts`
- `lingxing_ads_add_sp_keywords`
- `lingxing_ads_add_sp_negative_keywords`
- `lingxing_ads_add_sp_negative_targets`
- `lingxing_ads_archive_sp_negatives`
- `lingxing_ads_operation_logs`
- `lingxing_ads_portfolios`
- `lingxing_ads_sb_ad_groups`
- `lingxing_ads_sb_campaign_report`
- `lingxing_ads_sb_campaigns`
- `lingxing_ads_sb_creative_report`
- `lingxing_ads_sb_creatives`
- `lingxing_ads_sb_negative_keywords`
- `lingxing_ads_sb_negative_targets`
- `lingxing_ads_sb_purchased_asin_report`
- `lingxing_ads_sb_targets`
- `lingxing_ads_sd_ad_groups`
- `lingxing_ads_sd_campaign_report`
- `lingxing_ads_sd_campaigns`
- `lingxing_ads_sd_negative_targets`
- `lingxing_ads_sd_product_ad_report`
- `lingxing_ads_sd_product_ads`
- `lingxing_ads_sd_target_report`
- `lingxing_ads_sd_targets`
- `lingxing_ads_sp_ad_groups`
- `lingxing_ads_sp_campaign_report`
- `lingxing_ads_sp_campaigns`
- `lingxing_ads_sp_keyword_report`
- `lingxing_ads_sp_keywords`
- `lingxing_ads_sp_negative_targets_or_keywords`
- `lingxing_ads_sp_product_ad_report`
- `lingxing_ads_sp_product_ads`
- `lingxing_ads_sp_search_term_report`
- `lingxing_ads_sp_target_report`
- `lingxing_ads_sp_targets`
- `lingxing_ads_update_sp_ad_group`
- `lingxing_ads_update_sp_campaign`
- `lingxing_ads_update_sp_keyword`
- `lingxing_ads_update_sp_product_ads`
- `lingxing_ads_update_sp_target`
- `lingxing_amazon_listing`
- `lingxing_asin_ads_daily_rollup`
- `lingxing_asin_product_snapshot`
- `lingxing_exp_ads_sb_ad_group_report`
- `lingxing_exp_ads_sb_campaign_placement_report`
- `lingxing_exp_ads_sb_keyword_placement_report`
- `lingxing_exp_ads_sb_search_term_report`
- `lingxing_exp_ads_sb_target_report`
- `lingxing_exp_ads_sd_ad_group_report`
- `lingxing_exp_ads_sd_match_target_report`
- `lingxing_exp_ads_sp_ad_group_report`
- `lingxing_exp_ads_sp_placement_report`
- `lingxing_exp_ads_sp_purchased_asin_report`
- `lingxing_fba_warehouse_detail`
- `lingxing_health_check`
- `lingxing_local_product_costs`
- `lingxing_marketplaces`
- `lingxing_multi_channel_orders`
- `lingxing_order_details`
- `lingxing_order_lists`
- `lingxing_product_performance`
- `lingxing_profit_report_order_list`
- `lingxing_rate_limit_policy`
- `lingxing_refund_orders`
- `lingxing_report_export_create`
- `lingxing_report_export_download`
- `lingxing_report_export_query`
- `lingxing_report_export_refresh_url`
- `lingxing_return_analysis`
- `lingxing_sales_outbound_orders`
- `lingxing_seller_lists`
- `lingxing_shipment_settlement_report`
- `lingxing_smoke_check`
- `lingxing_source_transaction`
- `lingxing_voice_of_buyer`

## Tool Index

| # | Tool | Origin | Category | Required args | Optional args | Endpoint | Rate limit | Description |
|---:|---|---|---|---|---|---|---|---|
| 1 | `lingxing_ad_accounts` | `manual` | `manual` | None | type, sid, profile_id, country_code, status | `Manual` | 限流：endpoint /basicOpen/baseData/account/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。 |
| 2 | `lingxing_ads_add_sp_keywords` | `manual` | `manual` | keywords | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/spTarget/addKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 添加 SP 关键词，单次最多 1000 个；默认 dry_run，不确认不执行。 |
| 3 | `lingxing_ads_add_sp_negative_keywords` | `manual` | `manual` | negative_keywords | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/spTarget/addNegativeKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 添加 SP 否定关键词，支持活动层级和广告组层级；默认 dry_run，不确认不执行。 |
| 4 | `lingxing_ads_add_sp_negative_targets` | `manual` | `manual` | asins | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/spTarget/addNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 添加 SP 否定 ASIN，支持活动层级和广告组层级；默认 dry_run，不确认不执行。 |
| 5 | `lingxing_ads_archive_sp_negatives` | `manual` | `manual` | targetIds | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/spTarget/archiveNegatives，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 归档 SP 否定关键词或否定 ASIN，需传官方 target_id；默认 dry_run，不确认不执行。 |
| 6 | `lingxing_ads_operation_logs` | `manual` | `manual` | sid, log_source, sponsored_type, operate_type, start_date, end_date | offset, length | `Manual` | 限流：endpoint /pb/openapi/newad/apiLogStandard，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。 | 查询广告操作日志，支持 SP/SB/SD、ERP/亚马逊后台来源和广告对象类型过滤。 |
| 7 | `lingxing_ads_portfolios` | `endpoint_spec` | `ad_base` | sid | profile_id | `/pb/openapi/newad/portfolios` | 限流：endpoint /pb/openapi/newad/portfolios，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 广告组合列表。 |
| 8 | `lingxing_ads_sb_ad_group_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sbAdGroupHourData` | 限流：endpoint /pb/openapi/newad/sbAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告组小时数据。 |
| 9 | `lingxing_ads_sb_ad_groups` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/hsaAdGroups` | 限流：endpoint /pb/openapi/newad/hsaAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告组基础数据。 |
| 10 | `lingxing_ads_sb_campaign_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sbCampaignHourData` | 限流：endpoint /pb/openapi/newad/sbCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动小时数据。 |
| 11 | `lingxing_ads_sb_campaign_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/hsaCampaignReports` | 限流：endpoint /pb/openapi/newad/hsaCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动日报。 |
| 12 | `lingxing_ads_sb_campaigns` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/hsaCampaigns` | 限流：endpoint /pb/openapi/newad/hsaCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告活动基础数据。 |
| 13 | `lingxing_ads_sb_creative_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/listHsaProductAdReport` | 限流：endpoint /pb/openapi/newad/listHsaProductAdReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告创意日报。 |
| 14 | `lingxing_ads_sb_creatives` | `endpoint_spec` | `ad_base` | sid | profile_id | `/pb/openapi/newad/hsaProductAds` | 限流：endpoint /pb/openapi/newad/hsaProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告创意基础数据。 |
| 15 | `lingxing_ads_sb_negative_keywords` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/hsaNegativeKeywords` | 限流：endpoint /pb/openapi/newad/hsaNegativeKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 否定关键词基础数据，用于查看 SB 否定关键词。 |
| 16 | `lingxing_ads_sb_negative_targets` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/hsaNegativeTargets` | 限流：endpoint /pb/openapi/newad/hsaNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 否定商品投放基础数据，用于查看 SB 否定商品投放。 |
| 17 | `lingxing_ads_sb_placement_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sbAdPlacementHourData` | 限流：endpoint /pb/openapi/newad/sbAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 广告位小时数据。 |
| 18 | `lingxing_ads_sb_purchased_asin_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id | `/pb/openapi/newad/hsaPurchasedAsinReports` | 限流：endpoint /pb/openapi/newad/hsaPurchasedAsinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。 |
| 19 | `lingxing_ads_sb_target_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sbTargetHourData` | 限流：endpoint /pb/openapi/newad/sbTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 投放小时数据。 |
| 20 | `lingxing_ads_sb_targets` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sbTargeting` | 限流：endpoint /pb/openapi/newad/sbTargeting，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SB 投放基础数据。 |
| 21 | `lingxing_ads_sd_ad_group_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdAdGroupHourData` | 限流：endpoint /pb/openapi/newad/sdAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告组小时数据。 |
| 22 | `lingxing_ads_sd_ad_groups` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sdAdGroups` | 限流：endpoint /pb/openapi/newad/sdAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告组基础数据。 |
| 23 | `lingxing_ads_sd_advertise_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdAdvertiseHourData` | 限流：endpoint /pb/openapi/newad/sdAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告小时数据。 |
| 24 | `lingxing_ads_sd_campaign_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdCampaignHourData` | 限流：endpoint /pb/openapi/newad/sdCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动小时数据。 |
| 25 | `lingxing_ads_sd_campaign_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdCampaignReports` | 限流：endpoint /pb/openapi/newad/sdCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动日报。 |
| 26 | `lingxing_ads_sd_campaigns` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sdCampaigns` | 限流：endpoint /pb/openapi/newad/sdCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告活动基础数据。 |
| 27 | `lingxing_ads_sd_negative_targets` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sdNegativeTargets` | 限流：endpoint /pb/openapi/newad/sdNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 否定商品定位基础数据，用于查看 SD 否定投放对象。 |
| 28 | `lingxing_ads_sd_product_ad_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdProductAdReports` | 限流：endpoint /pb/openapi/newad/sdProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告商品日报，可直接按 ASIN 聚合。 |
| 29 | `lingxing_ads_sd_product_ads` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sdProductAds` | 限流：endpoint /pb/openapi/newad/sdProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 广告商品基础数据。 |
| 30 | `lingxing_ads_sd_target_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdTargetHourData` | 限流：endpoint /pb/openapi/newad/sdTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 投放小时数据。 |
| 31 | `lingxing_ads_sd_target_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdTargetReports` | 限流：endpoint /pb/openapi/newad/sdTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 商品定位日报。 |
| 32 | `lingxing_ads_sd_targets` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/sdTargets` | 限流：endpoint /pb/openapi/newad/sdTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SD 商品定位基础数据。 |
| 33 | `lingxing_ads_sp_ad_group_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spAdGroupHourData` | 限流：endpoint /pb/openapi/newad/spAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告组小时数据。 |
| 34 | `lingxing_ads_sp_ad_groups` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spAdGroups` | 限流：endpoint /pb/openapi/newad/spAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告组基础数据。 |
| 35 | `lingxing_ads_sp_advertise_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spAdvertiseHourData` | 限流：endpoint /pb/openapi/newad/spAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告小时数据。 |
| 36 | `lingxing_ads_sp_campaign_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spCampaignHourData` | 限流：endpoint /pb/openapi/newad/spCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动小时数据。 |
| 37 | `lingxing_ads_sp_campaign_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spCampaignReports` | 限流：endpoint /pb/openapi/newad/spCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动日报。 |
| 38 | `lingxing_ads_sp_campaigns` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spCampaigns` | 限流：endpoint /pb/openapi/newad/spCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告活动基础数据。 |
| 39 | `lingxing_ads_sp_keyword_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spKeywordReports` | 限流：endpoint /pb/openapi/newad/spKeywordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 关键词日报。 |
| 40 | `lingxing_ads_sp_keywords` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spKeywords` | 限流：endpoint /pb/openapi/newad/spKeywords，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 关键词基础数据。 |
| 41 | `lingxing_ads_sp_negative_targets_or_keywords` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spNegativeTargetsOrKeywords` | 限流：endpoint /pb/openapi/newad/spNegativeTargetsOrKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 否定投放基础数据，返回否定关键词和否定商品投放，用于归档前查找 target_id。 |
| 42 | `lingxing_ads_sp_placement_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spAdPlacementHourData` | 限流：endpoint /pb/openapi/newad/spAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告位小时数据。 |
| 43 | `lingxing_ads_sp_product_ad_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spProductAdReports` | 限流：endpoint /pb/openapi/newad/spProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告商品日报，可直接按 ASIN 聚合。 |
| 44 | `lingxing_ads_sp_product_ads` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spProductAds` | 限流：endpoint /pb/openapi/newad/spProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 广告商品基础数据。 |
| 45 | `lingxing_ads_sp_search_term_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail, target_type | `/pb/openapi/newad/queryWordReports` | 限流：endpoint /pb/openapi/newad/queryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 用户搜索词日报。 |
| 46 | `lingxing_ads_sp_target_hourly` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spTargetHourData` | 限流：endpoint /pb/openapi/newad/spTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 投放小时数据。 |
| 47 | `lingxing_ads_sp_target_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spTargetReports` | 限流：endpoint /pb/openapi/newad/spTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 商品定位日报。 |
| 48 | `lingxing_ads_sp_targets` | `endpoint_spec` | `ad_base` | sid | profile_id, state | `/pb/openapi/newad/spTargets` | 限流：endpoint /pb/openapi/newad/spTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | SP 商品定位基础数据。 |
| 49 | `lingxing_ads_update_sp_ad_group` | `manual` | `manual` | ad_groups | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/manage/putSpAdGroup，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 修改 SP 广告组，支持启停和默认竞价；默认 dry_run，不确认不执行。 |
| 50 | `lingxing_ads_update_sp_campaign` | `manual` | `manual` | campaigns | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/manage/putSpCampaign，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 修改 SP 广告活动和广告位，支持启停、预算、竞价策略和广告位比例；默认 dry_run，不确认不执行。 |
| 51 | `lingxing_ads_update_sp_keyword` | `manual` | `manual` | keywords | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/manage/putSpKeyword，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 修改 SP 关键词，支持启停和竞价；默认 dry_run，不确认不执行。 |
| 52 | `lingxing_ads_update_sp_product_ads` | `manual` | `manual` | product_ads | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/manage/putSpProductAds，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 修改 SP 广告商品启用/暂停状态，单次最多 1000 个；默认 dry_run，不确认不执行。 |
| 53 | `lingxing_ads_update_sp_target` | `manual` | `manual` | targeting_clauses | sid, profile_id, dry_run, confirm | `Manual` | 限流：endpoint /basicOpen/adReport/manage/putSpTarget，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 修改 SP 商品投放，支持启停和竞价；默认 dry_run，不确认不执行。 |
| 54 | `lingxing_amazon_listing` | `endpoint_spec` | `source` | sid, search_value | search_field, exact_search, store_type, listing_update_start_time, listing_update_end_time | `/erp/sc/data/mws/listing` | 限流：endpoint /erp/sc/data/mws/listing，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询亚马逊 Listing，可按 MSKU、ASIN 或本地 SKU 搜索，返回 fulfillment_channel_type 配送方式以及 FBA/FBM 库存字段。 |
| 55 | `lingxing_asin_ads_daily_rollup` | `manual` | `manual` | sid, asin, start_date, end_date | attribution_policy | `Manual` | 限流：聚合工具，涉及 6 个 endpoint；最严格为 /basicOpen/baseData/account/list 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按 ASIN 汇总每日广告指标，采用 balanced 归因。 |
| 56 | `lingxing_asin_daily_lists` | `manual` | `manual` | sid, event_date, metric_type | asin_type | `Manual` | 限流：endpoint /erp/sc/data/sales_report/asinDailyLists，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺、日期和指标类型拉取 AsinDailyLists。 |
| 57 | `lingxing_asin_product_snapshot` | `manual` | `manual` | sid, asins | start_date, end_date | `Manual` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /basicOpen/openapi/storage/fbaWarehouseDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按店铺 sid 查询 1 到 50 个 ASIN 的产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。单个 ASIN 也使用 asins 数组传入，例如 ["B0..."]；超过 50 个时客户端 Agent 应自行按 50 个一批拆分并串行调用。 |
| 58 | `lingxing_asin_weekly_rollup` | `manual` | `manual` | sid, asin, start_date, end_date | None | `Manual` | 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/sales_report/sales 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按周汇总 ASIN 的总销量、广告指标和促销标签。 |
| 59 | `lingxing_exp_ads_aba_report` | `endpoint_spec` | `ad_report` | country, data_start_time | None | `/pb/openapi/newad/abaReport` | 限流：endpoint /pb/openapi/newad/abaReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：ABA 搜索词周报下载信息。 |
| 60 | `lingxing_exp_ads_sb_ad_group_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/hsaAdGroupReports` | 限流：endpoint /pb/openapi/newad/hsaAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 广告组日报。 |
| 61 | `lingxing_exp_ads_sb_campaign_placement_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/hsaCampaignPlacementReports` | 限流：endpoint /pb/openapi/newad/hsaCampaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 广告位日报。 |
| 62 | `lingxing_exp_ads_sb_keyword_placement_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/listHsaKeywordPlacementReport` | 限流：endpoint /pb/openapi/newad/listHsaKeywordPlacementReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 关键词广告位日报。 |
| 63 | `lingxing_exp_ads_sb_search_term_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/hsaQueryWordReports` | 限流：endpoint /pb/openapi/newad/hsaQueryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 用户搜索词日报。 |
| 64 | `lingxing_exp_ads_sb_target_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/listHsaTargetingReport` | 限流：endpoint /pb/openapi/newad/listHsaTargetingReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SB 投放日报。 |
| 65 | `lingxing_exp_ads_sd_ad_group_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdAdGroupReports` | 限流：endpoint /pb/openapi/newad/sdAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SD 广告组日报。 |
| 66 | `lingxing_exp_ads_sd_match_target_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/sdMatchTargetReports` | 限流：endpoint /pb/openapi/newad/sdMatchTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SD 匹配目标日报。 |
| 67 | `lingxing_exp_ads_sp_ad_group_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/spAdGroupReports` | 限流：endpoint /pb/openapi/newad/spAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 广告组日报。 |
| 68 | `lingxing_exp_ads_sp_placement_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/campaignPlacementReports` | 限流：endpoint /pb/openapi/newad/campaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 广告位日报。 |
| 69 | `lingxing_exp_ads_sp_purchased_asin_report` | `endpoint_spec` | `ad_report` | sid, report_date | profile_id, show_detail | `/pb/openapi/newad/asinReports` | 限流：endpoint /pb/openapi/newad/asinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：SP 已购买 ASIN 报表。 |
| 70 | `lingxing_exp_finance_report_seller` | `endpoint_spec` | `profit_report` | sid, start_date, end_date | currency_code, monthly_query, order_status | `/bd/profit/report/open/report/seller/list` | 限流：endpoint /bd/profit/report/open/report/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 实验层：结算利润报表店铺视角。 |
| 71 | `lingxing_fba_stock_aggregate` | `endpoint_spec` | `stock` | sid, start_month, end_month | None | `/cost/center/openApi/fba/gather/query` | 限流：endpoint /cost/center/openApi/fba/gather/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | FBA 库存新报表汇总。 |
| 72 | `lingxing_fba_stock_detail` | `endpoint_spec` | `stock` | sid, start_month, end_month | None | `/cost/center/openApi/fba/detail/query` | 限流：endpoint /cost/center/openApi/fba/detail/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | FBA 库存新报表明细。 |
| 73 | `lingxing_fba_warehouse_detail` | `endpoint_spec` | `warehouse` | sid | search_field, search_value, cid, bid, attribute, asin_principal, status, senior_search_list, fulfillment_channel_type, is_hide_zero_stock, is_parant_asin_merge, is_contain_del_ls, query_fba_storage_quantity_list | `/basicOpen/openapi/storage/fbaWarehouseDetail` | 限流：endpoint /basicOpen/openapi/storage/fbaWarehouseDetail，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。 |
| 74 | `lingxing_finance_report_asin` | `endpoint_spec` | `profit_report` | sid, start_date, end_date | currency_code, search_value, monthly_query, summary_enabled, order_status | `/bd/profit/report/open/report/asin/list` | 限流：endpoint /bd/profit/report/open/report/asin/list，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。 | 结算利润报表 ASIN 视角。 |
| 75 | `lingxing_health_check` | `manual` | `manual` | None | None | `Manual` | 限流：endpoint /api/auth-server/oauth/access-token，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 检查领星环境变量、token 状态和基础连通性，不拉业务数据。 |
| 76 | `lingxing_local_product_costs` | `manual` | `manual` | None | sku_list, sku_identifier_list, update_time_start, update_time_end, create_time_start, create_time_end, page_size, include_supplier_quotes, include_raw | `Manual` | 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。 |
| 77 | `lingxing_local_products` | `endpoint_spec` | `product` | None | sku_list, sku_identifier_list, update_time_start, update_time_end, create_time_start, create_time_end | `/erp/sc/routing/data/local_inventory/productList` | 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。 |
| 78 | `lingxing_marketplaces` | `manual` | `manual` | None | None | `Manual` | 限流：endpoint /erp/sc/data/seller/allMarketplace，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 返回领星市场列表，并补充站点时区映射。 |
| 79 | `lingxing_multi_channel_orders` | `manual` | `manual` | sids, start_date, end_date | date_type, order_status, amazon_order_id, seller_fulfillment_order_id, include_product_detail, include_logistics_detail, include_transaction_detail, include_return_detail, page_size, max_records | `Manual` | 限流：聚合工具，涉及 5 个 endpoint；最严格为 /order/amzod/api/orderList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 查询亚马逊多渠道订单列表，按店铺 sid、日期范围和订单状态过滤；可选补充商品、物流、交易明细、退换货详情。为避免领星默认拉取最近 6 个月，本工具强制要求 start_date/end_date。 |
| 80 | `lingxing_order_details` | `manual` | `manual` | None | order_id, order_ids | `Manual` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/mws/orderDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。 |
| 81 | `lingxing_order_lists` | `manual` | `manual` | sid, start_date, end_date | date_type | `Manual` | 限流：endpoint /erp/sc/data/mws/orders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。 |
| 82 | `lingxing_product_performance` | `endpoint_spec` | `source` | sid, start_date, end_date | search_field, search_value, summary_field, mid, currency_code, is_recently_enum, purchase_status, sort_field, sort_type | `/bd/productPerformance/openApi/asinList` | 限流：endpoint /bd/productPerformance/openApi/asinList，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。 |
| 83 | `lingxing_profit_asin` | `endpoint_spec` | `profit` | sid, start_date, end_date | currency_code, search_value | `/bd/profit/statistics/open/asin/list` | 限流：endpoint /bd/profit/statistics/open/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | ASIN 维度利润统计。 |
| 84 | `lingxing_profit_parent_asin` | `endpoint_spec` | `profit` | sid, start_date, end_date | currency_code, search_value | `/bd/profit/statistics/open/parent/asin/list` | 限流：endpoint /bd/profit/statistics/open/parent/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 父 ASIN 维度利润统计。 |
| 85 | `lingxing_profit_report_order_list` | `endpoint_spec` | `profit_report_order` | start_date, end_date | search_date_field, sids, mids, fee_type, listing_owner, currency_code, search_field, search_value, sort_field, sort_type, settlement_status, fund_transfer_status, account_type, fulfillment, product_developer_uids, order_status, gmt_modified_start_date, gmt_modified_end_date, response_mode, preview_limit | `/basicOpen/finance/profitReport/order/transcation/list` | 限流：endpoint /basicOpen/finance/profitReport/order/transcation/list，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询利润报表订单 Transaction 视图；默认返回摘要，full 仅供本地 Excel 导出器。fee_type 映射到官方 eventSource，listing_owner 映射到官方 principalUids。 |
| 86 | `lingxing_profit_seller` | `endpoint_spec` | `profit` | sid, start_date, end_date | currency_code, search_value, monthly_query | `/bd/profit/statistics/open/seller/list` | 限流：endpoint /bd/profit/statistics/open/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 店铺维度利润统计。 |
| 87 | `lingxing_promotion_coupon` | `manual` | `manual` | sid, start_date, end_date | None | `Manual` | 限流：endpoint /basicOpen/promotionalActivities/coupon/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。 |
| 88 | `lingxing_promotion_listing` | `manual` | `manual` | sid, site_date, start_time, end_time | status, product_status, promotion_category | `Manual` | 限流：endpoint /basicOpen/promotion/listingList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。 |
| 89 | `lingxing_promotion_manage` | `manual` | `manual` | sid, start_date, end_date | None | `Manual` | 限流：endpoint /basicOpen/promotionalActivities/manage/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。 |
| 90 | `lingxing_promotion_sec_kill` | `manual` | `manual` | sid, start_date, end_date | None | `Manual` | 限流：endpoint /basicOpen/promotionalActivities/secKill/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。 |
| 91 | `lingxing_promotion_vip_discount` | `manual` | `manual` | sid, start_date, end_date | None | `Manual` | 限流：endpoint /basicOpen/promotionalActivities/vipDiscount/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。 |
| 92 | `lingxing_rate_limit_policy` | `manual` | `manual` | None | tool_name | `Manual` | 限流：本工具不直接调用领星业务 OpenAPI，或仅返回本地网关策略；客户端可并发调用，但不应把它作为业务查询循环。 | 返回当前 MCP 工具到领星 OpenAPI endpoint 的限流政策，供客户端 agent 在调用前按 endpoint 自主排队。 |
| 93 | `lingxing_refund_orders` | `endpoint_spec` | `source` | sid, start_date, end_date | date_type | `/erp/sc/data/mws_report/refundOrders` | 限流：endpoint /erp/sc/data/mws_report/refundOrders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询 FBA customer returns 报表，返回 FBA 退货订单源表原始数据。 |
| 94 | `lingxing_replenishment_asin_info` | `endpoint_spec` | `replenishment_info` | sid, asin | mode | `/erp/sc/routing/fbaSug/asin/getInfo` | 限流：endpoint /erp/sc/routing/fbaSug/asin/getInfo，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 补货建议 ASIN 明细。 |
| 95 | `lingxing_replenishment_summary` | `endpoint_spec` | `replenishment_summary` | sid | asin, mode | `/erp/sc/routing/restocking/analysis/getSummaryList` | 限流：endpoint /erp/sc/routing/restocking/analysis/getSummaryList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 补货建议列表。 |
| 96 | `lingxing_report_export_create` | `manual` | `manual` | sid, report_type | data_start_time, data_end_time, marketplace_ids, region, seller_id | `Manual` | 限流：endpoint /basicOpen/report/create/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 创建亚马逊报告导出任务。 |
| 97 | `lingxing_report_export_download` | `manual` | `manual` | None | url, sid, task_id, report_document_id, region, seller_id | `Manual` | 限流：聚合工具，涉及 2 个 endpoint；最严格为 /basicOpen/report/query/reportExportTask 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 下载并解析亚马逊报告导出文件。 |
| 98 | `lingxing_report_export_query` | `manual` | `manual` | task_id | sid, region, seller_id | `Manual` | 限流：endpoint /basicOpen/report/query/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询亚马逊报告导出任务结果。 |
| 99 | `lingxing_report_export_refresh_url` | `manual` | `manual` | report_document_id | sid, region, seller_id | `Manual` | 限流：endpoint /basicOpen/report/amazonReportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 续期亚马逊报告下载链接。 |
| 100 | `lingxing_resolve_daily_promotions` | `manual` | `manual` | sid, target_date | lookback_days | `Manual` | 限流：聚合工具，涉及 5 个 endpoint；最严格为 /basicOpen/promotion/listingList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。 |
| 101 | `lingxing_return_analysis` | `endpoint_spec` | `source` | startDate, endDate, asinType, dateType | mids, principalUid, searchField, searchValue, sortField, sortType, storeId | `/basicOpen/salesAnalysis/returnOrder/analysisLists` | 限流：endpoint /basicOpen/salesAnalysis/returnOrder/analysisLists，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询退货分析，按 MSKU / ASIN / 父 ASIN / SKU / SPU 等维度统计退货数量、退货件数、退货率和退货原因相关指标。 |
| 102 | `lingxing_sales_outbound_orders` | `manual` | `manual` | start_date, end_date | sids, amazon_seller_ids, time_type, status, logistics_status, platform_order_numbers, system_order_numbers, outbound_order_numbers, response_mode, preview_limit | `Manual` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 通过领星 OpenAPI 查询 ERP 销售出库单。可传 sids 或 amazon_seller_ids 定向查询；两者都不传时省略官方 sid_arr，一次 MCP 调用查询全部店铺，并按官方每页 200 条限制合并全部分页。默认 time_type=stock_delivered_at，按库存流水出库时间筛选。默认只返回摘要预览；生成 Excel 时由本地导出器使用 response_mode=full，避免把全量 JSON 放入模型上下文。 |
| 103 | `lingxing_seller_lists` | `manual` | `manual` | None | status, marketplace | `Manual` | 限流：聚合工具，涉及 2 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。 |
| 104 | `lingxing_shipment_settlement_report` | `manual` | `manual` | start_date, end_date | sids, amazon_seller_ids, time_type, country_codes, order_numbers, shipment_numbers, custom_numbers, mskus, skus, product_names, track_codes, fulfillment_type, response_mode, preview_limit | `Manual` | 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 通过领星 OpenAPI 查询亚马逊发货与结算差异数据。可传 sids 或 amazon_seller_ids 定向查询；两者都不传时，一次 MCP 调用自动覆盖全部启用中的亚马逊店铺；服务端按站点分组请求，并按官方每页 1000 条限制合并全部分页，避免跨站点混合数组返回空结果。默认 time_type=04，按结算时间筛选。默认只返回摘要预览；生成 Excel 时由本地导出器使用 response_mode=full，避免把全量 JSON 放入模型上下文。 |
| 105 | `lingxing_smoke_check` | `manual` | `manual` | None | sid, date | `Manual` | 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。 | 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。 |
| 106 | `lingxing_source_all_orders` | `endpoint_spec` | `source` | sid, start_date, end_date | date_type | `/erp/sc/data/mws_report/allOrders` | 限流：endpoint /erp/sc/data/mws_report/allOrders，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。 | 亚马逊源表所有订单。 |
| 107 | `lingxing_source_daily_inventory` | `endpoint_spec` | `source` | sid, event_date | None | `/erp/sc/data/mws_report/dailyInventory` | 限流：endpoint /erp/sc/data/mws_report/dailyInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表每日库存。 |
| 108 | `lingxing_source_manage_inventory` | `endpoint_spec` | `source` | sid | None | `/erp/sc/data/mws_report/manageInventory` | 限流：endpoint /erp/sc/data/mws_report/manageInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表 FBA 库存。 |
| 109 | `lingxing_source_reserved_inventory` | `endpoint_spec` | `source` | sid | None | `/erp/sc/data/mws_report/reservedInventory` | 限流：endpoint /erp/sc/data/mws_report/reservedInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表预留库存。 |
| 110 | `lingxing_source_transaction` | `endpoint_spec` | `source` | sid, event_date | None | `/erp/sc/data/mws_report/transaction` | 限流：endpoint /erp/sc/data/mws_report/transaction，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 亚马逊源表交易明细。 |
| 111 | `lingxing_store_sales` | `manual` | `manual` | sid, start_date, end_date | None | `Manual` | 限流：endpoint /erp/sc/data/sales_report/sales，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 按店铺和日期范围拉取 StoreSales，并自动合并分页。 |
| 112 | `lingxing_voice_of_buyer` | `endpoint_spec` | `source` | None | fulfillment_channel, sids, pxc_health, search_field, search_value, return_badge | `/basicOpen/customerService/voiceOfBuyer/list` | 限流：endpoint /basicOpen/customerService/voiceOfBuyer/list，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。 | 查询买家之声列表，返回 ASIN/MSKU/SKU 的满意度状况、不满意率、不满意订单数、订单总数、主要退货原因和退货标记。 |

## Tool Details

### 1. `lingxing_ad_accounts`

- Origin: `manual`
- Category: `manual`
- Description: 查询广告账号列表，可按 sid / profile_id / 国家 / 状态过滤。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/baseData/account/list
- Rate limit: 限流：endpoint /basicOpen/baseData/account/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: type, sid, profile_id, country_code, status
- Input schema:

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

### 2. `lingxing_ads_add_sp_keywords`

- Origin: `manual`
- Category: `manual`
- Description: 添加 SP 关键词，单次最多 1000 个；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/spTarget/addKeywords
- Rate limit: 限流：endpoint /basicOpen/adReport/spTarget/addKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: keywords
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "keywords": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 keywords 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "keywords"
  ],
  "additionalProperties": false
}
```

### 3. `lingxing_ads_add_sp_negative_keywords`

- Origin: `manual`
- Category: `manual`
- Description: 添加 SP 否定关键词，支持活动层级和广告组层级；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/spTarget/addNegativeKeywords
- Rate limit: 限流：endpoint /basicOpen/adReport/spTarget/addNegativeKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: negative_keywords
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "negative_keywords": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 negativeKeywords 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "negative_keywords"
  ],
  "additionalProperties": false
}
```

### 4. `lingxing_ads_add_sp_negative_targets`

- Origin: `manual`
- Category: `manual`
- Description: 添加 SP 否定 ASIN，支持活动层级和广告组层级；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/spTarget/addNegativeTargets
- Rate limit: 限流：endpoint /basicOpen/adReport/spTarget/addNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: asins
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "asins": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 asins 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "asins"
  ],
  "additionalProperties": false
}
```

### 5. `lingxing_ads_archive_sp_negatives`

- Origin: `manual`
- Category: `manual`
- Description: 归档 SP 否定关键词或否定 ASIN，需传官方 target_id；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/spTarget/archiveNegatives
- Rate limit: 限流：endpoint /basicOpen/adReport/spTarget/archiveNegatives，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: targetIds
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "targetIds": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "官方必填数组字段，字段名保持领星 API 文档命名。"
    }
  },
  "required": [
    "targetIds"
  ],
  "additionalProperties": false
}
```

### 6. `lingxing_ads_operation_logs`

- Origin: `manual`
- Category: `manual`
- Description: 查询广告操作日志，支持 SP/SB/SD、ERP/亚马逊后台来源和广告对象类型过滤。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /pb/openapi/newad/apiLogStandard
- Rate limit: 限流：endpoint /pb/openapi/newad/apiLogStandard，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。
- Required args: sid, log_source, sponsored_type, operate_type, start_date, end_date
- Optional args: offset, length
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "log_source": {
      "type": "string",
      "description": "all / erp / amazon。"
    },
    "sponsored_type": {
      "type": "string",
      "description": "sp / sb / sd。"
    },
    "operate_type": {
      "type": "string",
      "description": "campaigns / adGroups / productAds / keywords / negativeKeywords / targets / negativeTargets / profiles。"
    },
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "offset": {
      "type": "integer"
    },
    "length": {
      "type": "integer"
    }
  },
  "required": [
    "sid",
    "log_source",
    "sponsored_type",
    "operate_type",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 7. `lingxing_ads_portfolios`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: 广告组合列表。
- Endpoint: `/pb/openapi/newad/portfolios`
- Docs path: `docs/newAd/baseData/portfolios.md`
- Rate-limit endpoints: /pb/openapi/newad/portfolios
- Rate limit: 限流：endpoint /pb/openapi/newad/portfolios，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id
- Input schema:

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

### 8. `lingxing_ads_sb_ad_group_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 广告组小时数据。
- Endpoint: `/pb/openapi/newad/sbAdGroupHourData`
- Docs path: `docs/newAd/report/sbAdGroupHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sbAdGroupHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sbAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 9. `lingxing_ads_sb_ad_groups`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 广告组基础数据。
- Endpoint: `/pb/openapi/newad/hsaAdGroups`
- Docs path: `docs/newAd/baseData/hsaAdGroups.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaAdGroups
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 10. `lingxing_ads_sb_campaign_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 广告活动小时数据。
- Endpoint: `/pb/openapi/newad/sbCampaignHourData`
- Docs path: `docs/newAd/report/sbCampaignHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sbCampaignHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sbCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 11. `lingxing_ads_sb_campaign_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 广告活动日报。
- Endpoint: `/pb/openapi/newad/hsaCampaignReports`
- Docs path: `docs/newAd/report/hsaCampaignReports.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaCampaignReports
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 12. `lingxing_ads_sb_campaigns`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 广告活动基础数据。
- Endpoint: `/pb/openapi/newad/hsaCampaigns`
- Docs path: `docs/newAd/baseData/hsaCampaigns.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaCampaigns
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 13. `lingxing_ads_sb_creative_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 广告创意日报。
- Endpoint: `/pb/openapi/newad/listHsaProductAdReport`
- Docs path: `docs/newAd/report/listHsaProductAdReport.md`
- Rate-limit endpoints: /pb/openapi/newad/listHsaProductAdReport
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaProductAdReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 14. `lingxing_ads_sb_creatives`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 广告创意基础数据。
- Endpoint: `/pb/openapi/newad/hsaProductAds`
- Docs path: `docs/newAd/baseData/sbAdHasProductAds.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaProductAds
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id
- Input schema:

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

### 15. `lingxing_ads_sb_negative_keywords`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 否定关键词基础数据，用于查看 SB 否定关键词。
- Endpoint: `/pb/openapi/newad/hsaNegativeKeywords`
- Docs path: `docs/newAd/baseData/hsaNegativeKeywords.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaNegativeKeywords
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaNegativeKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 16. `lingxing_ads_sb_negative_targets`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 否定商品投放基础数据，用于查看 SB 否定商品投放。
- Endpoint: `/pb/openapi/newad/hsaNegativeTargets`
- Docs path: `docs/newAd/baseData/hsaNegativeTargets.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaNegativeTargets
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 17. `lingxing_ads_sb_placement_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 广告位小时数据。
- Endpoint: `/pb/openapi/newad/sbAdPlacementHourData`
- Docs path: `docs/newAd/report/sbAdPlacementHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sbAdPlacementHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sbAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 18. `lingxing_ads_sb_purchased_asin_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 已购买 ASIN 报表，用于按 ASIN 归因销售/订单。
- Endpoint: `/pb/openapi/newad/hsaPurchasedAsinReports`
- Docs path: `docs/newAd/report/hsaPurchasedAsinReports.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaPurchasedAsinReports
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaPurchasedAsinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id
- Input schema:

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

### 19. `lingxing_ads_sb_target_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SB 投放小时数据。
- Endpoint: `/pb/openapi/newad/sbTargetHourData`
- Docs path: `docs/newAd/report/sbTargetHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sbTargetHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sbTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 20. `lingxing_ads_sb_targets`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SB 投放基础数据。
- Endpoint: `/pb/openapi/newad/sbTargeting`
- Docs path: `docs/newAd/baseData/sbTargeting.md`
- Rate-limit endpoints: /pb/openapi/newad/sbTargeting
- Rate limit: 限流：endpoint /pb/openapi/newad/sbTargeting，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 21. `lingxing_ads_sd_ad_group_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 广告组小时数据。
- Endpoint: `/pb/openapi/newad/sdAdGroupHourData`
- Docs path: `docs/newAd/report/sdAdGroupHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sdAdGroupHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 22. `lingxing_ads_sd_ad_groups`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SD 广告组基础数据。
- Endpoint: `/pb/openapi/newad/sdAdGroups`
- Docs path: `docs/newAd/baseData/sdAdGroups.md`
- Rate-limit endpoints: /pb/openapi/newad/sdAdGroups
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 23. `lingxing_ads_sd_advertise_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 广告小时数据。
- Endpoint: `/pb/openapi/newad/sdAdvertiseHourData`
- Docs path: `docs/newAd/report/sdAdvertiseHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sdAdvertiseHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 24. `lingxing_ads_sd_campaign_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 广告活动小时数据。
- Endpoint: `/pb/openapi/newad/sdCampaignHourData`
- Docs path: `docs/newAd/report/sdCampaignHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sdCampaignHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 25. `lingxing_ads_sd_campaign_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 广告活动日报。
- Endpoint: `/pb/openapi/newad/sdCampaignReports`
- Docs path: `docs/newAd/report/sdCampaignReports.md`
- Rate-limit endpoints: /pb/openapi/newad/sdCampaignReports
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 26. `lingxing_ads_sd_campaigns`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SD 广告活动基础数据。
- Endpoint: `/pb/openapi/newad/sdCampaigns`
- Docs path: `docs/newAd/baseData/sdCampaigns.md`
- Rate-limit endpoints: /pb/openapi/newad/sdCampaigns
- Rate limit: 限流：endpoint /pb/openapi/newad/sdCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 27. `lingxing_ads_sd_negative_targets`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SD 否定商品定位基础数据，用于查看 SD 否定投放对象。
- Endpoint: `/pb/openapi/newad/sdNegativeTargets`
- Docs path: `docs/newAd/baseData/sdNegativeTargets.md`
- Rate-limit endpoints: /pb/openapi/newad/sdNegativeTargets
- Rate limit: 限流：endpoint /pb/openapi/newad/sdNegativeTargets，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 28. `lingxing_ads_sd_product_ad_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 广告商品日报，可直接按 ASIN 聚合。
- Endpoint: `/pb/openapi/newad/sdProductAdReports`
- Docs path: `docs/newAd/report/sdProductAdReports.md`
- Rate-limit endpoints: /pb/openapi/newad/sdProductAdReports
- Rate limit: 限流：endpoint /pb/openapi/newad/sdProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 29. `lingxing_ads_sd_product_ads`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SD 广告商品基础数据。
- Endpoint: `/pb/openapi/newad/sdProductAds`
- Docs path: `docs/newAd/baseData/sdProductAds.md`
- Rate-limit endpoints: /pb/openapi/newad/sdProductAds
- Rate limit: 限流：endpoint /pb/openapi/newad/sdProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 30. `lingxing_ads_sd_target_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 投放小时数据。
- Endpoint: `/pb/openapi/newad/sdTargetHourData`
- Docs path: `docs/newAd/report/sdTargetHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/sdTargetHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SD 商品定位日报。
- Endpoint: `/pb/openapi/newad/sdTargetReports`
- Docs path: `docs/newAd/report/sdTargetReports.md`
- Rate-limit endpoints: /pb/openapi/newad/sdTargetReports
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 32. `lingxing_ads_sd_targets`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SD 商品定位基础数据。
- Endpoint: `/pb/openapi/newad/sdTargets`
- Docs path: `docs/newAd/baseData/sdTargets.md`
- Rate-limit endpoints: /pb/openapi/newad/sdTargets
- Rate limit: 限流：endpoint /pb/openapi/newad/sdTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 33. `lingxing_ads_sp_ad_group_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告组小时数据。
- Endpoint: `/pb/openapi/newad/spAdGroupHourData`
- Docs path: `docs/newAd/report/spAdGroupHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/spAdGroupHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroupHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 34. `lingxing_ads_sp_ad_groups`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 广告组基础数据。
- Endpoint: `/pb/openapi/newad/spAdGroups`
- Docs path: `docs/newAd/baseData/spAdGroups.md`
- Rate-limit endpoints: /pb/openapi/newad/spAdGroups
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroups，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 35. `lingxing_ads_sp_advertise_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告小时数据。
- Endpoint: `/pb/openapi/newad/spAdvertiseHourData`
- Docs path: `docs/newAd/report/spAdvertiseHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/spAdvertiseHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdvertiseHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 36. `lingxing_ads_sp_campaign_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告活动小时数据。
- Endpoint: `/pb/openapi/newad/spCampaignHourData`
- Docs path: `docs/newAd/report/spCampaignHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/spCampaignHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaignHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 37. `lingxing_ads_sp_campaign_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告活动日报。
- Endpoint: `/pb/openapi/newad/spCampaignReports`
- Docs path: `docs/newAd/report/spCampaignReports.md`
- Rate-limit endpoints: /pb/openapi/newad/spCampaignReports
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaignReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 38. `lingxing_ads_sp_campaigns`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 广告活动基础数据。
- Endpoint: `/pb/openapi/newad/spCampaigns`
- Docs path: `docs/newAd/baseData/spCampaigns.md`
- Rate-limit endpoints: /pb/openapi/newad/spCampaigns
- Rate limit: 限流：endpoint /pb/openapi/newad/spCampaigns，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 39. `lingxing_ads_sp_keyword_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 关键词日报。
- Endpoint: `/pb/openapi/newad/spKeywordReports`
- Docs path: `docs/newAd/report/spKeywordReports.md`
- Rate-limit endpoints: /pb/openapi/newad/spKeywordReports
- Rate limit: 限流：endpoint /pb/openapi/newad/spKeywordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 40. `lingxing_ads_sp_keywords`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 关键词基础数据。
- Endpoint: `/pb/openapi/newad/spKeywords`
- Docs path: `docs/newAd/baseData/spKeywords.md`
- Rate-limit endpoints: /pb/openapi/newad/spKeywords
- Rate limit: 限流：endpoint /pb/openapi/newad/spKeywords，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 41. `lingxing_ads_sp_negative_targets_or_keywords`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 否定投放基础数据，返回否定关键词和否定商品投放，用于归档前查找 target_id。
- Endpoint: `/pb/openapi/newad/spNegativeTargetsOrKeywords`
- Docs path: `docs/newAd/baseData/spNegativeTargetsOrKeywords.md`
- Rate-limit endpoints: /pb/openapi/newad/spNegativeTargetsOrKeywords
- Rate limit: 限流：endpoint /pb/openapi/newad/spNegativeTargetsOrKeywords，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 42. `lingxing_ads_sp_placement_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告位小时数据。
- Endpoint: `/pb/openapi/newad/spAdPlacementHourData`
- Docs path: `docs/newAd/report/spAdPlacementHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/spAdPlacementHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdPlacementHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 43. `lingxing_ads_sp_product_ad_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 广告商品日报，可直接按 ASIN 聚合。
- Endpoint: `/pb/openapi/newad/spProductAdReports`
- Docs path: `docs/newAd/report/spProductAdReports.md`
- Rate-limit endpoints: /pb/openapi/newad/spProductAdReports
- Rate limit: 限流：endpoint /pb/openapi/newad/spProductAdReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 44. `lingxing_ads_sp_product_ads`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 广告商品基础数据。
- Endpoint: `/pb/openapi/newad/spProductAds`
- Docs path: `docs/newAd/baseData/spProductAds.md`
- Rate-limit endpoints: /pb/openapi/newad/spProductAds
- Rate limit: 限流：endpoint /pb/openapi/newad/spProductAds，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 45. `lingxing_ads_sp_search_term_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 用户搜索词日报。
- Endpoint: `/pb/openapi/newad/queryWordReports`
- Docs path: `docs/newAd/report/queryWordReports.md`
- Rate-limit endpoints: /pb/openapi/newad/queryWordReports
- Rate limit: 限流：endpoint /pb/openapi/newad/queryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail, target_type
- Input schema:

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

### 46. `lingxing_ads_sp_target_hourly`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 投放小时数据。
- Endpoint: `/pb/openapi/newad/spTargetHourData`
- Docs path: `docs/newAd/report/spTargetHourData.md`
- Rate-limit endpoints: /pb/openapi/newad/spTargetHourData
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargetHourData，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 47. `lingxing_ads_sp_target_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: SP 商品定位日报。
- Endpoint: `/pb/openapi/newad/spTargetReports`
- Docs path: `docs/newAd/report/spTargetReports.md`
- Rate-limit endpoints: /pb/openapi/newad/spTargetReports
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 48. `lingxing_ads_sp_targets`

- Origin: `endpoint_spec`
- Category: `ad_base`
- Description: SP 商品定位基础数据。
- Endpoint: `/pb/openapi/newad/spTargets`
- Docs path: `docs/newAd/baseData/spTargets.md`
- Rate-limit endpoints: /pb/openapi/newad/spTargets
- Rate limit: 限流：endpoint /pb/openapi/newad/spTargets，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: profile_id, state
- Input schema:

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

### 49. `lingxing_ads_update_sp_ad_group`

- Origin: `manual`
- Category: `manual`
- Description: 修改 SP 广告组，支持启停和默认竞价；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/manage/putSpAdGroup
- Rate limit: 限流：endpoint /basicOpen/adReport/manage/putSpAdGroup，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: ad_groups
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "ad_groups": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 adGroups 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "ad_groups"
  ],
  "additionalProperties": false
}
```

### 50. `lingxing_ads_update_sp_campaign`

- Origin: `manual`
- Category: `manual`
- Description: 修改 SP 广告活动和广告位，支持启停、预算、竞价策略和广告位比例；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/manage/putSpCampaign
- Rate limit: 限流：endpoint /basicOpen/adReport/manage/putSpCampaign，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: campaigns
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "campaigns": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 campaigns 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "campaigns"
  ],
  "additionalProperties": false
}
```

### 51. `lingxing_ads_update_sp_keyword`

- Origin: `manual`
- Category: `manual`
- Description: 修改 SP 关键词，支持启停和竞价；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/manage/putSpKeyword
- Rate limit: 限流：endpoint /basicOpen/adReport/manage/putSpKeyword，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: keywords
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "keywords": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 keywords 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "keywords"
  ],
  "additionalProperties": false
}
```

### 52. `lingxing_ads_update_sp_product_ads`

- Origin: `manual`
- Category: `manual`
- Description: 修改 SP 广告商品启用/暂停状态，单次最多 1000 个；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/manage/putSpProductAds
- Rate limit: 限流：endpoint /basicOpen/adReport/manage/putSpProductAds，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: product_ads
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "product_ads": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 productAds 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "product_ads"
  ],
  "additionalProperties": false
}
```

### 53. `lingxing_ads_update_sp_target`

- Origin: `manual`
- Category: `manual`
- Description: 修改 SP 商品投放，支持启停和竞价；默认 dry_run，不确认不执行。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/adReport/manage/putSpTarget
- Rate limit: 限流：endpoint /basicOpen/adReport/manage/putSpTarget，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: targeting_clauses
- Optional args: sid, profile_id, dry_run, confirm
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid；sid 和 profile_id 至少传一个，建议传 sid。"
    },
    "profile_id": {
      "type": "integer",
      "description": "广告 Profile ID；传入时优先使用。"
    },
    "dry_run": {
      "type": "boolean",
      "description": "默认 true；true 时只返回待提交请求体，不调用领星写接口。"
    },
    "confirm": {
      "type": "boolean",
      "description": "执行写入必须显式传 true；否则只返回计划。"
    },
    "targeting_clauses": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": true
      },
      "description": "官方 targetingClauses 对象数组，字段按领星 API 文档传入。"
    }
  },
  "required": [
    "targeting_clauses"
  ],
  "additionalProperties": false
}
```

### 54. `lingxing_amazon_listing`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 查询亚马逊 Listing，可按 MSKU、ASIN 或本地 SKU 搜索，返回 fulfillment_channel_type 配送方式以及 FBA/FBM 库存字段。
- Endpoint: `/erp/sc/data/mws/listing`
- Docs path: `docs/Sale/Listing.md`
- Rate-limit endpoints: /erp/sc/data/mws/listing
- Rate limit: 限流：endpoint /erp/sc/data/mws/listing，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, search_value
- Optional args: search_field, exact_search, store_type, listing_update_start_time, listing_update_end_time
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer"
    },
    "search_field": {
      "type": "string",
      "default": "seller_sku"
    },
    "search_value": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "exact_search": {
      "type": "integer",
      "default": 1
    },
    "store_type": {
      "type": "integer",
      "default": 1
    },
    "listing_update_start_time": {
      "type": "string"
    },
    "listing_update_end_time": {
      "type": "string"
    }
  },
  "required": [
    "sid",
    "search_value"
  ],
  "additionalProperties": false
}
```

### 55. `lingxing_asin_ads_daily_rollup`

- Origin: `manual`
- Category: `manual`
- Description: 按 ASIN 汇总每日广告指标，采用 balanced 归因。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/baseData/account/list, /pb/openapi/newad/hsaProductAds, /pb/openapi/newad/spProductAdReports, /pb/openapi/newad/sdProductAdReports, /pb/openapi/newad/hsaPurchasedAsinReports, /pb/openapi/newad/listHsaProductAdReport
- Rate limit: 限流：聚合工具，涉及 6 个 endpoint；最严格为 /basicOpen/baseData/account/list 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: sid, asin, start_date, end_date
- Optional args: attribution_policy
- Input schema:

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

### 56. `lingxing_asin_daily_lists`

- Origin: `manual`
- Category: `manual`
- Description: 按店铺、日期和指标类型拉取 AsinDailyLists。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/sales_report/asinDailyLists
- Rate limit: 限流：endpoint /erp/sc/data/sales_report/asinDailyLists，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, event_date, metric_type
- Optional args: asin_type
- Input schema:

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

### 57. `lingxing_asin_product_snapshot`

- Origin: `manual`
- Category: `manual`
- Description: 按店铺 sid 查询 1 到 50 个 ASIN 的产品快照，返回产品名、采购成本、前台售价、FBA 实时库存、产品表现销量 volume 和产品链接。单个 ASIN 也使用 asins 数组传入，例如 ["B0..."]；超过 50 个时客户端 Agent 应自行按 50 个一批拆分并串行调用。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/openapi/storage/fbaWarehouseDetail, /bd/productPerformance/openApi/asinList, /erp/sc/routing/data/local_inventory/productList
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /basicOpen/openapi/storage/fbaWarehouseDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: sid, asins
- Optional args: start_date, end_date
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sid": {
      "type": "integer",
      "description": "领星店铺 sid。"
    },
    "asins": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "ASIN 列表，支持 1 到 50 个；单个 ASIN 也传数组，超过 50 个请客户端按批次串行调用。",
      "minItems": 1,
      "maxItems": 50
    },
    "start_date": {
      "type": "string",
      "description": "销量统计开始日期，YYYY-MM-DD；不传时默认近 30 天。"
    },
    "end_date": {
      "type": "string",
      "description": "销量统计结束日期，YYYY-MM-DD；不传时默认昨天。"
    }
  },
  "required": [
    "sid",
    "asins"
  ],
  "additionalProperties": false
}
```

### 58. `lingxing_asin_weekly_rollup`

- Origin: `manual`
- Category: `manual`
- Description: 按周汇总 ASIN 的总销量、广告指标和促销标签。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/sales_report/sales, /basicOpen/baseData/account/list, /pb/openapi/newad/hsaProductAds, /pb/openapi/newad/spProductAdReports, /pb/openapi/newad/sdProductAdReports, /pb/openapi/newad/hsaPurchasedAsinReports, /pb/openapi/newad/listHsaProductAdReport, /basicOpen/promotion/listingList, /basicOpen/promotionalActivities/secKill/list, /basicOpen/promotionalActivities/manage/list, /basicOpen/promotionalActivities/vipDiscount/list, /basicOpen/promotionalActivities/coupon/list
- Rate limit: 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/sales_report/sales 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: sid, asin, start_date, end_date
- Optional args: None
- Input schema:

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

### 59. `lingxing_exp_ads_aba_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：ABA 搜索词周报下载信息。
- Endpoint: `/pb/openapi/newad/abaReport`
- Docs path: `docs/newAd/reportDownload/abaReport.md`
- Rate-limit endpoints: /pb/openapi/newad/abaReport
- Rate limit: 限流：endpoint /pb/openapi/newad/abaReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: country, data_start_time
- Optional args: None
- Input schema:

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

### 60. `lingxing_exp_ads_sb_ad_group_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SB 广告组日报。
- Endpoint: `/pb/openapi/newad/hsaAdGroupReports`
- Docs path: `docs/newAd/report/hsaAdGroupReports.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaAdGroupReports
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 61. `lingxing_exp_ads_sb_campaign_placement_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SB 广告位日报。
- Endpoint: `/pb/openapi/newad/hsaCampaignPlacementReports`
- Docs path: `docs/newAd/report/hsaCampaignPlacementReports.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaCampaignPlacementReports
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaCampaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 62. `lingxing_exp_ads_sb_keyword_placement_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SB 关键词广告位日报。
- Endpoint: `/pb/openapi/newad/listHsaKeywordPlacementReport`
- Docs path: `docs/newAd/report/listHsaKeywordPlacementReport.md`
- Rate-limit endpoints: /pb/openapi/newad/listHsaKeywordPlacementReport
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaKeywordPlacementReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 63. `lingxing_exp_ads_sb_search_term_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SB 用户搜索词日报。
- Endpoint: `/pb/openapi/newad/hsaQueryWordReports`
- Docs path: `docs/newAd/report/hsaQueryWordReports.md`
- Rate-limit endpoints: /pb/openapi/newad/hsaQueryWordReports
- Rate limit: 限流：endpoint /pb/openapi/newad/hsaQueryWordReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 64. `lingxing_exp_ads_sb_target_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SB 投放日报。
- Endpoint: `/pb/openapi/newad/listHsaTargetingReport`
- Docs path: `docs/newAd/report/listHsaTargetingReport.md`
- Rate-limit endpoints: /pb/openapi/newad/listHsaTargetingReport
- Rate limit: 限流：endpoint /pb/openapi/newad/listHsaTargetingReport，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 65. `lingxing_exp_ads_sd_ad_group_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SD 广告组日报。
- Endpoint: `/pb/openapi/newad/sdAdGroupReports`
- Docs path: `docs/newAd/report/sdAdGroupReports.md`
- Rate-limit endpoints: /pb/openapi/newad/sdAdGroupReports
- Rate limit: 限流：endpoint /pb/openapi/newad/sdAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 66. `lingxing_exp_ads_sd_match_target_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SD 匹配目标日报。
- Endpoint: `/pb/openapi/newad/sdMatchTargetReports`
- Docs path: `docs/newAd/report/sdMatchTargetReports.md`
- Rate-limit endpoints: /pb/openapi/newad/sdMatchTargetReports
- Rate limit: 限流：endpoint /pb/openapi/newad/sdMatchTargetReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 67. `lingxing_exp_ads_sp_ad_group_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SP 广告组日报。
- Endpoint: `/pb/openapi/newad/spAdGroupReports`
- Docs path: `docs/newAd/report/spAdGroupReports.md`
- Rate-limit endpoints: /pb/openapi/newad/spAdGroupReports
- Rate limit: 限流：endpoint /pb/openapi/newad/spAdGroupReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 68. `lingxing_exp_ads_sp_placement_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SP 广告位日报。
- Endpoint: `/pb/openapi/newad/campaignPlacementReports`
- Docs path: `docs/newAd/report/campaignPlacementReports.md`
- Rate-limit endpoints: /pb/openapi/newad/campaignPlacementReports
- Rate limit: 限流：endpoint /pb/openapi/newad/campaignPlacementReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 69. `lingxing_exp_ads_sp_purchased_asin_report`

- Origin: `endpoint_spec`
- Category: `ad_report`
- Description: 实验层：SP 已购买 ASIN 报表。
- Endpoint: `/pb/openapi/newad/asinReports`
- Docs path: `docs/newAd/report/asinReports.md`
- Rate-limit endpoints: /pb/openapi/newad/asinReports
- Rate limit: 限流：endpoint /pb/openapi/newad/asinReports，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_date
- Optional args: profile_id, show_detail
- Input schema:

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

### 70. `lingxing_exp_finance_report_seller`

- Origin: `endpoint_spec`
- Category: `profit_report`
- Description: 实验层：结算利润报表店铺视角。
- Endpoint: `/bd/profit/report/open/report/seller/list`
- Docs path: `docs/Finance/bdSeller.md`
- Rate-limit endpoints: /bd/profit/report/open/report/seller/list
- Rate limit: 限流：endpoint /bd/profit/report/open/report/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: currency_code, monthly_query, order_status
- Input schema:

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

### 71. `lingxing_fba_stock_aggregate`

- Origin: `endpoint_spec`
- Category: `stock`
- Description: FBA 库存新报表汇总。
- Endpoint: `/cost/center/openApi/fba/gather/query`
- Docs path: `docs/Statistics/FbaStockAggregateListNew.md`
- Rate-limit endpoints: /cost/center/openApi/fba/gather/query
- Rate limit: 限流：endpoint /cost/center/openApi/fba/gather/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_month, end_month
- Optional args: None
- Input schema:

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

### 72. `lingxing_fba_stock_detail`

- Origin: `endpoint_spec`
- Category: `stock`
- Description: FBA 库存新报表明细。
- Endpoint: `/cost/center/openApi/fba/detail/query`
- Docs path: `docs/Statistics/FbaStockDetailListNew.md`
- Rate-limit endpoints: /cost/center/openApi/fba/detail/query
- Rate limit: 限流：endpoint /cost/center/openApi/fba/detail/query，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_month, end_month
- Optional args: None
- Input schema:

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

### 73. `lingxing_fba_warehouse_detail`

- Origin: `endpoint_spec`
- Category: `warehouse`
- Description: 按 ASIN、MSKU、SKU、FNSKU 等字段查询领星 FBA 仓库库存明细，用于获取可售、在途、调仓和调查中等库存字段。
- Endpoint: `/basicOpen/openapi/storage/fbaWarehouseDetail`
- Docs path: `docs/Warehouse/FBAStock_v2.md`
- Rate-limit endpoints: /basicOpen/openapi/storage/fbaWarehouseDetail
- Rate limit: 限流：endpoint /basicOpen/openapi/storage/fbaWarehouseDetail，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: search_field, search_value, cid, bid, attribute, asin_principal, status, senior_search_list, fulfillment_channel_type, is_hide_zero_stock, is_parant_asin_merge, is_contain_del_ls, query_fba_storage_quantity_list
- Input schema:

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

### 74. `lingxing_finance_report_asin`

- Origin: `endpoint_spec`
- Category: `profit_report`
- Description: 结算利润报表 ASIN 视角。
- Endpoint: `/bd/profit/report/open/report/asin/list`
- Docs path: `docs/Finance/bdASIN.md`
- Rate-limit endpoints: /bd/profit/report/open/report/asin/list
- Rate limit: 限流：endpoint /bd/profit/report/open/report/asin/list，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。
- Required args: sid, start_date, end_date
- Optional args: currency_code, search_value, monthly_query, summary_enabled, order_status
- Input schema:

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

### 75. `lingxing_health_check`

- Origin: `manual`
- Category: `manual`
- Description: 检查领星环境变量、token 状态和基础连通性，不拉业务数据。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /api/auth-server/oauth/access-token
- Rate limit: 限流：endpoint /api/auth-server/oauth/access-token，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: None
- Input schema:

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 76. `lingxing_local_product_costs`

- Origin: `manual`
- Category: `manual`
- Description: 按本地 SKU 或 SKU 标识查询领星本地产品成本，返回采购价、头程运输成本、采购员和供应商报价。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/routing/data/local_inventory/productList
- Rate limit: 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: sku_list, sku_identifier_list, update_time_start, update_time_end, create_time_start, create_time_end, page_size, include_supplier_quotes, include_raw
- Input schema:

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

### 77. `lingxing_local_products`

- Origin: `endpoint_spec`
- Category: `product`
- Description: 按本地 SKU 或 SKU 标识查询领星本地产品列表，包含采购成本和供应商报价原始字段。
- Endpoint: `/erp/sc/routing/data/local_inventory/productList`
- Docs path: `docs/Product/ProductLists.md`
- Rate-limit endpoints: /erp/sc/routing/data/local_inventory/productList
- Rate limit: 限流：endpoint /erp/sc/routing/data/local_inventory/productList，1 req/s，burst 1，来源 conservative；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: sku_list, sku_identifier_list, update_time_start, update_time_end, create_time_start, create_time_end
- Input schema:

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

### 78. `lingxing_marketplaces`

- Origin: `manual`
- Category: `manual`
- Description: 返回领星市场列表，并补充站点时区映射。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/seller/allMarketplace
- Rate limit: 限流：endpoint /erp/sc/data/seller/allMarketplace，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: None
- Input schema:

```json
{
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

### 79. `lingxing_multi_channel_orders`

- Origin: `manual`
- Category: `manual`
- Description: 查询亚马逊多渠道订单列表，按店铺 sid、日期范围和订单状态过滤；可选补充商品、物流、交易明细、退换货详情。为避免领星默认拉取最近 6 个月，本工具强制要求 start_date/end_date。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /order/amzod/api/orderList, /order/amzod/api/orderDetails/productInformation, /order/amzod/api/orderDetails/logisticsInformation, /order/amzod/api/orderDetails/returnInformation, /basicOpen/openapi/salesOrder/multi-channel/list/transaction
- Rate limit: 限流：聚合工具，涉及 5 个 endpoint；最严格为 /order/amzod/api/orderList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: sids, start_date, end_date
- Optional args: date_type, order_status, amazon_order_id, seller_fulfillment_order_id, include_product_detail, include_logistics_detail, include_transaction_detail, include_return_detail, page_size, max_records
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "sids": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "领星店铺 sid 列表，至少 1 个。",
      "minItems": 1
    },
    "start_date": {
      "type": "string",
      "description": "订购时间或修改时间开始日期，YYYY-MM-DD。"
    },
    "end_date": {
      "type": "string",
      "description": "订购时间或修改时间结束日期，YYYY-MM-DD。"
    },
    "date_type": {
      "type": "integer",
      "description": "查询日期类型：1 订购时间，2 订单修改时间；默认 1。"
    },
    "order_status": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "订单状态枚举，需使用官方大写值，例如 NEW、PROCESSING、COMPLETE、CANCELLED。"
    },
    "amazon_order_id": {
      "type": "string",
      "description": "可选；在列表结果返回后按亚马逊订单号精确过滤。"
    },
    "seller_fulfillment_order_id": {
      "type": "string",
      "description": "可选；在列表结果返回后按卖家订单号精确过滤。"
    },
    "include_product_detail": {
      "type": "boolean",
      "description": "是否补充商品详情，默认 false。"
    },
    "include_logistics_detail": {
      "type": "boolean",
      "description": "是否补充物流详情，默认 false。"
    },
    "include_transaction_detail": {
      "type": "boolean",
      "description": "是否逐单补充交易明细，默认 false；该接口 1 req/s，订单多时会较慢。"
    },
    "include_return_detail": {
      "type": "boolean",
      "description": "是否补充退换货详情，默认 false。"
    },
    "page_size": {
      "type": "integer",
      "description": "分页大小，1 到 1000，默认 200。"
    },
    "max_records": {
      "type": "integer",
      "description": "最多拉取记录数，1 到 5000，默认 1000。"
    }
  },
  "required": [
    "sids",
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 80. `lingxing_order_details`

- Origin: `manual`
- Category: `manual`
- Description: 按亚马逊订单号查询订单详情，支持单个或多个订单号；多个订单号会按领星接口上限每 200 个自动分批请求。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/mws/orderDetail, /erp/sc/data/seller/lists, /erp/sc/data/seller/allMarketplace
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/mws/orderDetail 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: None
- Optional args: order_id, order_ids
- Input schema:

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

### 81. `lingxing_order_lists`

- Origin: `manual`
- Category: `manual`
- Description: 按店铺与时间窗口拉取订单列表 Orderlists，并自动合并分页。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/mws/orders
- Rate limit: 限流：endpoint /erp/sc/data/mws/orders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: date_type
- Input schema:

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

### 82. `lingxing_product_performance`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 产品表现汇总，可按 ASIN / 父ASIN / MSKU 查询浏览、会话、广告和销量指标。
- Endpoint: `/bd/productPerformance/openApi/asinList`
- Docs path: `docs/Statistics/AsinListNew.md`
- Rate-limit endpoints: /bd/productPerformance/openApi/asinList
- Rate limit: 限流：endpoint /bd/productPerformance/openApi/asinList，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: search_field, search_value, summary_field, mid, currency_code, is_recently_enum, purchase_status, sort_field, sort_type
- Input schema:

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

### 83. `lingxing_profit_asin`

- Origin: `endpoint_spec`
- Category: `profit`
- Description: ASIN 维度利润统计。
- Endpoint: `/bd/profit/statistics/open/asin/list`
- Docs path: `docs/Statistics/statisticsOpenASIN.md`
- Rate-limit endpoints: /bd/profit/statistics/open/asin/list
- Rate limit: 限流：endpoint /bd/profit/statistics/open/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: currency_code, search_value
- Input schema:

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

### 84. `lingxing_profit_parent_asin`

- Origin: `endpoint_spec`
- Category: `profit`
- Description: 父 ASIN 维度利润统计。
- Endpoint: `/bd/profit/statistics/open/parent/asin/list`
- Docs path: `docs/Statistics/statisticsOpenParent.md`
- Rate-limit endpoints: /bd/profit/statistics/open/parent/asin/list
- Rate limit: 限流：endpoint /bd/profit/statistics/open/parent/asin/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: currency_code, search_value
- Input schema:

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

### 85. `lingxing_profit_report_order_list`

- Origin: `endpoint_spec`
- Category: `profit_report_order`
- Description: 查询利润报表订单 Transaction 视图；默认返回摘要，full 仅供本地 Excel 导出器。fee_type 映射到官方 eventSource，listing_owner 映射到官方 principalUids。
- Endpoint: `/basicOpen/finance/profitReport/order/transcation/list`
- Docs path: `docs/Finance/profitReportOrderTranscationList.md`
- Rate-limit endpoints: /basicOpen/finance/profitReport/order/transcation/list
- Rate limit: 限流：endpoint /basicOpen/finance/profitReport/order/transcation/list，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: start_date, end_date
- Optional args: search_date_field, sids, mids, fee_type, listing_owner, currency_code, search_field, search_value, sort_field, sort_type, settlement_status, fund_transfer_status, account_type, fulfillment, product_developer_uids, order_status, gmt_modified_start_date, gmt_modified_end_date, response_mode, preview_limit
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "start_date": {
      "type": "string"
    },
    "end_date": {
      "type": "string"
    },
    "search_date_field": {
      "type": "string"
    },
    "sids": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "mids": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "fee_type": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "listing_owner": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "currency_code": {
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
    "sort_field": {
      "type": "string"
    },
    "sort_type": {
      "type": "string"
    },
    "settlement_status": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "fund_transfer_status": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "account_type": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "fulfillment": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "product_developer_uids": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "order_status": {
      "type": "string"
    },
    "gmt_modified_start_date": {
      "type": "string"
    },
    "gmt_modified_end_date": {
      "type": "string"
    },
    "response_mode": {
      "type": "string",
      "description": "默认 summary，仅返回预览；full 仅供本地 Excel 导出器调用。",
      "default": "summary",
      "enum": [
        "summary",
        "full"
      ]
    },
    "preview_limit": {
      "type": "integer",
      "description": "summary 模式预览条数，默认 20。",
      "default": 20,
      "minimum": 0,
      "maximum": 100
    }
  },
  "required": [
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 86. `lingxing_profit_seller`

- Origin: `endpoint_spec`
- Category: `profit`
- Description: 店铺维度利润统计。
- Endpoint: `/bd/profit/statistics/open/seller/list`
- Docs path: `docs/Statistics/statisticsOpenSeller.md`
- Rate-limit endpoints: /bd/profit/statistics/open/seller/list
- Rate limit: 限流：endpoint /bd/profit/statistics/open/seller/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: currency_code, search_value, monthly_query
- Input schema:

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

### 87. `lingxing_promotion_coupon`

- Origin: `manual`
- Category: `manual`
- Description: 拉取优惠券活动列表，并补充 coupon.amount_off / coupon.percent_off 标签。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotionalActivities/coupon/list
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/coupon/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: None
- Input schema:

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

### 88. `lingxing_promotion_listing`

- Origin: `manual`
- Category: `manual`
- Description: 拉取 promotionListingList，用于判断 ASIN 在某个日期窗口是否命中促销。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotion/listingList
- Rate limit: 限流：endpoint /basicOpen/promotion/listingList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, site_date, start_time, end_time
- Optional args: status, product_status, promotion_category
- Input schema:

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

### 89. `lingxing_promotion_manage`

- Origin: `manual`
- Category: `manual`
- Description: 拉取管理促销列表，并归类 buy_one_get_one / purchase_discount / fixed_price / social_media。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotionalActivities/manage/list
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/manage/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: None
- Input schema:

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

### 90. `lingxing_promotion_sec_kill`

- Origin: `manual`
- Category: `manual`
- Description: 拉取秒杀活动列表，并补充 best_deal / lightning_deal 标签。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotionalActivities/secKill/list
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/secKill/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: None
- Input schema:

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

### 91. `lingxing_promotion_vip_discount`

- Origin: `manual`
- Category: `manual`
- Description: 拉取会员折扣/价格折扣列表，并归类 prime_exclusive / all_customers。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotionalActivities/vipDiscount/list
- Rate limit: 限流：endpoint /basicOpen/promotionalActivities/vipDiscount/list，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: None
- Input schema:

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

### 92. `lingxing_rate_limit_policy`

- Origin: `manual`
- Category: `manual`
- Description: 返回当前 MCP 工具到领星 OpenAPI endpoint 的限流政策，供客户端 agent 在调用前按 endpoint 自主排队。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: None
- Rate limit: 限流：本工具不直接调用领星业务 OpenAPI，或仅返回本地网关策略；客户端可并发调用，但不应把它作为业务查询循环。
- Required args: None
- Optional args: tool_name
- Input schema:

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

### 93. `lingxing_refund_orders`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 查询 FBA customer returns 报表，返回 FBA 退货订单源表原始数据。
- Endpoint: `/erp/sc/data/mws_report/refundOrders`
- Docs path: `docs/SourceData/RefundOrders.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/refundOrders
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/refundOrders，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: date_type
- Input schema:

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

### 94. `lingxing_replenishment_asin_info`

- Origin: `endpoint_spec`
- Category: `replenishment_info`
- Description: 补货建议 ASIN 明细。
- Endpoint: `/erp/sc/routing/fbaSug/asin/getInfo`
- Docs path: `docs/FBASug/InfoASIN.md`
- Rate-limit endpoints: /erp/sc/routing/fbaSug/asin/getInfo
- Rate limit: 限流：endpoint /erp/sc/routing/fbaSug/asin/getInfo，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, asin
- Optional args: mode
- Input schema:

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

### 95. `lingxing_replenishment_summary`

- Origin: `endpoint_spec`
- Category: `replenishment_summary`
- Description: 补货建议列表。
- Endpoint: `/erp/sc/routing/restocking/analysis/getSummaryList`
- Docs path: `docs/FBASug/GetSummaryList.md`
- Rate-limit endpoints: /erp/sc/routing/restocking/analysis/getSummaryList
- Rate limit: 限流：endpoint /erp/sc/routing/restocking/analysis/getSummaryList，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: asin, mode
- Input schema:

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

### 96. `lingxing_report_export_create`

- Origin: `manual`
- Category: `manual`
- Description: 创建亚马逊报告导出任务。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/report/create/reportExportTask
- Rate limit: 限流：endpoint /basicOpen/report/create/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, report_type
- Optional args: data_start_time, data_end_time, marketplace_ids, region, seller_id
- Input schema:

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

### 97. `lingxing_report_export_download`

- Origin: `manual`
- Category: `manual`
- Description: 下载并解析亚马逊报告导出文件。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/report/query/reportExportTask, /basicOpen/report/amazonReportExportTask
- Rate limit: 限流：聚合工具，涉及 2 个 endpoint；最严格为 /basicOpen/report/query/reportExportTask 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: None
- Optional args: url, sid, task_id, report_document_id, region, seller_id
- Input schema:

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

### 98. `lingxing_report_export_query`

- Origin: `manual`
- Category: `manual`
- Description: 查询亚马逊报告导出任务结果。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/report/query/reportExportTask
- Rate limit: 限流：endpoint /basicOpen/report/query/reportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: task_id
- Optional args: sid, region, seller_id
- Input schema:

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

### 99. `lingxing_report_export_refresh_url`

- Origin: `manual`
- Category: `manual`
- Description: 续期亚马逊报告下载链接。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/report/amazonReportExportTask
- Rate limit: 限流：endpoint /basicOpen/report/amazonReportExportTask，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: report_document_id
- Optional args: sid, region, seller_id
- Input schema:

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

### 100. `lingxing_resolve_daily_promotions`

- Origin: `manual`
- Category: `manual`
- Description: 输入 sid + target_date，汇总 listing 和各促销详情，输出 ASIN 当天命中的统一促销标签。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /basicOpen/promotion/listingList, /basicOpen/promotionalActivities/secKill/list, /basicOpen/promotionalActivities/manage/list, /basicOpen/promotionalActivities/vipDiscount/list, /basicOpen/promotionalActivities/coupon/list
- Rate limit: 限流：聚合工具，涉及 5 个 endpoint；最严格为 /basicOpen/promotion/listingList 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: sid, target_date
- Optional args: lookback_days
- Input schema:

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

### 101. `lingxing_return_analysis`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 查询退货分析，按 MSKU / ASIN / 父 ASIN / SKU / SPU 等维度统计退货数量、退货件数、退货率和退货原因相关指标。
- Endpoint: `/basicOpen/salesAnalysis/returnOrder/analysisLists`
- Docs path: `docs/Statistics/ReturnOrderAnalysisLists.md`
- Rate-limit endpoints: /basicOpen/salesAnalysis/returnOrder/analysisLists
- Rate limit: 限流：endpoint /basicOpen/salesAnalysis/returnOrder/analysisLists，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: startDate, endDate, asinType, dateType
- Optional args: mids, principalUid, searchField, searchValue, sortField, sortType, storeId
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "startDate": {
      "type": "string"
    },
    "endDate": {
      "type": "string"
    },
    "asinType": {
      "type": "string"
    },
    "dateType": {
      "type": "integer"
    },
    "mids": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "principalUid": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "searchField": {
      "type": "string"
    },
    "searchValue": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "sortField": {
      "type": "string"
    },
    "sortType": {
      "type": "string"
    },
    "storeId": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    }
  },
  "required": [
    "startDate",
    "endDate",
    "asinType",
    "dateType"
  ],
  "additionalProperties": false
}
```

### 102. `lingxing_sales_outbound_orders`

- Origin: `manual`
- Category: `manual`
- Description: 通过领星 OpenAPI 查询 ERP 销售出库单。可传 sids 或 amazon_seller_ids 定向查询；两者都不传时省略官方 sid_arr，一次 MCP 调用查询全部店铺，并按官方每页 200 条限制合并全部分页。默认 time_type=stock_delivered_at，按库存流水出库时间筛选。默认只返回摘要预览；生成 Excel 时由本地导出器使用 response_mode=full，避免把全量 JSON 放入模型上下文。
- Endpoint: `Manual`
- Docs path: `docs/Warehouse/WmsOrderList.md`
- Rate-limit endpoints: /erp/sc/data/seller/lists, /erp/sc/data/seller/allMarketplace, /erp/sc/routing/wms/order/wmsOrderList
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: start_date, end_date
- Optional args: sids, amazon_seller_ids, time_type, status, logistics_status, platform_order_numbers, system_order_numbers, outbound_order_numbers, response_mode, preview_limit
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "start_date": {
      "type": "string",
      "description": "开始日期，YYYY-MM-DD。"
    },
    "end_date": {
      "type": "string",
      "description": "结束日期，YYYY-MM-DD。"
    },
    "sids": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "可选；领星店铺 SID。与 amazon_seller_ids 均不传时查询全部店铺。"
    },
    "amazon_seller_ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "可选；亚马逊 seller_id，由服务端解析为官方 sid_arr。"
    },
    "time_type": {
      "type": "string",
      "description": "create_at、delivered_at、stock_delivered_at 或 update_at；默认 stock_delivered_at。"
    },
    "status": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "出库单状态：1 物流下单、2 待出库、3 已出库、4 已截单。"
    },
    "logistics_status": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "platform_order_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "system_order_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "outbound_order_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "response_mode": {
      "type": "string",
      "enum": [
        "summary",
        "full"
      ],
      "description": "默认 summary，仅返回预览；full 仅供本地 Excel 导出器调用。"
    },
    "preview_limit": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "summary 模式预览条数，默认 20。"
    }
  },
  "required": [
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 103. `lingxing_seller_lists`

- Origin: `manual`
- Category: `manual`
- Description: 获取亚马逊店铺列表，返回 sid、店铺名、站点、时区等信息；可按状态或站点过滤。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/seller/lists, /erp/sc/data/seller/allMarketplace
- Rate limit: 限流：聚合工具，涉及 2 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: None
- Optional args: status, marketplace
- Input schema:

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

### 104. `lingxing_shipment_settlement_report`

- Origin: `manual`
- Category: `manual`
- Description: 通过领星 OpenAPI 查询亚马逊发货与结算差异数据。可传 sids 或 amazon_seller_ids 定向查询；两者都不传时，一次 MCP 调用自动覆盖全部启用中的亚马逊店铺；服务端按站点分组请求，并按官方每页 1000 条限制合并全部分页，避免跨站点混合数组返回空结果。默认 time_type=04，按结算时间筛选。默认只返回摘要预览；生成 Excel 时由本地导出器使用 response_mode=full，避免把全量 JSON 放入模型上下文。
- Endpoint: `Manual`
- Docs path: `docs/Finance/SettlementReport.md`
- Rate-limit endpoints: /erp/sc/data/seller/lists, /erp/sc/data/seller/allMarketplace, /cost/center/api/settlement/report
- Rate limit: 限流：聚合工具，涉及 3 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: start_date, end_date
- Optional args: sids, amazon_seller_ids, time_type, country_codes, order_numbers, shipment_numbers, custom_numbers, mskus, skus, product_names, track_codes, fulfillment_type, response_mode, preview_limit
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "start_date": {
      "type": "string",
      "description": "开始日期，YYYY-MM-DD，双闭区间。"
    },
    "end_date": {
      "type": "string",
      "description": "结束日期，YYYY-MM-DD，双闭区间。"
    },
    "sids": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "可选；领星店铺 SID。与 amazon_seller_ids 均不传时查询全部启用店铺。"
    },
    "amazon_seller_ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "可选；亚马逊 seller_id。服务端自动解析配对 SID。"
    },
    "time_type": {
      "type": "string",
      "description": "时间类型：01 下单、02 付款、03 发货、04 结算、05 转账、06 更新；默认 04。"
    },
    "country_codes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "order_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "shipment_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "custom_numbers": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "mskus": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "skus": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "product_names": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "track_codes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "fulfillment_type": {
      "type": "string",
      "description": "可选；01 表示 FBA，不传表示全部。"
    },
    "response_mode": {
      "type": "string",
      "enum": [
        "summary",
        "full"
      ],
      "description": "默认 summary，仅返回预览；full 仅供本地 Excel 导出器调用。"
    },
    "preview_limit": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "description": "summary 模式预览条数，默认 20。"
    }
  },
  "required": [
    "start_date",
    "end_date"
  ],
  "additionalProperties": false
}
```

### 105. `lingxing_smoke_check`

- Origin: `manual`
- Category: `manual`
- Description: 按 SellerLists -> StoreSales -> Orderlists -> promotionListingList 做最小烟测。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/seller/lists, /erp/sc/data/seller/allMarketplace, /erp/sc/data/sales_report/sales, /erp/sc/data/mws/orders, /basicOpen/promotion/listingList, /basicOpen/baseData/account/list, /pb/openapi/newad/spProductAdReports, /pb/openapi/newad/sdProductAdReports, /pb/openapi/newad/hsaPurchasedAsinReports, /bd/profit/statistics/open/seller/list, /erp/sc/data/mws_report/allOrders, /erp/sc/data/mws_report/manageInventory
- Rate limit: 限流：聚合工具，涉及 12 个 endpoint；最严格为 /erp/sc/data/seller/lists 1 req/s，burst 1；客户端应按 endpoint 分组排队，避免并发拆分同类查询；完整策略可调用 lingxing_rate_limit_policy。
- Required args: None
- Optional args: sid, date
- Input schema:

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

### 106. `lingxing_source_all_orders`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 亚马逊源表所有订单。
- Endpoint: `/erp/sc/data/mws_report/allOrders`
- Docs path: `docs/SourceData/AllOrders.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/allOrders
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/allOrders，10 req/s，burst 10，来源 openapi_docs；该 endpoint 允许较高吞吐；客户端并发不应超过 burst=10，长期速率不应超过 10 req/s。
- Required args: sid, start_date, end_date
- Optional args: date_type
- Input schema:

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

### 107. `lingxing_source_daily_inventory`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 亚马逊源表每日库存。
- Endpoint: `/erp/sc/data/mws_report/dailyInventory`
- Docs path: `docs/SourceData/DailyInventory.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/dailyInventory
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/dailyInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, event_date
- Optional args: None
- Input schema:

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

### 108. `lingxing_source_manage_inventory`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 亚马逊源表 FBA 库存。
- Endpoint: `/erp/sc/data/mws_report/manageInventory`
- Docs path: `docs/SourceData/ManageInventory.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/manageInventory
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/manageInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: None
- Input schema:

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

### 109. `lingxing_source_reserved_inventory`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 亚马逊源表预留库存。
- Endpoint: `/erp/sc/data/mws_report/reservedInventory`
- Docs path: `docs/SourceData/ReservedInventory.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/reservedInventory
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/reservedInventory，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid
- Optional args: None
- Input schema:

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

### 110. `lingxing_source_transaction`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 亚马逊源表交易明细。
- Endpoint: `/erp/sc/data/mws_report/transaction`
- Docs path: `docs/SourceData/Transaction.md`
- Rate-limit endpoints: /erp/sc/data/mws_report/transaction
- Rate limit: 限流：endpoint /erp/sc/data/mws_report/transaction，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, event_date
- Optional args: None
- Input schema:

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

### 111. `lingxing_store_sales`

- Origin: `manual`
- Category: `manual`
- Description: 按店铺和日期范围拉取 StoreSales，并自动合并分页。
- Endpoint: `Manual`
- Docs path: `None`
- Rate-limit endpoints: /erp/sc/data/sales_report/sales
- Rate limit: 限流：endpoint /erp/sc/data/sales_report/sales，1 req/s，burst 1，来源 default；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: sid, start_date, end_date
- Optional args: None
- Input schema:

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

### 112. `lingxing_voice_of_buyer`

- Origin: `endpoint_spec`
- Category: `source`
- Description: 查询买家之声列表，返回 ASIN/MSKU/SKU 的满意度状况、不满意率、不满意订单数、订单总数、主要退货原因和退货标记。
- Endpoint: `/basicOpen/customerService/voiceOfBuyer/list`
- Docs path: `docs/Service/voiceOfBuyerList.md`
- Rate-limit endpoints: /basicOpen/customerService/voiceOfBuyer/list
- Rate limit: 限流：endpoint /basicOpen/customerService/voiceOfBuyer/list，1 req/s，burst 1，来源 openapi_docs；该 endpoint 按 1 秒 1 次串行调用；客户端不要对同一 endpoint 并发。
- Required args: None
- Optional args: fulfillment_channel, sids, pxc_health, search_field, search_value, return_badge
- Input schema:

```json
{
  "type": "object",
  "properties": {
    "fulfillment_channel": {
      "type": "string"
    },
    "sids": {
      "type": "array",
      "items": {
        "type": "integer"
      }
    },
    "pxc_health": {
      "type": "array",
      "items": {
        "type": "string"
      }
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
    "return_badge": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [],
  "additionalProperties": false
}
```
