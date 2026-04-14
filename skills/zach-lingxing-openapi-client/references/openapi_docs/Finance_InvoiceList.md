# 查询广告发票列表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/ads/invoice/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认值0|否|[int]|0|
|length|分页大小，默认20|否|[int]|20|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[1,2,136,139]|
|mids|国家id|否|[array]|[1,2]|
|ads_type|广告类型：<br>SPONSORED PRODUCTS<br>SPONSORED DISPLAY<br>SPONSORED BRANDS<br>SPONSORED BRANDS VIDEO|否|[array]|["SPONSORED PRODUCTS"]|
|invoice_start_time|开始时间【发票开具时间】|是|[string]|2024-06-01|
|invoice_end_time|结束时间【发票开具时间】|是|[string]|2024-07-20|
|search_type|搜索类型：<br>ads_campaign【对应页面广告活动】<br>invoice_id【对应发票编号】<br>msku<br>asin|否|[string]|invoice_id|
|search_value|搜索值|否|[string]|TRF6K4FJN-1|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "sid": [
        1,
        2,
        136,
        139
    ],
    "mid": [
        1,
        2
    ],
    "ads_type": [
        "SPONSORED PRODUCTS"
    ],
    "invoice_start_time": "2024-06-01",
    "invoice_end_time": "2024-07-20",
    "search_type": "invoice_id",
    "search_value": "TRF6K4FJN-1"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|81CA6A9A-A5C4-8B5E-5FED-E1C2EC04753C|
|response_time|响应时间|是|[string]|2023-04-07 12:11:12|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>invoice_id|发票编号|是|[string]|CDLPWKJPR-64|
|data>>status|状态|是|[string]|PAID_IN_FULL|
|data>>payment_method|付款类型|是|[string]|UNIFIED_BILLING|
|data>>from_date|账单周期开始时间|是|[string]|2022-12-29|
|data>>to_date|账单周期结束时间|是|[string]|2023-01-03|
|data>>currency_icon|币种符号|是|[string]|€|
|data>>amount|账单金额|是|[number]|420.65|
|data>>cost_amount|花费|是|[number]|422.76|
|data>>tax_amount|税费|是|[number]|0|
|data>>other_allocation_fee|调整费|是|[number]|-2.11|
|data>>invoice_date|开具时间|是|[string]|2023-01-02|
|data>>sid|店铺id|是|[int]|9|
|data>>store_name|店铺名称|是|[string]|JHL-DE-1|
|data>>country|国家名称|是|[string]|德国|

## 返回成功示例
```
{
    "code": 0,
    "message": null,
    "data": [
        {
            "status": "ISSUED",
            "amount": 1.9400,
            "sid": 136,
            "country": "美国",
            "invoice_id": "TRF6K4FJN-1",
            "payment_method": "UNIFIED_BILLING",
            "from_date": "2024-06-03",
            "to_date": "2024-06-04",
            "currency_icon": "$",
            "cost_amount": 1.9400,
            "tax_amount": 0.0000,
            "other_allocation_fee": 0.0000,
            "invoice_date": "2024-06-03",
            "store_name": "renxiao-US"
        }
    ],
    "error_details": null,
    "request_id": "cf4c5e99-1fbb-42d4-98fc-6a5697dd7f9d.1721879115549",
    "response_time": "2024-07-25 11:45:15",
    "total": 1
}
```