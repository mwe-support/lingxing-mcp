# 查询促销活动列表-管理促销
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/promotionalActivities/manage/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| start_date | 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-11-23 |
| end_date   | 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-12-20 |
| sids       | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [array]  | [102,144]  |
| offset     | 分页偏移量，默认0                                            | 否   | [int]    | 0          |
| length     | 分页长度，默认20，上限200                                    | 否   | [int]    | 20         |

## 返回结果

Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code                          | 状态码，0 成功                                               | 是   | [int]    | 0                                              |
| message                       | 消息提示                                                     | 是   | [string] | success                                        |
| error_details                 | 错误信息                                                     | 是   | [array]  |                                                |
| request_id                    | 请求链路id                                                   | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time                 | 响应时间                                                     | 是   | [string] | 2023-08-18 11:56:49                            |
| total                         | 总数                                                         | 是   | [int]    | 200                                            |
| data                          | 响应数据                                                     | 是   | [array]  |                                                |
|data>>promotion_id|促销活动id|是|[string]||
|data>>name|内部描述|是|[string]|Save $1 on swi... VPC-1-138675244 Coupon|
|data>>sid|店铺id|是|[int]|2|
|data>>promotion_type|活动类型：<br />3 买一赠一<br />4 购买折扣<br />5 一口价<br />8 社媒促销|是|[int]|4|
|data>>currency_icon|货币icon|是|[string]| |
|data>>origin_status|活动状态：<br />ACTIVE 进行中<br/>CANCELED 已取消<br/>EXPIRED 已过期<br/>PENDING 未开始|是|[string]|EXPIRED|
|data>>promotion_code|优惠码|是|[string]|不需要 |
|data>>sales_amount|活动总销售额|是|[string]|0|
|data>>sales_volume|活动总销量|是|[string]|0|
|data>>participate_condition|参与条件|是|[string]| At least this quantity of items\n80 |
|data>>participate_condition_num|参与条件数值|是|[string]|0|
|data>>buyer_gets|买家获得|是|[string]| Percent off\n1 |
|data>>buyer_gets_num|买家获得值|是|[string]|0|
|data>>purchase_product|需购买商品|是|[string]| 足球 |
|data>>discount_product|优惠商品|是|[string]| 计算机 |
|data>>exclude_product|排除商品|是|[string]| 遥控器 |
|data>>exchange_limit|是否限制兑换：<br>1 是<br />0 否|是|[int]|0|
|data>>promotion_start_time|活动开始时间【站点时间】|是|[string]|2022-08-26 02:00:00|
|data>>promotion_end_time|活动结束时间【站点时间】|是|[string]|2022-08-26 23:00:59|
|data>>first_sync_time|首次同步时间【站点时间】|是|[string]|2022-10-11 10:17:26|
|data>>last_sync_time|最后同步时间【站点时间】|是|[string]|2022-10-11 10:17:26|
|data>>remark|备注|是|[string]| ||

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "90930764718445a4af61b88a655ef10b.1694510506428",
    "response_time": "2023-09-12 17:21:47",
    "data": [
        {
            "name": "sss测试",
            "sid": 31,
            "promotion_type": 4,
            "currency_icon": "JP¥",
            "origin_status": "EXPIRED",
            "promotion_code": "不需要",
            "sales_amount": "0.00",
            "sales_volume": "0",
            "participate_condition": "At least this quantity of items\n80",
            "participate_condition_num": "80",
            "buyer_gets": "Percent off\n1",
            "buyer_gets_num": "1",
            "purchase_product": "测试1",
            "discount_product": "测试1",
            "exclude_product": "",
            "exchange_limit": "0",
            "promotion_start_time": "2023-01-10 10:00:00",
            "promotion_end_time": "2023-01-10 23:59:00",
            "first_sync_time": "2023-02-22 11:53:04",
            "last_sync_time": "2023-02-23 17:34:32",
            "remark": ""
        }
    ],
    "total": 1
}
```

