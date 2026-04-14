# 账单明细-ShopeeIncome

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/shopee/income/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| compareLogic | 字段比较条件逻辑关系：<br>`AND` 所有条件都满足<br>`OR` 满足任一条件<br>默认 `AND` | 否 | [string] | AND |
| currencyCode | 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算） | 否 | [string] | USD |
| endDate | 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期 | 否 | [string] | 2026-03-17 |
| envKey | 环境标识 | 否 | [string] | prod |
| expandChildren | 是否展开子项（商品明细），默认 `true` 展开树形结构 | 否 | [boolean] | true |
| exportFields | 导出字段值 | 否 | [array] | ["orderSn","amount"] |
| fieldCompares | 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定） | 否 | [array] | [{"field":"amount","operator":"gte","value":100}] |
| length | 分页大小，默认 `20`，最大不超过 `200` | 是 | [number] | 20 |
| offset | 分页偏移，默认 `0` | 是 | [number] | 0 |
| platformCode | 平台码 | 否 | [string] | shopee |
| searchExactly | 是否精确匹配 | 否 | [boolean] | false |
| searchExactly1 | 商品搜索是否精确匹配 | 否 | [boolean] | false |
| searchMultiValue | 多个搜索值（精确匹配） | 否 | [array] | ["230001","230002"] |
| searchMultiValue1 | 商品搜索值（多个，精确匹配） | 否 | [array] | ["MSKU001","MSKU002"] |
| searchSingleValue | 单个搜索值（支持模糊匹配，多个值用逗号分隔） | 否 | [string] | ORDER001,ORDER002 |
| searchSingleValue1 | 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔） | 否 | [string] | MSKU001,MSKU002 |
| searchType | 搜索类型：<br>`1` 平台单号 | 否 | [number] | 1 |
| searchType1 | 商品搜索类型：<br>`11` MSKU ID<br>`12` MSKU<br>`13` MSKU 名称<br>`14` 商品ID<br>`15` 全球商品货号<br>`16` 商品名称 | 否 | [number] | 12 |
| sids | 店铺 ID 数组 | 否 | [array] | [10001,10002] |
| sites | 站点数组 | 否 | [array] | ["SG","MY"] |
| sortField | 排序字段 | 否 | [string] | payoutTime |
| sortType | 排序方向：<br>`1` 升序/ASC<br>`0` 降序/DESC<br>默认 `0` | 否 | [string] | 0 |
| startDate | 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天 | 否 | [string] | 2026-03-01 |
| storeTypes | 店铺类型数组：<br>`1` 跨境店(CB)<br>`2` 本土店(Local) | 否 | [array] | [1,2] |


## 请求cURL示例

```bash
curl --location 'https://openapi.lingxing.com/basicOpen/finance/shopee/income/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "compareLogic": "AND",
    "currencyCode": "USD",
    "startDate": "2026-03-01",
    "endDate": "2026-03-17",
    "expandChildren": true,
    "length": 20,
    "offset": 0,
    "searchType": 1,
    "searchSingleValue": "ORDER20260317001",
    "searchType1": 12,
    "searchSingleValue1": "MSKU001",
    "sites": ["SG","MY"],
    "sids": [10001,10002],
    "storeTypes": [1,2]
}'
```

## 返回结果

JSON Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 状态码，0：成功 | 是 | [number] | 0 |
| message | 消息提示 | 是 | [string] | success |
| error_details | 数据校验失败时的错误详情 | 是 | [array] | [] |
| request_id | 请求链路id | 是 | [string] | ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035 |
| response_time | 响应时间 | 是 | [string] | 2025-10-23 00:47:29 |
| data | 响应数据 | 是 | [object] |  |
| data>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>totalSum | 汇总数据 | 是 | [object] |  |
| data>>totalSum>>actualCommissionFee | 实际佣金汇总 | 是 | [string] | 32.10 |
| data>>totalSum>>actualInstallationFee | 实际安装费汇总 | 是 | [string] | 5.20 |
| data>>totalSum>>actualServiceFee | 实际服务费汇总 | 是 | [string] | 18.60 |
| data>>totalSum>>actualShippingFee | 实际运费汇总 | 是 | [string] | -12.80 |
| data>>totalSum>>adsEscrowTopUpFeeOrTechnicalSupportFee | 技术支持费汇总 | 是 | [string] | 3.20 |
| data>>totalSum>>amount | 结算金额汇总 | 是 | [string] | 1250.50 |
| data>>totalSum>>amsCommissionFee | 联盟营销佣金汇总 | 是 | [string] | 6.50 |
| data>>totalSum>>buyerActualCashRefund | 退款给买家的现金金额汇总 | 是 | [string] | 12.00 |
| data>>totalSum>>buyerPaidPackagingFee | 买家支付包装费汇总 | 是 | [string] | 1.60 |
| data>>totalSum>>buyerPaidShippingFee | 买家支付运费汇总 | 是 | [string] | 20.50 |
| data>>totalSum>>buyerTotalAmount | 买家支付总金额汇总 | 是 | [string] | 1450.00 |
| data>>totalSum>>campaignFee | 活动费汇总 | 是 | [string] | 8.30 |
| data>>totalSum>>commissionFee | 佣金汇总 | 是 | [string] | 30.20 |
| data>>totalSum>>currency | 币种代码 | 是 | [string] | USD |
| data>>totalSum>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>totalSum>>deliverySellerProtectionFeePremiumAmount | 保险费汇总 | 是 | [string] | 0.80 |
| data>>totalSum>>discountedCostOfGoodsSold | 商品折后金额总额汇总 | 是 | [string] | 850.60 |
| data>>totalSum>>discountedItemPrice | 商品折后金额汇总 | 是 | [string] | 850.60 |
| data>>totalSum>>escrowImportTax | 进口税汇总 | 是 | [string] | 1.20 |
| data>>totalSum>>escrowTax | 跨境税汇总 | 是 | [string] | 2.10 |
| data>>totalSum>>fbsFee | FBS费汇总 | 是 | [string] | 3.40 |
| data>>totalSum>>finalEscrowProductGst | GST商品税汇总 | 是 | [string] | 1.10 |
| data>>totalSum>>finalEscrowShippingGst | GST运费税汇总 | 是 | [string] | 0.60 |
| data>>totalSum>>finalProductVatTax | VAT商品税汇总 | 是 | [string] | 1.50 |
| data>>totalSum>>finalReturnToSellerShippingFee | 退货给卖家运费汇总 | 是 | [string] | 2.40 |
| data>>totalSum>>finalShippingVatTax | VAT运费税汇总 | 是 | [string] | 0.70 |
| data>>totalSum>>installationFeePaidByBuyer | 买家支付安装费汇总 | 是 | [string] | 0.30 |
| data>>totalSum>>itemDiscount | 商品折扣额汇总 | 是 | [string] | 22.40 |
| data>>totalSum>>itemDiscountTotal | 商品折扣总额汇总 | 是 | [string] | 22.40 |
| data>>totalSum>>orderChargeableWeight | 订单计费重量汇总 | 是 | [string] | 12.50 |
| data>>totalSum>>otherFee | 其他费用汇总 | 是 | [string] | 3.20 |
| data>>totalSum>>otherOrderFee | 其他订单费汇总 | 是 | [string] | 1.20 |
| data>>totalSum>>overseasReturnServiceFee | 海外免退服务费汇总 | 是 | [string] | 1.00 |
| data>>totalSum>>proratedCoinsValueOffsetReturnItems | 退款/退货商品的按比例Shopee币抵消汇总 | 是 | [string] | 0.50 |
| data>>totalSum>>proratedPaymentChannelPromoBankOffsetReturnItems | 退货退款商品的按比例银行支付渠道优惠汇总 | 是 | [string] | 0.80 |
| data>>totalSum>>proratedPaymentChannelPromoShopeeOffsetReturnItems | 退货退款商品的按比例Shopee支付渠道优惠汇总 | 是 | [string] | 0.90 |
| data>>totalSum>>proratedSellerVoucherOffsetReturnItems | 退货退款商品的按比例卖家优惠券抵消汇总 | 是 | [string] | 1.10 |
| data>>totalSum>>proratedShopeeVoucherOffsetReturnItems | 退货商品的按比例Shopee优惠券抵消汇总 | 是 | [string] | 0.70 |
| data>>totalSum>>quantity | 销售数量汇总 | 是 | [number] | 5 |
| data>>totalSum>>refundAmount | 商品小计退款金额汇总 | 是 | [string] | 20.00 |
| data>>totalSum>>reverseShippingFee | 退货运费汇总 | 是 | [string] | 2.50 |
| data>>totalSum>>reverseShippingFeeSst | 退货运费SST汇总 | 是 | [string] | 0.10 |
| data>>totalSum>>rsfSellerProtectionFeeClaimAmount | 运费节省计划汇总 | 是 | [string] | 0.60 |
| data>>totalSum>>salesTaxOnLvg | LVG销售税汇总 | 是 | [string] | 0.20 |
| data>>totalSum>>sellerCoinCashBack | 卖家Shopee币回扣汇总 | 是 | [string] | 1.30 |
| data>>totalSum>>sellerLostCompensation | 损失赔偿汇总 | 是 | [string] | 0.40 |
| data>>totalSum>>sellerOrderProcessingFee | 订单处理费汇总 | 是 | [string] | 2.60 |
| data>>totalSum>>sellerProductRebateCommissionFeeOffset | 佣金抵扣金额汇总 | 是 | [string] | 0.90 |
| data>>totalSum>>sellerProductRebateServiceFeeOffset | 服务费抵扣金额汇总 | 是 | [string] | 0.50 |
| data>>totalSum>>sellerShippingDiscount | 卖家运费促销汇总 | 是 | [string] | 1.70 |
| data>>totalSum>>sellerTransactionFee | 交易手续费汇总 | 是 | [string] | 5.00 |
| data>>totalSum>>sellerVoucherCode | 优惠码 | 是 | [string] | SELLER-20260317 |
| data>>totalSum>>serviceFee | 服务费原始值汇总 | 是 | [string] | 19.80 |
| data>>totalSum>>shippingFeeDiscountFrom3pl | 3PL运费折扣汇总 | 是 | [string] | 0.40 |
| data>>totalSum>>shippingFeeSst | 运费SST汇总 | 是 | [string] | 0.20 |
| data>>totalSum>>shippingSellerProtectionFeeAmount | 运费节省计划费用汇总 | 是 | [string] | 0.50 |
| data>>totalSum>>shopeeDiscount | Shopee回扣金额汇总 | 是 | [string] | 4.10 |
| data>>totalSum>>shopeeShippingRebate | Shopee运费补贴汇总 | 是 | [string] | 2.30 |
| data>>totalSum>>thImportDuty | 泰国进口税汇总 | 是 | [string] | 0.10 |
| data>>totalSum>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>totalSum>>totalIncomeTax | 所得税总和汇总 | 是 | [string] | 1.80 |
| data>>totalSum>>totalOriginalItemPrice | 商品原价汇总 | 是 | [string] | 900.00 |
| data>>totalSum>>totalTariff | 关税总和汇总 | 是 | [string] | 0.30 |
| data>>totalSum>>totalVatTax | 增值税总和汇总 | 是 | [string] | 1.90 |
| data>>totalSum>>tradeInBonusBySeller | 以旧换新补贴汇总 | 是 | [string] | 0.50 |
| data>>totalSum>>vatOnImportedGoods | 进口增值税汇总 | 是 | [string] | 0.20 |
| data>>totalSum>>voucherFromSeller | 卖家优惠券汇总 | 是 | [string] | 6.30 |
| data>>totalSum>>withholdingPitTax | PIT汇总 | 是 | [string] | 0.40 |
| data>>totalSum>>withholdingTax | 收入预提税汇总 | 是 | [string] | 0.60 |
| data>>totalSum>>withholdingVatTax | 增值税预提汇总 | 是 | [string] | 0.30 |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>actualCommissionFee | 实际佣金 | 是 | [string] | 16.10 |
| data>>list>>actualInstallationFee | 实际安装费 | 是 | [string] | 2.60 |
| data>>list>>actualServiceFee | 实际服务费 | 是 | [string] | 9.30 |
| data>>list>>actualShippingFee | 实际运费（取反） | 是 | [string] | -6.40 |
| data>>list>>adsEscrowTopUpFeeOrTechnicalSupportFee | 技术支持费 | 是 | [string] | 1.60 |
| data>>list>>amount | 结算金额 | 是 | [string] | 625.25 |
| data>>list>>amsCommissionFee | 联盟营销佣金 | 是 | [string] | 3.25 |
| data>>list>>buyerActualCashRefund | 退款给买家的现金金额 | 是 | [string] | 6.00 |
| data>>list>>buyerPaidPackagingFee | 买家支付包装费 | 是 | [string] | 0.80 |
| data>>list>>buyerPaidShippingFee | 买家支付运费 | 是 | [string] | 10.25 |
| data>>list>>buyerPaymentMethod | 买家支付方式 | 是 | [string] | Credit Card |
| data>>list>>buyerTotalAmount | 买家支付总金额 | 是 | [string] | 725.00 |
| data>>list>>buyerUserName | 买家账号 | 是 | [string] | buyer_demo |
| data>>list>>campaignFee | 活动费 | 是 | [string] | 4.15 |
| data>>list>>children | 子项列表（商品明细） | 是 | [array] |  |
| data>>list>>commissionFee | 佣金原始值 | 是 | [string] | 15.10 |
| data>>list>>currency | 币种 | 是 | [string] | USD |
| data>>list>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>list>>dataType | 数据类型：`1` 订单汇总，`2` 商品明细 | 是 | [number] | 1 |
| data>>list>>deliverySellerProtectionFeePremiumAmount | 保险费 | 是 | [string] | 0.40 |
| data>>list>>discountedCostOfGoodsSold | 商品小计-商品金额（折扣后） | 是 | [string] | 425.30 |
| data>>list>>encryptedPayoutId | 账期加密ID（仅CB有） | 是 | [number] | 1234567890 |
| data>>list>>escrowImportTax | 进口税 | 是 | [string] | 0.60 |
| data>>list>>escrowTax | 跨境税 | 是 | [string] | 1.05 |
| data>>list>>fbsFee | FBS费 | 是 | [string] | 1.70 |
| data>>list>>finalEscrowProductGst | GST商品税 | 是 | [string] | 0.55 |
| data>>list>>finalEscrowShippingGst | GST运费税 | 是 | [string] | 0.30 |
| data>>list>>finalProductVatTax | VAT商品税 | 是 | [string] | 0.75 |
| data>>list>>finalReturnToSellerShippingFee | 退货给卖家运费 | 是 | [string] | 1.20 |
| data>>list>>finalShippingVatTax | VAT运费税 | 是 | [string] | 0.35 |
| data>>list>>hasChildren | 是否有子项 | 是 | [boolean] | true |
| data>>list>>id | 主键ID | 是 | [number] | 1001 |
| data>>list>>installationFeePaidByBuyer | 买家支付安装费 | 是 | [string] | 0.15 |
| data>>list>>instalmentPlan | 分期计划 | 是 | [string] | 3期免息 |
| data>>list>>itemDiscount | 商品折扣额 | 是 | [string] | 11.20 |
| data>>list>>itemDiscountTotal | 商品折扣总额 | 是 | [string] | 11.20 |
| data>>list>>orderChargeableWeight | 订单计费重量 | 是 | [string] | 6.25 |
| data>>list>>orderSn | 平台订单号 | 是 | [string] | ORDER20260317001 |
| data>>list>>originalItemPrice | 商品原价（商品维度） | 是 | [string] | 450.00 |
| data>>list>>originalPayoutTime | 原始结算时间戳 | 是 | [number] | 1742198400 |
| data>>list>>otherFee | 其他费用 | 是 | [string] | 1.60 |
| data>>list>>otherOrderFee | 其他订单费 | 是 | [string] | 0.60 |
| data>>list>>overseasReturnServiceFee | 海外免退服务费 | 是 | [string] | 0.50 |
| data>>list>>payoutSn | 账期ID | 是 | [string] | P20260317001 |
| data>>list>>payoutTime | 结算时间 | 是 | [string] | 2026-03-17 12:00:00 |
| data>>list>>platformCode | 平台码 | 是 | [string] | shopee |
| data>>list>>proratedCoinsValueOffsetReturnItems | 退款/退货商品的按比例Shopee币抵消 | 是 | [string] | 0.25 |
| data>>list>>proratedPaymentChannelPromoBankOffsetReturnItems | 退货退款商品的按比例银行支付渠道优惠 | 是 | [string] | 0.40 |
| data>>list>>proratedPaymentChannelPromoShopeeOffsetReturnItems | 退货退款商品的按比例Shopee支付渠道优惠 | 是 | [string] | 0.45 |
| data>>list>>proratedSellerVoucherOffsetReturnItems | 退货退款商品的按比例卖家优惠券抵消 | 是 | [string] | 0.55 |
| data>>list>>proratedShopeeVoucherOffsetReturnItems | 退货商品的按比例Shopee优惠券抵消 | 是 | [string] | 0.35 |
| data>>list>>refundAmount | 商品小计-退款金额 | 是 | [string] | 10.00 |
| data>>list>>reverseShippingFee | 退货运费 | 是 | [string] | 1.25 |
| data>>list>>reverseShippingFeeSst | 退货运费SST | 是 | [string] | 0.05 |
| data>>list>>rsfSellerProtectionFeeClaimAmount | 运费节省计划 | 是 | [string] | 0.30 |
| data>>list>>salesTaxOnLvg | LVG销售税 | 是 | [string] | 0.10 |
| data>>list>>sellerCoinCashBack | 卖家Shopee币回扣 | 是 | [string] | 0.65 |
| data>>list>>sellerLostCompensation | 损失赔偿 | 是 | [string] | 0.20 |
| data>>list>>sellerOrderProcessingFee | 订单处理费 | 是 | [string] | 1.30 |
| data>>list>>sellerProductRebateCommissionFeeOffset | 佣金抵扣金额 | 是 | [string] | 0.45 |
| data>>list>>sellerProductRebateServiceFeeOffset | 服务费抵扣金额 | 是 | [string] | 0.25 |
| data>>list>>sellerShippingDiscount | 卖家运费促销 | 是 | [string] | 0.85 |
| data>>list>>sellerTransactionFee | 交易手续费 | 是 | [string] | 2.50 |
| data>>list>>sellerVoucherCode | 优惠码 | 是 | [string] | SELLER-20260317 |
| data>>list>>serviceFee | 服务费原始值 | 是 | [string] | 9.90 |
| data>>list>>shippingFeeDiscountFrom3pl | 3PL运费折扣 | 是 | [string] | 0.20 |
| data>>list>>shippingFeeSst | 运费SST | 是 | [string] | 0.10 |
| data>>list>>shippingSellerProtectionFeeAmount | 运费节省计划费用 | 是 | [string] | 0.25 |
| data>>list>>shopeeDiscount | Shopee回扣金额 | 是 | [string] | 2.05 |
| data>>list>>shopeeShippingRebate | Shopee运费补贴 | 是 | [string] | 1.15 |
| data>>list>>site | 站点代码 | 是 | [string] | SG |
| data>>list>>siteDisplay | 站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>storeId | 店铺ID | 是 | [number] | 10001 |
| data>>list>>storeName | 店铺名 | 是 | [string] | Shopee-SG |
| data>>list>>storeType | 店铺类型：1-跨境店, 2-本土店 | 是 | [number] | 1 |
| data>>list>>storeTypeDisplay | 店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>thImportDuty | 泰国进口税 | 是 | [string] | 0.05 |
| data>>list>>totalIncomeTax | 所得税总和 | 是 | [string] | 0.90 |
| data>>list>>totalOriginalItemPrice | 商品小计-商品原价 | 是 | [string] | 450.00 |
| data>>list>>totalTariff | 关税总和 | 是 | [string] | 0.15 |
| data>>list>>totalVatTax | 增值税总和 | 是 | [string] | 0.95 |
| data>>list>>tradeInBonusBySeller | 以旧换新补贴 | 是 | [string] | 0.25 |
| data>>list>>transactionId | 交易ID（仅Local有） | 是 | [string] | TXN20260317001 |
| data>>list>>transactionType | 交易类型（仅Local有） | 是 | [string] | SALE |
| data>>list>>uniqueNo | 业务唯一键 | 是 | [string] | SHOPEE-INCOME-001 |
| data>>list>>vatOnImportedGoods | 进口增值税 | 是 | [string] | 0.10 |
| data>>list>>voucherFromSeller | 卖家优惠券 | 是 | [string] | 3.15 |
| data>>list>>withholdingPitTax | PIT | 是 | [string] | 0.20 |
| data>>list>>withholdingTax | 收入预提税 | 是 | [string] | 0.30 |
| data>>list>>withholdingVatTax | 增值税预提 | 是 | [string] | 0.15 |
| data>>list>>children>>actualCommissionFee | 子项-实际佣金 | 是 | [string] | 8.00 |
| data>>list>>children>>actualInstallationFee | 子项-实际安装费 | 是 | [string] | 1.20 |
| data>>list>>children>>actualServiceFee | 子项-实际服务费 | 是 | [string] | 4.30 |
| data>>list>>children>>actualShippingFee | 子项-实际运费（取反） | 是 | [string] | -3.10 |
| data>>list>>children>>adsEscrowTopUpFeeOrTechnicalSupportFee | 子项-技术支持费 | 是 | [string] | 0.80 |
| data>>list>>children>>amount | 子项-结算金额 | 是 | [string] | 320.10 |
| data>>list>>children>>amsCommissionFee | 子项-联盟营销佣金 | 是 | [string] | 1.80 |
| data>>list>>children>>buyerActualCashRefund | 子项-退款给买家的现金金额 | 是 | [string] | 2.50 |
| data>>list>>children>>buyerPaidPackagingFee | 子项-买家支付包装费 | 是 | [string] | 0.30 |
| data>>list>>children>>buyerPaidShippingFee | 子项-买家支付运费 | 是 | [string] | 4.50 |
| data>>list>>children>>buyerTotalAmount | 子项-买家支付总金额 | 是 | [string] | 360.00 |
| data>>list>>children>>campaignFee | 子项-活动费 | 是 | [string] | 2.10 |
| data>>list>>children>>commissionFee | 子项-佣金原始值 | 是 | [string] | 7.80 |
| data>>list>>children>>companyId | 子项-公司 ID | 是 | [number] | 1234567890 |
| data>>list>>children>>currency | 子项-币种 | 是 | [string] | USD |
| data>>list>>children>>currencyIcon | 子项-币种图标 | 是 | [string] | $ |
| data>>list>>children>>dataType | 子项-数据类型：`2` 商品明细 | 是 | [number] | 2 |
| data>>list>>children>>deliverySellerProtectionFeePremiumAmount | 子项-保险费 | 是 | [string] | 0.20 |
| data>>list>>children>>discountedCostOfGoodsSold | 子项-商品金额（折扣后） | 是 | [string] | 210.50 |
| data>>list>>children>>encryptedPayoutId | 子项-账期加密ID | 是 | [number] | 1234567890 |
| data>>list>>children>>escrowImportTax | 子项-进口税 | 是 | [string] | 0.30 |
| data>>list>>children>>escrowTax | 子项-跨境税 | 是 | [string] | 0.55 |
| data>>list>>children>>fbsFee | 子项-FBS费 | 是 | [string] | 0.90 |
| data>>list>>children>>finalEscrowProductGst | 子项-GST商品税 | 是 | [string] | 0.20 |
| data>>list>>children>>finalEscrowShippingGst | 子项-GST运费税 | 是 | [string] | 0.10 |
| data>>list>>children>>finalProductVatTax | 子项-VAT商品税 | 是 | [string] | 0.30 |
| data>>list>>children>>finalReturnToSellerShippingFee | 子项-退货给卖家运费 | 是 | [string] | 0.60 |
| data>>list>>children>>finalShippingVatTax | 子项-VAT运费税 | 是 | [string] | 0.15 |
| data>>list>>children>>globalItemSku | 子项-全球商品货号 | 是 | [string] | GLOBAL-SKU-001 |
| data>>list>>children>>id | 子项-主键ID | 是 | [number] | 2001 |
| data>>list>>children>>installationFeePaidByBuyer | 子项-买家支付安装费 | 是 | [string] | 0.05 |
| data>>list>>children>>instalmentPlan | 子项-分期计划 | 是 | [string] | 3期免息 |
| data>>list>>children>>itemDiscount | 子项-商品折扣额 | 是 | [string] | 5.60 |
| data>>list>>children>>itemDiscountTotal | 子项-商品折扣总额 | 是 | [string] | 5.60 |
| data>>list>>children>>itemId | 子项-商品ID | 是 | [number] | 3001001 |
| data>>list>>children>>itemName | 子项-商品名称 | 是 | [string] | Wireless Mouse |
| data>>list>>children>>itemNumber | 子项-商品序号 | 是 | [number] | 1 |
| data>>list>>children>>modelId | 子项-Model ID | 是 | [number] | 50001 |
| data>>list>>children>>modelName | 子项-Model名称 | 是 | [string] | Black |
| data>>list>>children>>modelSku | 子项-Model SKU | 是 | [string] | MODEL-SKU-001 |
| data>>list>>children>>msku | 子项-MSKU | 是 | [string] | MSKU001 |
| data>>list>>children>>mskuId | 子项-MSKU ID | 是 | [number] | 80001 |
| data>>list>>children>>mskuName | 子项-MSKU名称 | 是 | [string] | 无线鼠标-黑色 |
| data>>list>>children>>orderSn | 子项-平台订单号 | 是 | [string] | ORDER20260317001 |
| data>>list>>children>>originalItemPrice | 子项-商品原价 | 是 | [string] | 225.00 |
| data>>list>>children>>originalPayoutTime | 子项-原始结算时间戳 | 是 | [number] | 1742198400 |
| data>>list>>children>>otherFee | 子项-其他费用 | 是 | [string] | 0.80 |
| data>>list>>children>>otherOrderFee | 子项-其他订单费 | 是 | [string] | 0.30 |
| data>>list>>children>>overseasReturnServiceFee | 子项-海外免退服务费 | 是 | [string] | 0.20 |
| data>>list>>children>>parentId | 子项-父行ID | 是 | [number] | 1001 |
| data>>list>>children>>payoutSn | 子项-账期ID | 是 | [string] | P20260317001 |
| data>>list>>children>>payoutTime | 子项-结算时间 | 是 | [string] | 2026-03-17 12:00:00 |
| data>>list>>children>>platformCode | 子项-平台码 | 是 | [string] | shopee |
| data>>list>>children>>proratedCoinsValueOffsetReturnItems | 子项-按比例Shopee币抵消 | 是 | [string] | 0.10 |
| data>>list>>children>>proratedPaymentChannelPromoBankOffsetReturnItems | 子项-按比例银行支付渠道优惠 | 是 | [string] | 0.15 |
| data>>list>>children>>proratedPaymentChannelPromoShopeeOffsetReturnItems | 子项-按比例Shopee支付渠道优惠 | 是 | [string] | 0.18 |
| data>>list>>children>>proratedSellerVoucherOffsetReturnItems | 子项-按比例卖家优惠券抵消 | 是 | [string] | 0.20 |
| data>>list>>children>>proratedShopeeVoucherOffsetReturnItems | 子项-按比例Shopee优惠券抵消 | 是 | [string] | 0.12 |
| data>>list>>children>>quantity | 子项-商品销售数量 | 是 | [number] | 2 |
| data>>list>>children>>refundAmount | 子项-退款金额 | 是 | [string] | 4.00 |
| data>>list>>children>>reverseShippingFee | 子项-退货运费 | 是 | [string] | 0.60 |
| data>>list>>children>>reverseShippingFeeSst | 子项-退货运费SST | 是 | [string] | 0.02 |
| data>>list>>children>>rsfSellerProtectionFeeClaimAmount | 子项-运费节省计划 | 是 | [string] | 0.15 |
| data>>list>>children>>salesTaxOnLvg | 子项-LVG销售税 | 是 | [string] | 0.05 |
| data>>list>>children>>sellerCoinCashBack | 子项-卖家Shopee币回扣 | 是 | [string] | 0.30 |
| data>>list>>children>>sellerLostCompensation | 子项-损失赔偿 | 是 | [string] | 0.10 |
| data>>list>>children>>sellerOrderProcessingFee | 子项-订单处理费 | 是 | [string] | 0.60 |
| data>>list>>children>>sellerProductRebateCommissionFeeOffset | 子项-佣金抵扣金额 | 是 | [string] | 0.20 |
| data>>list>>children>>sellerProductRebateServiceFeeOffset | 子项-服务费抵扣金额 | 是 | [string] | 0.10 |
| data>>list>>children>>sellerShippingDiscount | 子项-卖家运费促销 | 是 | [string] | 0.40 |
| data>>list>>children>>sellerTransactionFee | 子项-交易手续费 | 是 | [string] | 1.20 |
| data>>list>>children>>sellerVoucherCode | 子项-优惠码 | 是 | [string] | SELLER-20260317 |
| data>>list>>children>>serviceFee | 子项-服务费原始值 | 是 | [string] | 4.50 |
| data>>list>>children>>shippingFeeDiscountFrom3pl | 子项-3PL运费折扣 | 是 | [string] | 0.10 |
| data>>list>>children>>shippingFeeSst | 子项-运费SST | 是 | [string] | 0.05 |
| data>>list>>children>>shippingSellerProtectionFeeAmount | 子项-运费节省计划费用 | 是 | [string] | 0.10 |
| data>>list>>children>>shopeeDiscount | 子项-Shopee回扣金额 | 是 | [string] | 1.00 |
| data>>list>>children>>shopeeShippingRebate | 子项-Shopee运费补贴 | 是 | [string] | 0.50 |
| data>>list>>children>>site | 子项-站点代码 | 是 | [string] | SG |
| data>>list>>children>>siteDisplay | 子项-站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>children>>storeId | 子项-店铺ID | 是 | [number] | 10001 |
| data>>list>>children>>storeName | 子项-店铺名 | 是 | [string] | Shopee-SG |
| data>>list>>children>>storeType | 子项-店铺类型 | 是 | [number] | 1 |
| data>>list>>children>>storeTypeDisplay | 子项-店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>children>>thImportDuty | 子项-泰国进口税 | 是 | [string] | 0.03 |
| data>>list>>children>>totalIncomeTax | 子项-所得税总和 | 是 | [string] | 0.40 |
| data>>list>>children>>totalOriginalItemPrice | 子项-商品原价 | 是 | [string] | 225.00 |
| data>>list>>children>>totalTariff | 子项-关税总和 | 是 | [string] | 0.06 |
| data>>list>>children>>totalVatTax | 子项-增值税总和 | 是 | [string] | 0.45 |
| data>>list>>children>>tradeInBonusBySeller | 子项-以旧换新补贴 | 是 | [string] | 0.10 |
| data>>list>>children>>transactionId | 子项-交易ID | 是 | [string] | TXN20260317001 |
| data>>list>>children>>transactionType | 子项-交易类型 | 是 | [string] | SALE |
| data>>list>>children>>uniqueNo | 子项-业务唯一键 | 是 | [string] | SHOPEE-INCOME-001-1 |
| data>>list>>children>>vatOnImportedGoods | 子项-进口增值税 | 是 | [string] | 0.05 |
| data>>list>>children>>voucherFromSeller | 子项-卖家优惠券 | 是 | [string] | 1.60 |
| data>>list>>children>>withholdingPitTax | 子项-PIT | 是 | [string] | 0.10 |
| data>>list>>children>>withholdingTax | 子项-收入预提税 | 是 | [string] | 0.15 |
| data>>list>>children>>withholdingVatTax | 子项-增值税预提 | 是 | [string] | 0.07 |

## 返回成功示例

```json
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035",
    "response_time": "2025-10-23 00:47:29",
    "data": {
        "totalCount": 2,
        "totalSum": {
            "amount": "1250.50",
            "currency": "USD",
            "currencyIcon": "$",
            "sellerVoucherCode": "SELLER-20260317",
            "quantity": 5,
            "totalCount": 2
        },
        "list": [
            {
                "uniqueNo": "SHOPEE-INCOME-001",
                "hasChildren": true,
                "orderSn": "ORDER20260317001",
                "storeName": "Shopee-SG",
                "site": "SG",
                "siteDisplay": "新加坡",
                "storeId": 10001,
                "storeType": 1,
                "storeTypeDisplay": "跨境店",
                "payoutSn": "P20260317001",
                "encryptedPayoutId": 1234567890,
                "payoutTime": "2026-03-17 12:00:00",
                "instalmentPlan": "3期免息",
                "transactionId": "TXN20260317001",
                "transactionType": "SALE",
                "amount": "625.25",
                "currency": "USD",
                "currencyIcon": "$",
                "sellerVoucherCode": "SELLER-20260317",
                "children": [
                    {
                        "uniqueNo": "SHOPEE-INCOME-001-1",
                        "parentId": 1001,
                        "itemNumber": 1,
                        "itemId": 3001001,
                        "itemName": "Wireless Mouse",
                        "modelId": 50001,
                        "modelName": "Black",
                        "modelSku": "MODEL-SKU-001",
                        "mskuId": 80001,
                        "msku": "MSKU001",
                        "mskuName": "无线鼠标-黑色",
                        "globalItemSku": "GLOBAL-SKU-001",
                        "quantity": 2,
                        "amount": "320.10",
                        "sellerVoucherCode": "SELLER-20260317"
                    }
                ]
            }
        ]
    }
}
```
