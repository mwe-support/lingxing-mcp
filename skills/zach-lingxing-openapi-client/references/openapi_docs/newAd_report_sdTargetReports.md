# SD商品定位报表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdTargetReports` | HTTPS | POST | 10 |

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
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|nd8492d4-7a15-11ed-b162-0242ac1c0004|
|response_time|响应时间|是|[string]|2022-11-03 14:09:15|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>target_id|商品定位ID|是|[number]|1640591198|
|data>>targeting_type|投放类别|是|[string]|TARGETING_EXPRESSION|
|data>>targeting_text|投放内容|是|[string]|asin="B0DEMO8901"|
|data>>targeting_expression|投放表达式|是|[string]|asin="B0DEMO8901"|
|data>>ad_group_id|广告组ID|是|[number]|1640591197|
|data>>campaign_id|广告活动ID|是|[number]|1640591196|
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>impressions|展示量|是|[number]|111|
|data>>clicks|点击量|是|[number]|2|
|data>>cost|花费|是|[number]|10.92|
|data>>tactic|投放类型|是|[string]|T00020|
|data>>report_date|报表日期|是|[string]|2021-09-29|
|data>>same_orders|直接成交订单数|是|[number]|1|
|data>>orders|订单数|是|[number]|1|
|data>>same_sales|直接成交销售额|是|[number]|60.67|
|data>>sales|销售额|是|[number]|60.67|
|data>>units|销量|是|[number]|1|
|data>>view_impressions|可见展示量|是|[number]|88|
