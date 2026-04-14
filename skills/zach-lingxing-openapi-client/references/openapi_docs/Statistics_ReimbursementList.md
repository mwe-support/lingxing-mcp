# 查询亚马逊赔偿报告列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/mwsReport/reimbursementList` | HTTPS | POST | 1 |

## 请求参数

| 参数名      | 说明   | 必填 |  类型 | 示例   |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| offset            | 分页偏移量，默认0       | 否  | [int]    |0|
| length            | 分页长度，默认20，上限200 | 否  | [int]    |20|
| search_field      | 搜索字段：<br>reimbursement_id 赔偿编号<br />amazon_order_id 订单号<br />asin ASIN<br />msku MSKU<br />fnsku FNSKU<br />item_name 标题 | 否   | [string] |asin|
| search_value      | 搜索值                     | 否   | [string] |B0BB389BKQ|
| sids              | 店铺id，多个使用英文逗号分割 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [string] |109|
| start_date        | 批准日期开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否 | [string] |2023-06-01|
| end_date          | 批准日期结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否 | [string] |2023-06-30|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "search_field": "asin",
    "search_value": "B0BB389BKQ",
    "sids": "109",
    "start_date": "2023-06-01",
    "end_date": "2023-06-30"
}
```

## 返回结果
Json Object

| 参数名                                     | 说明 | 必填 | 类型                                                         | 示例   |
| ------------------------------------------ | ---------- | ------------------------------------------------------------ | ------ | ------ |
| code                                | 状态码，0 成功     | 是    | [int]    | 0 |
| message                             | 提示信息           | 是          | [string] | success |
| error_details                       | 错误信息           | 是          | [array]  |      |
| request_id                          | 请求链路id             | 是            | [string] | 600cb4e475ec460ea18eaca36ddf9c7c.1692091237061 |
| response_time                       | 响应时间 | 是 | [string] | 2023-08-15 17:20:37 |
| total                               | 总数 | 是 | [int]    | 200 |
| data                                | 响应数据 | 是 | [array]  |        |
| data>>sid                           | 店铺id           | 是          | [int] | 1 |
| data>>approval_date                 | 批准日期【站点时间】 | 是 | [string] | 2021-08-06T08:07:45+00:00 |
| data>>approval_date_locale          | 批准日期【北京时间】 | 是 | [string] | 2021-08-06 |
| data>>reimbursement_id              | 赔偿编号           | 是          | [string] | 2221094461 |
| data>>case_id                       | 问题编号           | 是          | [string] |  |
| data>>amazon_order_id               | 亚马逊订单号       | 是      | [string] | 111-8056674-6381837 |
| data>>reason                        | 原因               | 是              | [string] | Reimbursement_Reversal |
| data>>msku                          | MSKU            | 是           | [string] | MSKU6B40E65 |
| data>>fnsku                         | FNSKU       | 是      | [string] | FND0456B4 |
| data>>asin                          | ASIN            | 是           | [string] | B0ABCABCAB |
| data>>item_name          | 标题          | 是         | [string] | lingxing amazon product title E1 |
| data>>condition                     | 状况               | 是              | [string] | NewItem |
| data>>currency_unit                 | 币种               | 是              | [string] | USD |
| data>>amount_per_unit               | 每件商品赔偿金额   | 是  | [string] | 10.000000 |
| data>>amount_total                  | 总金额             | 是            | [string] | 10.000000 |
| data>>quantity_reimbursed_cash      | 赔偿数量（现金）   | 是  | [int] | 1 |
| data>>quantity_reimbursed_inventory | 赔偿数量（库存）   | 是  | [int] | 2 |
| data>>quantity_reimbursed_total     | 赔偿数量（总计）   | 是  | [int] | 1 |
| data>>original_reimbursement_id     | 原始赔偿编号       | 是      | [string] | 7399587871 |
| data>>original_reimbursement_type   | 赔偿类型       | 是      | [string] | CustomerReturn |

## 返回示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "3288221c85594cc19ccfc5b78271a106.1693188677770",
    "response_time": "2023-08-28 10:11:18",
    "total": 1,
    "data": [
        {
            "sid": 2,
            "approval_date": "2021-08-21T12:18:36+00:00",
            "approval_date_locale": "2021-08-21",
            "reimbursement_id": "8121901951",
            "case_id": "",
            "amazon_order_id": "111-8056674-6381837",
            "reason": "Reimbursement_Reversal",
            "msku": "MSKU930D2FB",
            "fnsku": "FN14E7B48",
            "asin": "B0ABC74351",
            "item_name": "lingxing amazon product title A1DD4657FB",
            "condition": "NewItem",
            "currency_unit": "USD",
            "amount_per_unit": "10.110000",
            "amount_total": "10.110000",
            "quantity_reimbursed_cash": 1,
            "quantity_reimbursed_inventory": 1,
            "quantity_reimbursed_total": 0,
            "original_reimbursement_id": "7302313601",
            "original_reimbursement_type": "Damaged_Warehouse"
        }
    ]
}
```
