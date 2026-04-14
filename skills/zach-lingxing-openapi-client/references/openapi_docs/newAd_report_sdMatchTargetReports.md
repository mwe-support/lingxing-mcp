# SD匹配的目标报表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdMatchTargetReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报表日期|是|[string]|2022-06-01|
|show_detail|是否展示完整归因期信息【默认0】：0 否，1 是|否|[int]|1|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页条数，默认15|否|[int]|15|

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
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|52688b81-2398-4e60-9617-619fc2cf5789|
|response_time|响应时间|是|[string]|2023-03-20 10:30:32|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>campaign_id|广告活动id|是|[number]|199391935779690|
|data>>ad_group_id|广告组id|是|[number]|26997248113546|
|data>>target_id|投放id（关键词/商品投放 根据target_type）|是|[number]|149428281501570|
|data>>target_text|投放的内容|是|[string]|category="Körbe & Behälter"|
|data>>matched_target|匹配的投放|是|[string]|B07R6WG38H|
|data>>currency|货币|是|[string]|EUR|
|data>>impressions|展示量|是|[number]|56|
|data>>clicks|点击量|是|[number]|2|
|data>>cost|花费|是|[number]|0|
|data>>same_orders|直接成交订单数|是|[number]|0|
|data>>orders|订单数|是|[number]|0|
|data>>same_sales|直接成交销售额|是|[number]|0|
|data>>sales|销售额|是|[number]|0|
|data>>units|销量|是|[number]|0|
|data>>new_to_brand_orders|品牌新买家订单数量|是|[number]|0|
|data>>new_to_brand_sales|品牌新买家销售额|是|[number]|0|
|data>>new_to_brand_units|品牌新买家销量|是|[number]|0|
|data>>view_imporessions|可见展示量|是|[int]|0|
|data>>report_date|报表日期|是|[string]|2022-03-07|
|data>>same_orders_1d|直接成交订单数(1d)【show_detail=1返回】|否|[number]|0|
|data>>orders_1d|销售额(1d)【show_detail=1返回】|否|[number]|0|
|data>>same_sales_1d|直接成交销售额(1d)【show_detail=1返回】|否|[number]|0|
|data>>sales_1d|销售额(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_7d|直接成交订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_7d|订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_7d|直接成交销售额(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_7d|销售额(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_30d|直接成交订单数(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_30d|订单数(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_30d|直接成交销售额(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_30d|销售额(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_14d|直接成交订单数(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_14d|订单数(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_14d|直接成交销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_14d|销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_1d|销量(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_7d|销量(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_14d|销量(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_30d|销量(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>new_to_brand_orders_14d|品牌新买家订单数量(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>new_to_brand_sales_14d|品牌新买家销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>new_to_brand_units_14d|品牌新买家销量(14d)【show_detail=1时返回字段】|否|[number]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",                         
    "error_details": [],
    "request_id": "52688b81-2398-4e60-9617-619fc2cf5789",
    "response_time": "2023-03-20 10:30:32",
    "total": 1,
    "data": [
        {
            "profile_id": 121923590660074,
            "campaign_id": 199391935779690,
            "ad_group_id": 26997248113546,
            "target_id": 149428281501570,
            "target_text": "category=\"Körbe & Behälter\"",
            "matched_target": "B07R6WG38H",
            "currency": "EUR",
            "impressions": 56,
            "clicks": 2,
            "cost": 0.00,
            "same_orders": 0,
            "orders": 0,
            "same_sales": 0.00,
            "sales": 0.00,
            "units": 0,
            "new_to_brand_orders": 0,
            "new_to_brand_sales": 0.00,
            "new_to_brand_units": 0,
            "report_date": "2022-03-07",
            "same_orders_1d": 0,
            "orders_1d": 0,
            "same_sales_1d": 0.00,
            "sales_1d": 0.00,
            "same_orders_7d": 0,
            "orders_7d": 0,
            "same_sales_7d": 0.00,
            "sales_7d": 0.00,
            "same_orders_30d": 0,
            "orders_30d": 0,
            "same_sales_30d": 0.00,
            "sales_30d": 0.00,
            "same_orders_14d": 0,
            "orders_14d": 0,
            "same_sales_14d": 0.00,
            "sales_14d": 0.00,
            "units_1d": 0,
            "units_7d": 0,
            "units_14d": 0,
            "units_30d": 0,
            "new_to_brand_orders_14d": 0,
            "new_to_brand_sales_14d": 0.00,
            "new_to_brand_units_14d": 0
        }
    ]
}
```
