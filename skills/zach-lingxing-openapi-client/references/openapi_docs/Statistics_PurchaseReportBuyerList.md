# 查询采购报表列表 - 采购员

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/report/purchase/buyer/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名       | 说明                                                      | 必填 | 类型     | 示例       |
| :----------- | :-------------------------------------------------------- | :--- | :------- | :--------- |
| offset       | 分页偏移量，默认0                                         | 否   | [int] |0|
| length       | 分页长度，默认20，上限200                                 | 否   | [int] |20|
| start_date   | 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否   | [string] |2023-05-01|
| end_date     | 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否   | [string] |2023-07-30|
| time_type    | 时间类型：1 下单时间，2 到货时间                          | 否   | [int] |1|
| product_type | 产品类型：<br/>1 普通产品<br />2 组合产品<br />3 辅料       | 否   | [array]  |[1,2,3]|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "start_date": "2023-05-01",
    "end_date": "2023-07-30",
    "time_type": 1,
    "product_type": [1,2,3]
}
```

## 返回结果
Json Object

| 参数名                       | 说明                 | 必填 | 类型     | 示例                                           |
| :--------------------------- | :------------------- | ---- | :------- | :--------------------------------------------- |
| code                         | 状态码，0 成功       | 是   | [int]    | 0                                              |
| message                      | 消息提示             | 是   | [string] | success                                        |
| error_details                | 错误信息             | 是   | [array]  |                                                |
| request_id                   | 请求链路id           | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time                | 响应时间             | 是   | [string] | 2023-08-18 11:56:49                            |
| total                        | 总数                 | 是   | [int]    | 200                                            |
| data                         | 响应数据             | 是   | [array]  |                                                |
| data>>buyer_name             | 采购员               | 是   | [string] | 管理员                                         |
| data>>warehouse_name         | 仓库名称             | 是   | [array]  | ["仓库s1","仓库k2"]                              |
| data>>purchase_quantity      | 采购量               | 是   | [string] | 2672442                                        |
| data>>receive_quantity       | 到货量               | 是   | [string] | 2661838                                        |
| data>>wait_quantity          | 待到货量             | 是   | [string] | 10604                                          |
| data>>good_quantity          | 良品量               | 是   | [string] | 2658361                                        |
| data>>bad_quantity           | 次品量               | 是   | [string] | 5                                              |
| data>>return_quantity        | 退货量               | 是   | [string] | 0                                              |
| data>>purchase_amount        | 订单金额             | 是   | [string] | 291817.77                                      |
| data>>receive_amount         | 到货金额             | 是   | [string] | 51.25                                          |
| data>>wait_amount            | 待到货金额           | 是   | [string] | 291766.52                                      |
| data>>return_amount          | 退货金额             | 是   | [string] | 0.00                                           |
| data>>bad_rate               | 次品率               | 是   | [string] | 0.02%                                         |
| data>>return_rate            | 退货率               | 是   | [string] | 0.05%                                         |
| data>>overdue_quantity       | 逾期数量             | 是   | [string] | 7490                                           |
| data>>overdue_time           | 逾期时长             | 是   | [string] | 6882天9小时                                    |
| data>>overdue_quantity_rate  | 逾期率（按采购量）   | 是   | [string] | 68.79%                                          |
| data>>overdue_time_avg       | 平均逾期时长         | 是   | [string] | 132天9小时                                     |
| data>>overdue_order_rate     | 逾期率（按采购单量） | 是   | [string] | 3.64%                                      |
| data>>overdue_order_quantity | 逾期采购单量         | 是   | [string] | 21                                             |
| data>>order_time_avg         | 平均下单时长         | 是   | [string] | 14天10小时                                     |
| data>>order_count            | 采购单量             | 是   | [string] | 20                                             |
| data>>exchange_quantity      | 换货量               | 是   | [string] | 200                                            |

## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "92b00b822f38428a8843f0a41a62d622.1693033850439",
    "response_time": "2023-08-26 15:10:50",
    "data": [
        {
            "buyer_name": "",
            "warehouse_name": [
                "仓库1",
                "仓库11"
            ],
            "purchase_quantity": 3178633,
            "receive_quantity": 2233411,
            "wait_quantity": 900422,
            "good_quantity": 1190696,
            "bad_quantity": 0,
            "return_quantity": 1008,
            "purchase_amount": "55671760.21",
            "receive_amount": "39211989.32",
            "wait_amount": "15049368.74",
            "return_amount": "26939.65",
            "bad_rate": "0.00%",
            "return_rate": "0.05%",
            "overdue_quantity": 64008,
            "overdue_time": "21658天12小时",
            "overdue_quantity_rate": "2.01%",
            "overdue_time_avg": "65天16小时",
            "overdue_order_rate": "3.64%",
            "overdue_order_quantity": 12,
            "order_time_avg": "4天19小时",
            "order_count": 331,
            "exchange_quantity": 0
        }
    ],
    "total": 53
}
```