# 查询Listing标记标签列表

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/listingManage/queryListingRelationTagList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|bind_detail|listing数据，上限100|是|[array]||
|bind_detail>>sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|17|
|bind_detail>>relation_id|msku，[查询亚马逊Listing](docs/Sale/Listing) 接口对应字段【seller_sku】|是|[string]|HOLDER001|

## 请求示例
```
{
    "bind_detail": [
        {
            "sid": 104,
            "relation_id": "msku-1"
        }
    ]
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|77ac259a67d5462594c83b80669b6eae.1692331008758|
|response_time|响应时间|是|[string]|2023-08-18 11:56:49|
|total|总数|是|[int]|0|
|data|响应数据|是|[array]||
|data>>relation_id|msku|是|[string]|HOLDER001|
|data>>sid|店铺id|是|[int]|17|
|data>>tag_infos|标签列表|是|[array]||
|data>>tag_infos>>global_tag_id|标签id|是|[string]|907365081622413333|
|data>>tag_infos>>tag_name|标签名称|是|[string]|家具大卖|
|data>>tag_infos>>color|颜色|是|[string]|#9C9CA0|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "ea0fae50098442a8bc3f9acd8ab7e47e.1696906826858",
    "response_time": "2023-10-10 11:00:28",
    "data": [
        {
            "relation_id": "HOLDER001",
            "sid": 17,
            "tag_infos": [
                {
                    "global_tag_id": "907365081622413333",
                    "tag_name": "家具大卖",
                    "color": "#9C9CA0"
                }
            ]
        }
    ],
    "total": 1
}

```