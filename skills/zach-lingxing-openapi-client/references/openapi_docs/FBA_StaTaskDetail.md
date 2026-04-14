# 查询STA任务详情
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-plan/detail` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05 |
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-plan/detail?access_token=value&timestamp=value&sign=value&app_key=value' \
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
|data>>addressVO|发货地址|是|[object]| |
|data>>addressVO>>addressLine1|街道地址1|是|[string]| |
|data>>addressVO>>addressLine2|街道地址2|是|[string]| |
|data>>addressVO>>city|城市|是|[string]| |
|data>>addressVO>>countryCode|国家code|是|[string]| |
|data>>addressVO>>countryName|国家名称|是|[string]| |
|data>>addressVO>>email|邮箱|是|[string]| |
|data>>addressVO>>phoneNumber|电话号码|是|[string]| |
|data>>addressVO>>postalCode|邮政编码|是|[string]| |
|data>>addressVO>>shipperName|发货方名称|是|[string]| |
|data>>addressVO>>stateOrProvinceCode|州/省/地区|是|[string]| |
|data>>gmtCreate|创建时间|是|[string]| |
|data>>gmtModified|更新时间|是|[string]| |
|data>>inboundPlanId|STA任务编号|是|[string]| |
|data>>planCreateTime|计划创建时间|是|[string]| |
|data>>planName|STA任务名称|是|[string]| |
|data>>planUpdateTime|计划更新时间|是|[string]| |
|data>>productList|商品信息|是|[array]| |
|data>>productList>>asin|asin|是|[string]| |
|data>>productList>>fnsku|fnsku|是|[string]| |
|data>>productList>>msku|msku|是|[string]| |
|data>>productList>>parentAsin|父asin|是|[string]| |
|data>>productList>>productName|品名|是|[string]| |
|data>>productList>>quantity|申报量|是|[int]| |
|data>>productList>>sku|sku|是|[string]| |
|data>>productList>>title|标题(【listing】中的标题)|是|[string]| |
|data>>productList>>url|图片url|是|[string]| |
|data>>shipmentList|货件信息|是|[array]| |
|data>>shipmentList>>shipmentId|货件id|是|[string]| |
|data>>shipmentList>>shipmentConfirmationId|货件单号|是|[string]| |
|data>>shipmentList>>status|货件状态: <br> WORKING <br> READY_TO_SHIP <br> SHIPPED <br> RECEIVING <br> CANCELLED <br> DELETED <br> CLOSED <br> ERROR <br> IN_TRANSIT <br> DELIVERED <br> CHECKED_IN <br> UNCONFIRMED |是|[string]| |
|data>>status|STA任务状态：<br>ACTIVE 进行中<br>VOIDED 已取消<br>SHIPPED  已发货|是|[string]| ||
|data>>position_type|分仓方式，1-先装箱再分仓，2-先分仓再装箱|是|[int]|1|


## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "574FB0B8-FD6E-8D29-91FD-295B55CF5398",
    "response_time": "2024-07-31 14:41:25",
    "data": {
        "addressVO": {
            "addressLine1": "街道地址1",
            "addressLine2": "街道地址2",
            "city": "城市",
            "countryCode": "国家code",
            "countryName": "国家名称",
            "email": "邮箱",
            "phoneNumber": "电话号码",
            "postalCode": "邮政编码",
            "shipperName": "发货方名称",
            "stateOrProvinceCode": "州/省/地区"
        },
        "gmtCreate": "创建时间",
        "gmtModified": "更新时间",
        "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
        "planCreateTime": "计划创建时间",
        "planName": "STA任务名称",
        "planUpdateTime": "计划更新时间",
        "productList": [{
            "asin": "asin",
            "fnsku": "fnsku",
            "msku": "msku",
            "parentAsin": "父asin",
            "productName": "品名",
            "quantity": "申报量",
            "sku": "sku",
            "title": "标题(【listing】中的标题)",
            "url": "图片url"
        }],
        "shipmentList": [{
            "shipmentId": "货件id",
            "shipmentConfirmationId": "货件单号",
            "status": "货件状态"
        }],
        "status": "STA任务状态"
    }
}
```