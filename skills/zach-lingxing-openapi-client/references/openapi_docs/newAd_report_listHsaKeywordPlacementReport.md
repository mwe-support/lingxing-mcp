# SB关键词-广告位报告
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/listHsaKeywordPlacementReport` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|sponsored_type|广告类型：<br>ALL|是|[string]|ALL|
|target_type|投放类型：<br>keyword|是|[string]|keyword|
|report_date|报告日期，格式：Y-m-d|是|[string]|2022-06-01|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认15|否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "sponsored_type": "ALL",
    "target_type": "keyword",
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
|data>>report_date|报告日期|是|[string]|2019-10-20|
|data>>profile_id|亚马逊店铺数字id|是|[number]| |
|data>>match_type|匹配方式|是|[string]| |
|data>>keyword_id|关键词id|是|[number]| |
|data>>keyword_text|关键词内容|是|[string]| |
|data>>campaign_id|广告活动id|是|[number]| |
|data>>clicks|点击|是|[number]| |
|data>>cost|花费|是|[number]| |
|data>>impressions|曝光|是|[number]| |
|data>>orders|订单数|是|[number]| |
|data>>new_to_brand_orders|品牌新买家订单数量|是|[number]| |
|data>>new_to_brand_units|品牌新买家销量|是|[number]| |
|data>>new_to_brand_order_percentage|品牌新买家订单百分比|是|[number]| |
|data>>new_to_brand_order_rate|品牌新买家转换率|是|[number]| |
|data>>new_to_brand_sales|品牌新买家销售额|是|[number]| |
|data>>sales|销售额|是|[number]| |
|data>>creative_type|广告类型：<br>default=》SB<br>video=》SBV|是|[string]|SB|
|data>>placement_type|广告位类型：<br>1 Other Placements<br>2 Other on-Amazon<br>3 Top of Search|是|[int]|1|
