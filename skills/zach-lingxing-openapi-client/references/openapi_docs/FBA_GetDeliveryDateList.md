# 查询可选送达时间
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-shipment/getDeliveryDateList` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]| |
|shipmentId|货件id，对应[查询货件方案](docs/FBA/ShipmentPreView)接口对应字段【shipmentId】|是|[string]|"shd10e38ca-45e7-4a97-8512-780acf343f4b3" |
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-shipment/getDeliveryDateList?access_token=value&timestamp=value&sign=value&app_key=value' \
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
|data>>shipmentId|货件单号|是|[string]| |
|data>>shipmentList|可选送达时间|是|[array]| |
|data>>shipmentList>>deliveryWindowOptionId|选项id|是|[string]| |
|data>>shipmentList>>endDate|结束时间<br>格式：yyyy-MM-dd HH:mm:ss|是|[string]| |
|data>>shipmentList>>startDate|开始时间<br>格式：yyyy-MM-dd HH:mm:ss|是|[string]| |
|data>>shipmentList>>validUntil|过期时间<br>格式：yyyy-MM-dd HH:mm:ss|是|[string]| ||


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": [],
    "requestId": "3b3d867e7d014971a580549f107c8c5a.1732773886069",
    "responseTime": "2024-11-28T14:04:46.069",
    "data": {
        "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
        "shipmentId": "货件单号",
        "shipmentList": [{
            "deliveryWindowOptionId": "选项id",
            "endDate": "结束时间",
            "startDate": "开始时间",
            "validUntil": "过期时间"
        }]
    }
}
```