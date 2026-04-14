# 查询广告发票基本信息
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/ads/invoice/detail` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|invoice_id|广告发票编号|是|[string]|TRF6K4FJN-1|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|136|

## 请求示例
```
{
    "invoice_id": "TRF6K4FJN-1",
    "sid": 136
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
|data|响应数据|是|[object]||
|data>>invoice_id|广告发票编号|是|[string]|TRF6K4FJN-1|
|data>>payment_method|付款类型|是|[string]|UNIFIED_BILLING|
|data>>from_date|账单周期开始时间|是|[string]|2023-01-02|
|data>>to_date|账单周期结算时间|是|[string]|2023-01-06|
|data>>currency_icon|币种符号|是|[string]|$|
|data>>currency_code|符号币种|是|[string]|USD|
|data>>amount|账单金额|是|[number]|1.9400|
|data>>invoice_date|发票时间|是|[string]|2023-01-05|
|data>>address|地址|是|[string]|null|

## 返回成功示例
```
{
    "code": 0,
    "message": null,
    "data": {
        "amount": 1.9400,
        "address": null,
        "invoice_id": "TRF6K4FJN-1",
        "payment_method": "UNIFIED_BILLING",
        "from_date": "2024-06-03",
        "to_date": "2024-06-04",
        "currency_icon": "$",
        "currency_code": "USD",
        "invoice_date": "2024-06-03"
    },
    "error_details": null,
    "request_id": "9941460b-ae8b-4c88-865d-de9f28272915.1721897153312",
    "response_time": "2024-07-25 16:45:53",
    "total": 0
}
```
