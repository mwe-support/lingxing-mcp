# 查询亚马逊源报表—Amazon Fulfilled Shipments
查询 Amazon Fulfilled Shipments 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/getAmazonFulfilledShipmentsList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|shipment_date_after|快照开始时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss，<br>开始结束时间区间支持7天|是|[string]|2024-01-01 00:00:00|
|shipment_date_before|快照结束时间【shipment_date_locale】，格式：Y-m-d hh-mm-ss，<br>开始结束时间区间支持7天|是|[string]|2024-01-06 00:00:00|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "shipment_date_after": "2024-01-01 00:00:00",
    "shipment_date_before": "2024-01-06 00:00:00",
    "amazon_order_id": ["123-1234567-1234567","789-1234567-1234567"],
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|EBF82D68-51E2-9993-517B-19F2D10A40A5|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]||
|data>>sid|店铺id|是|[int]|1|
|data>>amazon_order_id|亚马逊为订单提供的可显示的唯一编号|是|[string]|123-6589275-65894821|
|data>>merchant_order_id|卖家为订单提供的唯一标识|是|[string]| |
|data>>shipment_id|加密的亚马逊货件编号	|是|[string]|4B5614520|
|data>>shipment_item_id|加密的亚马逊货件商品编号|是|[string]|DKTGdTZzRRRR|
|data>>amazon_order_item_id|亚马逊为订单内商品提供的唯一可显示编号|是|[string]|432798708695061|
|data>>merchant_order_item_id|为订单内商品提供的唯一标识|是|[string]| |
|data>>purchase_date|订单下单日期（报表时间，含时区）|是|[string]|2020-07-26T16:30:30+00:00|
|data>>purchase_date_locale|订单下单日期（站点时间，含时区）|是|[string]|2020-07-26T09:30:30-07:00|
|data>>payments_date|买家付款处理完成的日期（报表时间，含时区）|是|[string]|2020-07-26T23:46:56+00:00|
|data>>payments_date_locale|买家付款处理完成的日期（站点时间，含时区）|是|[string]|2020-07-26T16:46:56-07:00|
|data>>shipment_date|亚马逊完成货件（已配送）的日期（报表时间，含时区）|是|[string]|2020-07-26T23:46:56+00:00|
|data>>shipment_date_locale|亚马逊完成货件（已配送）的日期（站点时间，含时区）|是|[string]|2020-07-26T16:46:56-07:00|
|data>>reporting_date|提供报告数据的日期（报表时间，含时区）|是|[string]|2020-07-27T02:47:03+00:00|
|data>>reporting_date_locale|提供报告数据的日期（站点时间，含时区）|是|[string]|2020-07-26T19:47:03-07:00|
|data>>sku|卖家为商品定义的唯一标识|是|[string]|SKUTEST028C37E|
|data>>product_name|商品的简称，在商品详情页面上和浏览器的标题栏以粗体字显示|是|[string]|[演示数据]SanDisk Extreme microSD UHS-I带适配器|
|data>>quantity_shipped|此商品已配送的数量|是|[number]|1|
|data>>currency|购物使用的货币|是|[string]|USD|
|data>>item_price|买家为商品支付的金额。金额是总金额，不是单价。|是|[string]|10.99|
|data>>item_tax|买家支付的商品税。金额是总金额，不是单价。|是|[string]|0.85|
|data>>shipping_price|买家支付的运费。金额是总金额，不是单价。|是|[string]|0.00|
|data>>shipping_tax|买家支付的运费税。金额是总金额，不是单价。|是|[string]|0.00|
|data>>gift_wrap_price|买家为礼品包装支付的金额。金额是总金额，不是单价。|是|[string]|0.00|
|data>>gift_wrap_tax|买家支付的礼品包装税。金额是总金额，不是单价。|是|[string]|0.00|
|data>>ship_service_level|买家期望卖家使用的配送服务类型（例如，标准配送与加急配送）|是|[string]|Expedited|
|data>>ship_country|ISO 3166 标准的收件地址的国家/地区二字代码|是|[string]|US|
|data>>bill_country|ISO 3166 标准的账单地址的国家/地区二字代码|是|[string]| |
|data>>item_promotion_discount|订单商品的促销折扣|是|[string]|0.00|
|data>>ship_promotion_discount|配送费的促销折扣|是|[string]|0.00|
|data>>carrier|配送包裹的承运人|是|[string]|AMZN_US|
|data>>tracking_number|包裹的承运人追踪编码|是|[string]|C7B1C7A93|
|data>>estimated_arrival_date|预计送达买家地址的日期（报表时间，含时区）|是|[string]|2020-07-28T03:00:00+00:00|
|data>>estimated_arrival_date_locale|预计送达买家地址的日期（站点时间，含时区）|是|[string]|1970-01-01|
|data>>fulfillment_center_id|配送订单的运营中心的唯一标识|是|[string]|AKS1|
|data>>fulfillment_channel|说明订单的配送方式：亚马逊物流网络 (AFN) 或卖家自配送 (MFN)|是|[string]|AFN|
|data>>sales_channel|订单来源|是|[string]|Amazon.com|
|data>>points_granted|积分成本（日本站）|是|[string]| |
|total|总数|是|[int]|1168970|
