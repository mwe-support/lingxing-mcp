# 刊登管理-获取指定 productType 的 JSON Schema
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/publish/manage/getProductType` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 数据字典 |  限制 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | :------------ | :------------ |
|marketplaceId|市场ID|是|[string]| | |xxxxxxxxxxxxxxxx|
|productTypeOrigin|商品原始类型|是|[string]| | |ADVERTISEMENT_COLLECTIBLES|
## 请求示例
```
{
    "marketplaceId": "xxxxxxxxxxxxxxxx",
    "productTypeOrigin": "ADVERTISEMENT_COLLECTIBLES"
}
```
## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]|[]|
|request_id|请求链路id|是|[string]|b1d0217888784ce597131ff1c3fdbd2b.1753351351953|
|response_time|响应时间|是|[string]|2025-07-24 18:02:34|
|data|响应数据|是|[object]| |
|data>>productType|商品分类信息|是|[object]| |
|data>>productType>>productTypeUniqueId|商品类型唯一id|是|[string]|514829689877954560|
|data>>productType>>marketplaceId|市场id|是|[string]|xxxxxxxxxxxxxxxx|
|data>>productType>>productTypeOrigin|商品类型|是|[string]|ADVERTISEMENT_COLLECTIBLES|
|data>>productType>>displayName|商品类型名称|是|[string]|ADVERTISEMENT_COLLECTIBLES|
|data>>productType>>properties|商品类型的JSON Schema(站点语言版本)|是|[string]||
|data>>productType>>propertiesZh|商品类型的JSON Schema(中文版本)|是|[string]||
|total| |是|[number]|0|

## 返回成功示例
```
{
  "code": 0,
  "message": "success",
  "error_details": [],
  "request_id": "b1d0217888784ce597131ff1c3fdbd2b.1753351351953",
  "response_time": "2025-07-24 18:02:34",
  "data": {
    "productType": {
      "productTypeUniqueId": "514829689877954560",
      "productType": "advertisementcollectibles",
      "marketplaceId": "xxxxxxxxxxxxxxxx",
      "name": "ADVERTISEMENT_COLLECTIBLES",
      "displayName": "ADVERTISEMENT_COLLECTIBLES",
      "propertyGroups": "",
      "properties": "",
      "propertiesZh": ""
    }
  },
  "total": 0
}
```