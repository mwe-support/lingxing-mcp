# 查询促销活动列表-优惠券
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/promotionalActivities/coupon/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| start_date | 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-11-23 |
| end_date   | 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-12-20 |
| sids       | 店铺id，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [array]  | [102,144]  |
| offset     | 分页偏移量，默认0                                            | 否   | [int]    | 0          |
| length     | 分页长度，默认20，上限200                                    | 否   | [int]    | 20         |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code                        | 状态码，0 成功                                               | 是   | [int]    | 0                                              |
| message                     | 消息提示                                                     | 是   | [string] | success                                        |
| error_details               | 错误信息                                                     | 是   | [array]  | |
|request_id| 请求链路id |是|[string]| 77ac259a67d5462594c83b80669b6eae.1692331008758 |
|response_time| 响应时间 |是|[string]| 2023-08-18 11:56:49 |
|total| 总数 |是|[int]| 200 |
|data| 响应数据 |是|[array]| |
|data>>promotion_id|促销活动id|是|[string]||
|data>>name|优惠券名称|是|[string]|nnn|
|data>>sid|店铺id|是|[int]|2|
|data>>currency_icon|货币icon|是|[string]|JP¥ |
|data>>origin_status|活动状态：<br>ACTIVE 进行中<br>CANCELED 已取消<br>EXPIRED 已过期<br>RUNNING 生效中<br>NEEDS ACTION 需要注意<br>EXPIRING SOON 即将过期<br>SUBMITTED 已提交<br>FAILED 失败|是|[string]|FAILED|
|data>>discount|折扣|是|[string]|JP¥11.00 |
|data>>budget|预算|是|[string]|JP¥10084.0|
|data>>cost|支出|是|[string]|0|
|data>>draw_quantity|领取数|是|[string]|0|
|data>>exchange_quantity|兑换数|是|[string]|0|
|data>>exchange_rate|兑换率|是|[string]|15|
|data>>sales_amount|活动总销售额|是|[string]|0|
|data>>sales_volume|活动总销量|是|[string]|0|
|data>>promotion_start_time|活动开始时间【站点时间】|是|[string]|2022-10-14 14:16:48|
|data>>promotion_end_time|活动结束时间【站点时间】|是|[string]|2022-10-14 14:17:01|
|data>>first_sync_time|首次同步时间【站点时间】|是|[string]|2022-10-14 14:17:34|
|data>>last_sync_time|最后同步时间【站点时间】|是|[string]|2022-10-14 14:17:37|
|data>>remark|备注|是|[string]|remark|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "067547ee9d7b437d8247d0117bbb3234.1694486464787",
    "response_time": "2023-09-12 10:41:06",
    "total": 2553,
    "data": [
        {
            "name": "表示価格より ¥11 OFF c23085",
            "sid": 31,
            "currency_icon": "JP¥",
            "origin_status": "FAILED",
            "discount": "JP¥11.00",
            "budget": "JP¥10084.0",
            "cost": "0.00",
            "draw_quantity": "0",
            "exchange_quantity": "0",
            "exchange_rate": "0.00",
            "sales_amount": "0.00",
            "sales_volume": "0",
            "promotion_start_time": "2023-04-08 00:00:00",
            "promotion_end_time": "2023-04-09 00:00:00",
            "first_sync_time": "2023-08-22 11:30:27",
            "last_sync_time": "2023-08-22 11:30:27",
            "remark": ""
        }
    ]
}
```

