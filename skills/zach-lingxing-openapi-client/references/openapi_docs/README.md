# 领星 OpenAPI 本地文档索引

这些文档由 `scripts/sync_docs.py` 从官方 `_sidebar.md` 自动发现，只同步当前仓库需要的 Amazon 相关只读接口页面。

| 本地文件 | 模块 | 请求方式 | 分页 | V2 头 | 官方路径 | API Path | 标题 |
|---|---|---|---|---|---|---|---|
| `01_GetToken.md` | `Authorization` | `POST` | `none` | `false` | `docs/Authorization/GetToken.md` | `/api/auth-server/oauth/access-token` | 获取 access-token和refresh-token |
| `BasicData_AccoutLists.md` | `BasicData` | `GET` | `none` | `false` | `docs/BasicData/AccoutLists.md` | `/erp/sc/data/account/lists` | 查询ERP用户信息列表 |
| `04_AllMarketplace.md` | `BasicData` | `GET` | `none` | `false` | `docs/BasicData/AllMarketplace.md` | `/erp/sc/data/seller/allMarketplace` | 查询亚马逊市场列表 |
| `BasicData_AttachmentDownload.md` | `BasicData` | `POST` | `none` | `false` | `docs/BasicData/AttachmentDownload.md` | `/erp/sc/routing/common/file/download` | 下载附件 |
| `BasicData_ConceptSellerLists.md` | `BasicData` | `GET` | `none` | `false` | `docs/BasicData/ConceptSellerLists.md` | `/erp/sc/data/seller/conceptLists` | 查询亚马逊概念店铺列表 |
| `BasicData_Currency.md` | `BasicData` | `POST` | `none` | `false` | `docs/BasicData/Currency.md` | `/erp/sc/routing/finance/currency/currencyMonth` | 查询汇率 |
| `BasicData_CustomAttachmentDownload.md` | `BasicData` | `POST` | `none` | `false` | `docs/BasicData/CustomAttachmentDownload.md` | `/erp/sc/routing/customized/file/download` | 定制化附件下载接口 |
| `03_SellerLists.md` | `BasicData` | `GET` | `none` | `false` | `docs/BasicData/SellerLists.md` | `/erp/sc/data/seller/lists` | 查询亚马逊店铺列表 |
| `BasicData_StateList.md` | `BasicData` | `POST` | `none` | `false` | `docs/BasicData/StateList.md` | `/basicOpen/multiplatform/profit/report/stateList` | 获取国家下的州、省编码 |
| `BasicData_WorldStateLists.md` | `BasicData` | `POST` | `none` | `false` | `docs/BasicData/WorldStateLists.md` | `/erp/sc/data/worldState/lists` | 查询亚马逊国家下地区列表 |
| `FBA_BoxInfo.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/BoxInfo.md` | `/erp/sc/routing/fba/shipment/boxInfo` | 查询货件装箱信息 |
| `FBA_FBAReceivedInventory.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/FBAReceivedInventory.md` | `/erp/sc/data/fba_report/receivedInventory` | 查询FBA到货接收明细 |
| `FBA_FBAShipmentList.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/FBAShipmentList.md` | `/erp/sc/data/fba_report/shipmentList` | 查询货件列表 |
| `FBA_GetDeliveryDateList.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetDeliveryDateList.md` | `/amzStaServer/openapi/inbound-shipment/getDeliveryDateList` | 查询可选送达时间 |
| `FBA_GetFbaProductList.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/GetFbaProductList.md` | `/erp/sc/routing/fba/shipment/getFbaProductList` | 查询FBA商品信息列表 |
| `FBA_GetHeadLogisticsFeeTypes.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetHeadLogisticsFeeTypes.md` | `/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes` | 获取发货单头程物流信息-其他费类型 |
| `FBA_GetInboundShipmentList.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/GetInboundShipmentList.md` | `/erp/sc/routing/storage/shipment/getInboundShipmentList` | 查询发货单列表 |
| `FBA_GetInboundShipmentListMwsDetailList.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetInboundShipmentListMwsDetailList.md` | `/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetailList` | 批量查询发货单详情 |
| `FBA_GetPrepareDetails.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetPrepareDetails.md` | `/amzStaServer/openapi/inbound-packing/getPrepDetails` | 获取商品预处理信息 |
| `FBA_GetSeaTrackSupplierCarriers.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetSeaTrackSupplierCarriers.md` | `/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers` | 获取发货单头程物流信息-承运商信息 |
| `FBA_GetTransportList.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/GetTransportList.md` | `/amzStaServer/openapi/inbound-shipment/getTransportList` | 查询承运方式 |
| `FBA_ListPackingGroupItems.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/ListPackingGroupItems.md` | `/amzStaServer/openapi/inbound-packing/listPackingGroupItems` | 查询包装组 |
| `FBA_ListShipmentBoxes.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/ListShipmentBoxes.md` | `/amzStaServer/openapi/inbound-shipment/listShipmentBoxes` | 查询货件装箱信息 |
| `FBA_Operate.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/Operate.md` | `/amzStaServer/openapi/task-plan/operate` | 查询异步任务状态 |
| `FBA_QuerySTATaskBoxInformation.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/QuerySTATaskBoxInformation.md` | `/amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking` | 查询STA任务包装组装箱信息 |
| `FBA_QuerySTATaskList.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/QuerySTATaskList.md` | `/amzStaServer/openapi/inbound-plan/page` | 查询STA任务列表 |
| `FBA_ShipFromAddressList.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/ShipFromAddressList.md` | `/erp/sc/routing/fba/shipment/shipFromAddressList` | 地址簿-发货地址列表 |
| `FBA_ShipmentDetailList.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/ShipmentDetailList.md` | `/amzStaServer/openapi/inbound-shipment/shipmentDetailList` | 查询货件详情 |
| `FBA_ShipmentPlanLists.md` | `FBA` | `POST` | `offset` | `false` | `docs/FBA/ShipmentPlanLists.md` | `/erp/sc/data/fba_report/shipmentPlanLists` | 查询FBA发货计划 |
| `FBA_ShipmentPreView.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/ShipmentPreView.md` | `/amzStaServer/openapi/inbound-shipment/shipmentPreView` | 查询货件方案 |
| `FBA_ShoppingAddress.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/ShoppingAddress.md` | `/basicOpen/openapi/fbaShipment/shoppingAddress` | 地址簿-配送地址详情 |
| `FBA_StaTaskDetail.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/StaTaskDetail.md` | `/amzStaServer/openapi/inbound-plan/detail` | 查询STA任务详情 |
| `FBA_getInboundPackingBoxInfo.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/getInboundPackingBoxInfo.md` | `/amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo` | 查询货件方案的装箱信息 |
| `FBA_getInboundShipmentListMwsDetail.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/getInboundShipmentListMwsDetail.md` | `/erp/sc/routing/storage/shipment/getInboundShipmentListMwsDetail` | 查询发货单详情 |
| `FBA_printFbaLabels.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/printFbaLabels.md` | `/erp/sc/storage/shipment/printFbaLabels` | 查询FBA货件箱子、卡板标签 |
| `FBA_printFnskuLabels.md` | `FBA` | `POST` | `none` | `false` | `docs/FBA/printFnskuLabels.md` | `/erp/sc/storage/shipment/printFnskuLabels` | 查询FBA货件商品FNSKU标签 |
| `FBALimit_GetIpiInfo.md` | `FBALimit` | `POST` | `offset` | `false` | `docs/FBALimit/GetIpiInfo.md` | `/erp/sc/routing/fbaLimit/restock/getIpiInfo` | 查询IPI信息 |
| `FBALimit_replenishmentRestrictionList.md` | `FBALimit` | `POST` | `offset` | `false` | `docs/FBALimit/replenishmentRestrictionList.md` | `/basicOpen/openapi/replenishmentRestriction/page/list` | 查询补货限制列表 |
| `FBASug_ConfigASIN.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/ConfigASIN.md` | `/erp/sc/routing/fbaSug/asin/getConfig` | 查询规则 - ASIN |
| `FBASug_ConfigMSKU.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/ConfigMSKU.md` | `/erp/sc/routing/fbaSug/msku/getConfig` | 查询规则 - MSKU |
| `FBASug_DailySalesInfoFeatureASIN.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/DailySalesInfoFeatureASIN.md` | `/erp/sc/routing/fbaSug/asin/getDailySalesInfoFeature` | 按ASIN查询FBA补货建议图表 |
| `FBASug_DailySalesInfoFeatureMSKU.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/DailySalesInfoFeatureMSKU.md` | `/erp/sc/routing/fbaSug/msku/getDailySalesInfoFeature` | 按MSKU查询FBA补货建议图表 |
| `FBASug_GetSummaryList.md` | `FBASug` | `POST` | `offset` | `false` | `docs/FBASug/GetSummaryList.md` | `/erp/sc/routing/restocking/analysis/getSummaryList` | 查询补货列表 |
| `FBASug_InfoASIN.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/InfoASIN.md` | `/erp/sc/routing/fbaSug/asin/getInfo` | 查询建议信息-ASIN |
| `FBASug_InfoMSKU.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/InfoMSKU.md` | `/erp/sc/routing/fbaSug/msku/getInfo` | 查询建议信息-MSKU |
| `FBASug_SourceListASIN.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/SourceListASIN.md` | `/erp/sc/routing/fbaSug/asin/getSourceList` | 查询报表型数据明细-ASIN |
| `FBASug_SourceListMSKU.md` | `FBASug` | `POST` | `none` | `false` | `docs/FBASug/SourceListMSKU.md` | `/erp/sc/routing/fbaSug/msku/getSourceList` | 查询报表型数据明细-MSKU |
| `Finance_ComputeManual.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/ComputeManual.md` | `/bd/profit/report/open/report/settle/compute/manual` | 立即重算-利润报表数据 |
| `Finance_CostStream.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/CostStream.md` | `/cost/center/api/cost/stream` | 查询FBA成本计价流水 |
| `Finance_FianceProfitMsku.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/FianceProfitMsku.md` | `/erp/sc/routing/finance/ProfitState/profitMsku` | 查询利润报表（旧） - MSKU |
| `Finance_InvoiceCampaignList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/InvoiceCampaignList.md` | `/bd/profit/report/open/report/ads/invoice/campaign/list` | 查询广告发票活动列表 |
| `Finance_InvoiceDetail.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/InvoiceDetail.md` | `/bd/profit/report/open/report/ads/invoice/detail` | 查询广告发票基本信息 |
| `Finance_InvoiceList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/InvoiceList.md` | `/bd/profit/report/open/report/ads/invoice/list` | 查询广告发票列表 |
| `Finance_OrderProfitListMSKU.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/OrderProfitListMSKU.md` | `/basicOpen/finance/mreport/OrderProfit` | 查询订单利润-MSKU |
| `Finance_QueryReceiptFundsList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/QueryReceiptFundsList.md` | `/basicOpen/finance/queryReceiptFundsList` | 查询收款单列表 |
| `Finance_RequestFundsOrderList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/RequestFundsOrderList.md` | `/basicOpen/finance/requestFunds/order/list` | 查询请款单列表 |
| `Finance_SettlementExportUrlGet.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/SettlementExportUrlGet.md` | `/bd/sp/api/open/settlement/export/url/get` | 查询settlement下载URL |
| `Finance_SettlementReport.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/SettlementReport.md` | `/cost/center/api/settlement/report` | 查询发货结算报告 |
| `Finance_bdASIN.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdASIN.md` | `/bd/profit/report/open/report/asin/list` | 查询利润报表-ASIN |
| `Finance_bdMSKU.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdMSKU.md` | `/bd/profit/report/open/report/msku/list` | 查询利润报表-MSKU |
| `Finance_bdOrder.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/bdOrder.md` | `/bd/profit/report/open/report/order/list` | 查询利润报表-订单 |
| `Finance_bdParentASIN.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdParentASIN.md` | `/bd/profit/report/open/report/parent/asin/list` | 查询利润报表-父ASIN |
| `Finance_bdSKU.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdSKU.md` | `/bd/profit/report/open/report/sku/list` | 查询利润报表-SKU |
| `Finance_bdSeller.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdSeller.md` | `/bd/profit/report/open/report/seller/list` | 查询利润报表-店铺 |
| `Finance_bdSellerSummary.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/bdSellerSummary.md` | `/bd/profit/report/open/report/seller/summary/list` | 查询利润报表-店铺月度汇总 |
| `Finance_centerOdsDetailQuery.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/centerOdsDetailQuery.md` | `/cost/center/ods/detail/query` | 查询库存分类账detail数据 |
| `Finance_feeManagementDiscard.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/feeManagementDiscard.md` | `/bd/fee/management/open/feeManagement/otherFee/discard` | 作废费用单 |
| `Finance_feeManagementEdit.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/feeManagementEdit.md` | `/bd/fee/management/open/feeManagement/otherFee/edit` | 编辑费用单 |
| `Finance_feeManagementList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/feeManagementList.md` | `/bd/fee/management/open/feeManagement/otherFee/list` | 查询费用明细列表 |
| `Finance_feeManagementType.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/feeManagementType.md` | `/bd/fee/management/open/feeManagement/otherFee/type` | 查询费用类型列表 |
| `Finance_lazadaPayoutList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/lazadaPayoutList.md` | `/basicOpen/finance/lazada/payout/list` | 回款明细-LazadaPayout |
| `Finance_lazadaSettlementList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/lazadaSettlementList.md` | `/basicOpen/finance/lazada/settlement/list` | 账单明细-LazadaSettlement |
| `Finance_profitAsin.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/profitAsin.md` | `/erp/sc/routing/finance/ProfitState/profitAsin` | 查询利润报表（旧） - ASIN（父级） |
| `Finance_profitAsinSon.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/profitAsinSon.md` | `/erp/sc/routing/finance/ProfitState/profitAsinSon` | 查询利润报表（旧） - ASIN（子级） |
| `Finance_profitReportOrderTranscationList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/profitReportOrderTranscationList.md` | `/basicOpen/finance/profitReport/order/transcation/list` | 查询利润报表 - 订单维度transaction视图 |
| `Finance_profitSettlement.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/profitSettlement.md` | `/erp/sc/routing/finance/ProfitState/profitSettlement` | 查询利润报表（旧）-结算明细 |
| `Finance_receivableReportList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/receivableReportList.md` | `/bd/sp/api/open/monthly/receivable/report/list` | 应收报告-列表查询 |
| `Finance_reportListDetail.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/reportListDetail.md` | `/bd/sp/api/open/monthly/receivable/report/list/detail` | 应收报告-详情-列表 |
| `Finance_reportListDetailInfo.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/reportListDetailInfo.md` | `/bd/sp/api/open/monthly/receivable/report/list/detail/info` | 应收报告-详情-基础信息 |
| `Finance_requestFundsPoolCustomFeeList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolCustomFeeList.md` | `/basicOpen/finance/requestFundsPool/customFee/list` | 查询请款池-其他应付款 |
| `Finance_requestFundsPoolInboundList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolInboundList.md` | `/basicOpen/finance/requestFundsPool/inbound/list` | 查询请款池 - 货款月结 |
| `Finance_requestFundsPoolLogisticsList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolLogisticsList.md` | `/basicOpen/finance/requestFundsPool/logistics/list` | 查询请款池-物流请款 |
| `Finance_requestFundsPoolOtherFeeList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolOtherFeeList.md` | `/basicOpen/finance/requestFundsPool/otherFee/list` | 查询请款池-其他费用 |
| `Finance_requestFundsPoolPrepayList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolPrepayList.md` | `/basicOpen/finance/requestFundsPool/prepay/list` | 查询请款池 - 货款预付款 |
| `Finance_requestFundsPoolPurchaseList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/requestFundsPoolPurchaseList.md` | `/basicOpen/finance/requestFundsPool/purchase/list` | 查询请款池 - 货款现结 |
| `Finance_settlementSummaryList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/settlementSummaryList.md` | `/bd/sp/api/open/settlement/summary/list` | 查询结算中心 - 结算汇总 |
| `Finance_settlementTransactionList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/settlementTransactionList.md` | `/bd/sp/api/open/settlement/transaction/detail/list` | 查询结算中心 - 交易明细 |
| `Finance_shopeeAdjustmentList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/shopeeAdjustmentList.md` | `/basicOpen/finance/shopee/adjustment/list` | 账单明细-ShopeeAdjustment |
| `Finance_shopeeIncomeList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/shopeeIncomeList.md` | `/basicOpen/finance/shopee/income/list` | 账单明细-ShopeeIncome |
| `Finance_shopeePayoutList.md` | `Finance` | `POST` | `offset` | `false` | `docs/Finance/shopeePayoutList.md` | `/basicOpen/finance/shopee/payout/list` | 回款明细-ShopeePayout |
| `Finance_summaryQuery.md` | `Finance` | `POST` | `none` | `false` | `docs/Finance/summaryQuery.md` | `/cost/center/ods/summary/query` | 查询库存分类账summary数据 |
| `Sale_FBMOrderDetail.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/FBMOrderDetail.md` | `/erp/sc/routing/order/Order/getOrderDetail` | 查询亚马逊自发货订单详情 |
| `Sale_FBMOrderList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/FBMOrderList.md` | `/erp/sc/routing/order/Order/getOrderList` | 查询亚马逊自发货订单列表 |
| `Sale_GetFulfillmentResult.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/GetFulfillmentResult.md` | `/pb/mp/order/getFulfillmentResult` | 查询亚马逊标发结果 |
| `Sale_GetMerchantShippingGroup.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/GetMerchantShippingGroup.md` | `/basicOpen/openapi/publish/manage/getMerchantShippingGroup` | 刊登管理-获取运费模板 |
| `Sale_GetPrices.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/GetPrices.md` | `/listing/listing/open/api/listing/getPrices` | 批量获取Listing费用 |
| `Sale_Listing.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/Listing.md` | `/erp/sc/data/mws/listing` | 查询亚马逊Listing |
| `Sale_LogisticsInformation.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/LogisticsInformation.md` | `/order/amzod/api/orderDetails/logisticsInformation` | 查询亚马逊多渠道订单详情-物流信息 |
| `Sale_MCFOrderList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/MCFOrderList.md` | `/order/amzod/api/orderList` | 查询亚马逊多渠道订单列表-v2 |
| `Sale_MutilChannelTransactionDetail.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/MutilChannelTransactionDetail.md` | `/basicOpen/openapi/salesOrder/multi-channel/list/transaction` | 多渠道订单-交易明细 |
| `Sale_OrderDetail.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/OrderDetail.md` | `/erp/sc/data/mws/orderDetail` | 查询亚马逊订单详情 |
| `07_Orderlists.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/Orderlists.md` | `/erp/sc/data/mws/orders` | 查询亚马逊订单列表 |
| `Sale_ProductInformation.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/ProductInformation.md` | `/order/amzod/api/orderDetails/productInformation` | 查询亚马逊多渠道订单详情-商品信息 |
| `Sale_ProductList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/ProductList.md` | `/listing/publish/openapi/amazon/product/list` | 刊登管理-查询刊登结果 |
| `Sale_PublishManageCategoryChildren.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/PublishManageCategoryChildren.md` | `/basicOpen/openapi/publish/manage/categoryChildren` | 刊登管理-查询 Amazon 子分类 |
| `Sale_PublishManageCategoryRoot.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/PublishManageCategoryRoot.md` | `/basicOpen/openapi/publish/manage/categoryRoot` | 刊登管理-查询 Amazon 根分类 |
| `Sale_PublishManageGetProductType.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/PublishManageGetProductType.md` | `/basicOpen/openapi/publish/manage/getProductType` | 刊登管理-获取指定 productType 的 JSON Schema |
| `Sale_QueryProductList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/QueryProductList.md` | `/listing/publish/openapi/amazon/product/search` | 查询已有商品信息 |
| `Sale_ReturnInfomation.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/ReturnInfomation.md` | `/order/amzod/api/orderDetails/returnInformation` | 查询亚马逊多渠道订单详情-退货换货信息 |
| `Sale_UnlinkListing.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/UnlinkListing.md` | `/basicOpen/listingManage/unLinkListingPairs` | 解除Listing配对 |
| `Sale_adjustPriceAdjustPriceManual.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/adjustPriceAdjustPriceManual.md` | `/basicOpen/module/adjustPrice/AdjustPriceManual` | 查询调价队列 |
| `Sale_afterSaleList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/afterSaleList.md` | `/erp/sc/routing/amzod/order/afterSaleList` | 查询售后订单列表 |
| `Sale_fbaFeeDifferenceList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/fbaFeeDifferenceList.md` | `/basicOpen/openapi/sale/fbaFeeDifference/order/list` | FBA费差异-异常订单-订单 |
| `Sale_fbaFeeDifferenceMskuList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/fbaFeeDifferenceMskuList.md` | `/basicOpen/openapi/sale/fbaFeeDifference/msku/list` | FBA费差异-异常订单-MSKU |
| `Sale_globalTagPageList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/globalTagPageList.md` | `/basicOpen/globalTag/listing/page/list` | 查询Listing标签列表 |
| `Sale_listingOperateLogPageList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/listingOperateLogPageList.md` | `/basicOpen/listingManage/listingOperateLog/pageList` | 查询Listing操作日志列表 |
| `Sale_promotionCouponAllDetailBatch.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionCouponAllDetailBatch.md` | `/promotionApi/open/promotion/couponAllDetailBatch` | 查询优惠券详情+listing+订单(批量) |
| `Sale_promotionListingDetailCoupon.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionListingDetailCoupon.md` | `/basicOpen/promotion/listingDetailCoupon` | 查询商品折扣详情-列表-优惠卷 |
| `Sale_promotionListingDetailManage.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionListingDetailManage.md` | `/basicOpen/promotion/listingDetailManage` | 查询商品折扣详情-列表-管理促销 |
| `Sale_promotionListingDetailPrimeDiscount.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionListingDetailPrimeDiscount.md` | `/basicOpen/promotion/listingDetailPrimeDiscount` | 查询商品折扣详情-列表-会员折扣 |
| `Sale_promotionListingDetailSecKill.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionListingDetailSecKill.md` | `/basicOpen/promotion/listingDetailSecKill` | 查询商品折扣详情-列表-秒杀 |
| `08_PromotionListingList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/promotionListingList.md` | `/basicOpen/promotion/listingList` | 查询商品折扣列表 |
| `Sale_promotionManagementAllDetailBatch.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionManagementAllDetailBatch.md` | `/promotionApi/open/promotion/managementAllDetailBatch` | 查询管理促销详情+listing+订单(批量) |
| `Sale_promotionPrimeDiscountAllDetailBatch.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionPrimeDiscountAllDetailBatch.md` | `/promotionApi/open/promotion/primeDiscountAllDetailBatch` | 查询会员折扣or价格折扣详情+listing+订单(批量) |
| `Sale_promotionSecKillAllDetailBatch.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionSecKillAllDetailBatch.md` | `/promotionApi/open/promotion/secKillAllDetailBatch` | 查询秒杀详情+listing+订单(批量) |
| `12_PromotionalActivitiesCouponList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionalActivitiesCouponList.md` | `/basicOpen/promotionalActivities/coupon/list` | 查询促销活动列表-优惠券 |
| `10_PromotionalActivitiesManageList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionalActivitiesManageList.md` | `/basicOpen/promotionalActivities/manage/list` | 查询促销活动列表-管理促销 |
| `09_PromotionalActivitiesSecKillList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/promotionalActivitiesSecKillList.md` | `/basicOpen/promotionalActivities/secKill/list` | 查询促销活动列表-秒杀 |
| `11_PromotionalActivitiesVipDiscountList.md` | `Sale` | `POST` | `offset` | `false` | `docs/Sale/promotionalActivitiesVipDiscountList.md` | `/basicOpen/promotionalActivities/vipDiscount/list` | 查询促销活动列表-会员折扣/价格折扣 |
| `Sale_queryListingRelationTagList.md` | `Sale` | `POST` | `none` | `false` | `docs/Sale/queryListingRelationTagList.md` | `/basicOpen/listingManage/queryListingRelationTagList` | 查询Listing标记标签列表 |
| `SourceData_AdjustmentList.md` | `SourceData` | `POST` | `none` | `false` | `docs/SourceData/AdjustmentList.md` | `/basicOpen/openapi/mwsReport/adjustmentList` | 查询亚马逊源报表-盘存记录 |
| `SourceData_AfnFulfillableQuantity.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/AfnFulfillableQuantity.md` | `/erp/sc/data/mws_report/getAfnFulfillableQuantity` | 查询亚马逊源报表-FBA可售库存 |
| `SourceData_AllOrders.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/AllOrders.md` | `/erp/sc/data/mws_report/allOrders` | 查询亚马逊源报表-所有订单 |
| `SourceData_DailyInventory.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/DailyInventory.md` | `/erp/sc/data/mws_report/dailyInventory` | 查询亚马逊源报表-每日库存 |
| `SourceData_FbaOrders.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/FbaOrders.md` | `/erp/sc/data/mws_report/fbaOrders` | 查询亚马逊源报表-FBA订单 |
| `SourceData_ManageInventory.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/ManageInventory.md` | `/erp/sc/data/mws_report/manageInventory` | 查询亚马逊源报表-FBA库存 |
| `SourceData_RefundOrders.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/RefundOrders.md` | `/erp/sc/data/mws_report/refundOrders` | 查询亚马逊源报表-FBA退货订单 |
| `SourceData_RemovalLists.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/RemovalLists.md` | `/erp/sc/data/fba_report/removalLists` | 查询亚马逊源报表-移除货件（旧） |
| `SourceData_RemovalOrderListNew.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/RemovalOrderListNew.md` | `/erp/sc/routing/data/order/removalOrderListNew` | 查询亚马逊源报表-移除订单（新） |
| `SourceData_RemovalShipmentList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/RemovalShipmentList.md` | `/erp/sc/statistic/removalShipment/list` | 查询亚马逊源报表-移除货件（新） |
| `SourceData_ReservedInventory.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/ReservedInventory.md` | `/erp/sc/data/mws_report/reservedInventory` | 查询亚马逊源报表-预留库存 |
| `SourceData_SourceRemovalOrders.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/SourceRemovalOrders.md` | `/erp/sc/data/mws_report/removalOrders` | 查询亚马逊源报表-移除订单（旧） |
| `SourceData_Transaction.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/Transaction.md` | `/erp/sc/data/mws_report/transaction` | 查询亚马逊源报表-交易明细 |
| `SourceData_fbaExchangeOrderList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/fbaExchangeOrderList.md` | `/erp/sc/routing/data/order/fbaExchangeOrderList` | 查询亚马逊源报表-FBA换货订单 |
| `SourceData_fbmReturnOrderList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/fbmReturnOrderList.md` | `/erp/sc/routing/data/order/fbmReturnOrderList` | 查询亚马逊源报表-FBM退货订单 |
| `SourceData_getAmazonFulfilledShipmentsList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/getAmazonFulfilledShipmentsList.md` | `/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList` | 查询亚马逊源报表—Amazon Fulfilled Shipments |
| `SourceData_getFbaAgeList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/getFbaAgeList.md` | `/erp/sc/routing/fba/fbaStock/getFbaAgeList` | 查询亚马逊源报表—库龄表 |
| `SourceData_getFbaInventoryEventDetailList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/getFbaInventoryEventDetailList.md` | `/erp/sc/data/mws_report/getFbaInventoryEventDetailList` | 查询亚马逊源报表——Inventory Event Detail |
| `SourceData_v1getAmazonFulfilledShipmentsList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/v1getAmazonFulfilledShipmentsList.md` | `/erp/sc/data/mws_report_v1/getAmazonFulfilledShipmentsList` | 查询亚马逊源报表—Amazon Fulfilled Shipments v1 |
| `SourceData_v1getFbaInventoryEventDetailList.md` | `SourceData` | `POST` | `offset` | `false` | `docs/SourceData/v1getFbaInventoryEventDetailList.md` | `/erp/sc/data/mws_report_v1/getFbaInventoryEventDetailList` | 查询亚马逊源表数据--Inventory Event Detail v1 |
| `Statistics_AmazonReportExportTask.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/AmazonReportExportTask.md` | `/basicOpen/report/amazonReportExportTask` | 报告导出 - 报告下载链接续期 |
| `06_AsinDailyLists.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/AsinDailyLists.md` | `/erp/sc/data/sales_report/asinDailyLists` | 查询亚马逊销量统计 |
| `Statistics_AsinList.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/AsinList.md` | `/erp/sc/data/sales_report/asinList` | 查询产品表现（旧） |
| `Statistics_AsinListNew.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/AsinListNew.md` | `/bd/productPerformance/openApi/asinList` | 查询产品表现 |
| `Statistics_FBAStorageFeeLongTerm.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/FBAStorageFeeLongTerm.md` | `/erp/sc/data/fba_report/storageFeeLongTerm` | 查询FBA长期仓储费 |
| `Statistics_FBAStorageFeeMonth.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/FBAStorageFeeMonth.md` | `/erp/sc/data/fba_report/storageFeeMonth` | 查询FBA月仓储费 |
| `Statistics_FbaStockAggregateListNew.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/FbaStockAggregateListNew.md` | `/cost/center/openApi/fba/gather/query` | 库存报表-FBA-新版-汇总 |
| `Statistics_FbaStockDetailListNew.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/FbaStockDetailListNew.md` | `/cost/center/openApi/fba/detail/query` | 库存报表-FBA-新版-明细 |
| `Statistics_FbaStockReportList.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/FbaStockReportList.md` | `/erp/sc/routing/fba/fbaStockReport/getList` | 库存报表-FBA-历史报表-汇总-明细 |
| `Statistics_LocalAggregateList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/LocalAggregateList.md` | `/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseSummaryList` | 库存报表-本地仓-历史报表-汇总 |
| `Statistics_LocalAggregateListNew.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/LocalAggregateListNew.md` | `/inventory/center/openapi/storageReport/local/aggregate/list` | 库存报表-本地仓-新报表-汇总 |
| `Statistics_LocalDetailList.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/LocalDetailList.md` | `/erp/sc/routing/inventoryLog/WareHouseReport/getLocalWareHouseDetailList` | 库存报表-本地仓-历史报表-明细 |
| `Statistics_LocalDetailListNew.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/LocalDetailListNew.md` | `/inventory/center/openapi/storageReport/local/detail/page` | 库存报表-本地仓-新报表-明细 |
| `Statistics_MonthRefund.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/MonthRefund.md` | `/erp/sc/routing/finance/Refund/profitMonthRefund` | 查询退款量（旧） |
| `Statistics_OverseasAggregateList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/OverseasAggregateList.md` | `/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaSummaryList` | 库存报表-海外仓-历史报表-汇总 |
| `Statistics_OverseasAggregateListNew.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/OverseasAggregateListNew.md` | `/inventory/center/openapi/storageReport/overseas/aggregate/list` | 库存报表-海外仓-新报表-汇总 |
| `Statistics_OverseasDetailList.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/OverseasDetailList.md` | `/erp/sc/routing/inventoryLog/WareHouseReport/getOverSeaDetailList` | 库存报表-海外仓-历史报表-明细 |
| `Statistics_OverseasDetailListNew.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/OverseasDetailListNew.md` | `/inventory/center/openapi/storageReport/overseas/detail/page` | 库存报表-海外仓-新报表-明细 |
| `Statistics_PlatformStatisticsSaleStatPageListV2.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/PlatformStatisticsSaleStatPageListV2.md` | `/basicOpen/platformStatisticsV2/saleStat/pageList` | 查询销量统计列表v2 |
| `Statistics_ProfitMsku.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/ProfitMsku.md` | `/erp/sc/routing/finance/ProfitStatis/profitMsku` | 查询利润统计（旧）-MSKU |
| `Statistics_PurchaseReportBuyerList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/PurchaseReportBuyerList.md` | `/basicOpen/report/purchase/buyer/list` | 查询采购报表列表 - 采购员 |
| `Statistics_PurchaseReportProductList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/PurchaseReportProductList.md` | `/basicOpen/report/purchase/product/list` | 查询采购报表列表 - 产品 |
| `Statistics_PurchaseReportSupplierList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/PurchaseReportSupplierList.md` | `/basicOpen/report/purchase/supplier/list` | 查询采购报表列表 - 供应商 |
| `Statistics_ReimbursementList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/ReimbursementList.md` | `/basicOpen/openapi/mwsReport/reimbursementList` | 查询亚马逊赔偿报告列表 |
| `Statistics_ReturnOrderAnalysisLists.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/ReturnOrderAnalysisLists.md` | `/basicOpen/salesAnalysis/returnOrder/analysisLists` | 统计-查询退货分析 |
| `05_StoreSales.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/StoreSales.md` | `/erp/sc/data/sales_report/sales` | 查询店铺汇总销量 |
| `Statistics_operateLogList.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/operateLogList.md` | `/basicOpen/operateManage/operateLog/list` | 查询运营日志 |
| `Statistics_operateLogV2List.md` | `Statistics` | `POST` | `offset` | `false` | `docs/Statistics/operateLogV2List.md` | `/basicOpen/operateManage/operateLog/list/v2` | 查询运营日志(新) |
| `Statistics_performanceTrendByHour.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/performanceTrendByHour.md` | `/basicOpen/salesAnalysis/productPerformance/performanceTrendByHour` | 查询asin360小时数据 |
| `Statistics_reportQueryReportExportTask.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/reportQueryReportExportTask.md` | `/basicOpen/report/query/reportExportTask` | 报告导出-查询导出任务结果 |
| `Statistics_statisticsOpenASIN.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/statisticsOpenASIN.md` | `/bd/profit/statistics/open/asin/list` | 查询利润统计-ASIN |
| `Statistics_statisticsOpenMSKU.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/statisticsOpenMSKU.md` | `/bd/profit/statistics/open/msku/list` | 查询利润统计-MSKU |
| `Statistics_statisticsOpenParent.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/statisticsOpenParent.md` | `/bd/profit/statistics/open/parent/asin/list` | 查询利润统计-父ASIN |
| `Statistics_statisticsOpenSeller.md` | `Statistics` | `POST` | `none` | `false` | `docs/Statistics/statisticsOpenSeller.md` | `/bd/profit/statistics/open/seller/list` | 查询利润统计-店铺 |
| `newAd_baseData_dspAccountList.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/baseData/dspAccountList.md` | `/basicOpen/baseData/account/list` | 查询广告账号列表 |
| `newAd_baseData_newadsbDivideAsinReports.md` | `newAd` | `POST` | `next_token` | `true` | `docs/newAd/baseData/newadsbDivideAsinReports.md` | `/pb/openapi/newad/sbDivideAsinReports` | SB分摊 |
| `newAd_report_ProductAnalysisList.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/ProductAnalysisList.md` | `/basicOpen/adReport/productOrderAnalysis/list` | 出单时段分析（产品） |
| `newAd_report_WalmartQueryAdvertiserList.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/WalmartQueryAdvertiserList.md` | `/basicOpen/adReport/advertiser/list` | 查询沃尔玛广告主列表 |
| `newAd_report_asinReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/asinReports.md` | `/pb/openapi/newad/asinReports` | SP已购买商品报表 |
| `newAd_report_campaignPlacementReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/campaignPlacementReports.md` | `/pb/openapi/newad/campaignPlacementReports` | SP广告位报告 |
| `newAd_report_dspReportOrderList.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/dspReportOrderList.md` | `/basicOpen/dspReport/order/list` | 查询DSP报告列表-订单 |
| `newAd_report_hsaAdGroupReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/hsaAdGroupReports.md` | `/pb/openapi/newad/hsaAdGroupReports` | SB广告组报表 |
| `newAd_report_hsaCampaignPlacementReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/hsaCampaignPlacementReports.md` | `/pb/openapi/newad/hsaCampaignPlacementReports` | SB广告活动-广告位报告 |
| `newAd_report_hsaCampaignReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/hsaCampaignReports.md` | `/pb/openapi/newad/hsaCampaignReports` | SB广告活动报表 |
| `newAd_report_hsaPurchasedAsinReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/hsaPurchasedAsinReports.md` | `/pb/openapi/newad/hsaPurchasedAsinReports` | SB广告归因于广告的购买报告 |
| `newAd_report_hsaQueryWordReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/hsaQueryWordReports.md` | `/pb/openapi/newad/hsaQueryWordReports` | SB用户搜索词报表 |
| `newAd_report_listHsaKeywordPlacementReport.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/listHsaKeywordPlacementReport.md` | `/pb/openapi/newad/listHsaKeywordPlacementReport` | SB关键词-广告位报告 |
| `newAd_report_listHsaProductAdReport.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/listHsaProductAdReport.md` | `/pb/openapi/newad/listHsaProductAdReport` | SB广告创意报告 |
| `newAd_report_listHsaTargetingReport.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/listHsaTargetingReport.md` | `/pb/openapi/newad/listHsaTargetingReport` | SB广告的投放报告 |
| `newAd_report_queryWordReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/queryWordReports.md` | `/pb/openapi/newad/queryWordReports` | SP用户搜索词报表 |
| `newAd_report_sbAdGroupHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sbAdGroupHourData.md` | `/pb/openapi/newad/sbAdGroupHourData` | SB广告组小时数据 |
| `newAd_report_sbAdPlacementHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sbAdPlacementHourData.md` | `/pb/openapi/newad/sbAdPlacementHourData` | SB广告位小时数据 |
| `newAd_report_sbCampaignHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sbCampaignHourData.md` | `/pb/openapi/newad/sbCampaignHourData` | SB广告活动小时数据 |
| `newAd_report_sbTargetHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sbTargetHourData.md` | `/pb/openapi/newad/sbTargetHourData` | SB投放小时数据 |
| `newAd_report_sdAdGroupHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sdAdGroupHourData.md` | `/pb/openapi/newad/sdAdGroupHourData` | SD广告组小时数据 |
| `newAd_report_sdAdGroupReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdAdGroupReports.md` | `/pb/openapi/newad/sdAdGroupReports` | SD广告组报表 |
| `newAd_report_sdAdvertiseHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sdAdvertiseHourData.md` | `/pb/openapi/newad/sdAdvertiseHourData` | SD广告小时数据 |
| `newAd_report_sdAsinReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdAsinReports.md` | `/pb/openapi/newad/sdAsinReports` | SD已购买商品报表 |
| `newAd_report_sdCampaignHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sdCampaignHourData.md` | `/pb/openapi/newad/sdCampaignHourData` | SD广告活动小时数据 |
| `newAd_report_sdCampaignReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdCampaignReports.md` | `/pb/openapi/newad/sdCampaignReports` | SD广告活动报表 |
| `newAd_report_sdMatchTargetReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdMatchTargetReports.md` | `/pb/openapi/newad/sdMatchTargetReports` | SD匹配的目标报表 |
| `newAd_report_sdProductAdReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdProductAdReports.md` | `/pb/openapi/newad/sdProductAdReports` | SD广告商品报表 |
| `newAd_report_sdTargetHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/sdTargetHourData.md` | `/pb/openapi/newad/sdTargetHourData` | SD投放小时数据 |
| `newAd_report_sdTargetReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/sdTargetReports.md` | `/pb/openapi/newad/sdTargetReports` | SD商品定位报表 |
| `newAd_report_spAdGroupHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/spAdGroupHourData.md` | `/pb/openapi/newad/spAdGroupHourData` | SP广告组小时数据 |
| `newAd_report_spAdGroupReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/spAdGroupReports.md` | `/pb/openapi/newad/spAdGroupReports` | SP广告组报表 |
| `newAd_report_spAdPlacementHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/spAdPlacementHourData.md` | `/pb/openapi/newad/spAdPlacementHourData` | SP广告位小时数据 |
| `newAd_report_spAdvertiseHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/spAdvertiseHourData.md` | `/pb/openapi/newad/spAdvertiseHourData` | SP广告小时数据 |
| `newAd_report_spCampaignHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/spCampaignHourData.md` | `/pb/openapi/newad/spCampaignHourData` | SP广告活动小时数据 |
| `newAd_report_spCampaignReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/spCampaignReports.md` | `/pb/openapi/newad/spCampaignReports` | SP广告活动报表 |
| `newAd_report_spKeywordReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/spKeywordReports.md` | `/pb/openapi/newad/spKeywordReports` | SP关键词报表 |
| `newAd_report_spProductAdReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/spProductAdReports.md` | `/pb/openapi/newad/spProductAdReports` | SP广告商品报表 |
| `newAd_report_spTargetHourData.md` | `newAd` | `POST` | `none` | `true` | `docs/newAd/report/spTargetHourData.md` | `/pb/openapi/newad/spTargetHourData` | SP投放小时数据 |
| `newAd_report_spTargetReports.md` | `newAd` | `POST` | `offset` | `true` | `docs/newAd/report/spTargetReports.md` | `/pb/openapi/newad/spTargetReports` | SP商品定位报表 |
