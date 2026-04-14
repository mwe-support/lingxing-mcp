## 查询利润统计-父ASIN
支持查询新版利润统计的父ASIN维度

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/statistics/open/parent/asin/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| offset      | 分页偏移量| 否 |[int] |0|
| length      | 分页长度，上限10000 | 否 |[int]| 1000  |
| mids        | 站点id | 否 | [array]  |[2]|
| sids        | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否 | [array]  |[17] |
| startDate   | 开始时间，双闭区间【开始结束时间间隔最长不能跨度7天】 | 是 | [string] |2022-09-21|
| endDate     | 结束时间，双闭区间【开始结束时间间隔最长不能跨度7天】 | 是 | [string] |2022-09-25|
| searchField | 搜索值类型：parent_asin|否|[string]| parent_asin |
| searchValue | 搜索值 | 否 |[array]|B07DFKF00SG |
| currencyCode     | 币种code	 | 否  | [string] |CNY|

## 请求示例
```
{
    "offset": 0,
    "length": 1,
    "sids": [
        104
    ],
    "startDate": "2023-07-16",
    "endDate": "2023-07-21",
    "searchField": "parent_asin",
    "searchValue": [
        "B07DFKF00SG"
    ],
    "currencyCode":"CNY"
}
```
## 返回结果
Json Object

| 参数名                                     | 说明                                | 类型    | 示例   |
| :---------------------------------------- | :----------------------------------| :-------| :------ |
| code                                        | 状态码，0 成功                       | [int]   |        |
| msg                                         | 消息提示                            | [string]  |        |
| data                                        | 响应数据                              | [array]  |        |
| data>>total                                 | 总数                                | [int]   |        |
| data>>records                               | 查询数据列表                        | [array]   |        |
| data>>records>>totalFbaAndFbmQuantity       | fba和fbm销量加总，用于计算占比        | [int] |        |
| data>>records>>totalFbaAndFbmAmount         | fba和fbm销售额加总，用于计算占比       | [number] |        |
| data>>records>>id                           | 记录id【非业务唯一键】                | [string]  |        |
| data>>records>>dataDate                     | 日期                              | [string]  |        |
| data>>records>>isDisplayDetail              | 是否展示明细                        | [boolean] |        |
| data>>records>>smallImageUrl                | 图片                                | [string]  |        |
| data>>records>>parentAsin                   | 父asin                              | [string]  |        |
| data>>records>>asin                         | asin                                | [string]  |        |
| data>>records>>sid                          | 店铺id                                 | [array]  |        |
| data>>records>>storeName                    | 店铺名                                | [array]  |        |
| data>>records>>sids                         | 店铺id，多个以逗号分隔              | [string]  |        |
| data>>records>>asins                        | 列表行对应的所有asin，多个以英文逗号分隔 | [string]  |        |
| data>>records>>country                      | 国家                                | [array]  |        |
| data>>records>>countryCode                  | 国家简码                             | [array]  |        |
| data>>records>>localName                    | 品名                                | [string]  |        |
| data>>records>>localSku                     | sku                                 | [string]  |        |
| data>>records>>itemName                     | 标题                                | [string]  |        |
| data>>records>>principalRealname            | 负责人                              | [string]  |        |
| data>>records>>listingTagIds                | listing标签id                       | [string]  |        |
| data>>records>>categoryName                 | 分类                                | [string]  |        |
| data>>records>>brandName                    | 品牌                                | [string]  |        |
| data>>records>>currencyCode                 | 币种                                | [string]  |        |
| data>>records>>currencyIcon                 | 币种符号                            | [string]  |        |
| data>>records>>totalSalesQuantity           | 销量                                | [int]   |        |
| data>>records>>fbaSalesQuantity             | FBA销量                             | [int]   |        |
| data>>records>>fbmSalesQuantity             | FBM销量                             | [int]   |        |
| data>>records>>totalReshipQuantity          | 补换货量                            | [int]   |        |
| data>>records>>reshipFbmProductSalesQuantity | FBM补（换）货量                     | [int]   |        |
| data>>records>>reshipFbmProductSaleRefundsQuantity | FBM补（换）货退回量                 | [int]   |        |
| data>>records>>reshipFbaProductSalesQuantity | FBA补（换）货量                     | [int]   |        |
| data>>records>>reshipFbaProductSaleRefundsQuantity | FBA补（换）货退回量                 | [int]   |        |
| data>>records>>mcFbaFulfillmentFeesQuantity | 多渠道销量                          | [int]   |        |
| data>>records>>totalAdsSales                | 广告销售额                           | [number] |      |
| data>>records>>adsSdSales                   | sd广告销售额                         | [number] |        |
| data>>records>>adsSpSales                   | sp广告销售额                         | [number] |        |
| data>>records>>totalAdsSalesQuantity        | 广告销量                            | [number] |       |
| data>>records>>adsSdSalesQuantity           | sd广告销量                          | [number] |      |
| data>>records>>adsSpSalesQuantity           | sp广告销量                          | [number] |      |
| data>>records>>totalSalesAmount             | 销售额                              | [number]  |        |
| data>>records>>fbaSaleAmount                | FBA销售额                           | [number]  |        |
| data>>records>>fbmSaleAmount                | FBM销售额                           | [number]  |        |
| data>>records>>totalSalesAmountWithTax      | 含税销售额                           | [number] |        |
| data>>records>>shippingCredits              | 买家运费                            | [number]  |        |
| data>>records>>promotionalRebates           | 促销折扣                            | [number]  |        |
| data>>records>>fbaInventoryCredit           | FBA库存赔偿                         | [number]  |        |
| data>>records>>cashOnDelivery               | COD                                 | [number]  |        |
| data>>records>>otherInAmount                | 其他收入                            | [number]  |        |
| data>>records>>giftWrapCredits              | 包装收入                            | [number]  |        |
| data>>records>>guaranteeClaims              | 买家交易保障索赔额                  | [number]  |        |
| data>>records>>costOfPoIntegersGranted      | 积分抵减收入                        | [number]  |        |
| data>>records>>fbaLiquidationProceeds       | 清算收入                            | [number]  |        |
| data>>records>>fbaLiquidationProceedsAdjustments | 清算调整                      | [number]  |        |
| data>>records>>amazonShippingReimbursement  | 亚马逊运费赔偿                      | [number]  |        |
| data>>records>>safeTReimbursement           | Safe-T索赔                          | [number]  |        |
| data>>records>>netcoTransaction             | Netco交易                           | [number]  |        |
| data>>records>>reimbursements               | 赔偿收入                            | [number]  |        |
| data>>records>>clawbacks                    | 追索收入                            | [number]  |        |
| data>>records>>sharedComminglingVatIncome   | 混合VAT收入                         | [number] |        |
| data>>records>>others                       | 其他                                | [number]  |        |
| data>>records>>totalSalesRefunds            | 收入退款额                          | [number]  |        |
| data>>records>>fbaSalesRefunds              | FBA销售退款额                       | [number]  |        |
| data>>records>>fbmSalesRefunds              | FBM销售退款额                       | [number]  |        |
| data>>records>>shippingCreditRefunds        | 买家运费退款额                      | [number]  |        |
| data>>records>>giftWrapCreditRefunds        | 买家包装退款额                      | [number]  |        |
| data>>records>>chargebacks                  | 卖家拒付                            | [number]  |        |
| data>>records>>costOfPoIntegersReturned     | 积分抵减退回                        | [number]  |        |
| data>>records>>promotionalRebateRefunds     | 促销折扣退款额                      | [number]  |        |
| data>>records>>totalFeeRefunds              | 费用退款额                          | [number]  |        |
| data>>records>>sellingFeeRefunds            | 平台费退款额                        | [number]  |        |
| data>>records>>fbaTransactionFeeRefunds     | 发货费退款额                        | [number]  |        |
| data>>records>>refundAdministrationFees     | 交易费用退款额                      | [number]  |        |
| data>>records>>otherTransactionFeeRefunds   | 其他订单费退款额                    | [number]  |        |
| data>>records>>refundForAdvertiser          | 广告退款额                          | [number]  |        |
| data>>records>>pointsAdjusted               | 积分费用                            | [number]  |        |
| data>>records>>shippingLabelRefunds         | 运输标签费退款                      | [number]  |        |
| data>>records>>refundsQuantity              | 退款量                              | [int]   |        |
| data>>records>>refundsRate                  | 退款率                              | [number]  |        |
| data>>records>>fbaReturnsQuantity           | 退货量                              | [int]  |        |
| data>>records>>fbaReturnsSaleableQuantity   | 退货量（可售）                       | [int]  |        |
| data>>records>>fbaReturnsUnsaleableQuantity | 退货量（不可售）                     | [int]  |        |
| data>>records>>platformFee                  | 平台费                              | [number]  |        |
| data>>records>>fbaDeliveryFee               | FBA发货费                           | [number]  |        |
| data>>records>>otherTransactionFees         | 其他订单费用                        | [number]  |        |
| data>>records>>totalAdsCost                 | 广告费                              | [number]  |        |
| data>>records>>adsSpCost                    | SP广告费                            | [number]  |        |
| data>>records>>adsSbCost                    | SB广告费                            | [number]  |        |
| data>>records>>adsSbvCost                   | SBV广告费                           | [number]  |        |
| data>>records>>adsSdCost                    | SD广告费                            | [number]  |        |
| data>>records>>sharedCostOfAdvertising      | 差异分摊                            | [number]  |        |
| data>>records>>sharedAdsAlCost             | Live广告    | [number]                             |        |
| data>>records>>sharedAdsCcCost	          | 创作者计划     | [number]                            |        |
| data>>records>>sharedAdsSspaotCost	      | TV广告      | [number]                           |        |
| data>>records>>sharedAdsSarCost	          | 零售商赞助广告   | [number]                              |        |
| data>>records>>promotionFee                 | 推广费                              | [number]  |        |
| data>>records>>sharedSubscriptionFee        | 订阅费                              | [number]  |        |
| data>>records>>sharedLdFee                  | 秒杀费                              | [number]  |        |
| data>>records>>sharedCouponFee              | 优惠券                              | [number]  |        |
| data>>records>>sharedEarlyReviewerProgramFee | 早期评论人计划                      | [number]  |        |
| data>>records>>sharedVineFee                | vine                                | [number]  |        |
| data>>records>>totalStorageFee              | FBA仓储费                           | [number]  |        |
| data>>records>>fbaStorageFee                | 月度仓库费                          | [number]  |        |
| data>>records>>sharedFbaStorageFee          | 月度仓储费差异                      | [number]  |        |
| data>>records>>longTermStorageFee           | 长期仓储费                          | [number]  |        |
| data>>records>>sharedLongTermStorageFee     | 长期仓储费差异                      | [number]  |        |
| data>>records>>sharedStorageRenewalBilling  | 库存续订费用                        | [number]  |        |
| data>>records>>sharedFbaDisposalFee         | FBA销毁费                           | [number]  |        |
| data>>records>>sharedFbaRemovalFee          | FBA移除费                           | [number]  |        |
| data>>records>>sharedFbaInboundTransportationProgramFee | 入仓手续费              | [number]  |        |
| data>>records>>sharedLabelingFee            | 标签费                              | [number]  |        |
| data>>records>>sharedPolybaggingFee         | 塑料包装费                          | [number]  |        |
| data>>records>>sharedBubblewrapFee          | 泡沫包装费                          | [number]  |        |
| data>>records>>sharedTapingFee              | 胶带费                              | [number]  |        |
| data>>records>>sharedFbaCustomerReturnFee   | FBA卖家退回费                       | [number]  |        |
| data>>records>>sharedFbaInboundDefectFee    | FBA仓储费入库缺陷费                        | [number]  |        |
| data>>records>>sharedFbaOverageFee          | 超量仓储费                          | [number]  |        |
| data>>records>>sharedAmazonPartneredCarrierShipmentFee | 合作承运费               | [number]  |        |
| data>>records>>sharedFbaInboundConvenienceFee | 入库配置费                              | [number]  |        |
| data>>records>>sharedItemFeeAdjustment      | 库存调整费用                        | [number]  |        |
| data>>records>>sharedOtherFbaInventoryFees  | 其他仓储费                          | [number]  |        |
| data>>records>>sharedFbaIntegerernationalInboundFee | FBA国际物流货运费             | [number]  |        |
| data>>records>>adjustments                  | 调整费用                            | [number]  |        |
| data>>records>>totalPlatformOtherFee        | 平台其他费                          | [number]  |        |
| data>>records>>shippingLabelPurchases       | 运输标签费                          | [number]  |        |
| data>>records>>sharedChargesToCreditCard    | 信用卡扣款                          | [number]  |        |
| data>>records>>sharedCarrierShippingLabelAdjustments | 承运人装运标签调整费          | [number]  |        |
| data>>records>>sharedLiquidationsFees       | 清算费                              | [number]  |        |
| data>>records>>sharedManualProcessingFee    | 人工处理费用                        | [number]  |        |
| data>>records>>sharedOtherServiceFees       | 其他服务费                          | [number]  |        |
| data>>records>>totalSalesTax                | 销售税                              | [number]  |        |
| data>>records>>taxCollected                 | VAT/GST                             | [number]  |        |
| data>>records>>tcsIgstCollected             | TCS-IGST                            | [number]  |        |
| data>>records>>tcsSgstCollected             | TCS-SGST                            | [number]  |        |
| data>>records>>tcsCgstCollected             | TCS-CGST                            | [number]  |        |
| data>>records>>sharedComminglingVatExpenses | 混合VAT                             | [number]  |        |
| data>>records>>sharedTaxAdjustment          | 销售税调整                   	       | [number] |        |
| data>>records>>salesTaxRefund               | 销售税退款额                        | [number]  |        |
| data>>records>>taxRefunded                  | VAT/GST                             | [number]  |        |
| data>>records>>tcsIgstRefunded              | TCS-IGST                            | [number]  |        |
| data>>records>>tcsSgstRefunded              | TCS-SGST                            | [number]  |        |
| data>>records>>tcsCgstRefunded              | TCS-CGST                            | [number]  |        |
| data>>records>>salesTaxWithheld             | 市场税                              | [number]  |        |
| data>>records>>refundTaxWithheld            | 市场税退款额                        | [number]  |        |
| data>>records>>tdsSection194ONet            | 混合网路费用                        | [number]  |        |
| data>>records>>customOrderFee               | 订单其他费                         | [number] |        |
| data>>records>>customOrderFeePrincipal      | 站外推广费-本金                    | [number] |        |
| data>>records>>customOrderFeeCommission     | 站外推广费-佣金                    | [number] |        |
| data>>records>>estimateFeeStr               | 预估费用                  	     | [array] |         |
| data>>records>>estimateFeeStr>>id           | 费用id                      	     | [string] |         |
| data>>records>>estimateFeeStr>>name         | 费用名称                      	 | [string] |         |
| data>>records>>estimateFeeStr>>amount       | 费用金额                      	 | [number] |         |
| data>>records>>cgPrice                      | 采购成本                            | [number]  |        |
| data>>records>>hasCgPriceDetail             | 是否有采购成本明细                  | [int]   |        |
| data>>records>>cgUnitPrice                  | 采购单价                            | [number]  |        |
| data>>records>>proportionOfCg               | 采购占比                            | [number]  |        |
| data>>records>>cgTransportCosts             | 头程运费                            | [number]  |        |
| data>>records>>hasCgTransportCostsDetail    | 是否有物流（头程）成本明细          | [int]   |        |
| data>>records>>firstTripUnitPrice           | 头程单价                            | [number]  |        |
| data>>records>>proportionOfCgTransport      | 头程占比                            | [number]  |        |
| data>>records>>cgOtherCostsTotal            | 其他成本                            | [number]  |        |
| data>>records>>cgOtherUnitCosts             | 其他单价                            | [number]  |        |
| data>>records>>hasCgOtherCostsDetail        | 是否有其他成本明细                  | [int]   |        |
| data>>records>>proportionOfCgOtherCosts     | 其他成本占比                        | [number]  |        |
| data>>records>>totalCost                    | 合计成本                            | [number]  |        |
| data>>records>>proportionOfTotalCost        | 合计成本占比                        | [number]  |        |
| data>>records>>grossProfit                  | 毛利润                              | [number]  |        |
| data>>records>>grossProfitWithTax           | 含税毛利润                     | [number]  |        |
| data>>records>>grossRate                    | 毛利率                              | [number]  |        |
| data>>records>>grossRateWithTax             | 含税毛利率                        | [number]  |        |
| data>>records>>taxCollectedGiftWrap         | 销售税-礼品包装税                  | [number] |        |
| data>>records>>taxCollectedShipping         | 销售税-买家运费税                  | [number] |        |
| data>>records>>taxCollectedDiscount         | 销售税-促销折扣税                  | [number] |        |
| data>>records>>taxCollectedProduct          | 销售税-商品价格税                  | [number] |        |
| data>>records>>taxRefundedGiftWrap          | 销售税退款-礼品包装税               | [number] |        |
| data>>records>>taxRefundedShipping          | 销售税退款-买家运费税               | [number] |        |
| data>>records>>taxRefundedDiscount          | 销售税退款-促销折扣税               | [number] |        |
| data>>records>>taxRefundedProduct           | 销售税退款-商品价格税               | [number] |   &nbsp;  |


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
                "id": "52536",
                "dataDate": "2023-07-18",
                "isDisplayDetail": false,
                "smallImageUrl": "https://xxx/xxx.jpg",
                "parentAsin": "B07DFKF9SG",
                "asin": "B07DFKF9SG",
                "sid": [
                    "104"
                ],
                "storeName": [
                    "A1MQMW3JWPNCBX-US"
                ],
                "sids": null,
                "asins": "B07DFKF9SG",
                "country": [
                    "美国"
                ],
                "countryCode": [
                    "US"
                ],
                "localName": "123测试",
                "localSku": "23",
                "itemName": "Xenstar Swim Goggles",
                "principalRealname": "xxx",
                "listingTagIds": "907224269891252258,907215400818094343",
                "categoryName": null,
                "brandName": null,
                "currencyCode": "USD  ",
                "currencyIcon": "$     ",
                "totalSalesQuantity": 0,
                "fbaSalesQuantity": 0,
                "fbmSalesQuantity": 0,
                "totalReshipQuantity": 1,
                "reshipFbmProductSalesQuantity": 0,
                "reshipFbmProductSaleRefundsQuantity": 1,
                "reshipFbaProductSalesQuantity": 0,
                "reshipFbaProductSaleRefundsQuantity": 0,
                "mcFbaFulfillmentFeesQuantity": 0,
                "totalAdsSales": 0.00,
                "adsSdSales": 0.00,
                "adsSpSales": 0.00,
                "totalAdsSalesQuantity": 0,
                "adsSdSalesQuantity": 0,
                "adsSpSalesQuantity": 0,
                "totalSalesAmount": 0.00,
                "fbaSaleAmount": 0.00,
                "fbmSaleAmount": 0.00,
                "totalSalesAmountWithTax": 0.00,
                "shippingCredits": 0.00,
                "promotionalRebates": 0.00,
                "fbaInventoryCredit": 0.00,
                "cashOnDelivery": 0.00,
                "otherInAmount": 0.00,
                "giftWrapCredits": 0.00,
                "guaranteeClaims": 0.00,
                "costOfPoIntegersGranted": 0.00,
                "fbaLiquidationProceeds": 0.00,
                "fbaLiquidationProceedsAdjustments": 0.00,
                "amazonShippingReimbursement": 0.00,
                "safeTReimbursement": 0.00,
                "netcoTransaction": 0.00,
                "reimbursements": 0.00,
                "clawbacks": 0.00,
                "sharedComminglingVatIncome": 0.00,
                "others": 0.00,
                "totalSalesRefunds": -0.01,
                "fbaSalesRefunds": 0.00,
                "fbmSalesRefunds": -0.01,
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
                "refundsQuantity": 1,
                "refundsRate": 0.0000,
                "fbaReturnsQuantity": 0,
                "fbaReturnsSaleableQuantity": 0,
                "fbaReturnsUnsaleableQuantity": 0,
                "platformFee": 0.00,
                "fbaDeliveryFee": 0.00,
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
                "sharedFbaIntegerernationalInboundFee": 0.00,
                "adjustments": 0.00,
                "totalPlatformOtherFee": 0.00,
                "shippingLabelPurchases": 0.00,
                "sharedChargesToCreditCard": null,
                "sharedCarrierShippingLabelAdjustments": 0.00,
                "sharedLiquidationsFees": 0.00,
                "sharedManualProcessingFee": 0.00,
                "sharedOtherServiceFees": 0.00,
                "totalSalesTax": 0.00,
                "taxCollected": 0.00,
                "tcsIgstCollected": 0.00,
                "tcsSgstCollected": 0.00,
                "tcsCgstCollected": 0.00,
                "sharedComminglingVatExpenses": 0.00,
                "sharedTaxAdjustment": 0.00,
                "salesTaxRefund": -0.11,
                "taxRefunded": -0.11,
                "tcsIgstRefunded": 0.00,
                "tcsSgstRefunded": 0.00,
                "tcsCgstRefunded": 0.00,
                "salesTaxWithheld": 0.00,
                "refundTaxWithheld": 0.11,
                "tdsSection194ONet": 0.00,
                "customOrderFee": 0.00,
                "customOrderFeePrincipal": null,
                "customOrderFeeCommission": null,
                "estimateFeeStr": null,
                "cgPrice": 0.00,
                "hasCgPriceDetail": 0,
                "cgUnitPrice": 0.00,
                "proportionOfCg": 0.0000,
                "cgTransportCosts": 0.00,
                "hasCgTransportCostsDetail": 0,
                "firstTripUnitPrice": 0.00,
                "proportionOfCgTransport": 0.0000,
                "cgOtherCostsTotal": 0.00,
                "cgOtherUnitCosts": 0.00,
                "hasCgOtherCostsDetail": 0,
                "proportionOfCgOtherCosts": 0.0000,
                "totalCost": 0.00,
                "proportionOfTotalCost": 0.0000,
                "grossProfit": -0.01,
                "grossProfitWithTax": -0.01,
                "grossRate": 0.0000,
                "grossRateWithTax": 0.0909,
                "taxCollectedGiftWrap": 0.00,
                "taxCollectedShipping": 0.00,
                "taxCollectedDiscount": 0.00,
                "taxCollectedProduct": 0.00,
                "taxRefundedGiftWrap": 0.00,
                "taxRefundedShipping": 0.00,
                "taxRefundedDiscount": 0.00,
                "taxRefundedProduct": 0.00
            }
        ],
        "total": 1
    }
}
```