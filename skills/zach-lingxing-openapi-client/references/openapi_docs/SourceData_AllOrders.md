# 查询亚马逊源报表-所有订单
查询 All Orders Report By last update 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/allOrders` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|date_type|时间查询类型：【默认1】<br>1 下单日期<br>2 亚马逊订单更新时间|否|[int]|1|
|start_date|亚马逊当地下单时间，左闭区间，格式：Y-m-d|是|[string]|2020-04-01|
|end_date|亚马逊当地下单时间，右开区间，格式：Y-m-d|是|[string]|2024-08-05|
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

| 参数名  | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>amazon_order_id|亚马逊订单号|是|[string]|028-0316583-1645130|
|data>>merchant_order_id|卖家为订单提供的唯一编号|是|[string]|028-0316583-1645130|
|data>>last_updated_time|订单最近更新时间|是|[string]|  |
|data>>purchase_date|下单日期-格式化当地时间（当地时间, 时区）|是|[string]|2018-11-04T07:58:08+00:00|
|data>>purchase_date_locale|下单日期-对应亚马逊当地日期（不建议使用）|是|[string]|2018-11-04|
|data>>purchase_date_local|下单日期-店铺当地时间|是|[string]|2018-11-04 08:58:08|
|data>>shipment_date|发货时间-UTC时间|是|[string]|2018-11-04 08:58:08|
|data>>order_status|订单的当前状态|是|[string]|Shipped|
|data>>fulfillment_channel|订单的配送方式：<br>Amazon 亚马逊配送 (AFN) <br>Merchant 卖家自行配送 (MFN)|是|[string]|Amazon|
|data>>sales_channel|下单渠道|是|[string]|Amazon.de|
|data>>order_channel|CBA/WBA 订单下单的子渠道|是|[string]|  |
|data>>url|链接|是|[string]|  |
|data>>ship_service_level|配送服务类型|是|[string]|Standard|
|data>>sku|MSKU|是|[string]|DA189076B1|
|data>>asin|ASIN|是|[string]|B078W791QLD|
|data>>product_name|品名|是|[string]|Drehteller Cake Decorating Turntable|
|data>>item_status|该商品在订单内的当前状态	|是|[string]|Shipped|
|data>>quantity|此商品的购买数量|是|[number]|1|
|data>>currency|币种|是|[string]|EUR|
|data>>item_price|买家为商品支付的金额|是|[string]|13.99|
|data>>item_tax|买家为商品税支付的金额|是|[string]|  |
|data>>shipping_price|买家支付的运费金额|是|[string]|1.0|
|data>>shipping_tax|买家为运费税支付的金额|是|[string]|  |
|data>>gift_wrap_price|买家为礼品包装支付的金额|是|[string]|  |
|data>>gift_wrap_tax|买家为礼品包装税支付的金额|是|[string]|  |
|data>>item_promotion_discount|应用于订单商品的所有促销折扣的总和|是|[string]|  |
|data>>ship_promotion_discount|应用于配送的促销折扣|是|[string]|1.0|
|data>>promotion_ids|应用于此订单商品的所有商品促销的列表|是|[string]|DE Core Free Shipping 2018/04/24 20-00-00|
|data>>pid|本地产品id|是|[int]|212|
|data>>local_sku|本地产品SKU|是|[string]|Sun002-FBA63|
|data>>local_name|本地产品品名|是|[string]|  |
|data>>sid|店铺id|是|[int]|3|
|total|总数|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "F79152AD-CBC0-846C-DA15-54D7BFC5C835",
    "response_time": "2021-04-19 18:33:51",
    "data": [
        {
            "amazon_order_id": "111-01111-6646648",
            "merchant_order_id": "111-011110-6646648",
            "last_updated_time": 1602964702,
            "purchase_date": "2020-10-17T00:31:51+00:00",
            "purchase_date_locale": "2020-10-16",
            "purchase_date_local": "2020-10-16 17:31:51",
            "shipment_date": "2020-10-17T12:58:15-07:00",
            "order_status": "Shipped",
            "fulfillment_channel": "Amazon",
            "sales_channel": "Amazon.com",
            "order_channel": "",
            "url": "",
            "ship_service_level": "Expedited",
            "sku": "T1-1111-59G8",
            "asin": "B0711113",
            "product_name": "P",
            "item_status": "Shipped",
            "quantity": 1,
            "currency": "USD",
            "item_price": "7.99",
            "item_tax": "0.82",
            "shipping_price": "",
            "shipping_tax": "",
            "gift_wrap_price": "",
            "gift_wrap_tax": "",
            "item_promotion_discount": "",
            "ship_promotion_discount": "",
            "promotion_ids": "",
            "pid": 1,
            "local_sku": "视觉111",
            "local_name": "00.100",
            "sid": 1
        }
    ],
    "total": 2260
}
```
