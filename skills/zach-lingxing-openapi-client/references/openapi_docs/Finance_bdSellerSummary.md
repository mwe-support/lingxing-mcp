# 查询利润报表-店铺月度汇总

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/seller/summary/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名      | 说明   | 必填 |  类型 | 示例   |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| mids        |站点id | 否 |[array]|[2]|
| sids        |店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否 |[array]| [110] |
| monthlyQuery|是否按月查询：<br>false 按天【默认值】<br>true 按月|否 |[boolean] | false |
| startDate   |开始时间【结算时间，双闭区间】<br>按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d<br>按月：开始结束时间年月相同，格式：Y-m| 是 | [string] |2023-09-21|
| endDate     |结束时间【结算时间，双闭区间】<br>按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d<br>按月：开始结束时间年月相同，格式：Y-m| 是 | [string] |2023-10-20|
| currencyCode|币种code |否 |[string] | CNY |
| orderStatus|交易状态<br/>Deferred 已推迟<br/>Disbursed 已发放【默认】<br/>DisbursedAndPreSettled 已发放（含预结算）<br/>All 全部|否|[string]|"Disbursed"|

## 请求示例
```
{
    "mids": [
        2
    ],
    "sids": [
        110
    ],
    "monthlyQuery": false,
    "startDate": "2023-09-21",
    "endDate": "2023-10-20",
    "currencyCode": "CNY",
    "orderStatus": "Disbursed"
}
```
## 返回结果
Json Object

| 参数名                                          | 类型        | 说明                                                    | 示例   |
| :--------------------------------------------- | :--------- | :------------------------------------------------------ | :----- |
| code                                           | [int]      | 状态码，0 成功                                            |        |
| msg                                            | [string]   | 消息提示                                                 |        |
| data                                           | [object]   | 响应数据                                                 |        |
| data>>totalFbaAndFbmQuantity                   | [int]      | fba和fbm销量加总，用于计算占比                               |        |
| data>>totalFbaAndFbmAmount                     | [number]   | fba和fbm销售额加总，用于计算占比                             |        |
| data>>totalSalesQuantity                       | [int]      | 销量                                                         |        |
| data>>fbaSalesQuantity                         | [int]      | FBA销量                                                      |        |
| data>>fbmSalesQuantity                         | [int]      | FBM销量                                                      |        |
| data>>totalReshipQuantity                      | [int]      | 补换货量                                                     |        |
| data>>reshipFbmProductSalesQuantity            | [int]      | FBM补（换）货量                                              |        |
| data>>reshipFbmProductSaleRefundsQuantity      | [int]      | FBM补（换）货退回量                                          |        |
| data>>reshipFbaProductSalesQuantity            | [int]      | FBA补（换）货量                                              |        |
| data>>reshipFbaProductSaleRefundsQuantity      | [int]      | FBA补（换）货退回量                                          |        |
| data>>mcFbaFulfillmentFeesQuantity             | [int]      | 多渠道销量                                                   |        |
| data>>cgAbsQuantity               		      | [number]     | 成本数量绝对值                                              |        |
| data>>cgQuantity                  		      | [number]     | 成本数量                                                   |        |
| data>>totalAdsSales                            | [number]     | 广告销售额                                                   |        |
| data>>adsSdSales                               | [number]     | sd广告销售额                                                 |        |
| data>>adsSpSales                               | [number]     | sp广告销售额                                                 |        |
| data>>sharedAdsSbSales                         | [number]     | sb广告销售额                                                 |        |
| data>>sharedAdsSbvSales                        | [number]     | sbv广告销售额                                                |        |
| data>>totalAdsSalesQuantity                    | [int]      | 广告销量                                                     |        |
| data>>adsSdSalesQuantity                       | [int]      | sd广告销量                                                   |        |
| data>>adsSpSalesQuantity                       | [int]      | sp广告销量                                                   |        |
| data>>sharedAdsSbSalesQuantity                 | [int]      | sb广告销量                                                   |        |
| data>>sharedAdsSbvSalesQuantity                | [int]      | sbv广告销量                                                  |        |
| data>>totalSalesAmount                         | [number]     | 销售额                                                       |        |
| data>>fbaSaleAmount                            | [number]     | FBA销售额                                                    |        |
| data>>fbmSaleAmount                            | [number]     | FBM销售额                                                    |        |
| data>>shippingCredits                          | [number]     | 买家运费                                                     |        |
| data>>promotionalRebates                       | [number]     | 促销折扣                                                     |        |
| data>>fbaInventoryCredit                       | [number]     | FBA库存赔偿                                                  |        |
| data>>cashOnDelivery                           | [number]     | COD                                                          |        |
| data>>otherInAmount                            | [number]     | 其他收入                                                     |        |
| data>>fbaLiquidationProceeds                   | [number]     | 清算收入                                                     |        |
| data>>fbaLiquidationProceedsAdjustments        | [number]     | 清算调整                                                     |        |
| data>>amazonShippingReimbursement              | [number]     | 亚马逊运费赔偿                                               |        |
| data>>safeTReimbursement                       | [number]     | Safe-T索赔                                                   |        |
| data>>netcoTransaction                         | [number]     | Netco交易                                                    |        |
| data>>reimbursements                           | [number]     | 赔偿收入                                                     |        |
| data>>clawbacks                                | [number]     | 追索收入                                                     |        |
| data>>sharedComminglingVatIncome               | [number]     | 混合VAT收入                                                  |        |
| data>>giftWrapCredits                          | [number]     | 包装收入                                                     |        |
| data>>guaranteeClaims                          | [number]     | 买家交易保障索赔额                                           |        |
| data>>costOfPoIntegersGranted                  | [number]     | 积分抵减收入                                                 |        |
| data>>totalSalesRefunds                        | [number]     | 收入退款额                                                   |        |
| data>>fbaSalesRefunds                          | [number]     | FBA销售退款额                                                |        |
| data>>fbmSalesRefunds                          | [number]     | FBM销售退款额                                                |        |
| data>>shippingCreditRefunds                    | [number]     | 买家运费退款额                                               |        |
| data>>giftWrapCreditRefunds                    | [number]     | 买家包装退款额                                               |        |
| data>>chargebacks                              | [number]     | 买家拒付                                                     |        |
| data>>costOfPoIntegersReturned                 | [number]     | 积分抵减退回                                                 |        |
| data>>promotionalRebateRefunds                 | [number]     | 促销折扣退款额                                               |        |
| data>>totalFeeRefunds                          | [number]     | 费用退款额                                                   |        |
| data>>sellingFeeRefunds                        | [number]     | 平台费退款额                                                 |        |
| data>>fbaTransactionFeeRefunds                 | [number]     | 发货费退款额                                                 |        |
| data>>refundAdministrationFees                 | [number]     | 交易费用退款额                                               |        |
| data>>otherTransactionFeeRefunds               | [number]     | 其他订单费退款额                                             |        |
| data>>refundForAdvertiser                      | [number]     | 广告退款额                                                   |        |
| data>>pointsAdjusted                           | [number]     | 积分费用                                                     |        |
| data>>shippingLabelRefunds                     | [number]     | 运输标签费退款                                               |        |
| data>>refundsQuantity                          | [int]      | 退款量                                                       |        |
| data>>refundsRate                              | [number]     | 退款率                                                       |        |
| data>>fbaReturnsQuantity                       | [int]      | 退货量                                                       |        |
| data>>fbaReturnsSaleableQuantity               | [int]      | 退货量（可售）                                               |        |
| data>>fbaReturnsUnsaleableQuantity             | [int]      | 退货量（不可售）                                             |        |
| data>>fbaReturnsQuantityRate                   | [number]     | 退货率                                                       |        |
| data>>platformFee                              | [number]     | 平台费                                                       |        |
| data>>fbaDeliveryFee                           | [number]     | FBA发货费                                                    |        |
| data>>records>>mcFbaDeliveryFee                | [number]     | FBA发货费(多渠道)                                             |        |
| data>>records>>totalFbaDeliveryFee             | [number]     | FBA发货费合计                                                 |        |
| data>>otherTransactionFees                     | [number]     | 其他订单费用                                                 |        |
| data>>totalAdsCost                             | [number]     | 广告费                                                       |        |
| data>>adsSpCost                                | [number]     | SP广告费                                                     |        |
| data>>adsSbCost                                | [number]     | SB广告费                                                     |        |
| data>>adsSbvCost                               | [number]     | SBV广告费                                                    |        |
| data>>adsSdCost                                | [number]     | SD广告费                                                     |        |
| data>>sharedCostOfAdvertising                  | [number]     | 差异分摊                                                     |        |
| data>>records>>sharedAdsAlCost              | [number]     | Live广告                               |        |
| data>>records>>sharedAdsCcCost	           | [number]     | 创作者计划                               |        |
| data>>records>>sharedAdsSspaotCost	       | [number]     | TV广告                               |        |
| data>>records>>sharedAdsSarCost	           | [number]     | 零售商赞助广告                               |        |
| data>>promotionFee                             | [number]     | 推广费                                                       |        |
| data>>sharedSubscriptionFee                    | [number]     | 订阅费                                                       |        |
| data>>sharedLdFee                              | [number]     | 秒杀费                                                       |        |
| data>>sharedCouponFee                          | [number]     | 优惠券                                                       |        |
| data>>sharedEarlyReviewerProgramFee            | [number]     | 早期评论人计划                                               |        |
| data>>sharedVineFee                            | [number]     | vine                                                         |        |
| data>>totalStorageFee                          | [number]     | FBA仓储费                                                    |        |
| data>>fbaStorageFee                            | [number]     | 月度仓库费                                                   |        |
| data>>sharedFbaStorageFee                      | [number]     | 月度仓储费差异                                               |        |
| data>>longTermStorageFee                       | [number]     | 长期仓储费                                                   |        |
| data>>sharedLongTermStorageFee                 | [number]     | 长期仓储费差异                                               |        |
| data>>sharedStorageRenewalBilling              | [number]     | 库存续订费用                                                 |        |
| data>>sharedFbaDisposalFee                     | [number]     | FBA销毁费                                                    |        |
| data>>sharedFbaRemovalFee                      | [number]     | FBA移除费                                                    |        |
| data>>sharedFbaInboundTransportationProgramFee | [number]     | 入仓手续费                                                   |        |
| data>>sharedLabelingFee                        | [number]     | 标签费                                                       |        |
| data>>sharedPolybaggingFee                     | [number]     | 塑料包装费                                                   |        |
| data>>sharedBubblewrapFee                      | [number]     | 泡沫包装费                                                   |        |
| data>>sharedTapingFee                          | [number]     | 胶带费                                                       |        |
| data>>records>>sharedAwdProcessingFee   | [number]     | AWD处理费                           |        |
| data>>records>>sharedAwdTransportationFee   | [number]     | AWD运输费                           |        |
| data>>records>>sharedAwdStorageFee   | [number]     | AWD仓储费                           |        |
| data>>records>>sharedStarStorageFee   | [number]     | 卫星仓仓储费                           |        |
| data>>sharedFbaCustomerReturnFee               | [number]     | FBA卖家退回费                                                |        |
| data>>sharedFbaInboundDefectFee                | [number]     | FBA仓储费入库缺陷费                                                 |        |
| data>>sharedFbaOverageFee                      | [number]     | 超量仓储费                                                   |        |
| data>>sharedAmazonPartneredCarrierShipmentFee  | [number]     | 合作承运费                                                   |        |
| data>>sharedFbaInboundConvenienceFee           | [number]     | 入库配置费                                                       |        |
| data>>sharedItemFeeAdjustment                  | [number]     | 库存调整费用                                                 |        |
| data>>sharedOtherFbaInventoryFees              | [number]     | 其他仓储费                                                   |        |
| data>>fbaStorageFeeAccrual                     | [number]     | 月仓储费-本月计提                                            |        |
| data>>fbaStorageFeeAccrualDifference           | [number]     | 月仓储费-上月冲销                                            |        |
| data>>longTermStorageFeeAccrual                | [number]     | 长期仓储费-本月计提                                          |        |
| data>>longTermStorageFeeAccrualDifference      | [number]     | 长期仓储费-上月冲销                                          |        |
| data>>sharedFbaIntegerernationalInboundFee     | [number]     | FBA国际物流货运费                                            |        |
| data>>adjustments                              | [number]     | 调整费用                                                     |        |
| data>>totalPlatformOtherFee                    | [number]     | 平台其他费                                                   |        |
| data>>shippingLabelPurchases                   | [number]     | 运输标签费                                                   |        |
| data>>sharedCarrierShippingLabelAdjustments    | [number]     | 承运人装运标签调整费                                         |        |
| data>>sharedLiquidationsFees                   | [number]     | 清算费                                                       |        |
| data>>sharedManualProcessingFee                | [number]     | 人工处理费用                                                 |        |
| data>>sharedOtherServiceFees                   | [number]     | 其他服务费                                                   |        |
| data>>totalSalesTax                            | [number]     | 销售税                                                       |        |
| data>>tcsIgstCollected                         | [number]     | TCS-IGST                                                     |        |
| data>>tcsSgstCollected                         | [number]     | TCS-SGST                                                     |        |
| data>>tcsCgstCollected                         | [number]     | TCS-CGST                                                     |        |
| data>>sharedComminglingVatExpenses             | [number]     | 混合VAT                                                      |        |
| data>>taxCollected                		 | [number]     | VAT/GST                          |        |
| data>>taxCollectedProduct        		 | [number]     | 商品价格税                           |        |
| data>>taxCollectedDiscount        		 | [number]     | 促销折扣税                           |        |
| data>>taxCollectedShipping        		 | [number]     | 买家运费税                           |        |
| data>>taxCollectedGiftWrap        		 | [number]     | 礼品包装税                         | &nbsp;  |
| data>>sharedTaxAdjustment                      | [number]     | 商品税调整                                                   |        |
| data>>salesTaxRefund                           | [number]     | 销售税退款额                                                 |        |
| data>>tcsIgstRefunded                          | [number]     | TCS-IGST                                                     |        |
| data>>tcsSgstRefunded                          | [number]     | TCS-SGST                                                     |        |
| data>>tcsCgstRefunded                          | [number]     | TCS-CGST                                                     |        |
| data>>taxRefunded                              | [number]     | VAT/GST                                                      |        |
| data>>taxRefundedProduct          		 | [number]     | 商品价格税退款                        |        |
| data>>taxRefundedDiscount         		 | [number]     | 促销折扣税退款                        |        |
| data>>taxRefundedShipping         		 | [number]     | 买家运费税退款                        |        |
| data>>taxRefundedGiftWrap         		 | [number]     | 礼品包装税退款                        |        |
| data>>salesTaxWithheld                         | [number]     | 市场税                                                       |        |
| data>>refundTaxWithheld                        | [number]     | 市场税退款额                                                 |        |
| data>>tdsSection194ONet                        | [number]     | 混合网路费用                                                 |        |
| data>>cgPriceTotal                             | [number]     | 采购成本                                                     |        |
| data>>cgPriceAbsTotal            		 | [number]     | 采购成本绝对值                                                |        |
| data>>hasCgPriceDetail                         | [int]      | 是否有采购成本明细                                           |        |
| data>>cgUnitPrice                              | [number]     | 采购均价                                                     |        |
| data>>proportionOfCg                           | [number]     | 采购占比                                                     |        |
| data>>cgTransportCostsTotal                    | [number]     | 头程成本                                                     |        |
| data>>hasCgTransportCostsDetail                | [int]      | 是否有物流（头程）成本明细                                   |        |
| data>>cgTransportUnitCosts                     | [number]     | 头程均价                                                     |        |
| data>>proportionOfCgTransport                  | [number]     | 头程占比                                                     |        |
| data>>totalCost                                | [number]     | 合计成本                                                     |        |
| data>>proportionOfTotalCost                    | [number]     | 合计成本占比                                                 |        |
| data>>cgOtherCostsTotal                        | [number]     | 其他成本                                                     |        |
| data>>cgOtherUnitCosts                         | [number]     | 其他均价                                                     |        |
| data>>hasCgOtherCostsDetail                    | [int]      | 是否有其他成本明细                                           |        |
| data>>proportionOfCgOtherCosts                 | [number]     | 其他成本占比                                                 |        |
| data>>grossProfit                              | [number]     | 毛利润                                                       |        |
| data>>grossProfitTax                           | [number]     | 毛利润税费                                                    |        |
| data>>grossProfitIncome                        | [number]     | 毛利润收入                                                       |        |
| data>>grossRate                                | [number]     | 毛利率                                                       |        |
| data>>otherFeeStr                              | [array]      | 自定义费用信息                                                    |        |
| data>>otherFeeStr>>otherFeeTypeId              | [number]     | 费用标识                                                          |        |
| data>>otherFeeStr>>otherFeeName                | [string]     | 费用名称                                                         |        |
| data>>otherFeeStr>>feeAllocation               | [number]     | 费用                                                             |        |
| data>>customOrderFee                           | [number]     | 订单其他费                                                    |        |
| data>>customOrderFeePrincipal                  | [number]     | 站外推广费-本金                                              |        |
| data>>customOrderFeeCommission                 | [number]     | 站外推广费-佣金                                              |        |
| data>>records>>transactionStatus               | [string]     | 交易状态                             |       |
| data>>records>>transactionStatusCode           | [string]     | 交易状态码                           |       |
| data>>sids                                     | [string]     | 店铺ID，多个以英文逗号分隔                                       |        |
| data>>postedDateLocale                         | [string]     | 本地时间                                                     |        |
| data>>date                                     | [string]     | 年月日 用于展示的时间                                        |        |
| data>>storeName                                | [string]     | 店铺                                                         |        |
| data>>countryCode                              | [string]     | 国家编码                                                     |        |
| data>>country                                  | [string]     | 国家中文名                                                   |        |
| data>>sellerPrincipalRealname                  | [string]     | 店铺负责人                                                   |        |
| data>>currencyCode                             | [string]     | 币种                                                         |        |
| data>>currencyIcon                             | [string]     | 币种符号                                                     |        |
| data>>records>>others                          | [number]     | 平台收入中其他收入的其他费用                                                          |        | 
| data>>totalPlatformExpenditure                 | [number]     | 平台支出                                                     |        |
| data>>otherFeeTotal                            | [number]     | 其他费总和                                                   |  &nbsp;|

## 返回成功示例
```
{
    "code": 0,
    "msg": null,
    "data": [
        {
            "totalFbaAndFbmQuantity": 0,
            "totalFbaAndFbmAmount": null,
            "totalSalesQuantity": 0,
            "fbaSalesQuantity": 0,
            "fbmSalesQuantity": 0,
            "totalReshipQuantity": 0,
            "reshipFbmProductSalesQuantity": 0,
            "reshipFbmProductSaleRefundsQuantity": 0,
            "reshipFbaProductSalesQuantity": 0,
            "reshipFbaProductSaleRefundsQuantity": 0,
            "mcFbaFulfillmentFeesQuantity": 0,
            "cgAbsQuantity": null,
            "cgQuantity": 0,
            "fbaInventoryCreditQuantity": 0,
            "disposalQuantity": 0,
            "removalQuantity": 0,
            "totalAdsSales": null,
            "adsSdSales": null,
            "adsSpSales": null,
            "sharedAdsSbSales": null,
            "sharedAdsSbvSales": null,
            "totalAdsSalesQuantity": 0,
            "adsSdSalesQuantity": 0,
            "adsSpSalesQuantity": 0,
            "sharedAdsSbSalesQuantity": 0,
            "sharedAdsSbvSalesQuantity": 0,
            "totalSalesAmount": null,
            "fbaSaleAmount": null,
            "fbmSaleAmount": null,
            "shippingCredits": null,
            "promotionalRebates": null,
            "fbaInventoryCredit": null,
            "cashOnDelivery": null,
            "otherInAmount": null,
            "fbaLiquidationProceeds": null,
            "fbaLiquidationProceedsAdjustments": null,
            "amazonShippingReimbursement": null,
            "safeTReimbursement": null,
            "netcoTransaction": null,
            "reimbursements": null,
            "clawbacks": null,
            "sharedComminglingVatIncome": null,
            "giftWrapCredits": null,
            "guaranteeClaims": null,
            "costOfPoIntegersGranted": null,
            "others": null,
            "totalSalesRefunds": null,
            "fbaSalesRefunds": null,
            "fbmSalesRefunds": null,
            "shippingCreditRefunds": null,
            "giftWrapCreditRefunds": null,
            "chargebacks": null,
            "costOfPoIntegersReturned": null,
            "promotionalRebateRefunds": null,
            "totalFeeRefunds": null,
            "sellingFeeRefunds": null,
            "fbaTransactionFeeRefunds": null,
            "refundAdministrationFees": null,
            "otherTransactionFeeRefunds": null,
            "refundForAdvertiser": null,
            "pointsAdjusted": null,
            "shippingLabelRefunds": null,
            "refundsQuantity": 0,
            "refundsRate": 0.0000,
            "fbaReturnsQuantity": 0,
            "fbaReturnsSaleableQuantity": 0,
            "fbaReturnsUnsaleableQuantity": 0,
            "fbaReturnsQuantityRate": 0.0000,
            "platformFee": null,
            "totalFbaDeliveryFee": null,
            "fbaDeliveryFee": null,
            "mcFbaDeliveryFee": null,
            "otherTransactionFees": null,
            "totalAdsCost": null,
            "adsSpCost": null,
            "adsSbCost": null,
            "adsSbvCost": null,
            "adsSdCost": null,
            "sharedCostOfAdvertising": null,
            "promotionFee": null,
            "sharedSubscriptionFee": null,
            "sharedLdFee": null,
            "sharedCouponFee": null,
            "sharedEarlyReviewerProgramFee": null,
            "sharedVineFee": null,
            "totalStorageFee": null,
            "fbaStorageFee": null,
            "sharedFbaStorageFee": null,
            "longTermStorageFee": null,
            "sharedLongTermStorageFee": null,
            "sharedStorageRenewalBilling": null,
            "sharedFbaDisposalFee": null,
            "sharedFbaRemovalFee": null,
            "sharedFbaInboundTransportationProgramFee": null,
            "sharedLabelingFee": null,
            "sharedPolybaggingFee": null,
            "sharedBubblewrapFee": null,
            "sharedTapingFee": null,
            "sharedFbaCustomerReturnFee": null,
            "sharedFbaInboundDefectFee": null,
            "sharedFbaOverageFee": null,
            "sharedAmazonPartneredCarrierShipmentFee": null,
            "sharedFbaInboundConvenienceFee": null,
            "sharedItemFeeAdjustment": null,
            "sharedOtherFbaInventoryFees": null,
            "fbaStorageFeeAccrual": null,
            "fbaStorageFeeAccrualDifference": null,
            "longTermStorageFeeAccrual": null,
            "longTermStorageFeeAccrualDifference": null,
            "sharedFbaIntegerernationalInboundFee": null,
            "adjustments": null,
            "totalPlatformOtherFee": null,
            "shippingLabelPurchases": null,
            "sharedCarrierShippingLabelAdjustments": null,
            "sharedLiquidationsFees": null,
            "sharedManualProcessingFee": null,
            "sharedOtherServiceFees": null,
            "totalSalesTax": null,
            "taxCollected": null,
            "taxCollectedGiftWrap": null,
            "taxCollectedShipping": null,
            "taxCollectedDiscount": null,
            "taxCollectedProduct": null,
            "tcsIgstCollected": null,
            "tcsSgstCollected": null,
            "tcsCgstCollected": null,
            "sharedComminglingVatExpenses": null,
            "sharedTaxAdjustment": null,
            "salesTaxRefund": null,
            "taxRefunded": null,
            "taxRefundedGiftWrap": null,
            "taxRefundedShipping": null,
            "taxRefundedDiscount": null,
            "taxRefundedProduct": null,
            "tcsIgstRefunded": null,
            "tcsSgstRefunded": null,
            "tcsCgstRefunded": null,
            "salesTaxWithheld": null,
            "refundTaxWithheld": null,
            "tdsSection194ONet": null,
            "cgPriceTotal": null,
            "cgPriceAbsTotal": null,
            "hasCgPriceDetail": 0,
            "cgUnitPrice": 0.00,
            "proportionOfCg": null,
            "cgTransportCostsTotal": null,
            "hasCgTransportCostsDetail": 0,
            "cgTransportUnitCosts": 0.00,
            "proportionOfCgTransport": null,
            "totalCost": null,
            "proportionOfTotalCost": null,
            "cgOtherCostsTotal": null,
            "cgOtherUnitCosts": 0.00,
            "hasCgOtherCostsDetail": 0,
            "proportionOfCgOtherCosts": null,
            "grossProfit": null,
            "grossRate": null,
            "grossProfitIncome": null,
            "grossProfitTax": null,
            "otherFeeStr": [
                {
                    "otherFeeTypeId": 1004435,
                    "otherFeeName": "123",
                    "feeAllocation": 0.00
                }
            ],
            "customOrderFee": null,
            "customOrderFeePrincipal": null,
            "customOrderFeeCommission": null,
            "roi": null,
            "sids": "101",
            "postedDateLocale": "2023-05-10",
            "date": "2023-05-10",
            "storeName": null,
            "countryCode": null,
            "country": null,
            "sellerPrincipalRealname": null,
            "currencyCode": null,
            "currencyIcon": null,
            "totalPlatformExpenditure": null,
            "otherFeeTotal": null,
            "platformIncome":0,
            "platformFee":0,
            "grossProfitTax":0
        }
    ]
}
```