# 查询货件方案的装箱信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|否|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[long]| ||

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-packing/getInboundPackingBoxInfo?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "sid": 1
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功 |是|[int]| |
|message|消息提示 |是|[string]| |
|errorDetails|错误信息 |是|[array]| |
|requestId| 请求链路id|是|[string]| |
|responseTime| 响应时间|是|[string]| |
|data|响应数据 |是|[object]| |
|data>>inboundPlanId|STA任务编号|是|[string]| |
|data>>placementOptionList|货件方案id|是|[array]| |
|data>>placementOptionList>>placementOptionId|货件方案id|是|[string]| |
|data>>placementOptionList>>placementStatus|状态：含OFFERED、ACCEPTED、EXPIRED|是|[string]| |
|data>>placementOptionList>>shipmentInformationList|货件信息|是|[array]| |
|data>>placementOptionList>>shipmentInformationList>>shipmentId|货件id|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>volume|箱子总体积（先装箱再分仓时，返回箱子总重量；先分仓再装箱时，不返回箱子总重量）|否|[string]| |
|data>>placementOptionList>>shipmentInformationList>>volumeUnit|长度单位(IN-英制,CM-公制)|否|[string]| |
|data>>placementOptionList>>shipmentInformationList>>weight|箱子总重量（先装箱再分仓时，返回箱子总重量；先分仓再装箱时，不返回箱子总重量）|否|[string]| |
|data>>placementOptionList>>shipmentInformationList>>weightUnit|重量单位（LB-磅，KG-千克）|否|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList|装箱明细|是|[array]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>boxName|箱子名称|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>height|箱子高度|是|[number]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>length|箱子长度|是|[number]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>lengthUnit|长度单位：含IN、CM|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>weight|箱子重量|是|[number]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>weightUnit|重量单位：含LB、KG|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>width|箱子宽度|是|[number]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>total|商品总数量|是|[int]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList|商品明细|是|[array]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>asin|asin|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>fnsku|fnsku|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>msku|msku|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>parentAsin|父asin|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>productName|品名|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>quantityInBox|单箱数量|是|[int]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>sku|sku|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>title|标题|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>shipmentPackingList>>productList>>url|图片url|是|[string]| ||




## 返回成功示例
```
{
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": null,
    "requestId": "f91edad8ebb242c29312ce9d6968adc4.206.17399569715810141",
    "responseTime": "2025-02-19T17:23:06.164",
    "data": {
        "inboundPlanId": "wf1c7907e3-ccfe-4fd6-a8b9-6ff8f786e133",
        "placementOptionList": [
            {
                "placementOptionId": "pl05ef4dbd-ca5f-4108-8a58-354fd5fab88a",
                "placementStatus": "OFFERED",
                "shipmentInformationList": [
                    {
                        "shipmentId": "sh65e73e2e-855e-4490-96ed-b975a0247727",
                        "weight": "10.00",
                        "volume": "0.00",
                        "weightUnit": "KG",
                        "volumeUnit": "M³",
                        "shipmentPackingList": [
                            {
                                "boxName": "Box1",
                                "height": 10,
                                "length": 20,
                                "width": 15,
                                "lengthUnit": "CM",
                                "weight": 10,
                                "weightUnit": "KG",
                                "total": 5,
                                "productList": [
                                    {
                                        "asin": "B07X61XK8J",
                                        "fnsku": "X000123456",
                                        "msku": "SKU-123",
                                        "parentAsin": "B07X61XK8J",
                                        "productName": "Sample Product",
                                        "quantityInBox": 5,
                                        "sku": "SKU-123",
                                        "title": "Sample Product Title",
                                        "url": "https://example.com/image.jpg"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "placementOptionId": "pl13c5f6a9-5348-4b79-a3b2-7da84828f68d",
                "placementStatus": "OFFERED",
                "shipmentInformationList": [
                    {
                        "shipmentId": "shb8a42357-9267-4923-a522-b3c82d42656e",
                        "weight": "10.00",
                        "volume": "0.00",
                        "weightUnit": "KG",
                        "volumeUnit": "M³",
                        "shipmentPackingList": [
                            {
                                "boxName": "Box2",
                                "height": 12,
                                "length": 18,
                                "width": 16,
                                "lengthUnit": "CM",
                                "weight": 10,
                                "weightUnit": "KG",
                                "total": 3,
                                "productList": [
                                    {
                                        "asin": "B07X61XK8J",
                                        "fnsku": "X000123456",
                                        "msku": "SKU-123",
                                        "parentAsin": "B07X61XK8J",
                                        "productName": "Sample Product",
                                        "quantityInBox": 3,
                                        "sku": "SKU-123",
                                        "title": "Sample Product Title",
                                        "url": "https://example.com/image.jpg"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
```


