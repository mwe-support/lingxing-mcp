# 刊登管理-获取运费模板
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/publish/manage/getMerchantShippingGroup` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sellerId|店铺id|是|[string]|xxxxxxxxxxxxxxxx|
|marketplaceId|市场id|是|[string]|xxxxxxxxxxxxxxxx|
|productType|商品原始类目|是|[string]|ADVERTISEMENT_COLLECTIBLES|
|flag|默认传0，返回为空则传1，实时请求亚马逊获取后台最新数据|否|[number]|1|
## 请求示例
```
{
    "sellerId": "xxxxxxxxxxxxxxxx",
    "marketplaceId": "xxxxxxxxxxxxxxxx",
    "productType": "ADVERTISEMENT_COLLECTIBLES",
    "flag": 1
}
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]|[]|
|request_id|请求链路id|是|[string]|81a889484440454da2de2dc00666f893.1753351909264|
|response_time|响应时间|是|[string]|2025-07-24 18:11:56|
|data|响应数据|是|[array]||
|data>>name|运费模板名称|是|[string]|Migrated Template|
|data>>value|运费模板id|是|[string]|legacy-template-id|
|total|总数|是|[number]|1|
## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "81a889484440454da2de2dc00666f893.1753351909264",
    "response_time": "2025-07-24 18:11:56",
    "data": [{
        "name": "Migrated Template",
        "value": "legacy-template-id"
    }],
    "total": 1
}
```