# 查询亚马逊源报表-FBA换货订单
查询 Replacements Report 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/data/order/fbaExchangeOrderList` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid| 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|43|
|start_date|开始时间，左闭区间，格式：Y-m-d|是|[string]|2020-01-01|
|end_date|结束时间，右开区间，格式：Y-m-d|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 43,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]| success |
|error_details|错误信息 |是|[array]| |
|response_time|响应时间|是|[string]|2020-05-18 11:23:47 |
|request_id|请求链路id|是|[string]|07104411-0304-E343-5AF9-592E73D817E6|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>order_hash|订单唯一hash【不是唯一键】 |是|[string]| |
|data>>sid|店铺id|是|[int]| |
|data>>replacement_amazon_order_id| 换货订单号 |是|[string]| |
|data>>shipment_date|换货时间|是|[string]| |
|data>>asin|asin|是|[string]| |
|data>>seller_sku|msku|是|[string]| |
|data>>original_amazon_order_id|原始订单号|是|[string]| |
|data>>fulfillment_center_id|换货仓库|是|[string]| |
|data>>original_fulfillment_center_id|原始仓库|是|[string]| |
|data>>quantity|换货数量|是|[string]| |
|data>>replacement_reason_code|换货原因|是|[string]| |
|data>>sync_time|数据同步时间戳|是|[string]|&nbsp;|
