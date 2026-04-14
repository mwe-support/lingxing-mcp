# SD广告活动小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/sdCampaignHourData` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|report_date|报告日期，格式：Y-m-d 只能查询最近60天|是|[string]|2024-05-27|
|campaign_id|广告活动id|是|[number]|518010735332270|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功 |是|[number]|0|
|message| 提示消息 |是|[string]|操作成功|
|total| 总数 |是|[number]|20|
|error_details| 错误信息 |是|[array]| |
|request_id| 请求链路id |是|[string]|63c0b025-d3c0-4c62-adb2-e5b2fdd2a830|
|response_time| 响应时间 |是|[string]|2024-05-30 09:26:01|
|data| 响应数据 |是|[array]| |
|data>>campaign_id|广告活动id|是|[number]|518010735332270|
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-27|
|data>>hour|小时:<br/>0  表示0-1点之间<br/>1  表示 1-2点之间<br/>以此类推|是|[number]|1|
|data>>cost|花费|是|[number]|7.04|
|data>>clicks|点击量|是|[number]|15|
|data>>impressions|曝光量|是|[number]|9|
|data>>same_orders|直接成交订单|是|[number]|3|
|data>>orders|订单数|是|[number]|5|
|data>>same_sales|直接销售额|是|[number]|28.1|
|data>>sales|销售额|是|[number]|32.72|
|data>>units|销量|是|[number]|6|
|data>>ctr|点击/曝光|是|[number]|1.6667|
|data>>cvr|订单数/点击|是|[number]|0.3333|
|data>>cpa|花费/订单数|是|[number]|1.41|
|data>>roas|销售额/花费|是|[number]|4.65|
|data>>acos|花费/销售额|是|[number]|0.2152|
|data>>cpc|花费/点击|是|[number]|0.47|


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "campaign_id": 518010735332270,
            "profile_id": 2537307927915183,
            "report_date": "2024-05-27",
            "hour": 1,
            "cost": 7.04,
            "clicks": 15,
            "impressions": 9,
            "same_orders": 3,
            "orders": 5,
            "same_sales": 28.10,
            "sales": 32.72
            "units": 6,
            "ctr": 1.6667,
            "cvr": 0.3333,
            "cpa": 1.41,
            "roas": 4.65,
            "acos": 0.2152,
            "cpc": 0.47
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "63c0b025-d3c0-4c62-adb2-e5b2fdd2a830",
    "response_time": "2024-05-30 09:26:01"
}
```
