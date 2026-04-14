# 查询利润报表-订单

本接口即将下线【不再建议使用】，建议使用[查询利润报表 - 订单维度transaction视图](/docs/Finance/profitReportOrderTranscationList)

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/order/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，上限10000|否|[int]|20|
|mids|站点id|否|[array]|[180]|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[136]|
|search_date_field|时间类型：<br>posted_date_locale 结算时间<br>fund_transfer_datetime_locale 转账时间<br>shipment_datetime_locale 发货时间|是|[string]|fund_transfer_datetime_locale|
|start_date|开始时间|是|[string]|2023-01-21|
|end_date|结束时间|是|[string]|2024-07-20|
|search_field|搜索值类型：<br>亚马逊订单号：order_id<br>MSKU：seller_sku<br>Asin：asin<br>父asin：parent_asin<br>SKU：local_sku<br>品名：local_name|否|[string]|order_id|
|search_value|搜索的值|否|[array]|[""]|
|currency_code|币种code|否|[string]|CNY|
|account_type|报告类型：<br>Standard<br>Invoiced<br>Electronic<br>COD<br>PayWithAmazon|否|[string]|Standard|
|settlement_status|结算状态：<br>待结算：["Open", "Pending"]<br>已结算：["Closed"]|否|[array]|["Closed"]|
|fund_transfer_status|转账状态：<br>已转帐 Succeeded<br>转帐中 Processing<br>失败 Failed<br>未知 Unknown|否|[array]|["Succeeded","Unknown"]|
|event_source|来源：<br>SellerDealPayment<br>ServiceFee<br>Adjustment<br>Refund<br>SellerReviewEnrollmentPayment<br>RemovalShipmentAdjustment<br>ProductAdsPayment<br>Shipment<br>DebtRecovery<br>Liquidations Adjustments<br>Retrocharge<br>RemovalShipment|否|[array]|["ServiceFee","DebtRecovery"]|
|description|描述|否|[array]|["Subscription","RecoveryAmount"]|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "sids": [
        136
    ],
    "search_date_field": "fund_transfer_datetime_locale",
    "start_date": "2023-01-21",
    "end_date": "2024-07-20",
    "search_field": "order_id",
    "search_value": [
        ""
    ],
    "currency_code": "CNY",
    "account_type": "Standard",
    "settlement_status": [
        "Closed"
    ],
    "fund_transfer_status": [
        "Succeeded",
        "Unknown"
    ],
    "event_source": [
        "ServiceFee",
        "DebtRecovery"
    ],
    "description": [
        "Subscription",
        "RecoveryAmount"
    ]
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|14316922-d968-49dc-af7f-ac3aa4e29d09.1682560729730|
|response_time|响应时间|是|[string]|2023-04-27 09:58:50|
|total|总数|是|[int]|11345|
|data|响应数据|是|[array]||
|data>>id|记录id【非唯一值】,[唯一键参考](docs/Finance/bdOrder?id=附加说明)|是|[string]|97860842859265346195179669414178955639632303349797920144362032035134467346451|
|data>>sid|店铺id|是|[int]|8|
|data>>store_name|店铺名|是|[string]|JHL Official-01|
|data>>country_code|国家编码|是|[string]|UK|
|data>>country|国家|是|[string]|英国|
|data>>fid|结算编号|是|[string]|ABC|
|data>>description|描述，返回该行对应描述的拼接字符串<br>【枚举见附加说明】|是|[string]|PaidServicesFee,PointsAdjusted|
|data>>msku|MSKU|是|[string]|JX-MPNS-QJZP|
|data>>asin|asin|是|[string]|B07H2PWQR2|
|data>>fulfillment|订单类型：FBA、FBM、''|是|[string]|FBA|
|data>>principal|销售额|是|[number]|0|
|data>>commission|平台费|是|[number]|0|
|data>>tax|销售税额|是|[number]|0|
|data>>other|平台收入中其他收入的其他费用|是|[number]|0|
|data>>posted_datetime_locale|结算时间|是|[string]|2023-03-02 05:05:29|
|data>>currency_code|选择转化后币种|是|[string]|CNY|
|data>>currency_icon|选择转化后对应的币符|是|[string]|￥|
|data>>order_id|订单号|是|[string]|AMPSBilling_48155952912_3_2023_01_01|
|data>>event_source|来源|是|[string]|ServiceFee|
|data>>account_type|报告类型|是|[string]|Standard|
|data>>parent_asin|父asin|是|[string]|B07H2PWQR2|
|data>>local_name|品名|是|[string]|local_name|
|data>>local_sku|sku|是|[string]|local_sku|
|data>>settlement_status|结算状态|是|[array]|["Closed"]|
|data>>fund_transfer_status|转账状态|是|[array]|["Succeeded"]|
|data>>fund_transfer_datetime_locale|转账时间|是|[string]|2023-03-02 05:05:29|
|data>>shipment_datetime_locale|发货时间|是|[string]|2023-03-02 05:05:29|
|data>>small_image_url|图片|是|[string]|https://www.amazon.com/dp/B07H2PWQR2|
|data>>cost_quantity|成本数量|是|[number]|0|
|data>>product_sales_quantity|订单数量|是|[number]|0|
|data>>shipping_charge|买家运费|是|[number]|0|
|data>>promotional_rebates|促销折扣|是|[number]|0|
|data>>shipping_chargeback|运费拒付|是|[number]|0|
|data>>gift_wrap|礼品包装|是|[number]|0|
|data>>giftwrap_chargeback|礼品包装拒付|是|[number]|0|
|data>>fba_per_unit_fulfillment_fee|FBA费|是|[number]|0|
|data>>refund_commission|交易费用退款额|是|[number]|0|
|data>>shipping_tax|运费税|是|[number]|0|
|data>>sales_tax_withheld|市场税|是|[number]|0|
|data>>marketplace_facilitator_vat_principal|市场税-销售额|是|[number]|0|
|data>>marketplace_facilitator_vat_shipping|市场税-买家运费|是|[number]|0|
|data>>giftWrap_tax|礼物包装税|是|[number]|0|
|data>>promotion_discount_tax|促销折扣税|是|[number]|0|
|data>>shipping_discount_tax|运费折扣税|是|[number]|0|
|data>>restocking_fee|补货费|是|[number]|0|
|data>>other_transaction_fees_total|其他交易费总计|是|[number]|-17483.7|
|data>>other_transaction_fees_detail|其他交易费明细,所有未识别的明细汇总|是|[string]|{"PaidServicesFee":-17483.70}|
|data>>settlement_total|亚马逊结算小结|是|[number]|-17483.7|
|data>>purchase_costs_total|采购成本|是|[number]|0|
|data>>logistics_costs_total|头程成本|是|[number]|0|
|data>>other_costs_total|其他成本|是|[number]|0|
|data>>gross_profit|毛利润|是|[number]|-17483.7|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "14316922-d968-49dc-af7f-ac3aa4e29d09.1682560729730",
    "response_time": "2023-04-27 09:58:50",
    "total": 11345,
    "data": [
        {
            "id": "4289099",
            "sid": "8",
            "country": "英国",
            "fid": "",
            "description": "PaidServicesFee",
            "msku": "",
            "asin": "",
            "fulfillment": "",
            "principal": 0.00,
            "commission": 0.00,
            "tax": 0.00,
            "other": 0.00,
            "store_name": "JHM Official-01",
            "country_code": "UK",
            "posted_datetime_locale": "2023-03-02 05:05:29",
            "currency_code": "CNY",
            "currency_icon": "￥",
            "order_id": "AMPSBilling_48155952912_1_2023_01_01",
            "event_source": "ServiceFee",
            "account_type": "Standard",
            "parent_asin": "",
            "local_name": "",
            "local_sku": "",
            "settlement_status": "",
            "fund_transfer_status": "",
            "fund_transfer_datetime_locale": "",
            "shipment_datetime_locale": "",
            "small_image_url": "",
            "cost_quantity": 0,
            "product_sales_quantity": 0,
            "shipping_charge": 0.00,
            "promotional_rebates": 0.00,
            "shipping_chargeback": 0.00,
            "gift_wrap": 0.00,
            "giftwrap_chargeback": 0.00,
            "fba_per_unit_fulfillment_fee": 0.00,
            "refund_commission": 0.00,
            "shipping_tax": 0.00,
            "sales_tax_withheld": 0.00,
            "marketplace_facilitator_vat_principal": 0.00,
            "marketplace_facilitator_vat_shipping": 0.00,
            "giftWrap_tax": 0.00,
            "promotion_discount_tax": 0.00,
            "shipping_discount_tax": 0.00,
            "restocking_fee": 0.00,
            "other_transaction_fees_total": -17483.70,
            "other_transaction_fees_detail": "{\"PaidServicesFee\":-17483.70}",
            "settlement_total": -17483.70,
            "purchase_costs_total": 0.00,
            "logistics_costs_total": 0.00,
            "other_costs_total": 0.00,
            "gross_profit": -17483.70
        }
    ]
}
```

## 附加说明

- description字段枚举值如下：  
PointsAdjusted、TaxWithheldAdjustment、Principal、Tax、FBAPerUnitFulfillmentFee、Commission、MarketplaceFacilitatorTax-Principal、ShippingCharge、ShippingTax、ShippingChargeback、MarketplaceFacilitatorVAT-Principal、MarketplaceFacilitatorVAT-Shipping、FBALongTermStorageFee、ReserveDebit、ShippingDiscount、PromotionDiscount、MarketplaceFacilitatorTax-Shipping、FBACustomerRetrunFee、RefundCommission、ReserveCredit、FREE_REPLACEMENT_REFUND_ITEMS、WAREHOUSE_DAMAGE、CouponRedemptionFee、FBADisposalFee、FeeAmount、Revenue、CostOfPointsGranted、ShippingDiscountTax、PaymentMethodFee、CODChargeback、PromotionDiscountTax、RestockingFee、baseValue、feeAmount、GiftWrap、GiftWrapTax、GiftwrapChargeback、MarketplaceFacilitatorTax-Other、REVERSAL_REIMBURSEMENT、COMPENSATED_CLAWBACK、Subscription、FBAStorageFee、TaxAmount、VineFee、BaseTax、WAREHOUSE_LOST、RecoveryAmount、CostOfPointsReturned、TaxWithheld、NonSubscriptionFeeAdj、MarketplaceFacilitatorTax-RestockingFee、REMOVAL_ORDER_LOST、RevenueAdjustment、TaxAmountAdjustment、CSBAFee、ShippingHB、Goodwill、MiscAdjustment、FBAInboundDefectFee、FBAOverageFee、FailedDisbursement、taxValue、ReviewEnrollmentFee、FBARemovalFee、CommissionCorrection、ReturnShipping、PostageRefund_Postage、LiquidationsBrokerageFee、PaidServicesFee、WAREHOUSE_LOST_MANUAL、INCORRECT_FEES_NON_ITEMIZED
- 唯一键：
sid + posted_datetime_locale + fid + order_id + event_source + seller_sku