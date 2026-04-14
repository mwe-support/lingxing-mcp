# SP投放小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/spTargetHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                                                                                               | 必填 | 类型 | 示例 |
| :------------ |:-------------------------------------------------------------------------------------------------| :------------ | :------------ | :------------ |
|report_date| 报告日期，格式：Y-m-d 只能查询最近60天                                                  |是|[string]|2024-05-25|
|campaign_id| 广告活动id                                                                                           |是|[number]|532580134831120|
|agg_dimension| 聚合维度:<br/>target  投放维度<br/>both_ad_target  广告+投放维度 <br/> both_target_placement 投放+广告位placement维度 |是|[string]|both_ad_target|



## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功 |是|[number]|0|
|message| 提示消息 |是|[string]|操作成功|
|total| 总数 |是|[number]|1167|
|error_details| 错误信息 |是|[array]| |
|request_id| 请求链路id |是|[string]|f884f0a6-f1e9-49d1-b144-a85ee4b57ed9|
|response_time| 响应时间 |是|[string]|2024-05-28 17:38:00|
|data| 响应数据 |是|[array]| |
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-25|
|data>>hour|小时:<br/>0  表示0-1点之间<br/>1  表示 1-2点之间<br/>以此类推|是|[number]|23|
|data>>campaign_id|广告活动id|是|[number]|532580134831120|
|data>>ad_id|广告id【agg_dimension = both_ad_target 的时候才返回】|是|[number]|347244425807704|
|data>>asin|  |是|[string]|B085M7XMJF|
|data>>msku| |是|[null]| |
|data>>match_type|匹配方式【agg_dimension=-both_ad_target 时返回该字段】|是|[string]|EXACT|
|data>>targeting_id|投放id【agg_dimension=-both_ad_target 时返回该字段】|是|[number]|339153487021379|
|data>>targeting|投放表达式【agg_dimension=-both_ad_target 时返回该字段】|是|[string]|spotting scope with rangefinder|
|data>>placement| 广告位【当agg_dimension = both_target_placement 的时候才返回】|是|[string]||
|data>>impressions|曝光量|是|[number]|34|
|data>>clicks|点击量|是|[number]|7|
|data>>cost|花费|是|[number]|3.52|
|data>>same_orders|直接成交订单|是|[number]|2|
|data>>orders|订单数|是|[number]|1|
|data>>same_sales|直接销售额|是|[number]|28.89|
|data>>sales|销售额|是|[number]|54.03|
|data>>same_units|直接成交销量|是|[number]|3|
|data>>units|销量|是|[number]|11|
|data>>ctr|点击/曝光|是|[number]|0.2059|
|data>>cpc|花费/点击|是|[number]|0.5|
|data>>cvr|订单数/点击|是|[number]|0.1429|
|data>>cpa|花费/订单数|是|[number]|3.52|
|data>>acos|花费/销售额|是|[number]|0.0651|
|data>>roas|销售额/花费|是|[number]|15.35|
|data>>group_id|广告组id|是|[number]|287918863539910|


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "profile_id": 2537307927915183,
            "report_date": "2024-05-25",
            "hour": 23,
            "campaign_id": 532580134831120,
            "ad_id": 347244425807704,
            "asin": "B085M7XMJF",
            "match_type": "EXACT",
            "impressions": 34,
            "clicks": 7,
            "cost": 3.52,
            "same_orders": 2,
            "orders": 1,
            "same_sales": 28.89,
            "sales": 54.03,
            "same_units": 3,
            "units": 11,
            "ctr": 0.2059,
            "cpc": 0.50,
            "cvr": 0.1429,
            "cpa": 3.52,
            "acos": 0.0651,
            "roas": 15.35,
            "group_id": 287918863539910,
            "msku": null,
            "targeting_id": 339153487021379,
            "targeting": "spotting scope with rangefinder"
        }
    ],
    "total": 1167,
    "error_details": [],
    "request_id": "f884f0a6-f1e9-49d1-b144-a85ee4b57ed9",
    "response_time": "2024-05-28 17:38:00"
}
```
