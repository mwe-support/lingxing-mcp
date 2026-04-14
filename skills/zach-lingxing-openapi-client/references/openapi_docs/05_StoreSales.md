# 查询店铺汇总销量
支持按店铺维度查询店铺销量、销售额

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/sales_report/sales` | HTTPS | POST | 5 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|报表时间，格式：Y-m-d，闭区间|是|[string]|2020-01-01|
|end_date|报表时间，格式：Y-m-d，闭区间|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>r_date|报表日期|是|[string]|2019-05-20|
|data>>seller_sku|MSKU|是|[string]|JoborSWimming|
|data>>asin|ASIN|是|[string]|B07DFFF9SG|
|data>>product_name|品名|是|[string]|Xenstar xxxx Goggles, No xxxxx Fog xxxxx  Goggles for Men xxxxx Adult xxxxx Deep Blue|
|data>>currency_code|币种|是|[string]|USD|
|data>>order_items|当天订单项总量|是|[int]|2|
|data>>volume|销量|是|[int]|2|
|data>>amount|销售额|是|[string]|7.98|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "4B614F7A-C1C1-BBCF-CCBB-700EACE909E4",
    "response_time": "2024-08-09 09:29:38",
    "data": [
        {
            "r_date": "2023-05-23",
            "seller_sku": "HOLDER001",
            "asin": "B0BB389BKQ",
            "product_name": "NP Phone Holder",
            "currency_code": "USD",
            "order_items": 0,
            "volume": 0,
            "amount": "0.00"
        },
        {
            "r_date": "2022-06-23",
            "seller_sku": "Hair-Ties-P0360",
            "asin": "B0B4WP82TG",
            "product_name": "Heart Pearl Black Elastic Hair Ties High Stretch Jewelry Rubber Band Head Rope for Women Girls YiWu HENGFU",
            "currency_code": "USD",
            "order_items": 1,
            "volume": 1,
            "amount": "3.99"
        },
        {
            "r_date": "2022-12-14",
            "seller_sku": "Hair-Ties-P0360",
            "asin": "B0B4WP82TG",
            "product_name": "Heart Pearl Black Elastic Hair Ties High Stretch Jewelry Rubber Band Head Rope for Women Girls YiWu HENGFU.",
            "currency_code": "USD",
            "order_items": 0,
            "volume": 0,
            "amount": "0.00"
        }
    ],
    "total": 34
}
```
## 附加说明  
1. 本接口amount字段汇总的是实际付款的订单，不会汇总状态为Pending的订单，而界面上的数值是包含了预估的，所以会存在与界面不一致的情况