# 刊登管理-查询 Amazon 子分类
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/publish/manage/categoryChildren` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|storeId|店铺id|是|[number]|50|
|categoryUniqueId|类目唯一ID|是|[number]|107884128380125180|

## 请求示例
```
{
    "storeId": 50,
    "categoryUniqueId": 107884128380125180
}
```
## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]|[]|
|request_id|请求链路id|是|[string]|14bd51076a154066b999bd02659093a7.1753347741205|
|response_time|响应时间|是|[string]|2025-07-24 17:02:22|
|data|响应数据|是|[object]| |
|data>>category|类目对象|是|[object]| |
|data>>category>>categoryUniqueId|类目唯一ID|是|[string]|107884128380125187|
|data>>category>>categoryName|类目名称|是|[string]|Collectibles & Fine Art|
|data>>category>>categoryId|亚马逊定义的类目ID|是|[number]|4991426011|
|data>>category>>marketplaceId|市场ID|是|[string]|xxxxxxxxxxxxxxxx|
|data>>category>>parentId|父级ID|是|[number]|0|
|data>>category>>isRoot|否为根类目（1为根，0为子）|是|[number]|1|
|data>>category>>hasChildren|是否包含子类目（1有，0无）|是|[number]|1|
|data>>category>>childCategory|子类目id列表|是|[array]|["5525092011","3250697011"]|
|data>>category>>productTypeOrigin|商品原始类型|是|[array]||
|data>>categoryChildren|子类目列表|是|[array]||
|data>>categoryChildren>>categoryUniqueId|类目唯一ID|是|[string]|107884128724058118|
|data>>categoryChildren>>categoryName|类目名称|是|[string]|Advertising|
|data>>categoryChildren>>categoryId|类目ID|是|[number]|7301170011|
|data>>categoryChildren>>marketplaceId|市场ID|是|[string]|xxxxxxxxxxxxxxxx|
|data>>categoryChildren>>parentId|父级ID|是|[number]|4991426011|
|data>>categoryChildren>>isRoot|否为根类目（1为根，0为子）|是|[number]|0|
|data>>categoryChildren>>hasChildren|是否包含子类目（1有，0无）|是|[number]|0|
|data>>categoryChildren>>childCategory|子类目id列表|是|[array]|[]|
|data>>categoryChildren>>productTypeOrigin|商品原始类型|是|[array]|["ADVERTISEMENT_COLLECTIBLES"]|
|data>>categoryChildren>>browseNodeAttributes|类目节点属性|是|[object]||
|data>>categoryChildren>>categoryPathId|类目路径ID|是|[object]||
|data>>categoryChildren>>categoryPathName|类目路径名称|是|[object]||
|total|子类目总数|是|[number]|6|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "14bd51076a154066b999bd02659093a7.1753347741205",
    "response_time": "2025-07-24 17:02:22",
    "data": {
        "category": {
            "categoryUniqueId": "107884128380125187",
            "categoryName": "Collectibles & Fine Art",
            "categoryId": 4991426011,
            "marketplaceId": "xxxxxxxxxxxxxxxx",
            "parentId": 0,
            "isRoot": 1,
            "hasChildren": 1,
            "childCategory": ["5525092011", "3250697011"],
            "productTypeOrigin": [ "TRADING_CARDS_UNGRADED_INSERTS", "TRADING_CARDS_FACTORY_SEALED"]
        },
        "categoryChildren": [{
            "categoryUniqueId": "107884128724058118",
            "categoryName": "Advertising",
            "categoryId": 7301170011,
            "marketplaceId": "xxxxxxxxxxxxxxxx",
            "parentId": 4991426011,
            "isRoot": 0,
            "hasChildren": 0,
            "childCategory": [],
            "productTypeOrigin": ["ADVERTISEMENT_COLLECTIBLES"],
            "browseNodeAttributes": "{\"item_type_keyword\":\"automotive-pest-repellent-mats\"}",
            "categoryPathId": "15690151,15718271,23708133011,23708134011",
            "categoryPathName": "Automotive > Car Care > Automotive Pest Repellents > Pest Repellent Mats"
        }]
    },
    "total": 6
}
```