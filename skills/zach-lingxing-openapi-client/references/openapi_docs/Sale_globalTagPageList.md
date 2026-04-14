# 查询Listing标签列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/globalTag/listing/page/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限200|否|[int]|20|
|search_field|搜索类型：tag_name 标签名称|否|[string]|tag_name|
|search_value|搜索值|否|[string]|特殊Listing|

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|77ac259a67d5462594c83b80669b6eae.1692331008758|
|response_time|响应时间|是|[string]|2023-08-18 11:56:49|
|total|总数|是|[int]|19|
|data|响应数据|是|[array]||
|data>>global_tag_id|标签id|是|[string]|907197381346419251|
|data>>tag_name|标签名称|是|[string]|家电大卖|
|data>>type|标签类型|是|[string]|商品标签|
|data>>relation_count|标签条目|是|[int]|1|
|data>>tag_object|标签对象|是|[string]|ASIN|
|data>>create_by_name|创建人名称|是|[string]|jack|
|data>>modify_by_name|最后编辑人名称|是|[string]|lucy|
|data>>create_by|创建时间|是|[string]|2022-06-22 18:21:24|
|data>>modify_by|更新时间|是|[string]|2022-06-23 11:06:38|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "014d7dd55bab489094dd42eebc83eef9.1696840325147",
    "response_time": "2023-10-09 16:32:07",
    "data": [
        {
            "global_tag_id": "907365081622413333",
            "tag_name": "家具大卖",
            "type": "商品标签",
            "relation_count": 2,
            "tag_object": "ASIN",
            "create_by_name": "jack",
            "modify_by_name": "jack",
            "create_by": "2023-10-09 19:40:07",
            "modify_by": "2023-10-09 19:40:07"
        }  
     ],
    "total": 1
}
```