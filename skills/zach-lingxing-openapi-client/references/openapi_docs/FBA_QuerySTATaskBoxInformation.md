# 查询STA任务包装组装箱信息
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|packingGroupIdList|包装组id|是|[array]| |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||



## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-plan/listInboundPlanGroupPacking?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "packingGroupIdList": "包装组id",
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
|data>>inboundPlanId|STA任务编号|否|[string]| |
|data>>packingGroupList|包装组|否|[array]| |
|data>>packingGroupList>>packingGroupId|包装组id|是|[string]| |
|data>>packingGroupList>>shipmentPackingList|装箱明细|是|[array]| |
|data>>packingGroupList>>shipmentPackingList>>boxId|箱子id|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>height|箱子高度|是|[number]| |
|data>>packingGroupList>>shipmentPackingList>>length|箱子长度|是|[number]| |
|data>>packingGroupList>>shipmentPackingList>>lengthUnit|长度单位：含IN、CM|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>packageId|包裹id|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList|商品明细|是|[array]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>asin|asin|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>expiration|有效期|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>fnsku|fnsku|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>labelOwner|标签类型（AMAZON,SELLER,NONE）|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>msku|msku|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>parentAsin|父asin|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>prepOwner|预处理提供方（AMAZON,SELLER,NONE）|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>productName|品名|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>quantityInBox|单箱数量|是|[int]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>sku|sku|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>title|标题|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>productList>>url|图片url|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>total|商品总数量|是|[int]| |
|data>>packingGroupList>>shipmentPackingList>>weight|箱子重量|是|[number]| |
|data>>packingGroupList>>shipmentPackingList>>weightUnit|重量单位：含LB、KG|是|[string]| |
|data>>packingGroupList>>shipmentPackingList>>width|箱子宽度|是|[number]| ||

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
        "packingGroupList": [
            {
                "packingGroupId": "包装组id",
                "shipmentPackingList": [
                    {
                        "boxId": 3,
                        "height": 4,
                        "length": 5,
                        "lengthUnit": "CM",
                        "packageId": "包裹id",
                        "productList": [
                            {
                                "asin": "asin",
                                "expiration": "有效期",
                                "fnsku": "fnsku",
                                "labelOwner": "标签类型（AMAZON,SELLER,NONE）",
                                "msku": "msku",
                                "parentAsin": "父asin",
                                "prepOwner": "预处理提供方（AMAZON,SELLER,NONE）",
                                "productName": "品名",
                                "quantityInBox": 5,
                                "sku": "sku",
                                "title": "标题",
                                "url": "图片url"
                            }
                        ],
                        "total": 7,
                        "weight": 6,
                        "weightUnit": "KG",
                        "width": 3
                    }
                ]
            }
        ]
    }
}
```
