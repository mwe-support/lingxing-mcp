# 查询请款池 - 货款现结

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/purchase/list` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
|:------------|:------------|:------------|:------------|:------------|
|pay_status|支付状态【多个使用英文逗号分隔】：<br>0 未申请<br />1 已申请<br />2 部分付款<br />3 已付清|否|[string]|0,1|
|time_field|时间搜索类型：<br>create_time 创建时间|否|[string]|create_time|
|start_time|开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|end_time|结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|search_field|搜索类型：<br>sku SKU<br />order_sn 采购单号|否|[string]|order_sn|
|search_value|查询值|否|[string]|PO240725048|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限200|否|[int]|20|

## 请求示例
```
{
    "pay_status": "0,1",
    "time_field": "create_time",
    "start_time": "2024-07-25",
    "end_time": "2024-07-25",
    "search_field": "order_sn",
    "search_value": "PO240725048",
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

|参数名|说明|必填|类型|示例|
|:------------------------------------|:--------------------------------------|----|:-------|:---------------------------------------------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|77ac259a67d5462594c83b80669b6eae.1692331008758|
|response_time|响应时间|是|[string]|2023-08-18 11:56:49|
|total|总数|是|[int]|127|
|data|响应数据|是|[array]||
|data>>supplier_id|供应商ID|是|[string]|330|
|data>>supplier_name|供应商名称|是|[string]|委外供应商|
|data>>purchase_order_id|采购单ID|是|[string]|4617|
|data>>order_sn|采购单号|是|[string]|PO230807011|
|data>>custom_order_sn|自定义单号|是|[string]|PO230807011|
|data>>purchase_type|采购类型：<br>1 普通采购<br>2 1688 采购|是|[int]|1|
|data>>shipping_icon|运费币种符号|是|[string]|￥|
|data>>other_icon|其他费用币种符号|是|[string]|￥|
|data>>purchase_icon|采购金额|是|[string]|￥|
|data>>purchase_currency|采购币种|是|[string]|CNY|
|data>>shipping_currency|运费币种|是|[string]|CNY|
|data>>other_currency|其他费用币种|是|[string]|CNY|
|data>>amount_total|货值|是|[string]|0.00|
|data>>other_fee|运费|是|[string]|0.00|
|data>>shipping_price|其他费用|是|[string]|0.00|
|data>>quantity_total|采购量|是|[string]|20|
|data>>quantity_entry|到货量|是|[string]|20|
|data>>in_stock_amounts|到货金额|是|[string]|0.00|
|data>>return_amounts|退货金额|是|[string]|0.00|
|data>>discount_amount|折扣金额|是|[string]|0.00|
|data>>payable_amount|应付金额|是|[string]|0.00|
|data>>amount_paid|实付金额|是|[string]|0.00|
|data>>amount_not_paid|未付金额|是|[string]|0.00|
|data>>purchase_amount|采购金额|是|[string]|0.00|
|data>>applying_amount|申请中金额|是|[string]|0.00|
|data>>not_apply_amount|未申请金额|是|[string]|0.00|
|data>>settlement_method|结算方式|是|[string]|现结|
|data>>create_username|创建人|是|[string]|张三|
|data>>create_time|创建时间|是|[string]|2023-08-07 19:15:45|
|data>>remark|备注|是|[string]|333|
|data>>request_funds_type|请款类型：<br>0 无<br >1 采购单<br >2 产品<br >3 入库单|是|[int]|0|
|data>>request_funds_type_text|请款类型文本|是|[string]|-|
|data>>purchaser_id|采购方ID|是|[string]|4|
|data>>purchaser_name|采购方名称|是|[string]|采购公司456|
|data>>status|状态：<br>-1 作废<br>0 待审核<br> - 草稿<br>1 待下单<br> - 已审核<br>2 待签收 <br>- 已下单<br>9 完成|是|[int]|9|
|data>>status_text|状态说明|是|[string]|已完成|
|data>>pay_status|请款状态：<br> 0 未申请<br>1 已申请<br>2 部分付款<br>3 已付款|是|[int]|3|
|data>>pay_status_text|请款状态说明|是|[string]|已付清|


## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "60c51fb0ec4d4d009f77e679d72c1252.1695194071872",
    "response_time": "2023-09-20 15:14:33",
    "total": 1266,
    "data": [
        {
            "supplier_id": "3453",
            "supplier_name": "hqf委外供应商",
            "purchase_order_id": "68646",
            "order_sn": "PO220714006",
            "custom_order_sn": "PO220714006",
            "purchase_type": 1,
            "shipping_icon": "￥",
            "other_icon": "￥",
            "purchase_icon": "￥",
            "purchase_currency": "CNY",
            "shipping_currency": "CNY",
            "other_currency": "CNY",
            "amount_total": "72.12",
            "other_fee": "0.00",
            "shipping_price": "0.00",
            "quantity_total": 10,
            "quantity_entry": 10,
            "in_stock_amounts": "72.12",
            "return_amounts": "0.00",
            "discount_amount": "0.00",
            "payable_amount": "72.12",
            "amount_paid": "0.00",
            "amount_not_paid": "72.12",
            "purchase_amount": "72.12",
            "applying_amount": "72.12",
            "not_apply_amount": "0.00",
            "settlement_method": "现结",
            "create_username": "0超级管理员01",
            "create_time": "2022-07-14 21:33:23",
            "remark": "",
            "request_funds_type": 1,
            "request_funds_type_text": "采购单",
            "purchaser_id": 1,
            "purchaser_name": "默认采购方",
            "status": 9,
            "status_text": "已完成",
            "pay_status": 1,
            "pay_status_text": "已申请"
        }
    ]
}
```