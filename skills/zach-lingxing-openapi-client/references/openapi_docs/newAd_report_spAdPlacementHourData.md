# SP广告位小时数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/spAdPlacementHourData` | HTTPS | POST | 1 |

**请求参数**

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|report_date|报告日期，格式：Y-m-d 只能查询最近60天|是|[string]|2024-05-25|
|campaign_id|广告活动id|是|[number]|549538041400637|

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
|data>>campaign_id|广告活动id|是|[number]|549538041400637|
|data>>profile_id|店铺id|是|[number]|2537307927915183|
|data>>report_date|报告日期|是|[string]|2024-05-25|
|data>>placement|广告位|是|[string]|Detail Page on-Amazon|
|data>>hour|小时：<br> 0   0-1点之间 <br>1   1-2点之间 <br>以此类推|是|[number]|9|
|data>>cost|花费|是|[number]|0.29|
|data>>clicks|点击量|是|[number]|15|
|data>>impressions|曝光量|是|[number]|19|
|data>>same_orders|直接成交订单|是|[number]|4|
|data>>orders|订单数|是|[number]|5|
|data>>same_sales|直接销售额|是|[number]|0.36|
|data>>sales|销售额|是|[number]|14.44|
|data>>same_units|直接成交销量|是|[number]|1|
|data>>units|销量|是|[number]|4|
|data>>cpc|花费/点击|是|[number]|0.02|
|data>>cvr|订单数/点击|是|[number]|0.3333|
|data>>cpa|花费/订单数|是|[number]|0.06|
|data>>acos|花费/销售额|是|[number]|0.0201|
|data>>roas|销售额/花费|是|[number]|49.79|
|data>>ctr|点击/曝光|是|[number]|0.7895|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "data": [
        {
            "campaign_id": 549538041400637,
            "profile_id": 2537307927915183,
            "report_date": "2024-05-25",
            "placement": "Detail Page on-Amazon",
            "hour": 9,
            "cost": 0.29,
            "clicks": 15,
            "impressions": 19,
            "same_orders": 4,
            "orders": 5,
            "same_sales": 0.36,
            "sales": 14.44,
            "same_units": 1,
            "units": 4,
            "cpc": 0.02,
            "cvr": 0.3333,
            "cpa": 0.06,
            "acos": 0.0201,
            "roas": 49.79,
            "ctr": 0.7895
        }
    ],
    "total": 1,
    "error_details": [],
    "request_id": "76d8f0b5-4c45-462e-96c6-31ff9ad10140",
    "response_time": "2024-05-28 15:21:07"
}
```
