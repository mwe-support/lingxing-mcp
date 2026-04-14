# 查询货件详情
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-shipment/shipmentDetailList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|shipmentIds|货件id|是|[array]|["shd10e38ca-45e7-4a97-8512-780acf343f4b3"] |
|sid|店铺ID，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-shipment/shipmentDetailList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "shipmentIds": "货件id",
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
|data| |是|[object]| |
|data>>inboundPlanId|STA任务编号|是|[string]| |
|data>>shipmentList| |是|[array]| |
|data>>shipmentList>>alphaCode|承运方式|是|[string]| |
|data>>shipmentList>>amazonReferenceId|关联号|是|[string]| |
|data>>shipmentList>>endDate|送达时段-结束时间<br>格式：yyyy-MM-dd HH:mm:ss|是|[string]| |
|data>>shipmentList>>inboundRegion|入库区域|是|[string]| |
|data>>shipmentList>>itemCount|商品总数|是|[int]| |
|data>>shipmentList>>itemList|商品信息|是|[array]| |
|data>>shipmentList>>itemList>>asin|asin|是|[string]| |
|data>>shipmentList>>itemList>>fnsku|fnsku|是|[string]| |
|data>>shipmentList>>itemList>>msku|msku|是|[string]| |
|data>>shipmentList>>itemList>>parentAsin|父asin|是|[string]| |
|data>>shipmentList>>itemList>>productName|品名|是|[string]| |
|data>>shipmentList>>itemList>>quantity|申报量|是|[int]| |
|data>>shipmentList>>itemList>>sku|sku|是|[string]| |
|data>>shipmentList>>itemList>>title|标题|是|[string]| |
|data>>shipmentList>>itemList>>url|图片url|是|[string]| |
|data>>shipmentList>>pickUpId|提货单号|是|[string]| |
|data>>shipmentList>>sendAddress| |是|[object]| |
|data>>shipmentList>>sendAddress>>addressLine1|街道地址1|是|[string]| |
|data>>shipmentList>>sendAddress>>addressLine2|街道地址2|是|[string]| |
|data>>shipmentList>>sendAddress>>addressName|地址名称|是|[string]| |
|data>>shipmentList>>sendAddress>>city|城市|是|[string]| |
|data>>shipmentList>>sendAddress>>country|国家名称|是|[string]| |
|data>>shipmentList>>sendAddress>>countryCode|国家code|是|[string]| |
|data>>shipmentList>>sendAddress>>email|邮箱|是|[string]| |
|data>>shipmentList>>sendAddress>>phoneNumber|电话号码|是|[string]| |
|data>>shipmentList>>sendAddress>>postalCode|邮政编码|是|[string]| |
|data>>shipmentList>>sendAddress>>stateOrProvinceCode|省市区code|是|[string]| |
|data>>shipmentList>>shipingTime|发货日期<br>格式：yyyy-MM-dd|是|[string]| |
|data>>shipmentList>>shipmentConfirmationId|货件单号|是|[string]| |
|data>>shipmentList>>shipmentName|货件名称|是|[string]| |
|data>>shipmentList>>shippingAddress| |是|[object]| |
|data>>shipmentList>>shippingAddress>>addressLine1|街道地址1|是|[string]| |
|data>>shipmentList>>shippingAddress>>addressLine2|街道地址2|是|[string]| |
|data>>shipmentList>>shippingAddress>>addressName|地址名称|是|[string]| |
|data>>shipmentList>>shippingAddress>>city|城市|是|[string]| |
|data>>shipmentList>>shippingAddress>>country|国家名称|是|[string]| |
|data>>shipmentList>>shippingAddress>>countryCode|国家code|是|[string]| |
|data>>shipmentList>>shippingAddress>>email|邮箱|是|[string]| |
|data>>shipmentList>>shippingAddress>>phoneNumber|电话号码|是|[string]| |
|data>>shipmentList>>shippingAddress>>postalCode|邮政编码|是|[string]| |
|data>>shipmentList>>shippingAddress>>stateOrProvinceCode|省市区code|是|[string]| |
|data>>shipmentList>>shippingMode|货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））|是|[string]| |
|data>>shipmentList>>shippingSolution|承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)|是|[string]| |
|data>>shipmentList>>sid|店铺ID|是|[long]| |
|data>>shipmentList>>startDate|送达时段-开始时间|是|[string]| |
|data>>shipmentList>>status|货件状态|是|[string]| |
|data>>shipmentList>>trackingNumberList|追踪编号|是|[array]| |
|data>>shipmentList>>trackingNumberList>>boxId|箱号|是|[string]| |
|data>>shipmentList>>trackingNumberList>>trackingNumber|追踪编号|是|[string]| |
|data>>shipmentList>>warehouseId|物流中心编码|是|[string]| ||

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
        "shipmentList": [{
            "alphaCode": "承运方式",
            "amazonReferenceId": "关联号",
            "endDate": "送达时段-结束时间",
            "inboundRegion": "入库区域",
            "itemCount": "商品总数",
            "itemList": [{
                "asin": "asin",
                "fnsku": "fnsku",
                "msku": "msku",
                "parentAsin": "父asin",
                "productName": "品名",
                "quantity": "申报量",
                "sku": "sku",
                "title": "标题",
                "url": "图片url"
            }],
            "pickUpId": "提货单号",
            "sendAddress": {
                "addressLine1": "街道地址1",
                "addressLine2": "街道地址2",
                "addressName": "地址名称",
                "city": "城市",
                "country": "国家名称",
                "countryCode": "国家code",
                "email": "邮箱",
                "phoneNumber": "电话号码",
                "postalCode": "邮政编码",
                "stateOrProvinceCode": "省市区code"
            },
            "shipingTime": "发货日期",
            "shipmentConfirmationId": "货件单号",
            "shipmentName": "货件名称",
            "shippingAddress": {
                "addressLine1": "街道地址1",
                "addressLine2": "街道地址2",
                "addressName": "地址名称",
                "city": "城市",
                "country": "国家名称",
                "countryCode": "国家code",
                "email": "邮箱",
                "phoneNumber": "电话号码",
                "postalCode": "邮政编码",
                "stateOrProvinceCode": "省市区code"
            },
            "shippingMode": "货件类型（GROUND_SMALL_PARCEL代表小包裹快递（SPD）、FREIGHT_LTL代表汽运零担（LTL））",
            "shippingSolution": "承运人(USE_YOUR_OWN_CARRIER代表其他承运人、AMAZON_PARTNERED_CARRIER代表亚马逊合作承运人)",
            "sid": "店铺ID",
            "startDate": "送达时段-开始时间",
            "status": "货件状态",
            "trackingNumberList": [{
                "boxId": "箱号",
                "trackingNumber": "追踪编号"
            }],
            "warehouseId": "物流中心编码"
        }]
    }
}
```