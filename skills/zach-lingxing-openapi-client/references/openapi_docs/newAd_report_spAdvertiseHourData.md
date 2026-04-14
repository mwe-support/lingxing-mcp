# SP广告小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/spAdvertiseHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|report_date|报告日期，格式：Y-m-d 只能查询最近60天|是|[string]|2024-05-25|
|campaign_id|广告活动id|是|[number]|93889904442110|
|agg_dimension|聚合维度: <br>ad  广告维度 <br>both_ad_target  广告+投放维度|是|[string]|both_ad_target|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|操作成功|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|DHJ9190-7404-9BDF-3F41-01F0401D1315|
|response_time|响应时间|是|[string]|2023-02-17 09:59:19|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-25|
|data>>hour|小时:<br/>0  表示0-1点之间<br/>1  表示 1-2点之间<br/>以此类推|是|[number]|9|
|data>>campaign_id|广告活动id|是|[number]|93889904442110|
|data>>ad_id|广告id|是|[number]|559437347444970|
|data>>msku|msku|是|[null]| |
|data>>asin|asin|是|[object]|B07VC7ZN6P|
|data>>impressions|曝光量|是|[object]|4|
|data>>clicks|点击量|是|[number]|7|
|data>>cost|花费|是|[object]|5.18|
|data>>same_orders|直接成交订单|是|[number]|1|
|data>>orders|订单数|是|[number]|6|
|data>>same_sales|直接销售额|是|[number]|36.93|
|data>>sales|销售额|是|[number]|71.82|
|data>>same_units|直接成交销量|是|[number]|3|
|data>>units|销量|是|[number]|5|
|data>>match_type|匹配方式（当聚合维度为：both_ad_target 该字段有值）|是|[string]|TARGETING_EXPRESSION_PREDEFINED|
|data>>targeting_id|投放id（当聚合维度为：both_ad_target 该字段有值）|是|[number]|371645786382332|
|data>>targeting|投放表达式（当聚合维度为：both_ad_target 该字段有值）|是|[string]|complements|
|data>>ctr|点击/曝光|是|[number]|1.75|
|data>>cpc|花费/点击|是|[number]|0.74|
|data>>cvr|订单数/点击|是|[number]|0.8571|
|data>>cpa|花费/订单数|是|[number]|0.86|
|data>>acos|花费/销售额|是|[number]|0.0721|
|data>>roas|销售额/花费|是|[number]|13.86|
|data>>group_id|广告组id|是|[number]|332914711385626|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "profile_id": 2537307927915183,
            "report_date": "2024-05-25",
            "hour": 9,
            "campaign_id": 93889904442110,
            "ad_id": 559437347444970,
            "asin": "B07VC7ZN6P",
            "impressions": 4,
            "clicks": 7,
            "cost": 5.18,
            "same_orders": 1,
            "orders": 6,
            "same_sales": 36.93,
            "sales": 71.82,
            "same_units": 3,
            "units": 5,
            "match_type": "TARGETING_EXPRESSION_PREDEFINED",
            "ctr": 1.7500,
            "cpc": 0.74,
            "cvr": 0.8571,
            "cpa": 0.86,
            "acos": 0.0721,
            "roas": 13.86,
            "group_id": 332914711385626,
            "msku": null,
            "targeting_id": 371645786382332,
            "targeting": "complements"
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "42d2ba31-e50e-44e4-8870-5b4d945a52ae",
    "response_time": "2024-05-28 17:31:17"
}
```
