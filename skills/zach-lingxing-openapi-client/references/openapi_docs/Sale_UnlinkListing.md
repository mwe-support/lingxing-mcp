# 解除Listing配对

支持批量解除Listing配对

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/listingManage/unLinkListingPairs` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                                             | 必填 | 类型 | 示例 |
| :------------ |:-----------------------------------------------| :------------ | :------------ | :------------ |
|list| 解除配对列表 |是|[array]||
|list>>storeId| 对应[亚马逊店铺](/docs/BasicData/SellerLists)【sid】 |是|[int]|31|
|list>>msku| msku                               |是|[string]|09-CJWX-DFQH|

## 请求curl示例
```
curl --location --request POST 'https://openapi.lingxing.com/basicOpen/listingManage/unLinkListingPairs?app_key=value&access_token=value&timestamp=value&sign=value' \
--header 'Content-Type: application/json' \
--data-raw '{
    "list": [
        {
            "storeId": 31,
            "msku": "09-CJWX-DFQH"
        },
        {
            "storeId": 31,
            "msku": "7K-YYWO-O4GB"
        }
    ]
}'
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|[]|
|request_id|请求链路id|是|[string]|83AAED7E-A5CF-6A09-6446-36F51AA3EEBA|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "79482a3cda144524a4666fc934d8d146.1746759752485",
    "response_time": "2025-05-09 11:02:33",
    "data": null
}
```