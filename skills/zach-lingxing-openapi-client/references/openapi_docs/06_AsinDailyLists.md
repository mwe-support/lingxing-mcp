# 查询亚马逊销量统计
支持按Asin或MSKU查询销量、订单量、销售额

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/sales_report/asinDailyLists` | HTTPS | POST | 5 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|event_date|报表时间【站点时间】，格式：Y-m-d |是|[string]|2024-08-05|
|asin_type|查询维度：【默认1】<br>1 asin<br>2 msku|否|[int]|1| 
|type|类型：【默认1】<br>1 销售额<br>2 销量<br>3 订单量|否|[int]|1| 
|offset|分页偏移量，默认0|否|[int]|0| 
|length|分页长度，默认1000|否|[int]|1000| 

## 请求示例
```
{
    "sid": 109,
    "event_date": "2024-08-05",
    "asin_type": 1,
    "type": 1,
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
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sid|店铺id|是|[int]|1|
|data>>r_date|报表日期【站点时间】|是|[string]|2020-11-13|
|data>>currency_code|币种|是|[string]|USD|
|data>>seller_sku|MSKU|是|[string]|Hair-Ties|
|data>>asin|ASIN|是|[string]|B01GO06AU8G|
|data>>product_name|品名|是|[string]|Combination Locks  Waterproof Padlock|
|data>>map_value|参数type对应的统计量|是|[number]|363.10|
