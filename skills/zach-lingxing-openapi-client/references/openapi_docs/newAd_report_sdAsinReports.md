# SD已购买商品报表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdAsinReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报表日期，格式：Y-m-d|是|[string]|2022-06-01|
|show_detail|是否展示完整归因期信息【默认0】：0 否，1 是|否|[int]|1|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认15|否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "report_date": "2022-06-01",
    "show_detail": 1,
    "offset": 0,
    "length": 15
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| 0|
|message|提示消息|是|[string]|操作成功|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|DHJ9190-7404-9BDF-3F41-01F0401D1315|
|response_time|响应时间|是|[string]|2023-02-17 09:59:19|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>tactic|投放类型|是|[string]|T00020|
|data>>ad_group_id|广告组id|是|[number]|52782146712574|
|data>>campaign_id|广告活动id|是|[number]|69898171172999|
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>asin|ASIN|是|[string]|B07XBZXPQP|
|data>>sku|SKU|是|[string]|4O-JLG6-JL9Z|
|data>>currency|货币|是|[string]|USD|
|data>>report_date|报表日期|是|[string]|2021-06-23|
|data>>other_asin|Other Asin|是|[string]|B07PLVMWY9|
|data>>other_units|销量|是|[number]|0|
|data>>other_units_1d|销量(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_units_7d|销量(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_units_14d|销量(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_units_30d|订单数(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_sales|销售额|是|[number]|0|
|data>>other_sales_1d|销售额(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_sales_7d|销售额(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_sales_14d|销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_sales_30d|销售额(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_orders|订单|是|[null]|0|
|data>>other_orders_1d|订单数(1d)【show_detail=1时返回字段】|否|[null]|0|
|data>>other_orders_7d|订单数(7d)【show_detail=1时返回字段】|否|[null]|0|
|data>>other_orders_14d|订单数(14d)【show_detail=1时返回字段】|否|[null]|0|
|data>>other_orders_30d|订单数(30d)【show_detail=1时返回字段】|否|[null]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "DHJ9190-7404-9BDF-3F41-01F0401D1315",
    "response_time": "2023-02-24 09:26:58",
    "total": 1,
    "data": [
        {
            "tactic": "T00020",
            "ad_group_id": 215189196202698,
            "campaign_id": 77765272166097,
            "profile_id": 121923590660074,
            "asin": "B07T1BCQ2G",
            "sku": "7686J0159",
            "currency": "USD",
            "report_date": "2021-06-23",
            "other_asin": "B07T3FT5KJ",
            "other_units": 1,
            "other_sales": 9.99,
            "other_orders": null,
            "other_units_1d": 1,
            "other_units_7d": 1,
            "other_units_14d": 1,
            "other_units_30d": 1,
            "other_sales_1d": 9.99,
            "other_sales_7d": 9.99,
            "other_sales_14d": 9.99,
            "other_sales_30d": 9.99,
            "other_orders_1d": null,
            "other_orders_7d": null,
            "other_orders_14d": null,
            "other_orders_30d": null
        }
    ]
}
```
