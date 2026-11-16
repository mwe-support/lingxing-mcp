# 生产领星 MCP 官方 API 契约核对（2026-11-16）

基线为生产提交 `a94269415a0927bd1a3e4d20a60bbeca6a98f18d`。从生产注册表、角色配置、手写调用及聚合依赖整理出 113 个工具、109 个去重 API；另以 AST 字面量交叉检查调用范围，未发现清单外的业务/鉴权路径。核对全部注册实现，包括当前角色未开放的小时工具；本次不新增工具或扩大任何角色。

## 官方证据

109 对官方新版 HTML 和旧版 Markdown 均于本日成功获取。新版 schema 字段和表格、原始 Markdown 互相补核，保留 URL、UTC 获取时间、原文 SHA-256。所有 API 地址和方法匹配（仅官方两处省略路径开头斜杠）。[JSON快照](official-api-contracts-2026-11-16.json)保存逐接口证据；只有 2 个店铺/市场 GET，其余为 POST。下载链接使用原签名 CDN URL，不能把企业 Bearer 发送到 CDN。

仓库快照仅保留字段名、类型、必填等结构事实及来源，不复制整页或参数说明原文；核查原文保留在本地任务目录。

全部 API 的本地既有队列均不高于文档容量；保留较保守的速率，未以此次核对为理由提高生产并发。限流字段是本地策略，不能把本地1RPS误说成官方容量1。4个否定广告读取的来源标签已据此改为conservative。

## 修改与兼容

- 21 个日报采用官方 V2 顶层 next_token。游标请求不混入offset；重复游标或已知total尚未取全却无后续游标时明确失败。offset/page接口未返回total时按满页继续，保留未知total为null。
- 18 个广告基础对象原已采用游标，维持该方案；补 SP 否定类型与 SB 必填选择器。13 个小时工具按活动ID/聚合维度单次读取，不再错用日报参数或自动查询profile。
- 校验当前工具已有的官方必填项、声明的枚举、日期和批量边界；单店Listing/产品表现sid使用字符串。删除统计接口未有官方依据的monthly_query公开参数，按月查询继续使用结算利润报表。
- 写工具使用正式参数表的嵌套类型、必填和已知批次上限；两接口分别采用profile_id，其余profileId。JSON布尔双确认、state/bid以及固定基准值条件均在入口检查；可选数值字段不使用时应省略。
- 保留退货分析200条页大小、storeId数组、SID/Profile隔离、原工具名及角色配置。源报表停更/即将下线提示进入工具说明与结果warnings，不自行换到未审计的新接口。
- 官方新增可选字段在原始结果中继续透传；没有为每个可选字段另造工具能力、自动调度或真实写测试。

## 文档冲突与处理

- 部分广告页新公告称V2为游标，旧请求头表仍称offset。21日报请求/响应均有next_token，本次以该明确字段契约迁移；真实SP日报/基础两页游标已确认推进。
- 负ASIN文案称支持活动层级，但正式表将adGroupId列为必填。本次按参数表校验并更新工具说明，活动层级省略该字段的用法仍需官方澄清；没有真实写入探测。
- 活动budgetType正文daily、旧示例DAILY不一致，保留string透传，不臆造统一大小写。发货结算参数按正式camelCase表，未跟随示例改成全小写。
- 产品表现sid类型栏写object，文字明确单店字符串、多店数组；按文字规则和真实请求验证处理，不把类型栏误当成要求发送JSON对象。
- 12份旧式小时参数表同时标campaign_id和campaign_ids必填，按该表保留要求；SP target最新版明确二选一/合并去重最多50个，单独实现其规则。未为测试开放这些工具的角色权限。
- 日期上限按end-start的经过天数校验。统计差7天、结算利润报表差31天已获上游code=0；其他双闭日期个数的边界没有冒称逐一线上实测。订单一年按日历周年处理。
- 退货分析offset存在“页码/偏移量”表述混杂。固定官方支持的sortField后，length=2、offset=0/1/2按ASIN身份哈希观察到A/B、B/C、C/D，确认是记录位移；保留offset推进与200页长，默认显式按退货量排序。
- 退货分析新版写ASC/DESC，但真实上游对DESC返回code=400及“sortType只能是asc或desc”；省略和小写desc在length=2/200均成功。按运行证据兼容两种大小写输入，出站统一小写。最初大写候选未部署。

## 验证与部署

生产改动前源码已归档并保留tracked文件哈希：`/public/lingxing-mcp-backups/api-contract-sync-20261116-122511`，不包含运行凭证或token缓存。候选版本在独立目录测试后再部署，失败恢复原文件并重启。

最终验证结果：

- 服务器独立候选目录运行83项客户端、服务层、MCP、文档索引、XLSX、认证、审计和HTTP请求头测试全部通过；生产Python编译和角色检查通过。
- 真实只读服务验证20/20成功，包括13个小时报告、SP/SD日报、广告基础对象、产品表现、统计、同月财务和退货分析；另有15组有界读取/续页检查。部分样本返回空数据，只证明请求被接受，不冒称验证了全部业务数据的准确性。
- 生产已重启，运行工具schema与候选完全一致，原可见工具名与角色范围保持。角色数量minimal=14、operations=76、restricted_operations=73、finance=22、自定义codex_ads_test=31。
- 公网MCP鉴权、店铺GET、广告日报POST及完整只读烟测通过；烟测11个业务状态全部true、零警告。Bearer传输在真实发送前核验；没有token写回URL。
- 当前生产源码与Git同步采用附注tag `lingxing-official-api-contract-sync-2026-11-16`，它继续包含此前 `lingxing-official-auth-bearer-migration-2026-11-16` 的认证迁移提交。

写接口仅做离线替身/预演，没有执行真实业务写入；报告任务创建/下载不为验收而额外生成业务任务。没有声称对109个API逐个执行了真实业务调用。仓库及相邻模板目录缺少release_audit.py，该项未执行。

## 逐接口核对（109/109）

“契约一致”表示地址、方法及当前使用参数/数据路径经源码与官方逐项对照；不表示对该接口做了真实业务请求。所有行受共享认证/分页相关修复覆盖。容量是官方令牌桶容量，本地可能更保守。

| # | API / 关联工具 | 核对结果与处理 | 官方容量 | 官方文档 |
|---|---|---|---:|---|
| 1 | `POST /api/auth-server/oauth/access-token`<br>`lingxing_health_check` | multipart/缓存不变；接入已公布的集中限流 | 100 | [官方](https://apidoc.lingxing.com/new/api-docs/Authorization/GetToken/) |
| 2 | `POST /api/auth-server/oauth/refresh`<br>鉴权内部依赖 | multipart/一次性续约语义不变；接入集中限流 | 100 | [官方](https://apidoc.lingxing.com/new/api-docs/Authorization/RefreshToken/) |
| 3 | `POST /basicOpen/adReport/manage/putSpAdGroup`<br>`lingxing_ads_update_sp_ad_group` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/adReportManagePutSpAdGroup/) |
| 4 | `POST /basicOpen/adReport/manage/putSpCampaign`<br>`lingxing_ads_update_sp_campaign` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/adReportManagePutSpCampaign/) |
| 5 | `POST /basicOpen/adReport/manage/putSpKeyword`<br>`lingxing_ads_update_sp_keyword` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/adReportManagePutSpKeyword/) |
| 6 | `POST /basicOpen/adReport/manage/putSpProductAds`<br>`lingxing_ads_update_sp_product_ads` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/adReportManagePutSpProductAds/) |
| 7 | `POST /basicOpen/adReport/manage/putSpTarget`<br>`lingxing_ads_update_sp_target` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/adReportManagePutSpTarget/) |
| 8 | `POST /basicOpen/adReport/spTarget/addKeywords`<br>`lingxing_ads_add_sp_keywords` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/SpAddKeywords/) |
| 9 | `POST /basicOpen/adReport/spTarget/addNegativeKeywords`<br>`lingxing_ads_add_sp_negative_keywords` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/SpAddNegativeKeywords/) |
| 10 | `POST /basicOpen/adReport/spTarget/addNegativeTargets`<br>`lingxing_ads_add_sp_negative_targets` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/SpAddNegativeTargets/) |
| 11 | `POST /basicOpen/adReport/spTarget/archiveNegatives`<br>`lingxing_ads_archive_sp_negatives` | 嵌套必填/类型/枚举/已知批次上限及严格预演双确认校验；未做真实写入 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/SpArchiveNegatives/) |
| 12 | `POST /basicOpen/baseData/account/list`<br>`lingxing_smoke_check`<br>`lingxing_ad_accounts`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/dspAccountList/) |
| 13 | `POST /basicOpen/customerService/voiceOfBuyer/list`<br>`lingxing_voice_of_buyer` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Service/voiceOfBuyerList/) |
| 14 | `POST /basicOpen/finance/profitReport/order/transcation/list`<br>`lingxing_profit_report_order_list` | 校验Deferred结束日为今天；保留原字段映射/摘要导出 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Finance/profitReportOrderTranscationList/) |
| 15 | `POST /basicOpen/openapi/salesOrder/multi-channel/list/transaction`<br>`lingxing_multi_channel_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/MutilChannelTransactionDetail/) |
| 16 | `POST /basicOpen/openapi/storage/fbaWarehouseDetail`<br>`lingxing_asin_product_snapshot`<br>`lingxing_fba_warehouse_detail` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Warehouse/FBAStock_v2/) |
| 17 | `POST /basicOpen/promotion/listingList`<br>`lingxing_promotion_listing`<br>`lingxing_resolve_daily_promotions`<br>`lingxing_smoke_check`<br>`lingxing_asin_weekly_rollup` | 日期跨度90天检查；保留原活动归一化与分页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/promotionListingList/) |
| 18 | `POST /basicOpen/promotionalActivities/coupon/list`<br>`lingxing_promotion_coupon`<br>`lingxing_resolve_daily_promotions`<br>`lingxing_asin_weekly_rollup` | 日期跨度90天检查；保留原活动归一化与分页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/promotionalActivitiesCouponList/) |
| 19 | `POST /basicOpen/promotionalActivities/manage/list`<br>`lingxing_promotion_manage`<br>`lingxing_resolve_daily_promotions`<br>`lingxing_asin_weekly_rollup` | 日期跨度90天检查；保留原活动归一化与分页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/promotionalActivitiesManageList/) |
| 20 | `POST /basicOpen/promotionalActivities/secKill/list`<br>`lingxing_promotion_sec_kill`<br>`lingxing_resolve_daily_promotions`<br>`lingxing_asin_weekly_rollup` | 日期跨度90天检查；保留原活动归一化与分页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/promotionalActivitiesSecKillList/) |
| 21 | `POST /basicOpen/promotionalActivities/vipDiscount/list`<br>`lingxing_promotion_vip_discount`<br>`lingxing_resolve_daily_promotions`<br>`lingxing_asin_weekly_rollup` | 日期跨度90天检查；保留原活动归一化与分页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/promotionalActivitiesVipDiscountList/) |
| 22 | `POST /basicOpen/report/amazonReportExportTask`<br>`lingxing_report_export_refresh_url`<br>`lingxing_report_export_download` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/AmazonReportExportTask/) |
| 23 | `POST /basicOpen/report/create/reportExportTask`<br>`lingxing_report_export_create` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/reportCreateReportExportTask/) |
| 24 | `POST /basicOpen/report/query/reportExportTask`<br>`lingxing_report_export_query`<br>`lingxing_report_export_download` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/reportQueryReportExportTask/) |
| 25 | `POST /basicOpen/salesAnalysis/returnOrder/analysisLists`<br>`lingxing_return_analysis` | 必填/枚举/366天检查，sortType兼容大小写并按实测出站小写；保留 storeId 数组及 length=200 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/ReturnOrderAnalysisLists/) |
| 26 | `POST /bd/productPerformance/openApi/asinList`<br>`lingxing_asin_product_snapshot`<br>`lingxing_product_search`<br>`lingxing_product_performance` | 单店 sid 改字符串；搜索最多50项、时间跨度92天；多店数组/200店保持 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/AsinListNew/) |
| 27 | `POST /bd/profit/report/open/report/asin/list`<br>`lingxing_finance_report_asin` | 按天跨度31天；按月YYYY-MM且同月 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Finance/bdASIN/) |
| 28 | `POST /bd/profit/report/open/report/seller/list`<br>`lingxing_exp_finance_report_seller` | 按天跨度31天；按月YYYY-MM且同月 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Finance/bdSeller/) |
| 29 | `POST /bd/profit/statistics/open/asin/list`<br>`lingxing_profit_asin` | 校验YYYY-MM-DD、跨度7天；字段/返回路径保持 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/statisticsOpenASIN/) |
| 30 | `POST /bd/profit/statistics/open/parent/asin/list`<br>`lingxing_profit_parent_asin` | 校验YYYY-MM-DD、跨度7天；字段/返回路径保持 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/statisticsOpenParent/) |
| 31 | `POST /bd/profit/statistics/open/seller/list`<br>`lingxing_smoke_check`<br>`lingxing_profit_seller` | 校验YYYY-MM-DD、跨度7天；字段/返回路径保持 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/statisticsOpenSeller/) |
| 32 | `POST /cost/center/api/settlement/report`<br>`lingxing_shipment_settlement_report` | 契约一致，保持现有受影响调用/分页/字段映射 | 3 | [官方](https://apidoc.lingxing.com/new/api-docs/Finance/SettlementReport/) |
| 33 | `POST /cost/center/openApi/fba/detail/query`<br>`lingxing_fba_stock_detail` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/FbaStockDetailListNew/) |
| 34 | `POST /cost/center/openApi/fba/gather/query`<br>`lingxing_fba_stock_aggregate` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/FbaStockAggregateListNew/) |
| 35 | `POST /erp/sc/data/mws/listing`<br>`lingxing_amazon_listing` | 出站 sid 改字符串；搜索最多10项，枚举校验 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/Listing/) |
| 36 | `POST /erp/sc/data/mws/orderDetail`<br>`lingxing_order_details` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/OrderDetail/) |
| 37 | `POST /erp/sc/data/mws/orders`<br>`lingxing_order_lists`<br>`lingxing_smoke_check` | 校验一年跨度、日期类型及type=3秒级格式 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/Orderlists/) |
| 38 | `POST /erp/sc/data/mws_report/allOrders`<br>`lingxing_smoke_check`<br>`lingxing_source_all_orders` | 烟测改 YYYY-MM-DD，相邻日期左闭右开 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/AllOrders/) |
| 39 | `POST /erp/sc/data/mws_report/dailyInventory`<br>`lingxing_source_daily_inventory` | 补2023-12-01后停止更新警告；修复无total续页 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/DailyInventory/) |
| 40 | `POST /erp/sc/data/mws_report/manageInventory`<br>`lingxing_smoke_check`<br>`lingxing_source_manage_inventory` | 契约一致，保持现有受影响调用/分页/字段映射 | 5 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/ManageInventory/) |
| 41 | `POST /erp/sc/data/mws_report/refundOrders`<br>`lingxing_refund_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/RefundOrders/) |
| 42 | `POST /erp/sc/data/mws_report/reservedInventory`<br>`lingxing_source_reserved_inventory` | 契约一致，保持现有受影响调用/分页/字段映射 | 5 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/ReservedInventory/) |
| 43 | `POST /erp/sc/data/mws_report/transaction`<br>`lingxing_source_transaction` | 补官方即将下线及每月3日后可查上月提示；不自行删除或迁移 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/SourceData/Transaction/) |
| 44 | `POST /erp/sc/data/sales_report/asinDailyLists`<br>`lingxing_asin_daily_lists` | 契约一致；共享分页修复无total首批截断 | 5 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/AsinDailyLists/) |
| 45 | `POST /erp/sc/data/sales_report/sales`<br>`lingxing_store_sales`<br>`lingxing_smoke_check`<br>`lingxing_asin_weekly_rollup` | 契约一致，保持现有受影响调用/分页/字段映射 | 5 | [官方](https://apidoc.lingxing.com/new/api-docs/Statistics/StoreSales/) |
| 46 | `GET /erp/sc/data/seller/allMarketplace`<br>`lingxing_seller_lists`<br>`lingxing_marketplaces`<br>`lingxing_order_details`<br>`lingxing_shipment_settlement_report`<br>`lingxing_sales_outbound_orders`<br>`lingxing_product_search`<br>`lingxing_smoke_check` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/BasicData/AllMarketplace/) |
| 47 | `GET /erp/sc/data/seller/lists`<br>`lingxing_seller_lists`<br>`lingxing_order_details`<br>`lingxing_shipment_settlement_report`<br>`lingxing_sales_outbound_orders`<br>`lingxing_product_search`<br>`lingxing_smoke_check` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/BasicData/SellerLists/) |
| 48 | `POST /erp/sc/routing/data/local_inventory/productList`<br>`lingxing_asin_product_snapshot`<br>`lingxing_local_product_costs`<br>`lingxing_local_products` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Product/ProductLists/) |
| 49 | `POST /erp/sc/routing/fbaSug/asin/getInfo`<br>`lingxing_replenishment_asin_info` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/FBASug/InfoASIN/) |
| 50 | `POST /erp/sc/routing/restocking/analysis/getSummaryList`<br>`lingxing_replenishment_summary` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/FBASug/GetSummaryList/) |
| 51 | `POST /erp/sc/routing/wms/order/wmsOrderList`<br>`lingxing_sales_outbound_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Warehouse/WmsOrderList/) |
| 52 | `POST /order/amzod/api/orderDetails/logisticsInformation`<br>`lingxing_multi_channel_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/LogisticsInformation/) |
| 53 | `POST /order/amzod/api/orderDetails/productInformation`<br>`lingxing_multi_channel_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/ProductInformation/) |
| 54 | `POST /order/amzod/api/orderDetails/returnInformation`<br>`lingxing_multi_channel_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/ReturnInfomation/) |
| 55 | `POST /order/amzod/api/orderList`<br>`lingxing_multi_channel_orders` | 契约一致，保持现有受影响调用/分页/字段映射 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/Sale/MCFOrderList/) |
| 56 | `POST /pb/openapi/newad/abaReport`<br>`lingxing_exp_ads_aba_report` | 校验最近45天内周日；维持 object 无分页 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/reportDownload/abaReport/) |
| 57 | `POST /pb/openapi/newad/apiLogStandard`<br>`lingxing_ads_operation_logs` | 日期至多一个月；meta 保留 total/offset/length，维持显式单页 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/apiLogStandard/) |
| 58 | `POST /pb/openapi/newad/asinReports`<br>`lingxing_exp_ads_sp_purchased_asin_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/asinReports/) |
| 59 | `POST /pb/openapi/newad/campaignPlacementReports`<br>`lingxing_exp_ads_sp_placement_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/campaignPlacementReports/) |
| 60 | `POST /pb/openapi/newad/hsaAdGroupReports`<br>`lingxing_exp_ads_sb_ad_group_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/hsaAdGroupReports/) |
| 61 | `POST /pb/openapi/newad/hsaAdGroups`<br>`lingxing_ads_sb_ad_groups` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/hsaAdGroups/) |
| 62 | `POST /pb/openapi/newad/hsaCampaignPlacementReports`<br>`lingxing_exp_ads_sb_campaign_placement_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/hsaCampaignPlacementReports/) |
| 63 | `POST /pb/openapi/newad/hsaCampaignReports`<br>`lingxing_ads_sb_campaign_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/hsaCampaignReports/) |
| 64 | `POST /pb/openapi/newad/hsaCampaigns`<br>`lingxing_ads_sb_campaigns` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/hsaCampaigns/) |
| 65 | `POST /pb/openapi/newad/hsaNegativeKeywords`<br>`lingxing_ads_sb_negative_keywords` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/hsaNegativeKeywords/) |
| 66 | `POST /pb/openapi/newad/hsaNegativeTargets`<br>`lingxing_ads_sb_negative_targets` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/hsaNegativeTargets/) |
| 67 | `POST /pb/openapi/newad/hsaProductAds`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup`<br>`lingxing_ads_sb_creatives` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sbAdHasProductAds/) |
| 68 | `POST /pb/openapi/newad/hsaPurchasedAsinReports`<br>`lingxing_smoke_check`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup`<br>`lingxing_ads_sb_purchased_asin_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/hsaPurchasedAsinReports/) |
| 69 | `POST /pb/openapi/newad/hsaQueryWordReports`<br>`lingxing_exp_ads_sb_search_term_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/hsaQueryWordReports/) |
| 70 | `POST /pb/openapi/newad/listHsaKeywordPlacementReport`<br>`lingxing_exp_ads_sb_keyword_placement_report` | 补 sponsored_type=ALL、target_type=keyword；V2 游标 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/listHsaKeywordPlacementReport/) |
| 71 | `POST /pb/openapi/newad/listHsaProductAdReport`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup`<br>`lingxing_ads_sb_creative_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/listHsaProductAdReport/) |
| 72 | `POST /pb/openapi/newad/listHsaTargetingReport`<br>`lingxing_exp_ads_sb_target_report` | 补 sponsored_type=ALL、target_type=ALL；V2 游标 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/listHsaTargetingReport/) |
| 73 | `POST /pb/openapi/newad/portfolios`<br>`lingxing_ads_portfolios` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/portfolios/) |
| 74 | `POST /pb/openapi/newad/queryWordReports`<br>`lingxing_ads_sp_search_term_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/queryWordReports/) |
| 75 | `POST /pb/openapi/newad/sbAdGroupHourData`<br>`lingxing_ads_sb_ad_group_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sbAdGroupHourData/) |
| 76 | `POST /pb/openapi/newad/sbAdPlacementHourData`<br>`lingxing_ads_sb_placement_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sbAdPlacementHourData/) |
| 77 | `POST /pb/openapi/newad/sbCampaignHourData`<br>`lingxing_ads_sb_campaign_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sbCampaignHourData/) |
| 78 | `POST /pb/openapi/newad/sbTargetHourData`<br>`lingxing_ads_sb_target_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sbTargetHourData/) |
| 79 | `POST /pb/openapi/newad/sbTargeting`<br>`lingxing_ads_sb_targets` | 补 ads_type=ALL、targeting_type=ALL | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sbTargeting/) |
| 80 | `POST /pb/openapi/newad/sdAdGroupHourData`<br>`lingxing_ads_sd_ad_group_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdAdGroupHourData/) |
| 81 | `POST /pb/openapi/newad/sdAdGroupReports`<br>`lingxing_exp_ads_sd_ad_group_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdAdGroupReports/) |
| 82 | `POST /pb/openapi/newad/sdAdGroups`<br>`lingxing_ads_sd_ad_groups` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sdAdGroups/) |
| 83 | `POST /pb/openapi/newad/sdAdvertiseHourData`<br>`lingxing_ads_sd_advertise_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdAdvertiseHourData/) |
| 84 | `POST /pb/openapi/newad/sdCampaignHourData`<br>`lingxing_ads_sd_campaign_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdCampaignHourData/) |
| 85 | `POST /pb/openapi/newad/sdCampaignReports`<br>`lingxing_ads_sd_campaign_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdCampaignReports/) |
| 86 | `POST /pb/openapi/newad/sdCampaigns`<br>`lingxing_ads_sd_campaigns` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sdCampaigns/) |
| 87 | `POST /pb/openapi/newad/sdMatchTargetReports`<br>`lingxing_exp_ads_sd_match_target_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdMatchTargetReports/) |
| 88 | `POST /pb/openapi/newad/sdNegativeTargets`<br>`lingxing_ads_sd_negative_targets` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sdNegativeTargets/) |
| 89 | `POST /pb/openapi/newad/sdProductAdReports`<br>`lingxing_smoke_check`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup`<br>`lingxing_ads_sd_product_ad_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdProductAdReports/) |
| 90 | `POST /pb/openapi/newad/sdProductAds`<br>`lingxing_ads_sd_product_ads` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sdProductAds/) |
| 91 | `POST /pb/openapi/newad/sdTargetHourData`<br>`lingxing_ads_sd_target_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdTargetHourData/) |
| 92 | `POST /pb/openapi/newad/sdTargetReports`<br>`lingxing_ads_sd_target_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/sdTargetReports/) |
| 93 | `POST /pb/openapi/newad/sdTargets`<br>`lingxing_ads_sd_targets` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/sdTargets/) |
| 94 | `POST /pb/openapi/newad/spAdGroupHourData`<br>`lingxing_ads_sp_ad_group_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spAdGroupHourData/) |
| 95 | `POST /pb/openapi/newad/spAdGroupReports`<br>`lingxing_exp_ads_sp_ad_group_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spAdGroupReports/) |
| 96 | `POST /pb/openapi/newad/spAdGroups`<br>`lingxing_ads_sp_ad_groups` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spAdGroups/) |
| 97 | `POST /pb/openapi/newad/spAdPlacementHourData`<br>`lingxing_ads_sp_placement_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spAdPlacementHourData/) |
| 98 | `POST /pb/openapi/newad/spAdvertiseHourData`<br>`lingxing_ads_sp_advertise_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spAdvertiseHourData/) |
| 99 | `POST /pb/openapi/newad/spCampaignHourData`<br>`lingxing_ads_sp_campaign_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spCampaignHourData/) |
| 100 | `POST /pb/openapi/newad/spCampaignReports`<br>`lingxing_ads_sp_campaign_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spCampaignReports/) |
| 101 | `POST /pb/openapi/newad/spCampaigns`<br>`lingxing_ads_sp_campaigns` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spCampaigns/) |
| 102 | `POST /pb/openapi/newad/spKeywordReports`<br>`lingxing_ads_sp_keyword_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spKeywordReports/) |
| 103 | `POST /pb/openapi/newad/spKeywords`<br>`lingxing_ads_sp_keywords` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spKeywords/) |
| 104 | `POST /pb/openapi/newad/spNegativeTargetsOrKeywords`<br>`lingxing_ads_sp_negative_targets_or_keywords` | 补 target_type；未指定时串行取 keyword/target 两类，保留原功能承诺 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spNegativeTargetsOrKeywords/) |
| 105 | `POST /pb/openapi/newad/spProductAdReports`<br>`lingxing_smoke_check`<br>`lingxing_asin_ads_daily_rollup`<br>`lingxing_asin_weekly_rollup`<br>`lingxing_ads_sp_product_ad_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spProductAdReports/) |
| 106 | `POST /pb/openapi/newad/spProductAds`<br>`lingxing_ads_sp_product_ads` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spProductAds/) |
| 107 | `POST /pb/openapi/newad/spTargetHourData`<br>`lingxing_ads_sp_target_hourly` | 补campaign参数及适用agg_dimension，按单次响应读取；不新增角色开放 | 1 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spTargetHourData/) |
| 108 | `POST /pb/openapi/newad/spTargetReports`<br>`lingxing_ads_sp_target_report` | 日报改V2 next_token；清除该接口未声明的show_detail默认值 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/report/spTargetReports/) |
| 109 | `POST /pb/openapi/newad/spTargets`<br>`lingxing_ads_sp_targets` | 契约一致，保持现有受影响调用/分页/字段映射 | 10 | [官方](https://apidoc.lingxing.com/new/api-docs/newAd/baseData/spTargets/) |

原始HTML/Markdown证据及四份分组审阅报告保留在本地任务目录，不把运行记录或企业数据复制进公开仓库。
