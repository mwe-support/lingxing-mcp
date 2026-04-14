# 多渠道订单-交易明细
支持查询【销售】>【SC订单】>【多渠道订单】交易明细数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/salesOrder/multi-channel/list/transaction ` | HTTPS | POST   | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ |:---|
|amazonOrderId|亚马逊订单ID|是|[string]| 1|
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]| 1|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/openapi/salesOrder/multi-channel/list/transaction?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "sid": 7,
    "amazonOrderId": "S03-4986301-7824623"
}'
```
## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]| |
|request_id|请求链路id|是|[string]|ae08ecdd89dd4c0380d3b41d41a57c3d.1727428866172|
|response_time|响应时间|是|[string]|2024-09-27 17:21:12|
|data| |是|[object]| |
|data>>list| |是|[array]| |
|data>>list>>costDetails|明细|是|[array]| |
|data>>list>>costDetails>>currencyAmount|金额|是|[string]|-JP¥713.00|
|data>>list>>costDetails>>type|交易类型|是|[string]|FBAPerUnitFulfillmentFee|
|data>>list>>currencyCode|币种|是|[string]|JPY|
|data>>list>>eventType|来源|是|[string]|Shipment|
|data>>list>>fid|结算编号|是|[string]|HIO94MRSKWFP|
|data>>list>>fundTransferDateLocale|转账日期|是|[string]|2021-04-15T20:24:37+09:00|
|data>>list>>postedDateLocale|结算时间|是|[string]|2021-04-08T06:21:30+09:00|
|data>>list>>productName|产品名|是|[string]|5356|
|data>>list>>quantity|数量|是|[string]|0|
|data>>list>>sellerSku|MSKU|是|[string]|1100X1644-1-2|
|data>>list>>sid|店铺id|是|[string]|7|
|data>>list>>sku|sku|是|[string]|35636|
|data>>list>>totalCurrencyAmount|总金额|是|[string]|JP¥-713.00|
|data>>totalCurrencyAmounts|总金额|是|[string]|-JP¥713.00|
|total|总数|是|[int]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "1e5ce657c37246a29f6ce1268fa6383f.1728616190379",
    "response_time": "2024-10-11 11:09:53",
    "data": {
        "list": [
            {
                "costDetails": [
                    {
                        "currencyAmount": "-JP¥713.00",
                        "type": "FBAPerUnitFulfillmentFee"
                    }
                ],
                "currencyCode": "JPY",
                "eventType": "Shipment",
                "fid": "HIO94MRSKWFP",
                "fundTransferDateLocale": "2021-04-15T20:24:37+09:00",
                "postedDateLocale": "2021-04-08T06:21:30+09:00",
                "productName": "5356",
                "quantity": "0",
                "sellerSku": "1100X1644-1-2",
                "sid": "7",
                "sku": "35636",
                "totalCurrencyAmount": "JP¥-713.00"
            }
        ],
        "totalCurrencyAmounts": "-JP¥713.00"
    },
    "total": 0
}
```