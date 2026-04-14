# 查询亚马逊源报表-FBA订单
查询 Amazon-Fulfilled Shipments Report 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/fbaOrders` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|date_type|日期搜索维度：【默认1】<br>1 下单日期<br>2 配送日期|否|[int]|1|
|start_date|开始日期，左闭区间，Y-m-d格式|是|[string] |2020-04-01|
|end_date|结束日期，右开区间，Y-m-d格式|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "date_type": 1,
    "start_date": "2020-04-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码， 0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|69F77F67-F288-B0C8-F453-C653E4D0FA93|
|response_time|响应时间|是|[string]|2021-05-14 18:08:36|
|data|响应数据|是|[array]|  |
|data>>amazon_order_id|订单号|是|[string]|112-4166816-7798631|
|data>>shipment_id|配送ID|是|[string]|DHySD0zRY|
|data>>shipment_item_id|配送子ID|是|[string]|D6ddjDd1R|
|data>>amazon_order_item_id|订单子项ID|是|[string]|37909714721266|
|data>>purchase_date|下单日期|是|[string]|2018-11-04T23:57:08+00:00|
|data>>payments_date|支付日期|是|[string]|2018-11-05T08:06:34+00:00|
|data>>shipment_date|配送日期（零时区）|是|[string]|2018-11-05T08:06:37+00:00|
|data>>reporting_date|报表日期|是|[string]|2018-11-05T09:06:42+00:00|
|data>>estimated_arrival_date|预计送达日期|是|[string]|2018-11-07T04:00:00+00:00|
|data>>sku|SKU|是|[string]|NP-10US-24Y8|
|data>>product_name|品名|是|[string]|Bicycle Saddle Dual Suspension Shock Absorbing|
|data>>quantity_shipped|数量|是|[number]|1|
|data>>currency|币种|是|[string]|USD|
|data>>item_price|商品金额|是|[string]|17.92|
|data>>item_tax|商品税|是|[string]|0.00|
|data>>shipping_price|运费金额|是|[string]|0.00|
|data>>shipping_tax|运费税|是|[string]|0.00|
|data>>gift_wrap_price|礼品包装费|是|[string]|0.00|
|data>>gift_wrap_tax|礼品包装税|是|[string]|0.00|
|data>>ship_service_level|配送级别|是|[string]|Expedited|
|data>>item_promotion_discount|订单商品促销折扣|是|[string]|0.00|
|data>>ship_promotion_discount|配送的促销折扣|是|[string]|0.00|
|data>>carrier|运输方|是|[string]|USPS|
|data>>tracking_number|快递号|是|[string]|9361289677090259988439|
|data>>fulfillment_channel|配送方式：<br>亚马逊配送 (AFN) <br>卖家自行配送 (MFN)|是|[string]|AFN|
|data>>points_granted|亚马逊授予买家的积分|是|[string]| &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "data": [
        {
            "sku": "Pink_Head_Rope",
            "currency": "USD",
            "carrier": "USPS",
            "amazon_order_id": "112-0065094-0449862",
            "shipment_id": "TBb1Gwxz1",
            "shipment_item_id": "DFJVVkwbH",
            "amazon_order_item_id": "67486918672938",
            "purchase_date": "2022-05-09T21:59:41+00:00",
            "payments_date": "2022-05-10T06:05:32+00:00",
            "shipment_date": "2022-05-10T06:05:32+00:00",
            "reporting_date": "2022-05-10T09:05:39+00:00",
            "estimated_arrival_date": "2022-05-12T03:00:00+00:00",
            "product_name": "Love Pearl Bottom Hair Circle Women's High Elastic Hair Binding Rope Jewelry Rubber Band Head Rope Pink",
            "quantity_shipped": 1,
            "item_price": "1.00",
            "item_tax": "0.00",
            "shipping_price": "0.00",
            "shipping_tax": "0.00",
            "gift_wrap_price": "0.00",
            "gift_wrap_tax": "0.00",
            "ship_service_level": "Expedited",
            "item_promotion_discount": "0.00",
            "ship_promotion_discount": "0.00",
            "tracking_number": "9374889705011506008135",
            "fulfillment_channel": "AFN",
            "points_granted": "",
            "hide_time": "2022-05-09 23:05:32",
            "buyer_email": "fbzdtkn3vgzftkk@marketplace.amazon.com",
            "buyer_name": "",
            "buyer_phone_number": "",
            "recipient_name": "",
            "ship_address_1": "",
            "ship_city": "BARNHART",
            "ship_state": "MO",
            "ship_postal_code": "63012",
            "ship_country": "US",
            "ship_phone_number": ""
        }
    ],
    "total": 9,
    "message": "操作成功",
    "request_id": "acb13574cdd14cd287043fadb895894e.1722930272131",
    "response_time": "2024-08-06 15:44:32",
    "error_details": []
}
```