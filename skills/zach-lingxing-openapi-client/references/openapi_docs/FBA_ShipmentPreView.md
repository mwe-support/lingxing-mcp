# 查询货件方案
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-shipment/shipmentPreView` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-shipment/shipmentPreView?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
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
|data>>placementOptionList|货件方案|是|[array]| |
|data>>placementOptionList>>feeCount|费用|是|[number]| |
|data>>placementOptionList>>fees|费用明细：array|是|[array]| |
|data>>placementOptionList>>fees>>amount|金额|是|[number]| |
|data>>placementOptionList>>fees>>code|货币类型：详见ISO 4217标准里的货币编码，例如USD、CNY等|是|[string]| |
|data>>placementOptionList>>fees>>target|费用项：例如'Placement Services', 'Fulfillment Fee Discount'等|是|[string]| |
|data>>placementOptionList>>fees>>type|费用类型：FEE, DISCOUNT等|是|[string]| |
|data>>placementOptionList>>placementOptionId|货件方案id|是|[string]| |
|data>>placementOptionList>>placementStatus|状态：含OFFERED、ACCEPTED、EXPIRED|是|[string]| |
|data>>placementOptionList>>shipmentInformationList|货件信息|是|[array]| |
|data>>placementOptionList>>shipmentInformationList>>address| |是|[object]| |
|data>>placementOptionList>>shipmentInformationList>>address>>addressLine1|详细街道地址1|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>addressLine2|详细街道地址2|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>city|城市|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>companyName|公司名称|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>countryCode|国家(地区）|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>email|邮箱|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>name|收货方名称|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>phoneNumber|电话|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>postalCode|邮政编码|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>address>>stateOrProvinceCode|州/省/地区|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemCount|商品总数|是|[int]| |
|data>>placementOptionList>>shipmentInformationList>>itemList|商品信息|是|[array]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>asin|asin|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>fnsku|fnsku|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>msku|msku|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>parentAsin|父asin|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>productName|品名：【产品管理】中的品名|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>sku|sku：【产品管理】中的sku|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>title|标题|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>itemList>>url|图片url|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>postalCodeMark|入库区域（美国站专属）|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>shipmentId|货件单号|是|[string]| |
|data>>placementOptionList>>shipmentInformationList>>shipmentName|货件名称, 当placementStatus=ACCEPTED时才有数据返回|否|[string]| |
|data>>placementOptionList>>shipmentInformationList>>wareHouseId|物流中心编码|是|[string]| ||
|data>>placementOptionList>>shipmentInformationList>>quantity|商品总申报量|是|[int]| |100|


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
        "placementOptionList": [{
            "feeCount": "费用",
            "fees": [{
                "amount": "金额",
                "code": "货币类型：详见ISO 4217标准里的货币编码，例如USD、CNY等",
                "target": "费用项：例如'Placement Services', 'Fulfillment Fee Discount'等",
                "type": "费用类型：FEE, DISCOUNT等"
            }],
            "placementOptionId": "货件方案id",
            "placementStatus": "状态：含OFFERED、ACCEPTED、EXPIRED",
            "shipmentInformationList": [{
                "address": {
                    "addressLine1": "详细街道地址1",
                    "addressLine2": "详细街道地址2",
                    "city": "城市",
                    "companyName": "公司名称",
                    "countryCode": "国家(地区）",
                    "email": "邮箱",
                    "name": "收货方名称",
                    "phoneNumber": "电话",
                    "postalCode": "邮政编码",
                    "stateOrProvinceCode": "州/省/地区"
                },
                "itemCount": "商品总数",
                "itemList": [{
                    "asin": "asin",
                    "fnsku": "fnsku",
                    "msku": "msku",
                    "parentAsin": "父asin",
                    "productName": "品名：【产品管理】中的品名",
                    "sku": "sku：【产品管理】中的sku",
                    "title": "标题",
                    "url": "图片url"
                }],
                "postalCodeMark": "入库区域（美国站专属）",
                "shipmentId": "货件单号",
                "shipmentName": "货件名称",
                "wareHouseId": "物流中心编码"
            }]
        }]
    }
}
```