# 查询利润报表 - 订单维度transaction视图
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/profitReport/order/transcation/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限1000|否|[int]|20|
|mids|站点id|否|[array]|[1,2]|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[124,123]|
|searchDateField|时间筛选类型:<br>posted_date_locale 结算时间【默认】<br>fund_transfer_datetime_locale 转账时间<br>shipment_datetime_locale 发货时间<br>order_datetime_locale 下单时间<br>accounting_time 入账时间|否|[string]|posted_date_locale|
|startDate|开始时间|是|[string]|2024-09-01|
|endDate|结束时间|是|[string]|2024-09-03|
|gmtModifiedStartDate|修改开始时间，格式：yyyy-MM-dd HH:mm:ss|否|[string]|2024-09-01 12:00:00|
|gmtModifiedEndDate|修改结束时间，格式：yyyy-MM-dd HH:mm:ss|否|[string]|2024-09-01 14:00:00|
|currencyCode|货币种类:<br>原币种【默认】<br>CNY<br>USD<br>EUR<br>JPY<br>AUD<br>CAD<br>MXN<br>GBP<br>INR<br>AED<br>SGD<br>SAR<br>BRL<br>SEK<br>PLN<br>TRY<br>HKD|否|[string]|USD|
|searchField|查询索引字段:<br>order_id 订单号【默认】<br>seller_sku MSKU<br>asin ASIN<br>parent_asin 父ASIN<br>local_sku SKU<br>local_name 品名<p style="color: red;">gmt_modified 修改时间【不再建议使用】</p>settlement_id Settlement ID<br>description 描述<br>fid 结算编号|否|[string]|order_id|
|searchValue|查询索引字段值|否|[array]|["xxxx"]|
|sortField|参与排序字段|否|[string]|postedDatetimeLocale|
|sortType|排序方式|否|[string]|desc|
|settlementStatus|结算状态<br>Open 待结算<br>Pending 结算中<br>Closed 已结算<br>Reconciled 已对账|否|[array]|["Closed"]|
|fundTransferStatus|转账状态:<br>Succeeded 已转账<br>Processing 转帐中<br>Failed 失败<br>Unknown 未知|否|[array]|["Succeeded"]|
|accountType|账单类型:<br>Standard<br>Invoiced<br>Electronic<br>COD<br>PayWithAmazon|否|[array]|["Standard"]|
|eventSource|费用类型:<br>Transfer<br>Adjustment<br>Debt<br>Refund<br>FBA Inventory Fee<br>Service Fee<br>Order|否|[array]|["Service Fee"]|
|fulfillment|订单类型:<br>FBA FBA<br>FBM FBM|否|[array]|["FBA"]|
|principalUids|listing负责人|否|[array]|[10616076]|
|productDeveloperUids|开发负责人|否|[array]|[1]|
|orderStatus|交易状态<br/>Deferred 已推迟（结束时间必须要今天才能获取已推迟数据）<br/>Disbursed 已发放【默认】<br/>DisbursedAndPreSettled 已发放（含`预结`算）<br/>All 全部|否|[string]|"Disbursed"|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "mids": [1,2],
    "sids": [124,123],
    "startDate": "2022-12-31",
    "endDate": "2023-03-01",
    "currencyCode": "USD",
    "searchField": "order_id",
    "searchValue": ["xxxx"],
    "sortField": "postedDatetimeLocale",
    "sortType": "desc",
    "settlementStatus": ["Closed"],
    "fundTransferStatus": ["Succeeded"],
    "searchDateField": "posted_date_locale",
    "accountType": ["Standard"],
    "eventSource": ["Service Fee"],
    "fulfillment": ["FBA"],
    "principalUids": [106160],
    "productDeveloperUids": [1],
    "gmtModifiedStartDate": "2024-09-01 12:00:00",
    "gmtModifiedEndDate": "2024-09-01 14:00:00",
    "orderStatus": "Deferred",
    "transactionStatus": [
        "Disbursed",
        "PreSettlement"
    ]
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|错误详情|是|[array]| |
|request_id|请求链路id|是|[string]|6f66d7b3602a4bb48563dc2eedace8e0.236.17255404176056375|
|response_time|响应时间|是|[string]|2024-09-05 20:46:58|
|data| |是|[object]| |
|data>>records| |是|[array]| |
|data>>records>>id|id|是|[string]|38959929246716175543322278226548439778262302539968746850187907781625596404240|
|data>>records>>sid|店铺id|是|[string]|6|
|data>>records>>transactionId|transactionId|是|[string]|22dd24b86a464cf2a7541252dc462587.1760926323389|
|data>>records>>storeName|店铺|是|[string]|篮球|
|data>>records>>country|国家|是|[string]|美国|
|data>>records>>countryCode|国家编码|是|[string]|US|
|data>>records>>postedDatetimeLocale|结算时间|是|[string]|2023-02-24 23:02:52|
|data>>records>>settlementStatus|结算状态|是|[string]|Closed|
|data>>records>>orderId|订单号|是|[string]| |
|data>>records>>fulfillment|订单类型|是|[string]| |
|data>>records>>orderDatetimeLocale|下单时间|是|[string]| |
|data>>records>>paymentDatetimeLocale|付款时间|是|[string]| |
|data>>records>>shipmentDatetimeLocale|发货时间|是|[string]| |
|data>>records>>fundTransferDatetimeLocale|转账时间|是|[string]|2023-03-03 15:31:52|
|data>>records>>fundTransferStatus|转账状态|是|[string]|Unknown|
|data>>records>>gmtModified|修改时间|是|[string]|2023-03-03 15:31:52|
|data>>records>>accountType|账单类型|是|[string]|Standard|
|data>>records>>eventSource|费用类型|是|[string]|Service Fee|
|data>>records>>settlementId|Settlement ID|是|[string]|17449132851|
|data>>records>>fid|结算编号|是|[string]|8RC4KL1HB615|
|data>>records>>smallImageUrl|图片|是|[string]| |
|data>>records>>msku|MSKU|是|[string]| |
|data>>records>>fnsku|FNSKU|是|[string]| |
|data>>records>>asin|ASIN|是|[string]| |
|data>>records>>parentAsin|父ASIN|是|[string]| |
|data>>records>>localName|品名|是|[string]| |
|data>>records>>localSku|SKU|是|[string]| |
|data>>records>>description|描述|是|[string]|Subscription|
|data>>records>>quantity|数量|是|[number]|0|
|data>>records>>principalRealname|Listing负责人|是|[string]| |
|data>>records>>productDeveloperRealname|开发负责人|是|[string]| |
|data>>records>>currencyCode|币种|是|[string]|USD|
|data>>records>>currencyIcon|币种符号|是|[string]|$|
|data>>records>>productSales|销售额|是|[number]|0|
|data>>records>>productSalesTax|销售税|是|[number]|0|
|data>>records>>shippingCredits|买家运费|是|[number]|0|
|data>>records>>shippingCreditsTax|买家运费税|是|[number]|0|
|data>>records>>giftwrapCredits|礼品包装|是|[number]|0|
|data>>records>>giftwrapCreditsTax|礼品包装税|是|[number]|0|
|data>>records>>amazonPointFee|积分|是|[number]|0|
|data>>records>>promotionalRebates|促销折扣|是|[number]|0|
|data>>records>>promotionalRebatesTax|促销折扣费|是|[number]|0|
|data>>records>>salesTaxCollected|代扣代缴增值税|是|[number]|0|
|data>>records>>lowValueGoods|低价值商品税|是|[number]|0|
|data>>records>>marketplaceWithheldTax|市场预扣税|是|[number]|0|
|data>>records>>tcsCgst|TCS_CGST|是|[number]|0|
|data>>records>>tcsSgst|TCS_SGST|是|[number]|0|
|data>>records>>tcsIgst|TCS_IGST|是|[number]|0|
|data>>records>>sellingFees|平台费|是|[number]|0|
|data>>records>>fbaFees|FBA费|是|[number]|0|
|data>>records>>otherTransactionFees|其他交易费|是|[number]|0|
|data>>records>>other|其他|是|[number]|-39.99|
|data>>records>>hiddenTax|隐藏税|是|[number]|0|
|data>>records>>settlementTotal|亚马逊结算小计|是|[number]|-39.99|
|data>>records>>purchaseCostsTotal|采购成本|是|[number]|0|
|data>>records>>logisticsCostsTotal|头程成本|是|[number]|0|
|data>>records>>otherCostsTotal|其他成本|是|[number]|0|
|data>>records>>customOrderFeeTotal|站外推广费|是|[number]|0|
|data>>records>>settlementGrossProfit|结算订单毛利润|是|[number]|-39.99|
|data>>records>>settlementGrossProfitRate|结算订单毛利率|是|[number]|0|
|data>>records>>promotionId|促销编码|是|[string]| |
|data>>records>>transactionStatus|交易状态|是|[string]| |
|data>>records>>transactionStatusCode|交易状态码|是|[string]| |
|data>>records>>deferredSubStatus|已推迟订单状态：<br/>已推迟<br/>预结算<br/>当月结算<br/>估实差异<br/>入账冲销<br/>|是|[string]| |
|data>>records>>deferredSubStatusCode|已推迟订单状态码：<br/>Deferred<br/>PreSettlement<br/>RegularSettlement<br/>PreSettlementReversal<br/>deferredReversal<br/>Disbursed|是|[string]| |
|data>>records>>shipPromotionDiscount|配送促销折扣|是|[number]|9|
|data>>records>>itemPromotionDiscount|商品促销折扣|是|[number]|9|
|data>>records>>odsEventType|odsEventType|是|[string]|ServiceFeeEventList|
|data>>records>>rowIndex|rowIndex|是|[number]|9|
|data>>records>>accountingTime|入账时间|是|[string]|"2025-07-15 03:31:10"|
|data>>total|总数|是|[number]|9|
|total|总数|是|[number]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "f898c15c933b40639f2250f96d9755be.1741745537314",
    "response_time": "2025-03-12 10:12:18",
    "data": {
        "records": [
            {
                "id": "113221103598719651224501253105676405764357882259729528092821266977197534979600",
                "sid": "136",
                "transactionId": "22dd24b86a464cf2a7541252dc462587.1760926323389",
                "storeName": "韧啸-US",
                "country": "美国",
                "countryCode": "US",
                "postedDatetimeLocale": "2024-11-13 01:24:24",
                "settlementStatus": "Closed",
                "orderId": "",
                "fulfillment": "",
                "orderDatetimeLocale": "",
                "paymentDatetimeLocale": "",
                "shipmentDatetimeLocale": "",
                "fundTransferDatetimeLocale": "2024-11-18 23:29:21",
                "fundTransferStatus": "Unknown",
                "gmtModified": "2025-01-31 09:50:43",
                "accountType": "Standard",
                "eventSource": "FBA Inventory Fee",
                "settlementId": "21164053811",
                "fid": "QA0DQPFT4NVX",
                "smallImageUrl": null,
                "msku": "",
                "fnsku": "",
                "asin": "",
                "parentAsin": "",
                "localName": null,
                "localSku": null,
                "description": "FBA Inbound Transportation Fee",
                "quantity": 0,
                "principalRealname": null,
                "productDeveloperRealname": null,
                "currencyCode": "USD",
                "currencyIcon": "$",
                "productSales": 0.00,
                "productSalesTax": 0.00,
                "shippingCredits": 0.00,
                "shippingCreditsTax": 0.00,
                "giftwrapCredits": 0.00,
                "giftwrapCreditsTax": 0.00,
                "amazonPointFee": 0.00,
                "promotionalRebates": 0.00,
                "promotionalRebatesTax": 0.00,
                "salesTaxCollected": 0.00,
                "lowValueGoods": 0.00,
                "marketplaceWithheldTax": 0.00,
                "tcsCgst": 0.00,
                "tcsSgst": 0.00,
                "tcsIgst": 0.00,
                "sellingFees": 0.00,
                "fbaFees": 0.00,
                "otherTransactionFees": 0.00,
                "other": -7.64,
                "hiddenTax": 0.00,
                "settlementTotal": -7.64,
                "purchaseCostsTotal": 0.00,
                "logisticsCostsTotal": 0.00,
                "otherCostsTotal": 0.00,
                "customOrderFeeTotal": 0.00,
                "settlementGrossProfit": -7.64,
                "settlementGrossProfitRate": 0.0000,
                "promotionId": "",
                "transactionStatus": "已发放",
                "transactionStatusCode": "Disbursed",
                "shipPromotionDiscount": null,
                "itemPromotionDiscount": null,
                "odsEventType": "ServiceFeeEventList",
                "rowIndex": 0
            }
        ],
        "total": 1
    },
    "total": 0
}
```