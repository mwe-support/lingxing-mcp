# SP已购买商品报表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/asinReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例         |
| :------------ | :------------ | :------------ | :------------ |:-----------|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】，sid跟profile_id其中一个必填|是|[int]| 109        |
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报表日期，格式：Y-m-d|是|[string]| 2022-06-01 |
|show_detail|是否展示完整归因期信息【默认0】：0 否，1 是|否|[int]| 1          |
|offset|分页偏移量，默认0|否|[int]| 0          |
|length|分页长度，默认15|否|[int]| 15         |

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
|request_id|请求链路id|是|[string]|78E28978-7404-9BDF-3F41-01F0401D1305|
|response_time|响应时间|是|[string]|2023-02-17 09:59:19|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>ad_group_id|广告组id|是|[number]|257935689603689|
|data>>campaign_id|广告活动id|是|[number]|280135158572753|
|data>>keyword_id|关键词id|是|[number]| |
|data>>keyword_text|关键词|是|[string]||
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>asin|ASIN|是|[string]|B07FFK8LTD|
|data>>sku|SKU|是|[string]|8999J2113|
|data>>currency|货币|是|[string]|USD|
|data>>target_id|投放id|是|[number]|252176660633338|
|data>>targeting_text|投放|是|[string]|asin="B078RD7R26"|
|data>>report_date|报表日期|是|[string]|2021-06-23|
|data>>other_asin|Other Asin|是|[string]|B09MT3989Q|
|data>>match_type|匹配类别|是|[string]||
|data>>targeting_type|投放类别|是|[string]|TARGETING_EXPRESSION|
|data>>other_units|销量|是|[number]|1|
|data>>other_units_1d|销量(1d)【show_detail=1时返回字段】|否|[number]|1|
|data>>other_units_7d|销量(7d)【show_detail=1时返回字段】|否|[number]|1|
|data>>other_units_14d|销量(14d)【show_detail=1时返回字段】|否|[number]|1|
|data>>other_units_30d|销量(30d)【show_detail=1时返回字段】|否|[number]|1|
|data>>other_sales|销售额|是|[number]|18.87|
|data>>other_sales_1d|销售额(1d)【show_detail=1时返回字段】|否|[number]|18.87|
|data>>other_sales_7d|销售额(7d)【show_detail=1时返回字段】|否|[number]|18.87|
|data>>other_sales_14d|销售额(14d)【show_detail=1时返回字段】|否|[number]|18.87|
|data>>other_sales_30d|销售额(30d)【show_detail=1时返回字段】|否|[number]|18.87|
|data>>other_orders|订单数|是|[number]|0|
|data>>other_orders_1d|订单数(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_orders_7d|订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_orders_14d|订单数(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>other_orders_30d|订单数(30d)【show_detail=1时返回字段】|否|[number]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "78E28978-7404-9BDF-3F41-01F0401D1305",
    "response_time": "2023-02-24 09:26:58",
    "total": 1,
    "data": [
        {
            "ad_group_id": 257935689603689,
            "campaign_id": 280135158572753,
            "keyword_id": 0,
            "keyword_text": null,
            "profile_id": 121923590660074,
            "asin": "B07FFK8LTD",
            "sku": "8999J2113",
            "currency": "USD",
            "target_id": 252176660633338,
            "targeting_text": "asin=\"B078RD7R26\"",
            "report_date": "2021-06-23",
            "other_asin": "B09MT3989Q",
            "match_type": null,
            "other_units": 1,
            "other_sales": 18.87,
            "other_orders": null,
            "other_units_1d": 1,
            "other_units_7d": 1,
            "other_units_14d": 1,
            "other_units_30d": 1,
            "other_sales_1d": 18.87,
            "other_sales_7d": 18.87,
            "other_sales_14d": 18.87,
            "other_sales_30d": 18.87,
            "targeting_type": "TARGETING_EXPRESSION",
            "other_orders_1d": null,
            "other_orders_7d": null,
            "other_orders_14d": null,
            "other_orders_30d": null
        }
    ]
}
```
