# 查询亚马逊源报表-盘存记录

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/mwsReport/adjustmentList` | HTTPS | POST | 1 |

## 请求参数

| 参数名            | 说明                                                         | 必填 | 类型     | 示例        |
| :---------------- | :----------------------------------------------------------- | :--- | :------- | :---------- |
| offset            | 分页偏移量，默认0                                            | 是   | [int]    | 0           |
| length            | 分页长度，默认20，上限10000                               | 是   | [int]    | 20          |
| sids | 店铺id，多个店铺以英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否 | [string] |1,2,109|
| search_field      | 搜索的字段：<br>asin ASIN<br />msku MSKU<br />fnsku FNSKU<br />item_name 标题<br />transaction_item_id 交易编号 | 否   | [string] |msku|
| search_value      | 搜索值                                                     | 否   | [string] |Black_ Head_Rop|
| start_date        | 发货日期开始时间【闭区间】，格式Y-m-d【report_date】          | 是   | [string] |2022-08-01|
| end_date          | 发货日期结束时间【闭区间】，格式Y-m-d【report_date】                 | 是   | [string] |2024-08-01|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "sids": "1,2,109",
    "search_field": "msku",
    "search_value": "Black_ Head_Rop",
    "start_date": "2022-08-01",
    "end_date": "2024-08-01"
}
```
## 返回结果
Json Object

| 参数名                      | 类型     | 描述                | 示例                                           |
| :-------------------------- | :------- | :------------------ | :--------------------------------------------- |
| code                        | [int]    | 状态码，0 成功      | 0                                              |
| message                     | [string] | 响应信息            | success                                        |
| error_details               | [array]  | 错误信息            |                                                |
| request_id                  | [string] | 请求链路id          | ed675502579045e1b41c951a69423b44.1692156385098 |
| response_time               | [string] | 响应时间            | 2023-08-16 11:26:25                            |
| total                       | [int]    | 总数                | 2                                              |
| data                        | [array]  | 响应数据            |                                                |
| data>>sid                   | [int]    | 店铺id              | 1                                              |
| data>>report_date           | [string] | 发货日期，格式Y-m-d | 2018-06-19                                     |
| data>>transaction_item_id   | [string] | 交易编号            | 32136404780                                    |
| data>>fnsku                 | [string] | FNSKU               | X00146ASDW                                     |
| data>>msku                  | [string] | MSKU                | KT08A1ASD345R                                  |
| data>>item_name             | [string] | 标题                | lingxing amazon product title                  |
| data>>fulfillment_center_id | [string] | 运营中心code        | MSP1                                           |
| data>>quantity              | [int]    | 数量                | 1                                              |
| data>>reason                | [string] | 原因code            | N                                              |
| data>>reason_text           | [string] | 原因                | Transfer from holding account                  |
| data>>disposition           | [string] | 库存属性            | SELLABLE                                       |

## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "67e595d6b0a24214a19fb3def13a01fc.1692932840766",
    "response_time": "2023-08-25 11:07:22",
    "data": [
        {
            "sid": 3,
            "report_date": "2019-05-01",
            "transaction_item_id": "38837449998",
            "fnsku": "FN5ASDEFF",
            "msku": "MSKU4GRW345",
            "item_name": "lingxing amazon product title 2",
            "fulfillment_center_id": "AKS1",
            "quantity": 5,
            "reason": "M",
            "disposition": "SELLABLE",
            "reason_text": "Inventory misplaced"
        },
        {
            "sid": 3,
            "report_date": "2019-05-01",
            "transaction_item_id": "38837561234",
            "fnsku": "AFEFRGTTT",
            "msku": "MSKU4GRW344",
            "item_name": "lingxing amazon product title 1",
            "fulfillment_center_id": "AKS1",
            "quantity": 1,
            "reason": "F",
            "disposition": "SELLABLE",
            "reason_text": "Inventory found"
        }
    ],
    "total": 168511
}
```