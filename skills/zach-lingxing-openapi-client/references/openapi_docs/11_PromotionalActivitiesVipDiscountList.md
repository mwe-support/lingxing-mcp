# 查询促销活动列表-会员折扣/价格折扣

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/promotionalActivities/vipDiscount/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名     | 说明                                                         | 必填 | 类型     | 示例       |
| :--------- | :----------------------------------------------------------- | :--- | :------- | :--------- |
| start_date | 开始日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-11-23 |
| end_date   | 结束日期【活动时间】，站点时间，闭区间，格式：Y-m-d，时间间隔最长不超过90天 | 否   | [string] | 2021-12-20 |
| sids | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [array]  | [102,144]  |
| offset | 分页偏移量，默认0  | 否   | [int]    | 0  |
| length | 分页长度，默认20，上限200  | 否   | [int] | 20  |

## 返回结果

Json Object

| 参数名                     | 说明                                                         | 必填 | 类型     | 示例                                           |
| :------------------------- | :----------------------------------------------------------- | :--- | :------- | :--------------------------------------------- |
| code    | 状态码，0 成功  | 是   | [int]    | 0  |
| message  | 消息提示  | 是   | [string] | success  |
| error_details  | 错误信息  | 是   | [array]  |  |
| request_id | 请求链路id  | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time| 响应时间  | 是   | [string] | 2023-08-18 11:56:49                            |
| total | 总数 | 是   | [int]    | 200   |
| data | 响应数据 | 是   | [array]  | |
|data>>promotion_id|促销活动id|是|[string]||
| data>>name | 折扣名称 | 是   | [string] | Ciwete Stainless Steel Kitchen Cookware Set    |
| data>>product_quantity | 商品数量 | 是   | [int]    | 128 |
| data>>sid | 店铺id | 是   | [int]    | 2 |
| data>>currency_icon | 货币icon | 是   | [string] | JP¥  |
| data>>customer_target | 消费群体类型 PRIME_EXCLUSIVE会员折扣 ALL CUSTOMERS价格折扣 | 是 | [string] |  |
| data>>origin_status | 活动状态：<br />ACTIVE 进行中 <br/>CANCELED 已取消<br/> EXPIRED 已过期<br/>AWAITTING 待上传商品<br/>SCHEDULED 已计划<br/> NEEDS ATTENTION 需要注意<br/>ENDED 已结束 | 是   | [string] | SCHEDULED                                      |
| data>>promotion_start_time | 活动开始时间【站点时间】| 是   | [string] | 2021-06-21 00:00:00 |
| data>>promotion_end_time | 活动结束时间【站点时间】 | 是   | [string] | 2021-06-27 23:59:00 |
| data>>first_sync_time | 首次同步时间【站点时间】 | 是   | [string] | 2022-10-11 10:17:26 |
| data>>last_sync_time | 最后同步时间【站点时间】| 是   | [string] | 2022-10-11 10:17:26 |
| data>>update_time | 更新时间【站点时间】| 是   | [string] | 11/14/22 11:22 PM |
| data>>remark | 备注 | 是   | [string] |  |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "dcdeafab005642a684944a207b8692aa.1694589378015",
    "response_time": "2023-09-13 15:16:19",
    "data": [
        {
            "name": "11_14_17_13",
            "sid": 32,
            "currency_icon": "$",
            "origin_status": "EXPIRED",
            "product_quantity": 0,
            "promotion_start_time": "2022-11-15 00:00:00",
            "promotion_end_time": "2022-11-16 23:59:00",
            "first_sync_time": "2023-04-26 13:03:22",
            "last_sync_time": "2023-04-26 13:03:22",
            "update_time":"11/14/22 11:22 PM"
            "remark": ""
        }
    ],
    "total": 1
}
```

