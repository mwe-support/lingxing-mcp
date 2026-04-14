# 查询请款池 - 货款月结

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/inbound/list` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
|:-----------|:-----------------------------------------------------------|:---|:-------|:----------|
|pay_status|状态：<br>0 未申请<br />10 已申请<br />20 已付清|否|[string]|0|
|time_field|时间搜索类型：<br>create_time 入库时间<br />prepay_time 应付款日|否|[string]|create_time|
|start_time|开始时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|end_time|结束时间【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d|否|[string]|2024-07-25|
|search_field|搜索类型：<br>order_sn 入库单号<br />purchase_order_sn 采购单号<br />sku SKU|否|[string]|order_sn|
|search_value|搜索值|否|[string]|IB240725029|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限200|否|[int]|20|

## 请求示例
```
{
    "pay_status": 0,
    "time_field": "create_time",
    "start_time": "2024-07-25",
    "end_time": "2024-07-25",
    "search_field": "order_sn",
    "search_value": "IB240725029",
    "offset": 0,
    "length": 20
}
```

## 返回结果
Json Object

|参数名|说明|必填|类型|示例|
|:---------------------------|:---------------|----|:-------|:---------------------------------------------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|77ac259a67d5462594c83b80669b6eae.1692331008758|
|response_time|响应时间|是|[string]|2023-08-18 11:56:49|
|total|总数|是|[int]|127|
|data|响应数据|是|[array]||
|data>>supplier_id|供应商id|是|[string]|264|
|data>>supplier_name|供应商|是|[string]|ANT供应商|
|data>>purchase_order_sn|采购单号|是|[string]|PO220725001|
|data>>purchaser_id|采购方ID|是|[string]|12|
|data>>purchaser_name|采购方名称|是|[string]|ANT|
|data>>order_sn|入库单号|是|[string]|IB220725003|
|data>>wid|仓库id|是|[string]|1|
|data>>ware_house_name|仓库名字|是|[string]|拉美仓|
|data>>opt_time|入库时间|是|[string]|2022-06-25 11:02:25|
|data>>name|结算账期|是|[string]|入库后付款|
|data>>prepay_date|应付款日|是|[string]|2023-06-30|
|data>>pay_status|状态：<br>0 未申请<br />10 已申请<br />20 已付清|是|[int]|未申请|
|data>>pay_status_text|状态说明|是|[string]|0|
|data>>request_funds_type|请款维度：<br />0 - <br />1 采购单维度<br />2 产品维度<br />3 入库单维度|是|[int]|0|
|data>>quantity_total|采购量|是|[string]|1000|
|data>>order_product_total|入库量|是|[string]|7|
|data>>amount_total|采购金额|是|[string]|34000.000000|
|data>>order_amount|到货金额|是|[string]|70.00|
|data>>request_funds_amount|请款金额|是|[string]|0.000000|
|data>>request_funds_discount|折扣金额|是|[string]|70.00|
|data>>not_apply_amount|未申请金额|是|[string]|0.00|
|data>>req_funds_order_sn|请款单号|是|[string]|RF230719003|
|data>>opt_uid|入库人id|是|[string]|1|
|data>>opt_realname|入库人姓名|是|[string]|jack|
|data>>cg_user|采购员|是|[string]|riry|

## 返回示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "43cb2911449f4074b17acb8ec5989492.1695206632110",
    "response_time": "2023-09-20 18:44:44",
    "data": [
        {
            "supplier_id": 226,
            "supplier_name": "ANT供应商",
            "purchase_order_sn": "PO220714001",
            "purchaser_id": 5,
            "purchaser_name": "ANT",
            "order_sn": "IB220714001",
            "order_id": "1_IB220714001",
            "wid": "91",
            "ware_house_name": "ANT仓库",
            "opt_time": "2022-07-14 14:12:06",
            "name": null,
            "prepay_date": "",
            "pay_status": 20,
            "pay_status_text": "已付清",
            "request_funds_type": 1,
            "quantity_total": 10,
            "order_product_total": "10",
            "amount_total": "10000.000000",
            "request_funds_amount": "0.000000",
            "request_funds_discount": "0.000000",
            "not_apply_amount": "10000.00",
            "req_funds_order_sn": "RF220714001",
            "opt_uid": 128768,
            "opt_realname": null,
            "cg_user": "jack"
        }
    ],
    "total": 1877
}
```