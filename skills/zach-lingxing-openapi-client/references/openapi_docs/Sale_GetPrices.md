# 批量获取Listing费用
支持获取Lisitng-FBA预估费

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/listing/listing/open/api/listing/getPrices` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|data|请求数据，上限500|是|[array]| |
|data>>sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|46545|
|data>>msku|MSKU|是|[string]|ABC-MSKU|

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|error_details>>sid|店铺id|是|[int]|468546351|
|error_details>>msku|MSKU|是|[string]|MSKU001-MSKU|
|error_details>>message|错误信息|是|[string]|店铺不存在|
|request_id|请求链路id|是|[string]|81CA6A9A-A5C4-8B5E-5FED-E1C2EC04753C|
|response_time|响应时间|是|[string]|2020-12-01 12:11:12|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|46545|
|data>>msku|MSKU|是|[string]|ABC-MSKU|
|data>>fba_fee|FBA预估费|是|[number]|12.32|
|data>>fba_fee_currency_code|FBA预估费币种符号|是|[string]|USD|
|total|总数|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "request_id": "2d2c6726-1aeb-11ee-8044-5254008fbf4a",
    "response_time": "2023-07-05 12:19:47",
    "error_details": [
        {
            "sid": 101,
            "msku": "Hair-Ties-P03611",
            "message": "错误：msku：Hair-Ties-P03601,不存在"
        }
    ],
    "data": [
        {
            "sid": 101,
            "msku": "HOLDER00111",
            "fba_fee": 3.22,
            "fba_fee_currency_code": "USD"
        }
    ],
    "total": 1
}
```

## 返回失败示例
```
{
    "code": 1,
    "message": "fail",
    "request_id": "9e09d24c-f3bf-11ed-a652-0242ac130003",
    "response_time": "2023-05-16 15:59:44",
    "error_details": [
        "sid_asin_list.0.sid 类型错误,必须是正整数"
    ],
    "data": []
}
```
