# 查询请款单列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFunds/order/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名  | 说明  | 必填 |  类型 | 示例   |
| :--------- |:----------| :---------- | :--------- | :---------- |
| offset | 分页偏移量，默认0   | 否 | [int]|0|
| length | 分页长度，默认20，上限200  | 否 |[int]|20|
| status | 状态：<br>1  待付款<br />2 已完成<br />3 已作废<br />121 待审批<br />122 已驳回<br />124 已作废 | 否 | [int] |1|
| search_field_time | 搜索时间类型：<br />apply_time 申请时间<br />real_pay_time 实际付款时间<br />prepay_time 预计付款时间| 否 |[string]| apply_time |
| start_date | 开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否 | [string] |2023-06-01|
| end_date | 结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d | 否 | [string] |2023-08-01|
| search_field | 搜索字段：purchase_order_sn 关联单据，order_sn  请款单号 | 否 | [string] |order_sn|
| search_value | 搜索值   | 否 | [string]|RF230801011|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "status": 1,
    "search_field_time": "apply_time",
    "start_date": "2023-06-01",
    "end_date": "2023-08-01",
    "search_field": "order_sn",
    "search_value": "RF230801011"
}
```

## 返回结果
Json Object

| 参数名   | 说明  | 必填 | 类型  | 示例   |
| ----------- |-----------| ---------- | ------ | ------ |
| code| 状态码，0 成功| 是 | [int] | 0 |
| message| 响应信息 | 是| [string] | success |
| error_details | 错误信息| 是| [array] | |
| request_id | 请求链路id   | 是   | [string] | xxxx.xxxx |
| response_time | 响应时间 | 是  | [string] | 2023-08-16 11:14:30 |
| total | 总数 | 是 | [int] | 113 |
| data | 响应数据 | 是 | [array] |  |
| data>>order_sn | 请款单号 | 是     | [string] | RF211027001 |
| data>>type | 费用类型：<br/>1 采购货款<br />2 物流款<br />3 采购预付款<br />4 其他应付款| 是 | [int] | 1 |
| data>>object_type | 付款对象类型 | 是  | [string] | 供应商 |
| data>>object_name | 付款对象名称 | 是  | [string] | 供应商10 |
| data>>payment_method | 支付方式 | 是  | [string] | 网银转账 |
| data>>icon | 币种符号 | 是   | [string] | ￥ |
| data>>amount_total | 付款金额 | 是    | [string] | 18000.00 |
| data>>amount_paid | 已付金额 | 是   | [string] | 11000.00 |
| data>>amount_unpaid | 未付金额 | 是 | [string] | 7000.00 |
| data>>prepay_time | 预计付款日期 | 是 | [string] | 2021-10-28 |
| data>>status | 状态：<br />1 待付款<br />2 已完成 <br />3 已作废<br />121 待审批<br />122 已驳回<br />124 审批流作废 | 是 | [int] | 2 |
| data>>apply_user | 申请人 | 是 | [string] | 管理员 |
| data>>remark | 申请备注 | 是 | [string] | 备注 |
| data>>apply_time | 申请时间 | 是 | [string] | 2022-07-14 14:17:28 |
| data>>pay_user | 实际付款人 | 是 | [string] | 管理员 |
| data>>real_pay_time | 实际付款日期 | 是 | [string] | 2022-07-14 |
| data>>items | 关联单号 | 是 | [array]  |  |
| data>>items>>business_sn | 业务单号 | 是 | [string] | PO220714001 |
| data>>items>>custom_order_sn | 自定义单号   | 是  | [string] | PO220714001 |
| data>>currency | 币种 | 是  | [string] | USD |
| data>>settlement_method | 结算方式  | 是 | [string] | 月结 |
| data>>sub_type | 子类型：<br />1  常规单据<br />2  1688 采购单 | 是 | [int] | 1 |
| data>>trade_method | 交易方式id | 是 | [string] | 0 |
| data>>trade_method_text  | 交易方式   | 是 | [string] | 先采后付 |
| data>>pay_currency | 付款币种 | 是 | [string] | USD |
| data>>pay_currency_icon | 付款币种符号 | 是 | [string] | $ |
| data>>pay_rate_type | 付款汇率类型：<br />1 付款指定汇率<br />2 请款指定汇率 | 是   | [int] | 1 |
| data>>pay_rate_type_text | 付款汇率类型 | 是 | [string] | 请款指定汇率 |
| data>>pay_rate | 付款汇率 | 是 | [string] | 0.0000 |
| data>>payer_id | 付款方 | 是 | [string] | 5 |
| data>>payer_name| 付款方名称 | 是 | [string] | ANT |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "b7849b32d3e44488a648994ee9bada63.1692946066602",
    "response_time": "2023-08-25 14:47:48",
    "total": 113 ,
    "data": [
        {
            "order_sn": "RF221114001",
            "type": 1,
            "object_type": "供应商",
            "object_name": "委外供应商",
            "payment_method": "网银转账",
            "icon": "￥",
            "amount_total": "72.12",
            "amount_paid": "0.00",
            "amount_unpaid": "72.12",
            "prepay_time": "2022-09-01",
            "status": 121,
            "apply_user": "管理员",
            "remark": "SFADSFDASDF",
            "apply_time": "2022-11-14 11:13:55",
            "pay_user": "申请人",
            "real_pay_time": "2022-09-21",
            "items": [
                {
                    "business_sn": "PO220714006",
                    "custom_order_sn": "PO220714006"
                }
            ],
            "currency": "CNY",
            "settlement_method": "现结",
            "sub_type": 1,
            "trade_method": "0",
            "trade_method_text": "",
            "pay_currency": "CNY",
            "pay_currency_icon": "￥",
            "pay_rate_type": 0,
            "pay_rate_type_text": "-",
            "pay_rate": "0.0000",
            "payer_id": "1",
            "payer_name": "默认采购方"
        }
    ]
}
```