# 查询承运方式

## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-shipment/getTransportList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|shipmentId|货件id，对应[查询货件方案](docs/FBA/ShipmentPreView)接口对应字段【shipmentId】|是|[string]|"shd10e38ca-45e7-4a97-8512-780acf343f4b3" |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-shipment/getTransportList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "shipmentId": "货件id",
    "sid": 1
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功|是|[int]|	0 |
|message|消息提示 |是|[string]|success |
|errorDetails|错误信息 |是|[array]| |
|requestId| 请求链路id|是|[string]| |
|responseTime|响应时间 |是|[string]| 2020-05-18 11:23:47|
|data| 响应数据|是|[object]| |
|data>>inboundPlanId|STA任务编号|是|[string]| |
|data>>shipmentId|货件号|是|[string]| |
|data>>transportVOList|承运方式列表|是|[array]| |
|data>>transportVOList>>alphaCode|承运方式编码|是|[string]| |
|data>>transportVOList>>alphaName|承运方式名称|是|[string]| |
|data>>transportVOList>>shippingMode|货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））|是|[string]| |
|data>>transportVOList>>shippingSolution|承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)|是|[string]| |
|data>>transportVOList>>transportationOptionId|承运方式ID|是|[string]| ||
|data>>transportVOList>>alphaAliasName|承运方式别名|否|[string]| ||

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "574FB0B8-FD6E-8D29-91FD-295B55CF5398",
    "response_time": "2024-07-31 14:41:25",
    "data": {
        "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
        "shipmentId": "货件号",
        "transportVOList": [{
        "alphaCode": "承运方式编码",
        "alphaName": "承运方式名称",
        "shippingMode": "货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））",
        "shippingSolution": "承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)",
        "transportationOptionId": "承运方式ID"
        }]
    }
}
```
