# SD广告商品报表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdProductAdReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报告日期，格式：Y-m-d|是|[string]|2022-06-01|
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
|data|响应数据|是|[array]| |
|data>>ad_id|商品广告id|是|[number]|1640591210|
|data>>asin|ASIN|是|[string]|B0DEMO9012|
|data>>sku|msku|是|[string]|SKU-DEMO-9012|
|data>>ad_group_id|广告组id|是|[number]|1640591204|
|data>>campaign_id|广告活动id|是|[number]|1640591203|
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>impressions|展示量|是|[number]|96|
|data>>clicks|点击量|是|[number]|0|
|data>>cost|花费|是|[number]|0|
|data>>tactic|投放类型|是|[string]|0|
|data>>report_date|报表日期|是|[string]|2021-09-29|
|data>>view_impressions|可见展示量|是|[number]|0|
|data>>same_orders|直接成交订单数|是|[number]| 0|
|data>>same_orders_1d|直接成交订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_7d|直接成交订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_14d|直接成交订单数(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_orders_30d|直接成交订单数(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders|订单数|是|[number]|0|
|data>>orders_1d|订单数(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_7d|订单数(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_14d|订单数(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>orders_30d|订单数(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales|销售额|是|[number]|0|
|data>>sales_1d|销售额(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_7d|销售额(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_14d|销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>sales_30d|销售额(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales|直接成交销售额|是|[number]|0|
|data>>same_sales_1d|直接成交销售额(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_7d|直接成交销售额(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_14d|直接成交销售额(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>same_sales_30d|直接成交销售额(30d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units|销量|是|[number]|0|
|data>>units_1d|销量(1d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_7d|销量(7d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_14d|销量(14d)【show_detail=1时返回字段】|否|[number]|0|
|data>>units_30d|销量(30d)【show_detail=1时返回字段】|否|[number]|0|


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
            "ad_id": 1640591210,
            "asin": "B0DEMO9012",
            "sku": "SKU-DEMO-9012",
            "ad_group_id": 1640591204,
            "campaign_id": 1640591203,
            "profile_id": 121923590660074,
            "impressions": 96,
            "clicks": 0,
            "cost": 0.00,
            "tactic": null,
            "report_date": "2021-09-29",
            "same_orders": 0,
            "orders": 0,
            "same_sales": 0.00,
            "sales": 0.00,
            "units": 0,
            "view_impressions": 57,
            "same_orders_14d": 0,
            "orders_14d": 0,
            "same_sales_14d": 0.00,
            "sales_14d": 0.00,
            "units_14d": 0,
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
            "units_1d": 0,
            "units_7d": 0,
            "units_30d": 0
        }
    ]
}
```
