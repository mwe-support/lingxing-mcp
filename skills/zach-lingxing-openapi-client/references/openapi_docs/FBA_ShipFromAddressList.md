# 地址簿-发货地址列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/shipment/shipFromAddressList` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[18]|
|search_field|搜索字段：<br>alias_name 地址簿别名<br>sender_name 发货方名称|否|[string]|sender_name|
|search_value|对应搜索字段模糊搜索值|否|[string]|创智|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/routing/fba/shipment/shipFromAddressList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "sid": [18],
    "search_field": "sender_name",
    "search_value": "创智",
    "offset": 0,
    "length": 20
}'
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|FFE89896-B9C5-1634-5589-6E0F89F0E4A2|
|response_time|响应时间|是|[string]|2022-10-18 22:39:55|
|data|地址簿列表|是|[array]| |
|data>>id|发货地址唯一id|是|[int]|12|
|data>>sid|店铺id|是|[int]|18|
|data>>alias_name|地址别名|是|[string]|别名1111|
|data>>country_code|国家code|是|[string]|AD|
|data>>country_name|发货国家/地区|是|[string]|安道尔|
|data>>sender_name|发货方名称|是|[string]|xxxx|
|data>>province|省/州/地区，美国发货地址限制长度为2位|是|[string]|xxxx|
|data>>city|城市|是|[string]|xxx|
|data>>region|区|是|[string]|xxx|
|data>>street_detail1|街道地址1|是|[string]|xxx|
|data>>street_detail2|街道地址2|是|[string]|xxx|
|data>>zip_code|邮编|是|[string]|417000|
|data>>phone| |是|[string]|133xxxx4987|
|data>>is_default|是否默认地址：<br>0 否<br>1 是|是|[int]|1|
|data>>seller_name|店铺名|是|[string]|xxxx-CA|
|data>>seller_country_name| |是|[string]|加拿大|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "85377076-5C98-ADDD-C004-329ACE6B7021",
    "response_time": "2022-12-08 18:35:58",
    "data": [
        {
            "id": 320,
            "sid": 16,
            "alias_name": "真个名字",
            "country_code": "CN",
            "country_name": "中国 内地",
            "sender_name": "创智云城A7",
            "province": "广东",
            "city": "深圳",
            "region": "",
            "street_detail1": "留仙洞1111",
            "street_detail2": "",
            "zip_code": "00332233",
            "phone": "12345667866",
            "is_default": 0,
            "seller_name": "8xxxxxED",
            "seller_country_name": "美国"
        },
        {
            "id": 319,
            "sid": 16,
            "alias_name": "别名1111",
            "country_code": "CN",
            "country_name": "中国 内地",
            "sender_name": "创智云城A7",
            "province": "广东",
            "city": "深圳",
            "region": "",
            "street_detail1": "留仙洞1111",
            "street_detail2": "",
            "zip_code": "00332233",
            "phone": "",
            "is_default": 0,
            "seller_name": "8xxxxxED",
            "seller_country_name": "美国"
        }
    ],
    "total": 2
}
```

