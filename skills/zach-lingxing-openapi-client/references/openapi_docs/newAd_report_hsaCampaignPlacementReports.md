# SB广告活动-广告位报告
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/hsaCampaignPlacementReports` | HTTPS | POST | 10 |

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
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认15|否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "report_date": "2022-06-01",
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
|request_id|请求链路id|是|[string]|478WOD3-7404-9BDF-8F41-01F0401D1305|
|response_time|响应时间|是|[string]|2023-02-17 09:59:19|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>clicks|点击量|是|[number]|14|
|data>>cost|花费|是|[number]|12.61|
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>impressions|展示量|是|[number]|865|
|data>>report_date|报表日期|是|[string]|2021-06-23|
|data>>campaign_id|广告活动id|是|[number]|162632371880150|
|data>>placement_type|广告位类型|是|[string]|Otheron-Amazon|
|data>>orders|订单数|是|[number]|3|
|data>>new_to_brand_orders|品牌新买家订单数量|是|[number]||
|data>>new_to_brand_units|品牌新买家销量|是|[number]||
|data>>new_to_brand_sales|品牌新买家销售额|是|[number]|0.0|
|data>>new_to_brand_order_percentage|品牌新买家订单百分比|是|[number]|0.0|
|data>>new_to_brand_order_rate|品牌新买家转换率|是|[number]|0.0|
|data>>sales|销售额|是|[number]|42.48|
|data>>creative_type|广告类型： default=》SB video=》SBV|是|[string]|video|
|data>>units|销量|是|[number]|453|
|data>>same_units|直接成交量|是|[number]|453|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "478WOD3-7404-9BDF-8F41-01F0401D1305",
    "response_time": "2023-02-24 10:56:58",
    "total": 1,
    "data": [
        {
            "clicks": 14,
            "cost": 12.61,
            "profile_id": 121923590660074,
            "impressions": 865,
            "report_date": "2021-06-23",
            "campaign_id": 162632371880150,
            "placement_type": "Otheron-Amazon",
            "orders": 3,
            "same_orders": 3,
            "new_to_brand_orders": null,
            "new_to_brand_units": null,
            "new_to_brand_sales": null,
            "same_sales": 42.48,
            "new_to_brand_order_percentage": null,
            "new_to_brand_order_rate": null,
            "sales": 42.48,
            "creative_type": "video"
        }
    ]
}
```
