# 查询FBA长期仓储费
查询FBA仓库长期仓储费数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/storageFeeLongTerm` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|start_date|收费日期，左闭区间|是|[string]|2020-01-01|
|end_date|收费日期，右开区间|是|[string]|2024-08-05|
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

| 参数名  | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| 0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sid|店铺id|是|[int]|6|
|data>>snapshot_date|时间|是|[string]|2018-08-15T08:00:00+00:00|
|data>>sku|SKU|是|[string]|KT11A17058-9999|
|data>>fnsku|FNSKU|是|[string]|X001GG2999|
|data>>asin|ASIN|是|[string]|B0734R9999|
|data>>product_name|标题|是|[string]|Premium Slim Belt Waist Trainer Workout Enchancer|
|data>>condition|状况|是|[string]|No Listing|
|data>>qty_charged_12_mo_long_term_storage_fee|12个月以上收费商品量|是|[string]| |
|data>>per_unit_volume|单个商品体积|是|[string]|0.0|
|data>>currency|币种|是|[string]|USD|
|data>>12_mo_long_terms_storage_fee|12个月以上收费|是|[string]|0.00|
|data>>qty_charged_6_mo_long_term_storage_fee|6-12个月收费商品量|是|[string]|1|
|data>>6_mo_long_terms_storage_fee|6-12个月收费|是|[string]|0.00|
|data>>volume_unit|体积单位|是|[string]|ft3|
|data>>country|国家|是|[string]|US|
|data>>is_small_and_light|是否是亚马逊轻小商品计划：Y 是，N 否, 空表示未知|是|[string]|N|
|data>>enrolled_in_small_and_light|是否注册亚马逊轻小商品计划：Y 是，N 否|是|[string]|N|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "FB044F29-4928-B5EB-CB23-1EAE8E20603B",
    "response_time": "2024-08-08 19:51:22",
    "data": [
        {
            "sid": 109,
            "snapshot_date": "2022-10-15T08:00:00+00:00",
            "snapshot_date_timestamp": 1665820800,
            "sku": "BPE-14-1",
            "fnsku": "B09MT9BKGH",
            "asin": "B09MT9BKGH",
            "product_name": "Love Pearl Bottom Hair Circle Women's High Elastic Hair Binding Rope Jewelry Rubber Band Head Rope Pink kara tao.",
            "condition": "Used",
            "qty_charged_12_mo_long_term_storage_fee": "0",
            "per_unit_volume": "0.0016",
            "currency": "USD",
            "12_mo_long_terms_storage_fee": "0",
            "qty_charged_6_mo_long_term_storage_fee": "1",
            "6_mo_long_terms_storage_fee": "0",
            "volume_unit": "cubic_feet",
            "country": "US",
            "is_small_and_light": "",
            "enrolled_in_small_and_light": "N"
        },
        {
            "sid": 109,
            "snapshot_date": "2023-04-15T08:00:00+00:00",
            "snapshot_date_timestamp": 1681545600,
            "sku": "HOLDER001",
            "fnsku": "B0BB389BKQ",
            "asin": "B0BB389BKQ",
            "product_name": "Phone Holder",
            "condition": "New",
            "qty_charged_12_mo_long_term_storage_fee": "0",
            "per_unit_volume": "0.0006",
            "currency": "USD",
            "12_mo_long_terms_storage_fee": "0",
            "qty_charged_6_mo_long_term_storage_fee": "198",
            "6_mo_long_terms_storage_fee": "0.14",
            "volume_unit": "cubic_feet",
            "country": "US",
            "is_small_and_light": "",
            "enrolled_in_small_and_light": ""
        }
    ],
    "total": 12
}
```