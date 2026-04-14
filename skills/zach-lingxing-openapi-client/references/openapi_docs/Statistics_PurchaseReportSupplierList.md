# 查询采购报表列表 - 供应商

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/report/purchase/supplier/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名       | 说明                                                      | 必填 | 类型     | 示例        |
| :----------- | :-------------------------------------------------------- | :--- | :------- | :---------- |
| offset       | 分页偏移量，默认0                                         | 否   | [int]    |0|
| length       | 分页长度，默认20，上限200                                 | 否   | [int]    |20|
| start_date   | 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否   | [string] |2023-06-01|
| end_date     | 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否   | [string] |2023-08-30|
| time_type    | 时间类型：<br/>1 下单时间<br />2 到货时间                   | 否   | [int]    |2|
| search_field | 搜索字段名：<br>order_no 单据号<br /> | 否   | [string] |order_no|
| search_value | 搜索值                                                    | 否   | [string] |1|
| product_type | 产品类型：<br/>1 普通产品<br />2 组合产品<br />3 辅料       | 否   | [array]  |[1,2,3]|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "start_date": "2023-06-01",
    "end_date": "2023-08-30",
    "time_type": 2,
    "search_field": "order_no",
    "search_value": "1",
    "product_type": [1,2,3]
}
```

## 返回结果
Json Object

| 参数名                       | 说明                      | 必填 | 类型     | 示例                                 |
| :--------------------------- | :------------------------ | ---- | :------- | :----------------------------------- |
| code                         | 状态码，0 成功            | 是   | [int]    | 0                                    |
| message                      | 消息提示                  | 是   | [string] | success                              |
| error_details                | 错误信息                  | 是   | [array]  |                                      |
| request_id                   | 请求链路id                | 是   | [string] | C3D9F541-8083-E376-EB5C-606A872F5C89 |
| response_time                | 响应时间                  | 是   | [string] | 2022-12-08 18:27:13                  |
| total                        | 总数                      | 是   | [int]    | 20                                   |
| data                         | 响应数据                  | 是   | [array]  |                                      |
| data>>supplier_name          | 供应商名称                | 是   | [string] | 供应商15                                     |
| data>>warehouse_name         | 仓库名称                  | 是   | [array]  | [北美仓,美国仓]                      |
| data>>buyer_name             | 采购员名称                | 是   | [array]  | [张三,tom]                           |
| data>>purchase_quantity      | 采购量                    | 是   | [string] | 2672442                              |
| data>>receive_quantity       | 到货量                    | 是   | [string] | 2661838                              |
| data>>wait_quantity          | 待到货量                  | 是   | [string] | 10604                                |
| data>>good_quantity          | 良品量                    | 是   | [string] | 2658361                              |
| data>>bad_quantity           | 次品量                    | 是   | [string] | 5                                    |
| data>>return_quantity        | 退货量                    | 是   | [string] | 0                                    |
| data>>total_amount           | 采购总金额                | 是   | [string] | 2057.50                              |
| data>>list>>shipping_fee     | 运费                      | 是   | [string] | 596.00                               |
| data>>list>>other_fee        | 其它费用                  | 是   | [string] | 0.00                                 |
| data>>purchase_amount        | 订单金额                  | 是   | [string] | 291817.77                            |
| data>>receive_amount         | 到货金额                  | 是   | [string] | 51.25                                |
| data>>wait_amount            | 待到货金额                | 是   | [string] | 291766.52                            |
| data>>return_amount          | 退货金额                  | 是   | [string] | 0.00                                 |
| data>>bad_rate               | 次品率                    | 是   | [string] | 0.02%                               |
| data>>return_rate            | 退货率                    | 是   | [string] | 0.05%                               |
| data>>order_count            | 采购单据量                | 是   | [string] | 12                                   |
| data>>overdue_quantity       | 逾期数量                  | 是   | [string] | 7490                                 |
| data>>overdue_time           | 逾期时长                  | 是   | [string] | 6882天9小时                          |
| data>>overdue_quantity_rate  | 逾期率（按采购量）        | 是   | [string] | 68.79%                                |
| data>>overdue_time_avg       | 平均逾期时长              | 是   | [string] | 132天9小时                           |
| data>>overdue_order_rate     | 逾期率（按采购单量）      | 是   | [string] | 3.85%                             |
| data>>overdue_order_quantity | 逾期采购单量              | 是   | [string] | 21                                   |
| data>>discount_amount        | 折扣金额                  | 是   | [string] | 0.00                                 |
| data>>payable_amount         | 应付金额                  | 是   | [string] | 639.20                               |
| data>>paid_amount            | 已付金额                  | 是   | [string] | 0.00                                 |
| data>>applying_amount        | 申请中金额                | 是   | [string] | 0.00                                 |
| data>>not_applied_amount     | 未申请金额                | 是   | [string] | 639.20                               |
| data>>unpaid_amount          | 未付金额                  | 是   | [string] | 639.20                               |
| data>>type_name              | 采购类型 【默认："汇总"】 | 是   | [string] | 汇总                                 |
| data>>order_sn               | 单据号【默认："汇总"】    | 是   | [string] | 汇总                                 |
| data>>exchange_quantity      | 换货量                    | 是   | [string] | 0                                    |

## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "d88a734bb9af465d8441b7b6b45572d7.1694156449975",
    "response_time": "2023-09-08 15:00:51",
    "total": 1 ,
    "data": [
        {
            "supplier_name": "供应商15",
            "warehouse_name": [
                "仓库1"
            ],
            "buyer_name": [],
            "purchase_quantity": "11575",
            "receive_quantity": "9560",
            "wait_quantity": "2015",
            "good_quantity": "4220",
            "bad_quantity": "0",
            "return_quantity": "0",
            "total_amount": "232057.50",
            "shipping_fee": "0.00",
            "other_fee": "0.00",
            "purchase_amount": "232057.50",
            "receive_amount": "187596.00",
            "wait_amount": "44461.50",
            "return_amount": "0.00",
            "bad_rate": "0.00%",
            "return_rate": "0.00%",
            "order_count": "1",
            "overdue_quantity": "0",
            "overdue_time": "-",
            "overdue_quantity_rate": "0.00%",
            "overdue_time_avg": "-",
            "overdue_order_rate": "0.00%",
            "overdue_order_quantity": "0",
            "discount_amount": "0.00",
            "payable_amount": "232057.50",
            "paid_amount": "0.00",
            "applying_amount": "0.00",
            "not_applied_amount": "232057.50",
            "unpaid_amount": "232057.50",
            "type_name": "汇总",
            "order_sn": "汇总",
            "exchange_quantity": "0"
        }
    ]
}
```