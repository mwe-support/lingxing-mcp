# 查询亚马逊源报表-FBA退货订单
查询 FBA customer returns 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/refundOrders` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|date_type|时间查询类型【默认1】：<br>1 退货时间【站点时间】<br>2 更新时间【北京时间】|否|[int]|1|
|start_date|开始时间，左闭右开，格式：Y-m-d |是|[string]|2020-01-01|
|end_date|结束时间，左闭右开，格式：Y-m-d |是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "date_type": 1,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明          | 必填 | 类型 | 示例 |
| :------------ |:------------| :------------ | :------------ | :------------ |
|code| 状态码，0 成功    |是|[int]| 0|
|message| 消息提示        |是|[string]|success|
|error_details| 错误信息        |是|[array]|  |
|request_id| 请求链路id      |是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time| 响应时间        |是|[string]|2020-05-18 11:23:47|
|data| 响应数据        |是|[array]|  |
|data>>sid| 店铺id        |是|[int]|3|
|data>>order_id| 订单号         |是|[string]|028-0034384-7536302|
|data>>local_sku| 本地产品sku     |是|[string]|456487456|
|data>>product_name| 品名          |是|[string]|6 Zoll Mikrofon Popschutz Studio Mikrofon|
|data>>sku| MSKU        |是|[string]|DA190379B1|
|data>>asin| ASIN        |是|[string]|B06XPGK9SHL|
|data>>fnsku| FNSKU       |是|[string]|X000NYD9RDX|
|data>>quantity| 数量          |是|[int]|1|
|data>>return_date| 退货时间【UTC时间】 |是|[string]|2019-01-17T02:28:18+00:00|
|data>>return_date_locale| 退货时间【站点时间】  |是|[string]|2020-06-04|
|data>>purchase_date| 订购时间【UTC时间】 |是|[string]|2019-01-17T02:28:18+00:00|
|data>>purchase_date_locale| 订购时间【站点时间】  |是|[string]|2020-06-04|
|data>>gmt_modified| 更新时间        |是|[string]|2023-06-08 09:48:10|
|data>>fulfillment_center_id| 存储库存的运营中心   |是|[string]|BTS2|
|data>>detailed_disposition| 商品状态属性      |是|[string]|SELLABLE|
|data>>reason| 退回原因        |是|[string]|NO_REASON_GIVEN|
|data>>status| 状态          |是|[string]|Unit returned to inventory|
|data>>license_plate_number| 唯一序列号       |是|[string]|LPNHE298128253|
|data>>customer_comments| 买家评论        |是|[string]| &nbsp; |
|data>>remark| 备注          |是|[string]|备注|
|data>>tag| 标签信息        |是|[array]| |
|data>>tag>>tag_name| 标签名称        |是|[string]|尺码问题|
|data>>tag>>tag_color| 标签颜色        |是|[string]|E76A5D|

## 返回成功示例

```
{
    "code":0,
    "message":"success",
    "error_details":[],
    "request_id":"3387708D-4BB5-BB28-F8CE-18EE2A3D591F",
    "response_time":"2023-06-30 17:30:02",
    "data":[
        {
            "sid":101,
            "order_id":"133666",
            "product_name":"SUPER J Cell Phone Armband Running Armband for Iphone Samsung Sports Phone Holder Waterproof",
            "sku":"JJ001",
            "asin":"B0BB9XV7CW",
            "fnsku":"B0BB9XV7CW",
            "quantity":1,
            "return_date":"2023-06-04T19:57:09+01:00",
            "return_date_locale":"2023-06-04",
            "purchase_date": "2023-08-13T07:20:35Z",
            "purchase_date_locale": "2023-08-13",
            "fulfillment_center_id":"AUS3",
            "detailed_disposition":"SELLABLE",
            "reason":"UNDELIVERABLE_UNKNOWN",
            "status":"Unit returned to inventory",
            "license_plate_number":"LPNT010424593",
            "customer_comments":"",
            "gmt_modified":"2023-06-08 09:48:10",
            "local_sku":"10369333",
            "remark":"备注",
            "tag":[
                {
                    "tag_name":"尺码问题",
                    "tag_color":"E76A5D"
                }
            ]
        }
    ],
    "total":1
}
```

## 返回失败示例

```
{
    "code": 102,
    "message": "参数不合法",
    "error_details": [
        "参数不能为空"
    ],
    "request_id": "CCF43BD7-A0A1-31BC-5B36-717DDF197755",
    "response_time": "2021-11-23 17:46:09",
    "data": [],
    "total": 0
}
```
