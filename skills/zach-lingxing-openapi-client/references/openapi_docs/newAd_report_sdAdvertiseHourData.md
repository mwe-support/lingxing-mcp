# SD广告小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdAdvertiseHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|report_date|报告日期，格式：Y-m-d 只能查询最近60天|是|[string]|2024-05-27|
|campaign_id|广告活动id|是|[number]|275026731985726|
|agg_dimension|聚合维度:<br>ad  广告维度<br>both_ad_target  广告+投放维度|是|[string]|ad|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 响应数据 |是|[number]|0|
|message| 提示消息 |是|[string]|操作成功|
|total| 总数 |是|[number]|1|
|error_details| 错误信息 |是|[array]| |
|request_id| 请求链路id |是|[string]|cccac210-5609-45d4-8754-3e3ee87ba075|
|response_time| 响应时间 |是|[string]|2024-05-30 09:58:23|
|data| 响应数据 |是|[array]| |
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-27|
|data>>hour|小时:<br>0  表示0-1点之间<br>1  表示 1-2点之间<br>以此类推|是|[number]|2|
|data>>campaign_id|店铺id|是|[number]|275026731985726|
|data>>ad_id|广告id|是|[number]|113105321288796|
|data>>asin|asin|是|[string]| |
|data>>targeting|投放表达式【agg_dimension=-both_ad_target 时返回字段】|是|[string]| |
|data>>targeting_id|投放id【agg_dimension=-both_ad_target 时返回字段】|是|[number]| |
|data>>msku|msku|是|[string]| |
|data>>impressions|曝光量|是|[number]|20|
|data>>clicks|点击量|是|[number]|15|
|data>>cost|花费|是|[number]|22.44|
|data>>same_orders|直接成交订单|是|[number]|2|
|data>>orders|订单数|是|[number]|6|
|data>>same_sales|直接销售额|是|[number]|36.4|
|data>>sales|销售额|是|[number]|42.89|
|data>>units|销量|是|[number]|13|
|data>>cpa|花费/订单数|是|[number]|3.74|
|data>>cvr|订单数/点击|是|[number]|0.4|
|data>>acos|花费/销售额|是|[number]|0.5232|
|data>>cpc|花费/点击|是|[number]|1.5|
|data>>roas|销售额/花费|是|[number]|1.91|
|data>>ctr|点击/曝光|是|[number]|0.75|
|data>>group_id|广告组id|是|[number]|18782512956555|


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "profile_id": 2537307927915183,
            "report_date": "2024-05-27",
            "hour": 2,
            "campaign_id": 275026731985726,
            "ad_id": 113105321288796,
            "asin": null,
            "msku": null,
            "targeting_id": 22117772586605,
            "targeting": "",
            "impressions": 20,
            "clicks": 15,
            "cost": 22.44,
            "same_orders": 2,
            "orders": 6,
            "same_sales": 36.40,
            "sales": 42.89,
            "units": 13,
            "cpa": 3.74,
            "cvr": 0.4000,
            "acos": 0.5232,
            "cpc": 1.50,
            "roas": 1.91,
            "ctr": 0.7500,
            "group_id": 18782512956555
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "cccac210-5609-45d4-8754-3e3ee87ba075",
    "response_time": "2024-05-30 09:58:23"
}
```
