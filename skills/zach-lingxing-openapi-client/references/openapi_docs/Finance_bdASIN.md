# 查询利润报表-ASIN

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/asin/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名      | 说明                                                                         | 必填 | 类型        | 示例   |
| :---------  |:---------------------------------------------------------------------------| :------------ |:----------| :------------ |
| offset      | 分页偏移量                                                                      | 否 | [int]     |0|
| length      | 分页长度，上限10000                                                               | 否 | [int]     | 1000  |
| mids        | 站点id                                                                       | 否 | [array]   |[2]|
| sids        | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否 | [array]   | [110] |
| monthlyQuery| 是否按月查询：<br>false 按天【默认值】<br>true 按月                                        |否 | [boolean] | false |
| startDate   | 开始时间【结算时间，双闭区间】<br>按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d<br>按月：开始结束时间年月相同，格式：Y-m | 是 | [string]  |2023-09-21|
| endDate     | 结束时间【结算时间，双闭区间】<br>按天：开始结束时间间隔最长不能跨度 31 天，格式：Y-m-d<br>按月：开始结束时间年月相同，格式：Y-m | 是 | [string]  |2023-10-20|
| searchField | 搜索值类型，ASIN                                                                 | 否 | [string]  | asin|
| searchValue | 搜索的值                                                                       |否 | [array]   | ["B085NQDDXS","B085NQLM2D"] |
| currencyCode| 币种code                                                                     |否 | [string]  | CNY  |
| summaryEnabled| 是否按asin汇总返回：<br>false 默认值 <br>true                                         |否 | [boolean] | false  |
| orderStatus|交易状态<br/>Deferred 已推迟<br/>Disbursed 已发放【默认】<br/>DisbursedAndPreSettled 已发放（含预结算）<br/>All 全部|否|[string]|"Disbursed"|

## 请求示例
```
{
    "offset": 0,
    "length": 1000,
    "mids": [
        2
    ],
    "sids": [
        110
    ],
    "monthlyQuery": false,
    "startDate": "2023-09-21",
    "endDate": "2023-10-20",
    "searchField": "asin",
    "searchValue": [
        "B085NQDDXS",
        "B085NQLM2D"

    ],
    "currencyCode": "CNY",
    "summaryEnabled": false
}
```

## 返回结果
Json Object

| 参数名                                       | 类型        | 说明                             | 示例   |
| :------------------------------------------ |:----------| :------------------------------- | :------ |
| code                                        | [int]     | 状态码，0 成功                    |        |
| msg                                         | [string]  | 消息提示                          |        |
| data                                        | [object]  | 响应数据                          |        |
| data>>total                                 | [int]     | 总数                              |        |
| data>>records                               | [array]   | 数据列表                           |        |
| data>>records>>totalFbaAndFbmQuantity       | [int]     | fba和fbm销量加总，用于计算占比        |        |
| data>>records>>totalFbaAndFbmAmount         | [number]  | fba和fbm销售额加总，用于计算占比      |        |
| data>>records>>totalSalesQuantity           | [int]     | 销量                              |        |
| data>>records>>fbaSalesQuantity             | [int]     | FBA销量                           |        |
| data>>records>>fbmSalesQuantity             | [int]     | FBM销量                           |        |
| data>>records>>totalReshipQuantity          | [int]     | 补换货量                           |        |
| data>>records>>reshipFbmProductSalesQuantity| [int]     | FBM补（换）货量                     |        |
| data>>records>>reshipFbmProductSaleRefundsQuantity | [int]     | FBM补（换）货退回量                 |        |
| data>>records>>reshipFbaProductSalesQuantity | [int]     | FBA补（换）货量                    |       |
| data>>records>>reshipFbaProductSaleRefundsQuantity | [int]     | FBA补（换）货退回量                 |        |
| data>>records>>mcFbaFulfillmentFeesQuantity | [int]     | 多渠道销量                         |        |
| data>>records>>cgAbsQuantity                | [number]  | 成本数量绝对值                                              |        |
| data>>records>>cgQuantity                   | [number]  | 成本数量                                                   |        |
| data>>records>>totalAdsSales                | [number]  | 广告销售额                         |        |
| data>>records>>adsSdSales                   | [number]  | sd广告销售额                       |        |
| data>>records>>adsSpSales                   | [number]  | sp广告销售额                       |        |
| data>>records>>sharedAdsSbSales             | [number]  | sb广告销售额                       |        |
| data>>records>>sharedAdsSbvSales            | [number]  | sbv广告销售额                      |        |
| data>>records>>totalAdsSalesQuantity        | [int]     | 广告销量                           |        |
| data>>records>>adsSdSalesQuantity           | [int]     | sd广告销量                         |        |
| data>>records>>adsSpSalesQuantity           | [int]     | sp广告销量                         |        |
| data>>records>>sharedAdsSbSalesQuantity     | [int]     | sb广告销量                         |        |
| data>>records>>sharedAdsSbvSalesQuantity    | [int]     | sbv广告销量                        |        |
| data>>records>>totalSalesAmount             | [number]  | 销售额                             |        |
| data>>records>>fbaSaleAmount                | [number]  | FBA销售额                          |        |
| data>>records>>fbmSaleAmount                | [number]  | FBM销售额                          |        |
| data>>records>>shippingCredits              | [number]  | 买家运费                           |        |
| data>>records>>promotionalRebates           | [number]  | 促销折扣                           |        |
| data>>records>>fbaInventoryCredit           | [number]  | FBA库存赔偿                        |        |
| data>>records>>cashOnDelivery               | [number]  | COD                              |        |
| data>>records>>otherInAmount                | [number]  | 其他收入                           |        |
| data>>records>>fbaLiquidationProceeds       | [number]  | 清算收入                           |        |
| data>>records>>fbaLiquidationProceedsAdjustments | [number]  | 清算调整                           |        |
| data>>records>>amazonShippingReimbursement  | [number]  | 亚马逊运费赔偿                      |        |
| data>>records>>safeTReimbursement           | [number]  | Safe-T索赔                         |        |
| data>>records>>netcoTransaction             | [number]  | Netco交易                          |        |
| data>>records>>reimbursements               | [number]  | 赔偿收入                           |        |
| data>>records>>clawbacks                    | [number]  | 追索收入                           |        |
| data>>records>>sharedComminglingVatIncome   | [number]  | 混合VAT收入                        |        |
| data>>records>>giftWrapCredits              | [number]  | 包装收入                           |        |
| data>>records>>guaranteeClaims              | [number]  | 买家交易保障索赔额                   |        |
| data>>records>>costOfPointegersGranted      | [number]  | 积分抵减收入                       |        |
| data>>records>>totalSalesRefunds            | [number]  | 收入退款额                         |        |
| data>>records>>fbaSalesRefunds              | [number]  | FBA销售退款额                      |        |
| data>>records>>fbmSalesRefunds              | [number]  | FBM销售退款额                      |        |
| data>>records>>shippingCreditRefunds        | [number]  | 买家运费退款额                      |       |
| data>>records>>giftWrapCreditRefunds        | [number]  | 买家包装退款额                      |       |
| data>>records>>chargebacks                  | [number]  | 买家拒付                           |       |
| data>>records>>costOfPointegersReturned     | [number]  | 积分抵减退回                       |        |
| data>>records>>promotionalRebateRefunds     | [number]  | 促销折扣退款额                      |        |
| data>>records>>totalFeeRefunds              | [number]  | 费用退款额                         |        |
| data>>records>>sellingFeeRefunds            | [number]  | 平台费退款额                       |        |
| data>>records>>fbaTransactionFeeRefunds     | [number]  | 发货费退款额                       |        |
| data>>records>>refundAdministrationFees     | [number]  | 交易费用退款额                     |        |
| data>>records>>otherTransactionFeeRefunds   | [number]  | 其他订单费退款额                    |       |
| data>>records>>refundForAdvertiser          | [number]  | 广告退款额                         |        |
| data>>records>>pointsAdjusted               | [number]  | 积分费用                           |        |
| data>>records>>shippingLabelRefunds         | [number]  | 运输标签费退款                     |         |
| data>>records>>refundsQuantity              | [int]     | 退款量                             |        |
| data>>records>>refundsRate                  | [number]  | 退款率                            |        |
| data>>records>>fbaReturnsQuantity           | [int]     | 退货量                             |        |
| data>>records>>fbaReturnsSaleableQuantity   | [int]     | 退货量（可售）                       |        |
| data>>records>>fbaReturnsUnsaleableQuantity | [int]     | 退货量（不可售）                      |        |
| data>>records>>fbaReturnsQuantityRate       | [number]  | 退货率                             |        |
| data>>records>>fbaDeliveryFee               | [number]  | FBA发货费                          |        |
| data>>records>>mcFbaDeliveryFee             | [number]  | FBA发货费(多渠道)                   |        |
| data>>records>>totalFbaDeliveryFee          | [number]  | FBA发货费合计                       |        |
| data>>records>>otherTransactionFees         | [number]  | 其他订单费用                       |        |
| data>>records>>totalAdsCost                 | [number]  | 广告费                             |        |
| data>>records>>adsSpCost                    | [number]  | SP广告费                           |        |
| data>>records>>adsSbCost                    | [number]  | SB广告费                           |        |
| data>>records>>adsSbvCost                   | [number]  | SBV广告费                          |        |
| data>>records>>adsSdCost                    | [number]  | SD广告费                           |        |
| data>>records>>sharedCostOfAdvertising      | [number]  | 差异分摊                           |        |
| data>>records>>sharedAdsAlCost              | [number]     | Live广告                               |        |
| data>>records>>sharedAdsCcCost	           | [number]     | 创作者计划                               |        |
| data>>records>>sharedAdsSspaotCost	       | [number]     | TV广告                               |        |
| data>>records>>sharedAdsSarCost	           | [number]     | 零售商赞助广告                               |        |
| data>>records>>promotionFee                 | [number]  | 推广费                             |        |
| data>>records>>sharedSubscriptionFee        | [number]  | 订阅费                             |        |
| data>>records>>sharedLdFee                  | [number]  | 秒杀费                             |        |
| data>>records>>sharedCouponFee              | [number]  | 优惠券                             |        |
| data>>records>>sharedEarlyReviewerProgramFee| [number]  | 早期评论人计划                     |        |
| data>>records>>sharedVineFee                | [number]  | vine                               |        |
| data>>records>>totalStorageFee              | [number]  | FBA仓储费                          |        |
| data>>records>>fbaStorageFee                | [number]  | 月度仓库费                         |        |
| data>>records>>sharedFbaStorageFee          | [number]  | 月度仓储费差异                     |        |
| data>>records>>longTermStorageFee           | [number]  | 长期仓储费                         |        |
| data>>records>>sharedLongTermStorageFee     | [number]  | 长期仓储费差异                     |        |
| data>>records>>sharedStorageRenewalBilling  | [number]  | 库存续订费用                       |        |
| data>>records>>sharedFbaDisposalFee         | [number]  | FBA销毁费                          |        |
| data>>records>>sharedFbaRemovalFee          | [number]  | FBA移除费                          |        |
| data>>records>>sharedFbaInboundTransportationProgramFee | [number]  | 入仓手续费              |        |
| data>>records>>sharedLabelingFee            | [number]  | 标签费                             |        |
| data>>records>>sharedPolybaggingFee         | [number]  | 塑料包装费                         |        |
| data>>records>>sharedBubblewrapFee          | [number]  | 泡沫包装费                         |        |
| data>>records>>sharedTapingFee              | [number]  | 胶带费                             |        |
| data>>records>>sharedAwdProcessingFee   | [number]     | AWD处理费                           |        |
| data>>records>>sharedAwdTransportationFee   | [number]     | AWD运输费                           |        |
| data>>records>>sharedAwdStorageFee   | [number]     | AWD仓储费                           |        |
| data>>records>>sharedStarStorageFee   | [number]     | 卫星仓仓储费                           |        |
| data>>records>>sharedFbaCustomerReturnFee   | [number]  | FBA卖家退回费                      |        |
| data>>records>>sharedFbaInboundDefectFee    | [number]  | FBA仓储费入库缺陷费                       |        |
| data>>records>>sharedFbaOverageFee          | [number]  | 超量仓储费                         |        |
| data>>records>>sharedAmazonPartneredCarrierShipmentFee | [number]  | 合作承运费              |        |
| data>>records>>sharedFbaInboundConvenienceFee | [number]  | 入库配置费                          |        |
| data>>records>>sharedItemFeeAdjustment      | [number]  | 库存调整费用                       |        |
| data>>records>>sharedOtherFbaInventoryFees  | [number]  | 其他仓储费                         |        |
| data>>records>>fbaStorageFeeAccrual         | [number]  | 月仓储费-本月计提                   |        |
| data>>records>>fbaStorageFeeAccrualDifference | [number]  | 月仓储费-上月冲销                 |        |
| data>>records>>longTermStorageFeeAccrual    | [number]  | 长期仓储费-本月计提                 |        |
| data>>records>>longTermStorageFeeAccrualDifference | [number]  | 长期仓储费-上月冲销          |        |
| data>>records>>sharedFbaintegerernationalInboundFee | [number]  | FBA国际物流货运费          |        |
| data>>records>>adjustments                  | [number]  | 调整费用                          |        |
| data>>records>>totalPlatformOtherFee        | [number]  | 平台其他费                         |        |
| data>>records>>shippingLabelPurchases       | [number]  | 运输标签费                         |        |
| data>>records>>sharedCarrierShippingLabelAdjustments | [number]  | 承运人装运标签调整费        |        |
| data>>records>>sharedLiquidationsFees       | [number]  | 清算费                            |        |
| data>>records>>sharedManualProcessingFee    | [number]  | 人工处理费用                       |        |
| data>>records>>sharedOtherServiceFees       | [number]  | 其他服务费                         |        |
| data>>records>>totalSalesTax                | [number]  | 销售税                            |        |
| data>>records>>tcsIgstCollected             | [number]  | TCS-IGST                          |        |
| data>>records>>tcsSgstCollected             | [number]  | TCS-SGST                          |        |
| data>>records>>tcsCgstCollected             | [number]  | TCS-CGST                          |        |
| data>>records>>sharedComminglingVatExpenses | [number]  | 混合VAT                           |        |
| data>>records>>taxCollected                 | [number]  | VAT/GST                          |        |
| data>>records>>taxCollectedProduct          | [number]  | 商品价格税                           |        |
| data>>records>>taxCollectedDiscount         | [number]  | 促销折扣税                           |        |
| data>>records>>taxCollectedShipping         | [number]  | 买家运费税                           |        |
| data>>records>>taxCollectedGiftWrap         | [number]  | 礼品包装税                         | &nbsp;  |
| data>>records>>sharedTaxAdjustment          | [number]  | 商品税调整                       |        |
| data>>records>>salesTaxRefund               | [number]  | 销售税退款额                       |        |
| data>>records>>tcsIgstRefunded              | [number]  | TCS-IGST                         |        |
| data>>records>>tcsSgstRefunded              | [number]  | TCS-SGST                         |        |
| data>>records>>tcsCgstRefunded              | [number]  | TCS-CGST                         |        |
| data>>records>>taxRefunded                  | [number]  | VAT/GST                          |        |
| data>>records>>taxRefundedProduct           | [number]  | 商品价格税退款                        |        |
| data>>records>>taxRefundedDiscount          | [number]  | 促销折扣税退款                        |        |
| data>>records>>taxRefundedShipping          | [number]  | 买家运费税退款                        |        |
| data>>records>>taxRefundedGiftWrap          | [number]  | 礼品包装税退款                        |        |
| data>>records>>salesTaxWithheld             | [number]  | 市场税                            |        |
| data>>records>>refundTaxWithheld            | [number]  | 市场税退款额                       |        |
| data>>records>>tdsSection194ONet            | [number]  | 混合网路费用                       |        |
| data>>records>>cgPriceTotal                 | [number]  | 采购成本                          |        |
| data>>records>>cgPriceAbsTotal              | [number]  | 采购成本绝对值                                                |        |
| data>>records>>hasCgPriceDetail             | [int]     | 是否有采购成本明细                  |        |
| data>>records>>cgUnitPrice                  | [number]  | 采购均价                           |        |
| data>>records>>proportionOfCg               | [number]  | 采购占比                           |        |
| data>>records>>cgTransportCostsTotal        | [number]  | 头程成本                           |        |
| data>>records>>hasCgTransportCostsDetail    | [int]     | 是否有物流（头程）成本明细            |        |
| data>>records>>cgTransportUnitCosts         | [number]  | 头程均价                           |        |
| data>>records>>proportionOfCgTransport      | [number]  | 头程占比                           |        |
| data>>records>>totalCost                    | [number]  | 合计成本                           |        |
| data>>records>>proportionOfTotalCost        | [number]  | 合计成本占比                       |        |
| data>>records>>cgOtherCostsTotal            | [number]  | 其他成本                           |        |
| data>>records>>cgOtherUnitCosts             | [number]  | 其他均价                           |        |
| data>>records>>hasCgOtherCostsDetail        | [int]     | 是否有其他成本明细                   |        |
| data>>records>>proportionOfCgOtherCosts     | [number]  | 其他成本占比                        |        |
| data>>records>>grossProfit                  | [number]  | 毛利润                             |        |
| data>>records>>grossProfitTax               | [number]  | 毛利润税费                         |        |
| data>>records>>grossProfitIncome            | [number]  | 毛利润收入                          |        |
| data>>records>>grossRate                    | [number]  | 毛利率                             |        |
| data>>records>>otherFeeStr                  | [array]   | 自定义费用信息                      |        |
| data>>records>>otherFeeStr>>otherFeeTypeId  | [number]  | 费用标识                            |        |
| data>>records>>otherFeeStr>>otherFeeName    | [string]  | 费用名称                           |        |
| data>>records>>otherFeeStr>>feeAllocation   | [number]  | 费用                               |        |
| data>>records>>customOrderFee               | [number]  | 订单其他费                          |        |
| data>>records>>customOrderFeePrincipal      | [number]  | 站外推广费-本金                      |        |
| data>>records>>customOrderFeeCommission     | [number]  | 站外推广费-佣金                      |        |
| data>>records>>transactionStatus            | [string]  | 交易状态                             |       |
| data>>records>>transactionStatusCode        | [string]  | 交易状态码                           |       |
| data>>records>>id                           | [string]  | 记录id【非业务唯一键】                                         |        |
| data>>records>>postedDateLocale             | [string]  | 按天汇总                            |        |
| data>>records>>isDisplayDetail              | [boolean] | 是否展示明细                        |        |
| data>>records>>smallImageUrl                | [string]  | 图片                               |        |
| data>>records>>parentAsin                   | [string]  | 父asin                             |        |
| data>>records>>asin                         | [string]  | asin                               |        |
| data>>records>>storeName                    | [object]  | 店铺名称，单店铺查询为字符串类型，多店铺查询为字符串数组类型                               |        |
| data>>records>>sid                          | [string]  | 店铺id                             |        |
| data>>records>>sids                         | [string]  | 店铺id，多个以英文逗号分隔             |        |
| data>>records>>asins                        | [string]  | 该行的所有asin，asin维度取值与「asin」字段一致|       |
| data>>records>>country                      | [object]  | 国家，单店铺查询为字符串类型，多店铺查询为字符串数组类型                               |        |
| data>>records>>countryCode                  | [string]  | 国家                               |        |
| data>>records>>localName                    | [string]  | 品名                               |        |
| data>>records>>localSku                     | [string]  | sku                                |        |
| data>>records>>itemName                     | [string]  | 标题                               |        |
| data>>records>>principalRealname            | [string]  | 负责人                             |        |
| data>>records>>productDeveloperRealname     | [string]  | 产品开发负责人                       |        |
| data>>records>>categoryName                 | [string]  | 分类                               |        |
| data>>records>>brandName                    | [string]  | 品牌                               |        |
| data>>records>>currencyCode                 | [string]  | 币种                               |        |
| data>>records>>currencyIcon                 | [string]  | 币种符号                            |        |
| data>>records>>fbaInventoryCreditQuantity   | [number]  | 赔偿量                              |        |
| data>>records>>disposalQuantity             | [number]  | 销毁量                              |        |
| data>>records>>removalQuantity              | [number]  | 移除量                              |        |
| data>>records>>others                       | [number]  | 平台收入中其他收入的其他费用                                |        |
| data>>records>>listingTagIds                | [string]  | listing标签id                       | &nbsp; |
|data>>records>>platformIncome         |      [number]      |  平台收入   |   |
|data>>records>>platformExpense            |        [number]    |    平台支出   |   |
|data>>records>>grossProfitTax         |        [number]    |    合计税费   |   |


## 返回成功示例
```
{
    "code": 0,
    "msg": null,
    "data": {
        "records": [
            {
                "totalFbaAndFbmQuantity": 0,
                "totalFbaAndFbmAmount": 0.00,
                "totalSalesQuantity": 0,
                "fbaSalesQuantity": 0,
                "fbmSalesQuantity": 0,
                "totalReshipQuantity": 0,
                "reshipFbmProductSalesQuantity": 0,
                "reshipFbmProductSaleRefundsQuantity": 0,
                "reshipFbaProductSalesQuantity": 0,
                "reshipFbaProductSaleRefundsQuantity": 0,
                "mcFbaFulfillmentFeesQuantity": 0,
                "cgAbsQuantity": 0,
                "cgQuantity": 0,
                "fbaInventoryCreditQuantity": 0,
                "disposalQuantity": 0,
                "removalQuantity": 0,
                "totalAdsSales": 0.00,
                "adsSdSales": 0.00,
                "adsSpSales": 0.00,
                "sharedAdsSbSales": 0.00,
                "sharedAdsSbvSales": 0.00,
                "totalAdsSalesQuantity": 0,
                "adsSdSalesQuantity": 0,
                "adsSpSalesQuantity": 0,
                "sharedAdsSbSalesQuantity": 0,
                "sharedAdsSbvSalesQuantity": 0,
                "totalSalesAmount": 0.00,
                "fbaSaleAmount": 0.00,
                "fbmSaleAmount": 0.00,
                "shippingCredits": 0.00,
                "promotionalRebates": 0.00,
                "fbaInventoryCredit": 0.00,
                "cashOnDelivery": 0.00,
                "otherInAmount": 0.00,
                "fbaLiquidationProceeds": 0.00,
                "fbaLiquidationProceedsAdjustments": 0.00,
                "amazonShippingReimbursement": 0.00,
                "safeTReimbursement": 0.00,
                "netcoTransaction": 0.00,
                "reimbursements": 0.00,
                "clawbacks": 0.00,
                "sharedComminglingVatIncome": 0.00,
                "giftWrapCredits": 0.00,
                "guaranteeClaims": 0.00,
                "costOfPoIntegersGranted": 0.00,
                "others": 0.00,
                "totalSalesRefunds": 0.00,
                "fbaSalesRefunds": 0.00,
                "fbmSalesRefunds": 0.00,
                "shippingCreditRefunds": 0.00,
                "giftWrapCreditRefunds": 0.00,
                "chargebacks": 0.00,
                "costOfPoIntegersReturned": 0.00,
                "promotionalRebateRefunds": 0.00,
                "totalFeeRefunds": 0.00,
                "sellingFeeRefunds": 0.00,
                "fbaTransactionFeeRefunds": 0.00,
                "refundAdministrationFees": 0.00,
                "otherTransactionFeeRefunds": 0.00,
                "refundForAdvertiser": 0.00,
                "pointsAdjusted": 0.00,
                "shippingLabelRefunds": 0.00,
                "refundsQuantity": 0,
                "refundsRate": 0.0000,
                "fbaReturnsQuantity": 0,
                "fbaReturnsSaleableQuantity": 0,
                "fbaReturnsUnsaleableQuantity": 0,
                "fbaReturnsQuantityRate": 0.0000,
                "platformFee": 0.00,
                "totalFbaDeliveryFee": 0.00,
                "fbaDeliveryFee": 0.00,
                "mcFbaDeliveryFee": 0.00,
                "otherTransactionFees": 0.00,
                "totalAdsCost": 0.00,
                "adsSpCost": 0.00,
                "adsSbCost": 0.00,
                "adsSbvCost": 0.00,
                "adsSdCost": 0.00,
                "sharedCostOfAdvertising": 0.00,
                "promotionFee": 0.00,
                "sharedSubscriptionFee": 0.00,
                "sharedLdFee": 0.00,
                "sharedCouponFee": 0.00,
                "sharedEarlyReviewerProgramFee": 0.00,
                "sharedVineFee": 0.00,
                "totalStorageFee": 0.00,
                "fbaStorageFee": 0.00,
                "sharedFbaStorageFee": 0.00,
                "longTermStorageFee": 0.00,
                "sharedLongTermStorageFee": 0.00,
                "sharedStorageRenewalBilling": 0.00,
                "sharedFbaDisposalFee": 0.00,
                "sharedFbaRemovalFee": 0.00,
                "sharedFbaInboundTransportationProgramFee": 0.00,
                "sharedLabelingFee": 0.00,
                "sharedPolybaggingFee": 0.00,
                "sharedBubblewrapFee": 0.00,
                "sharedTapingFee": 0.00,
                "sharedFbaCustomerReturnFee": 0.00,
                "sharedFbaInboundDefectFee": 0.00,
                "sharedFbaOverageFee": 0.00,
                "sharedAmazonPartneredCarrierShipmentFee": 0.00,
                "sharedFbaInboundConvenienceFee": 0.00,
                "sharedItemFeeAdjustment": 0.00,
                "sharedOtherFbaInventoryFees": 0.00,
                "fbaStorageFeeAccrual": 0.00,
                "fbaStorageFeeAccrualDifference": 0.00,
                "longTermStorageFeeAccrual": 0.00,
                "longTermStorageFeeAccrualDifference": 0.00,
                "sharedFbaIntegerernationalInboundFee": 0.00,
                "adjustments": 0.00,
                "totalPlatformOtherFee": 0.00,
                "shippingLabelPurchases": 0.00,
                "sharedCarrierShippingLabelAdjustments": 0.00,
                "sharedLiquidationsFees": 0.00,
                "sharedManualProcessingFee": 0.00,
                "sharedOtherServiceFees": 0.00,
                "totalSalesTax": 0.00,
                "taxCollected": 0.00,
                "taxCollectedGiftWrap": 0.00,
                "taxCollectedShipping": 0.00,
                "taxCollectedDiscount": 0.00,
                "taxCollectedProduct": 0.00,
                "tcsIgstCollected": 0.00,
                "tcsSgstCollected": 0.00,
                "tcsCgstCollected": 0.00,
                "sharedComminglingVatExpenses": 0.00,
                "sharedTaxAdjustment": 0.00,
                "salesTaxRefund": 0.00,
                "taxRefunded": 0.00,
                "taxRefundedGiftWrap": 0.00,
                "taxRefundedShipping": 0.00,
                "taxRefundedDiscount": 0.00,
                "taxRefundedProduct": 0.00,
                "tcsIgstRefunded": 0.00,
                "tcsSgstRefunded": 0.00,
                "tcsCgstRefunded": 0.00,
                "salesTaxWithheld": 0.00,
                "refundTaxWithheld": 0.00,
                "tdsSection194ONet": 0.00,
                "cgPriceTotal": 0.00,
                "cgPriceAbsTotal": 0.00,
                "hasCgPriceDetail": 0,
                "cgUnitPrice": 0.00,
                "proportionOfCg": 0.0000,
                "cgTransportCostsTotal": 0.00,
                "hasCgTransportCostsDetail": 0,
                "cgTransportUnitCosts": 0.00,
                "proportionOfCgTransport": 0.0000,
                "totalCost": 0.00,
                "proportionOfTotalCost": 0.0000,
                "cgOtherCostsTotal": 0.00,
                "cgOtherUnitCosts": 0.00,
                "hasCgOtherCostsDetail": 0,
                "proportionOfCgOtherCosts": 0.0000,
                "grossProfit": -92.13,
                "grossRate": 0.0000,
                "grossProfitIncome": 0.0000,
                "grossProfitTax": 0.0000,
                "otherFeeStr": [
                    {
                        "otherFeeTypeId": 1174,
                        "otherFeeName": "56783",
                        "feeAllocation": -92.13
                    }
                ],
                "customOrderFee": 0.00,
                "customOrderFeePrincipal": 0.00,
                "customOrderFeeCommission": 0.00,
                "roi": -1.0000,
                "id": "77236",
                "postedDateLocale": "2023-05-15",
                "isDisplayDetail": false,
                "smallImageUrl": "",
                "asin": "B09J4VC1S9",
                "parentAsin": "",
                "storeName": "8p",
                "sid": "102",
                "sids": "102",
                "asins": "B09J4VC1S9",
                "country": "加拿大",
                "countryCode": "CA",
                "localName": "属性更新",
                "localSku": "SKUPUST",
                "itemName": "Monroe kk",
                "model": "",
                "principalRealname": "xxx",
                "productDeveloperRealname": null,
                "categoryName": "",
                "brandName": "",
                "currencyCode": "CAD",
                "currencyIcon": "CA$",
                "listingTagIds": "",
                "platformIncome":0,
                "platformFee":0,
                "grossProfitTax":0
            }
        ],
        "total": 29
    }
}
```

