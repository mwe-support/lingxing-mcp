# 获取发货单头程物流信息-承运商信息
用于发货单新版头程物流信息创建其他费
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/shipment/getSeaTrackSupplierCarriers` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|vehicle_type|运输类型【默认Sea】：<br>Sea 海运<br>Express 快递<br>Aviation 空运|否|[string]|Sea|
## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|B1859FE7-E155-AB56-54AD-9B8958CF2078|
|response_time|响应时间|是|[string]|2022-03-09 11:41:17|
|data|响应数据|是|[array]|  |
|data>>shippers|承运商code|是|[string]|matson|
|data>>name|承运商名称|是|[string]|Matson(Matson)|
|data>>home_page|承运商链接主页地址|是|[string]|https://www.matson.com/shipment-tracking.html|

