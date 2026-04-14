# 查询亚马逊源报表-FBA可售库存
查询 FBA Multi-Country Inventory Report 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/getAfnFulfillableQuantity` | HTTPS | POST | 5 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| 0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2021-02-04 13:53:16|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|2|
|data>>seller_sku|销售SKU|是|[string]|0B-HWC7-4ZOH|
|data>>fnsku|FNSKU|是|[string]|X001797EF81|
|data>>asin|ASIN|是|[string]|B08C49XHKFP|
|data>>condition_type|商品成色|是|[string]|NewItem|
|data>>country|国家二字码|是|[string]|GB|
|data>>afn_fulfillable_quantity|FBA可售数量|是|[number]|197|
|data>>gmt_modified|更新时间|是|[string]| &nbsp;|

