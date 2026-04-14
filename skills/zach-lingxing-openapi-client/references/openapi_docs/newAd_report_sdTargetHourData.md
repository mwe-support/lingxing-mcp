# SD投放小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdTargetHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                                              | 必填 | 类型 | 示例 |
| :------------ |:------------------------------------------------| :------------ | :------------ | :------------ |
|report_date| 报告日期，格式：Y-m-d 只能查询最近60天 |是|[string]|2024-05-27|
|campaign_id| 广告活动id                                          |是|[number]|556888946538776|
|agg_dimension| 聚合维度:<br>target  投放维度<br>both_ad_target  广告+投放维度 |是|[string]|target|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功 |是|[number]|0|
|message| 提示消息 |是|[string]|操作成功|
|total| 总数 |是|[number]|12|
|error_details| 错误信息 |是|[array]| |
|request_id| 请求链路id |是|[string]|9155ee2b-7946-4216-a77c-15607750f6f3|
|response_time| 响应时间 |是|[string]|2024-05-30 10:27:21|
|data| 响应数据 |是|[array]| |
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-27|
|data>>hour|小时:<br>0  表示0-1点之间<br>1  表示 1-2点之间<br>以此类推|是|[number]|2|
|data>>campaign_id|广告活动id|是|[number]|556888946538776|
|data>>ad_id|广告id【聚合维度为：both_ad_target时，该字段有数据】|是|[number]|309639059574636|
|data>>asin|asin【聚合维度为：both_ad_target时，该字段有数据】|是|[String]| |
|data>>msku|msku【聚合维度为：both_ad_target时，该字段有数据】|是|[String]| |
|data>>impressions|曝光量|是|[number]|11|
|data>>clicks|点击量|是|[number]|17|
|data>>cost|花费|是|[number]|14.66|
|data>>same_orders|直接成交订单|是|[number]|3|
|data>>orders|订单数|是|[number]|6|
|data>>same_sales|直接销售额|是|[number]|16.42|
|data>>sales|销售额|是|[number]|43.03|
|data>>units|销量|是|[number]|15|
|data>>ctr|点击/曝光|是|[number]|1.5455|
|data>>cpa|花费/订单数|是|[number]|2.44|
|data>>acos|花费/销售额|是|[number]|0.3407|
|data>>cpc|花费/点击|是|[number]|0.86|
|data>>roas|销售额/花费|是|[number]|2.94|
|data>>cvr|订单数/点击|是|[number]|0.3529|
|data>>group_id|广告组id|是|[number]|353711215349733|
|data>>targeting_id|投放id|是|[number]|534072414006380|
|data>>targeting|投放表达式|是|[string]||


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
            "campaign_id": 556888946538776,
            "ad_id": 309639059574636,
            "asin": null,
            "impressions": 11,
            "clicks": 17,
            "cost": 14.66,
            "same_orders": 3,
            "orders": 6,
            "same_sales": 16.42,
            "sales": 43.03,
            "units": 15,
            "ctr": 1.5455,
            "cpa": 2.44,
            "acos": 0.3407,
            "cpc": 0.86,
            "roas": 2.94,
            "cvr": 0.3529,
            "group_id": 353711215349733,
            "msku": null,
            "targeting_id": 534072414006380,
            "targeting": ""
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "9155ee2b-7946-4216-a77c-15607750f6f3",
    "response_time": "2024-05-30 10:27:21"
}
```
