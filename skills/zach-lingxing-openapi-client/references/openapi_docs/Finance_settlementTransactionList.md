# 查询结算中心 - 交易明细

支持查询亚马逊结算中心内的交易明细

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/settlement/transaction/detail/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量|否|[int]|0|
|length|分页长度，上限10000|否|[int]|20|
|countryCodes|站点id|否|[array]|[1]|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[136]|
|startDate|开始时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d<br>【无搜索值时，结算时间、修改时间二选一必填】|否|[string]|2023-09-24|
|endDate|结束时间【结算时间】，双闭区间，查询时间间隔不得超过7天，格式：Y-m-d<br>【无搜索值时，结算时间、修改时间二选一必填】|否|[string]|2023-09-30|
|eventType|来源，多个英文用逗号隔开，枚举见附加说明|否|[string]|ShipmentEventList|
|type|交易类型|否|[string]|Tax|
|searchField|搜索字段：<br>id 结算编号<br>amazon_order_id 订单编号<br>primary_id 主键编号【对应本接口返回id值】<br>settlement_id 账单编号【此项下，结算时间或更新时间必填】|否|[string]|id|
|searchValue|搜索值|否|[array]|["LWCBG07Y55I3"]|
|gmtModifiedStart|修改开始时间（北京时间），格式：Y-m-d H:i:s<br>【无搜索值时，结算时间、修改时间二选一必填】|否|[string]|2022-10-26 15:15:12|
|gmtModifiedEnd|修改结束时间（北京时间），格式：Y-m-d H:i:s<br>【无搜索值时，结算时间、修改时间二选一必填】|否|[string]|2022-10-26 16:15:12|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "countryCodes": [
        1
    ],
    "sids": [
        136
    ],
    "startDate": "2023-09-24",
    "endDate": "2023-09-30",
    "eventType": "ShipmentEventList",
    "type": "Tax"，
    "searchField": "id",
    "searchValue": [
        "LWCBG07Y55I3"
    ],
    "gmtModifiedStart": "2022-10-26 15:15:12",
    "gmtModifiedEnd": "2022-10-26 16:15:12"
}
```

## 返回结果

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|msg|返回信息|是|[string]||
|data|响应数据|是|[array]||
|data>>records||是|[array]||
|data>>records>>uniqueKey|交易明细唯一标识<br>备注：eventType=servicefeeeventlist时，uniqueKey会变动|是|[string]||
|data>>records>>amazonOrderId|订单号|是|[string]||
|data>>records>>sid|店铺id|是|[int]||
|data>>records>>storeName|店铺名|是|[string]||
|data>>records>>sellerId|亚马逊店铺id|是|[string]||
|data>>records>>countryCode|国家|是|[string]||
|data>>records>>accountType|报告类型|是|[string]||
|data>>records>>fulfillment|配送方式|是|[string]||
|data>>records>>eventType|来源<br>备注：eventType=servicefeeeventlist时，uniqueKey会变动|是|[string]||
|data>>records>>sellerSku|MSKU|是|[string]||
|data>>records>>type|交易类型|是|[string]||
|data>>records>>postedDateLocale|结算时间（站点时间）|是|[string]||
|data>>records>>currencyCode|币种|是|[string]||
|data>>records>>currencyAmount|金额|是|[number]||
|data>>records>>quantity|数量|是|[int]||
|data>>records>>processingStatus|结算状态：<br>Open 未结算<br>Closed 已结算<br>Reconciled 已对账|是|[string]||
|data>>records>>fundTransferStatus|转账状态：<br>Succeeded 已转账<br>Processing 转账中<br>Failed 失败<br>Unknown 未知|是|[string]||
|data>>records>>fid|结算编号|是|[string]||
|data>>records>>settlementId|settlement_id|是|[string]||
|data>>records>>localSku|sku|是|[string]||
|data>>records>>localName|品名|是|[string]||
|data>>records>>id|主键编号【非唯一键】|是|[string]||
|data>>records>>gmtModified|修改时间|是|[string]||
|data>>records>>sellerOrderId|卖方为订单定义的标识符|是|[string]||
|data>>records>>marketplaceName|市场名称|是|[string]||
|data>>records>>postedDate|结算日期|否|[string]|2024-06-06T08:29:00Z |
|data>>records>>financialEventGroupId|groupID|否|[string]|2bc77df899a347861b669e3b |
|data>>records>>fnsku|FNSKU|否|[string]|X00000STB1 |
|data>>records>>orderItemId|订单项ID|否|[string]|40667527236852 |
|data>>records>>merchantOrderId|商家订单ID|否|[string]|100119933999 |
|data>>records>>md5|MD5|否|[string]|4fe4d6bb8d6b2b728f97acd9b11de94f |
|data>>records>>companyId|公司ID|否|[long]|1039287 |
|data>>records>>gmtCreate|创建时间|否|[string]|2024-06-05 11:22:33 |
|data>>records>>level1|层级1|否|[string]|一级分类 |
|data>>records>>asin|ASIN|否|[string]|B00EXAMPLE |
|data>>records>>level2|层级2|否|[string]|二级分类 |
|data>>records>>promotionId|促销ID|否|[string]|PRM202406 |
|data>>records>>dealId|交易ID|否|[string]|DEAL12345 |
|data>>records>>feeType|费用类型|否|[string]|ShippingFee |
|data>>records>>dealDescription|交易描述|否|[string]|订单退款 |
|data>>records>>invoiceId|发票ID|否|[string]|INV202406 |
|data>>records>>transactionType|交易类型|否|[string]|Refund |
|data>>records>>feeDescription|费用描述|否|[string]|运费 |
|data>>records>>feeReason|费用原因|否|[string]|活动促销 |
|data>>records>>couponId|优惠券ID|否|[string]|QP123456 |
|data>>records>>sellerCouponDescription|卖家优惠券描述|否|[string]|满减优惠券 |
|data>>records>>clipOrRedemptionCount|剪辑或兑换计数|否|[int]|2 |
|data>>records>>paymentEventId|支付事件ID|否|[string]|PMT67890 |
|data>>records>>enrollmentId|注册ID|否|[string]|ENR202406 |
|data>>records>>parentAsin|父ASIN|否|[string]|B00PARENT123 |
|data>>records>>debtRecoveryType|债务恢复类型|否|[string]|DebtRecoveryTypeA |
|data>>records>>groupBeginDate|组开始日期|否|[string]|2024-06-01 |
|data>>records>>groupEndDate|组结束日期|否|[string]|2024-06-07 |
|data>>records>>orderId|订单ID|否|[string]|ORDER202406 |
|data>>records>>removalShipmentItemId|移除货件项ID|否|[string]|RS12345 |
|data>>records>>taxCollectionModel|税收模型|否|[string]|MarketplaceFacilitator |
|data>>records>>taxWithholdingPeriodStartDate|预扣税期间开始日期|否|[string]|2024-06-01 |
|data>>records>>taxWithholdingPeriodEndDate|预扣税期间结束日期|否|[string]|2024-06-05 |
|data>>records>>netCoTransactionId|净CO交易ID|否|[string]|NCOTID123 |
|data>>records>>swapReason|交换原因|否|[string]|换货 |
|data>>records>>marketplaceId|市场ID|否|[string]|A1F83G8C2ARO7P |
|data>>records>>adjustmentEventId|调整事件ID|否|[string]|ADJ7890 |
|data>>records>>safeTClaimId|SafeT索赔ID|否|[string]|STC202406 |
|data>>records>>reasonCode|原因代码|否|[string]|REASON123 |
|data>>records>>productDescription|产品描述|否|[string]|产品描述信息 |
|data>>records>>sourceBusinessEventType|源业务事件类型|否|[string]|EVENT_TYPE_A |
|data>>records>>businessObjectType|业务对象类型|否|[string]|Order |
|data>>records>>amountDescription|金额描述|否|[string]|实收金额 |
|data>>records>>level1Index|层级1索引|否|[int]|1 |
|data>>records>>level2Index|层级2索引|否|[int]|2 |
|data>>total|总数|是|[int]|1335|

## 返回成功示例

```
{
    "code": 0,
    "msg": null,
    "data": {
        "records": [
            {
                "uniqueKey": "",
                "amazonOrderId": "202-6458758-1434760",
                "sid": 8,
                "storeName": "JHL-Official-02",
                "countryCode": "UK",
                "accountType": "Standard",
                "fulfillment": "FBA",
                "eventType": "Shipment",
                "sellerId": "xxxxxxxxxxxxxxxx",
                "sellerSku": "1160U1139-A",
                "type": "Commission",
                "postedDateLocale": "2022-09-10T23:55:12+01:00",
                "currencyCode": "GBP",
                "currencyAmount": "-1.93",
                "quantity": 1,
                "processingStatus": "Closed",
                "fundTransferStatus": "Succeeded",
                "fid": "QA0DOY5ODNF8",
                "settlementId": "",
                "localSku": "",
                "localName": "",
                "id": "18327152",
                "gmtModified": "2022-09-11 07:06:37.401",
                "sellerOrderId": "",
                "marketplaceName": "Amazon.com",
                "postedDate": "2024-06-06T08:29:00Z",
                "financialEventGroupId": "2bc77df899a347861b669e3b",
                "fnsku": "X00000STB1",
                "orderItemId": "40667527236852",
                "merchantOrderId": "100119933999",
                "md5": "4fe4d6bb8d6b2b728f97acd9b11de94f",
                "companyId": 1039287,
                "gmtCreate": "",
                "level1": "一级分类",
                "asin": "B00EXAMPLE",
                "level2": "二级分类",
                "promotionId": "PRM202406",
                "dealId": "DEAL12345",
                "feeType": "ShippingFee",
                "dealDescription": "订单退款",
                "invoiceId": "INV202406",
                "transactionType": "Refund",
                "feeDescription": "运费",
                "feeReason": "活动促销",
                "couponId": "QP123456",
                "sellerCouponDescription": "满减优惠券",
                "clipOrRedemptionCount": 2,
                "paymentEventId": "PMT67890",
                "enrollmentId": "ENR202406",
                "parentAsin": "B00PARENT123",
                "debtRecoveryType": "DebtRecoveryTypeA",
                "groupBeginDate": "2024-06-01",
                "groupEndDate": "2024-06-07",
                "orderId": "ORDER202406",
                "removalShipmentItemId": "RS12345",
                "taxCollectionModel": "MarketplaceFacilitator",
                "taxWithholdingPeriodStartDate": "2024-06-01",
                "taxWithholdingPeriodEndDate": "2024-06-05",
                "netCoTransactionId": "NCOTID123",
                "swapReason": "换货",
                "marketplaceId": "A1F83G8C2ARO7P",
                "adjustmentEventId": "ADJ7890",
                "safeTClaimId": "STC202406",
                "reasonCode": "REASON123",
                "productDescription": "产品描述信息",
                "sourceBusinessEventType": "EVENT_TYPE_A",
                "businessObjectType": "Order",
                "amountDescription": "实收金额",
                "level1Index": 1,
                "level2Index": 2
            }
        ],
        "total": 1335
    }
}
```
## 附加说明
1. eventType=servicefeeeventlist时，uniqueKey会变动<br>建议拉取数据时，针对eventTpye=servicefeeeventlist类型的数据，把这个类型的数据作单独的删除与写入操作。
2. 当账单处于closed状态时uniqueKey不会变化。

eventType字段枚举

| 来源 | 传值    |  
| :------------ |:------|
| Shipment                | ShipmentEventList                     |
| Refund                  | RefundEventList                       |
| GuranteeClaim           | GuranteeClaimEventList                |
| Chargeback              | ChargebackEventList                   |
| PayWithAmazon           | PayWithAmazonEventList                |
| ServiceProviderCredit   | ServiceProviderCreditEventList        |
| Retrocharge             | RetrochargeEventList                  |
| RentalTransaction       | RentalTransactionEventList            |
| ProductAdsPayment       | ProductAdsPaymentEventList            |
| ServiceFee              | ServiceFeeEventList                   |
| SellerDealPayment       | SellerDealPaymentEventList            |
| DebtRecovery            | DebtRecoveryEventList                 |
| LoanServicing           | LoanServicingEventList                |
| Adjustment              | AdjustmentEventList                   |
| SAFETReimbursement      | SAFETReimbursementEventList           |
| SellerReviewEnrollment  | SellerReviewEnrollmentEventList       |
| FBALiquidation          | FBALiquidationEventList               |
| CouponPayment           | CouponPaymentEventList                |
| ImagingServicesFee      | ImagingServicesFeeEventList           |
| NetworkComminglingTransaction | NetworkComminglingTransactionEventList |
| AffordabilityExpense    | AffordabilityExpenseEventList         |
| AffordabilityExpenseReversal | AffordabilityExpenseReversalEventList |
| RemovalShipment         | RemovalShipmentEventList              |