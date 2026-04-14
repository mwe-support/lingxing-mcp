# 刊登管理-查询 Amazon 根分类
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/publish/manage/categoryRoot` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|storeId|店铺id|是|[number]|50|

## 请求示例
```
{
    "storeId": 50
}
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]|[]|
|request_id|请求链路id|是|[string]|3603fba915a7417baf2de82ec2807314.1753235287406|
|response_time|响应时间|是|[string]|2025-07-23 09:48:10|
|data|响应数据|是|[object]| |
|data>>category|类目列表|是|[array]||
|data>>category>>categoryUniqueId|类目唯一ID|是|[string]|107883898167361544|
|data>>category>>categoryName|类目名称|是|[string]|Amazon Instant Video|
|data>>category>>categoryId|亚马逊定义的类目ID|是|[number]|16261641|
|data>>category>>marketplaceId|市场ID|是|[string]|xxxxxxxxxxxxxxxx|
|data>>category>>parentId|父级ID|是|[number]|0|
|data>>category>>isRoot|否为根类目（1为根，0为子）|是|[number]|1|
|data>>category>>hasChildren|是否包含子类目（1有，0无）|是|[number]|1|
|data>>category>>childCategory|子类目ID列表|是|[array]|["16386761","16262841"]|
|total|总数|是|[number]|0|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "3603fba915a7417baf2de82ec2807314.1753235287406",
    "response_time": "2025-07-23 09:48:10",
    "data": {
        "category": [{
            "categoryUniqueId": "107883898167361544",
            "categoryName": "Amazon Instant Video",
            "categoryId": 16261641,
            "marketplaceId": "xxxxxxxxxxxxxxxx",
            "parentId": 0,
            "isRoot": 1,
            "hasChildren": 1,
            "childCategory": ["16386761", "16262841"]
        }]
    },
    "total": 0
}
```