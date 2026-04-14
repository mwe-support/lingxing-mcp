# 查询请款池-其他应付款
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/customFee/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0| 否   | [int]    | 0 |
|length|分页长度，默认20，上限200| 否   | [int]    | 20 |
|pay_status|支付状态【多个状态用英文逗号分隔】：<br />0 未申请<br />1 已申请<br />2 部分付款<br />3 已付清|否|[string]|3|
|search_field_time|时间搜索类型：<br />create_time   创建时间  <br />close_time     付清时间|否|[string]|create_time|
|start_time|开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-23|
|end_time|结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|search_field|搜索类型：<br />business_sn   费用单号<br />custom_fee_sn   其他应付单号|否|[string]|business_sn|
|search_value|搜索值|否|[string]|FY240703000001|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "pay_status": 3,
    "start_time": "2024-07-23",
    "end_time": "2024-07-25",
    "search_field_time": "create_time",
    "search_field": "business_sn",
    "search_value": "FY240703000001"
}
```

## 返回结果

Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 状态码，0 成功  | 是   | [int]    | 0 |
| message | 消息提示  | 是   | [string] | success |
| error_details | 错误信息  | 是   | [array]  |  |
| request_id | 请求链路id | 是   | [string] | 77ac259a67d5462594c83b80669b6eae.1692331008758 |
| response_time  | 响应时间 | 是   | [string] | 2023-08-18 11:56:49 |
| total | 总数 | 是   | [int]    | 127 |
| data | 响应数据 | 是   | [array]  |  |
|data>>custom_fee_sn|其他应付单号|是|[string]|QT221112002|
|data>>business_sn|费用单号|是|[string]|FY20221112000011|
|data>>object_id|应付对象id|是|[string]|301358744661164540|
|data>>object_name|应付对象名称|是|[string]|talk name|
|data>>pay_status|支付状态：<br />0 未申请<br />1 已申请<br />2 部分付款<br />3 已付清|是|[int]|1|
|data>>pay_status_text|支付状态说明|是|[string]|已申请|
|data>>fee_type_id| 应付费用类型id  | 是   | [string] | 304245167537685000 |
|data>>fee_type_text| 应付费用说明  | 是   | [string] | 其他费1  |
|data>>currency|币种|是|[string]|JPY|
|data>>fee|应付金额|是|[string]|32.00|
|data>>paid_fee|已付金额|是|[string]|0.00|
|data>>unpaid_fee|未付金额|是|[string]|32.00|
|data>>apply_fee|申请中金额|是|[string]|20.00|
|data>>unapply_fee|未申请金额|是|[string]|12.00|
|data>>create_uid|创建人id|是|[string]|1|
|data>>create_user|创建人名称|是|[string]|0超级管理员22222|
|data>>create_time|创建时间|是|[string]|2022-11-12 14:47:18|
|data>>applying_orders|申请中关联单据|是|[array]| |
|data>>applying_orders>>order_sn|请款单号|是|[string]| create_uid |
|data>>applying_orders>>status|请款单状态|是|[int]| 2 |
|data>>applying_orders>>status_text|请款单状态说明|是|[string]| 已说明 |
|data>>applying_orders>>apply_username|申请人名称|是|[string]| 管理员 |
|data>>applying_orders>>apply_amount|申请金额|是|[string]| 10.00 |
|data>>applying_orders>>apply_time|申请时间|是|[string]| 2023-09-21 16:57:13 |
|data>>applying_orders>>currency_icon|币种|是|[string]| $ |
|data>>applying_orders>>type|请款单标识|是|[string]| 1 |
|data>>paid_orders|已付关联单据|是|[array]| |
|data>>paid_orders>>order_sn| 请款单号| 是   | [string] | RF230921002 |
|data>>paid_orders>>status_text| 请款单状态：<br> 1 待付款<br>2 已完成<br>3 已作废<br>121 待审批<br>122 已驳回<br>124 已作废（审批） | 是   | [string] | 2 |
|data>>paid_orders>>apply_username| 申请人名称 | 是   | [string] | 张三 |
|data>>paid_orders>>apply_amount| 申请金额 | 是   | [string] | 10.23 |
|data>>paid_orders>>apply_time| 申请时间 | 是   | [string] | 2023-10-10 00:00:00  |
|data>>paid_orders>>currency_icon| 币种 | 是   | [string] | $ |
|data>>paid_orders>>type| 请款单标识  | 是  | [string] | 1 |

## 返回成功示例

```

{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "f2336a34d32f475ab38ad5461e47f3af.100.16966502275823543",
    "response_time": "2023-10-07 11:43:49",
    "data": [
        {
            "custom_fee_sn": "QT230921002",
            "business_sn": "FY230921000002",
            "object_id": "301358744661164544",
            "object_name": "jack name",
            "pay_status": 3,
            "pay_status_text": "已付清",
            "fee_type_id": "304297072910827520",
            "currency": "USD",
            "fee": "10.00",
            "paid_fee": "10.00",
            "apply_fee": "0.00",
            "create_uid": "1",
            "fee_type_text": "其他费1",
            "create_time": "2023-09-21 16:56:45",
            "create_user": "0超级管理员01",
            "unpaid_fee": "0.00",
            "unapply_fee": "0.00",
            "applying_orders": [],
            "paid_orders": [
                {
                    "order_sn": "RF230921002",
                    "status_text": "已完成",
                    "status": "2",
                    "apply_username": "0超级管理员01",
                    "apply_amount": "10.00",
                    "apply_time": "2023-09-21 16:57:13",
                    "currency_icon": "$",
                    "type": "1"
                }
            ]
        }
    ],
    "total": 2
}
```

