# SB投放小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sbTargetHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明            | 必填 | 类型 | 示例 |
| :------------ |:--------------| :------------ | :------------ | :------------ |
|report_date| 报告日期，格式：Y-m-d 只能查询最近60天 |是|[string]|2024-05-27|
|campaign_id| 广告活动id        |是|[number]|376330797186894|
|agg_dimension| 聚合维度：<br>target  投放|是|[string]|target|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功 |是|[number]|0|
|message| 提示消息 |是|[string]|操作成功|
|total| 总数 |是|[number]|1530|
|error_details| 错误信息 |是|[array]| |
|request_id| 请求链路id |是|[string]|f1fd19db-60c6-4eb5-8008-2647982a2a47|
|response_time| 响应时间 |是|[string]|2024-05-30 09:57:53|
|data| 响应数据 |是|[array]| |
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-27|
|data>>hour|小时:<br/>0  表示0-1点之间<br/>1  表示 1-2点之间<br/>以此类推|是|[number]|0|
|data>>campaign_id|广告活动id|是|[number]|376330797186894|
|data>>impressions|曝光量|是|[number]|4|
|data>>clicks|点击量|是|[number]|15|
|data>>cost|花费|是|[number]|2.58|
|data>>same_orders|直接成交订单|是|[number]|1|
|data>>orders|订单数|是|[number]|0|
|data>>same_sales|直接销售额|是|[number]|3.24|
|data>>sales|销售额|是|[number]|0|
|data>>units|销量|是|[number]|0|
|data>>cpa|花费/订单数|是|[number]| |
|data>>cvr|订单数/点击|是|[number]| |
|data>>acos|花费/销售额|是|[number]| |
|data>>cpc|花费/点击|是|[number]|0.17|
|data>>roas|销售额/花费|是|[number]| |
|data>>ctr|点击/曝光|是|[number]|3.75|
|data>>group_id|广告组id|是|[number]|536895036361547|
|data>>targeting_id|投放id|是|[number]|330121859572460|
|data>>targeting|投放表达式|是|[string]|red christmas shower curtains for bathroom|


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "profile_id": 2537307927915183,
            "report_date": "2024-05-27",
            "hour": 0,
            "campaign_id": 376330797186894,
            "impressions": 4,
            "clicks": 15,
            "cost": 2.58,
            "same_orders": 1,
            "orders": 0,
            "same_sales": 3.24,
            "sales": 0,
            "units": 0,
            "cpa": null,
            "cvr": null,
            "acos": null,
            "cpc": 0.17,
            "roas": null,
            "ctr": 3.7500,
            "group_id": 536895036361547,
            "targeting_id": 330121859572460,
            "targeting": "red christmas shower curtains for bathroom"
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "f1fd19db-60c6-4eb5-8008-2647982a2a47",
    "response_time": "2024-05-30 09:57:53"
}
```
