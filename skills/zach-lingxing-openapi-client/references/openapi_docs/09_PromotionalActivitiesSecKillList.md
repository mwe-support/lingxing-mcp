# 查询促销活动列表-秒杀
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/promotionalActivities/secKill/list` | HTTPS | POST | 1 |

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
| code                        | 状态码，0 成功                                              | 是   | [int]    | 0                                              |
| message                     | 消息提示                                                    | 是   | [string] | success                                        |
| error_details               | 错误信息                                                    | 是   | [array]  |                                                |
| request_id                  | 请求链路id                                                  | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time               | 响应时间                                                    | 是   | [string] | 2023-08-18 11:56:49                            |
| total                       | 总数                                                        | 是   | [int]    | 200                                            |
| data                        | 响应数据                                                    | 是   | [array]  |                                                |
|data>>promotion_id|促销活动id|是|[string]||
|data>>name|秒杀标题|是|[string]| Ciwete Stainless Steel Kitchen Cookware Set    |
|data>>product_quantity|商品数量|是|[int]| 128 |
|data>>sid|店铺id|是|[int]|2|
|data>>currency_icon|货币icon|是|[string]| JP¥ |
|data>>origin_status|活动状态：<br> ACTIVE 进行中<br>CANCELED 已取消<br>EXPIRED 已过期<br> APPROVED 未开始<br>SUPPRESSED 需要注意<br>DISMISSED 禁止显示 <br>DRAFT 未定<br>ENDED 已结束|是|[string]|CANCELLED|
|data>>promotion_type|秒杀类型：<br />1 Best Deal<br />2  Lighting Deal|是|[int]|2|
|data>>description|描述|是|[string]| 秒杀-2021/03/10 2-19-52-682                    |
|data>>seckill_fee|秒杀费|是|[string]|0|
|data>>sales_amount|活动总销售额|是|[string]|1963.34|
|data>>sales_volume|活动总销量|是|[string]|0|
|data>>participate_inventory|参与库存数|是|[string]|0|
|data>>sold_rate|售出率|是|[string]|0|
|data>>page_view|浏览量|是|[string]|1490|
|data>>exchange_rate|转化率|是|[string]|0|
|data>>promotion_start_time|活动开始时间【站点时间】|是|[string]|2021-06-21 00:00:00|
|data>>promotion_end_time|活动结束时间【站点时间】|是|[string]|2021-06-27 23:59:00|
|data>>first_sync_time|首次同步时间【站点时间】|是|[string]|2022-10-11 10:17:26|
|data>>last_sync_time|最后同步时间【站点时间】|是|[string]|2022-10-11 10:17:26|
|data>>remark|备注|是|[string]| ||

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "7e2d4738c4954d9e9ea39db0220c79d5.1694503723804",
    "response_time": "2023-09-12 15:28:44",
    "data": [
        {
            "name": "Ciwete Stainless Steel Kitchen Cookware Set",
            "product_quantity": 2,
            "sid": 31,
            "currency_icon": "JP¥",
            "origin_status": "CANCELLED",
            "promotion_type": 2,
            "description": "秒杀-2021/03/10 2-19-52-682",
            "seckill_fee": "0.00",
            "sales_amount": "0.00",
            "sales_volume": "0",
            "participate_inventory": "19",
            "sold_rate": "0.00",
            "page_view": "0",
            "exchange_rate": "0.00",
            "promotion_start_time": "2021-06-21 07:00:00",
            "promotion_end_time": "2021-06-28 06:59:00",
            "first_sync_time": "2023-03-03 16:43:08",
            "last_sync_time": "2023-03-03 16:43:08",
            "remark": ""
        }
    ],
    "total": 1
}
```

