# 查询请款池 - 货款预付款

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/prepay/list` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
|:-----------|:-----------------------------------------------------------|:---|:-------|:-----------|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限200|否|[int]|20|
|pay_status|支付状态：<br> 0  未申请<br />1  已申请<br />2  部分付款<br />3  已付清|否|[string]|3|
|start_time|开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-23|
|end_time|结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|time_field|时间搜索类型：<br>create_time  创建时间|否|[string]|create_time|
|search_field|搜索类型：<br>purchase_order_sn  采购单号<br />order_sn  预付款单号|否|[string]|order_sn|
|search_value|搜索值|否|[string]|PRE240724001|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "pay_status": 3,
    "start_time": "2024-07-23",
    "end_time": "2024-07-25",
    "time_field": "create_time",
    "search_field": "order_sn",
    "search_value": "PRE240724001"
}
```

## 返回结果
Json Object

|参数名|说明|必填|类型|示例|
|:----------------------|:-----------------------------------------------------------|----|:-------|:---------------------------------------------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|77ac259a67d5462594c83b80669b6eae.1692331008758|
|response_time|响应时间|是|[string]|2023-08-18 11:56:49|
|total|总数|是|[int]|127|
|data|响应数据|是|[array]||
|data>>purchase_order_sn|采购单号|是|[string]|PO211214006|
|data>>order_sn|预付款单号|是|[string]|RRE211221004|
|data>>custom_order_sn|自定义采购单号|是|[string]|PO230731002|
|data>>purchaser_id|采购方ID|是|[string]|4|
|data>>purchaser_name|采购方名称|是|[string]|采购公司456|
|data>>supplier_name|供应商名称|是|[string]|供应商1|
|data>>create_time|创建时间|是|[string]|2021-12-21 15:07:24|
|data>>pay_status|付款状态：<br> 0  未申请<br />1  已申请<br />2  部分付款<br />3  已付清|是|[int]|0|
|data>>pay_status_text|付款状态文本|是|[string]|未申请|
|data>>quantity_total|采购量|是|[string]|12|
|data>>amount_total|采购货值|是|[string]|343.00|
|data>>prepay_percent|预付比例|是|[string]|0.10|
|data>>currency|币种|是|[string]|CNY|
|data>>currency_icon|币种符号|是|[string]|￥|
|data>>payable_amount|应预付货值|是|[string]|34.30|
|data>>discount|折扣金额|是|[string]|0.00|
|data>>paid_fee|已付金额|是|[string]|0.00|
|data>>unpaid_fee|未付金额|是|[string]|34.30|
|data>>purchase_user|采购员|是|[string]|jack|

## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [
        
    ],
    "request_id": "8a4977a9a3954f4482c9699161659c02.1695264916126",
    "response_time": "2023-09-21 10:55:17",
    "data": [
        {
            "purchase_order_sn": "PO220714001",
            "order_sn": "PRE220714001",
            "custom_order_sn": "PO220714001",
            "purchaser_id": "5",
            "purchaser_name": "ANT",
            "supplier_name": "ANT供应商",
            "create_time": "2022-07-14 14:11:51",
            "pay_status": 0,
            "pay_status_text": "未申请",
            "quantity_total": "10",
            "amount_total": "10000.00",
            "prepay_percent": "10.00",
            "currency": "USD",
            "currency_icon": "$",
            "payable_amount": "1000.00",
            "discount": "0.00",
            "paid_fee": "0.00",
            "unpaid_fee": "1000.00",
            "apply_fee": "0.00",
            "unapply_fee": "1000.00",
            "purchase_user": "jack"
        }
    ],
    "total": 34
}
```

## 附加说明：
1. time_field start_time end_time 必须同时填写或者都不填