# 查询FBA月仓储费
支持查询FBA月仓储费数据
<br>唯一健：sid + fnsku + month_of_charge + fulfillment_center

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/storageFeeMonth` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|month|收费月份，格式：Y-m|是|[string]|2022-10|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "month": "2022-10",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| |
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应结果|是|[array]|  |
|data>>sid|店铺id|是|[int]|1|
|data>>asin|ASIN|是|[string]|B06VSK9999|
|data>>fnsku|FNSKU|是|[string]|X001Z9999|
|data>>product_name|标题|是|[string]|5 Pack Mini LED Flashlight Ultra Bright 300 Lumens|
|data>>fulfillment_center|仓库编号|是|[string]|LGB3|
|data>>country_code|国家代码|是|[string]|US|
|data>>longest_side|长边|是|[string]|6.811|
|data>>median_side|中间边|是|[string]|4.41|
|data>>shortest_side|短边|是|[string]|1.6142|
|data>>measurement_units|长中短边单位|是|[string]|inches|
|data>>weight|重量|是|[string]|0.4409|
|data>>weight_units|重量单位|是|[string]|pounds|
|data>>item_volume|体积|是|[string]|0.0281|
|data>>volume_units|体积单位|是|[string]|cubic feet|
|data>>product_size_tier|产品标准|是|[string]|Standard-Size|
|data>>average_quantity_on_hand|库存量|是|[string]|2.16|
|data>>average_quantity_pending_removal|待移除量|是|[string]|0.0|
|data>>estimated_total_item_volume|总体积|是|[string]|0.0607|
|data>>month_of_charge|收费月份|是|[string]|2019-01|
|data>>storage_rate|收费标准|是|[string]|0.69|
|data>>currency|币种|是|[string]|USD|
|data>>estimated_monthly_storage_fee|预估仓储费|是|[string]|0.0419|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "C06A83EF-7A35-E78F-D518-2DFCAFD67114",
    "response_time": "2024-08-09 09:27:00",
    "data": [
        {
            "sid": 109,
            "asin": "B0BB389BKQ",
            "fnsku": "B0BB389BKQ",
            "product_name": "Phone Holder",
            "fulfillment_center": "AKC1",
            "country_code": "US",
            "longest_side": "2.44",
            "median_side": "1.3",
            "shortest_side": "0.35",
            "measurement_units": "inches",
            "weight": "0.04",
            "weight_units": "pounds",
            "item_volume": "0.0006",
            "volume_units": "cubic feet",
            "product_size_tier": "Standard-Size",
            "average_quantity_on_hand": "40",
            "average_quantity_pending_removal": "0",
            "estimated_total_item_volume": "0.0257",
            "month_of_charge": "2022-10",
            "storage_rate": "2.4",
            "currency": "USD",
            "estimated_monthly_storage_fee": "0.0614",
            "v_uuid": "ff16cbb4-1824-4a77-80a2-7031d1f8a1e4",
            "company_id": 90128554873982976
        },
        {
            "sid": 109,
            "asin": "B0BB9XV7CW",
            "fnsku": "B0BB9XV7CW",
            "product_name": "SUPER J Cell Phone Armband Running Armband for Iphone Samsung Sports Phone Holder Waterproof",
            "fulfillment_center": "AKC1",
            "country_code": "US",
            "longest_side": "3.94",
            "median_side": "3.94",
            "shortest_side": "3.94",
            "measurement_units": "inches",
            "weight": "0.44",
            "weight_units": "pounds",
            "item_volume": "0.0353",
            "volume_units": "cubic feet",
            "product_size_tier": "Standard-Size",
            "average_quantity_on_hand": "1",
            "average_quantity_pending_removal": "0",
            "estimated_total_item_volume": "0.0353",
            "month_of_charge": "2022-10",
            "storage_rate": "2.4",
            "currency": "USD",
            "estimated_monthly_storage_fee": "0.0842",
            "v_uuid": "67f42f4c-5e32-4c02-8270-4656ecec60f3",
            "company_id": 90128554873982976
        }
    ],
    "total": 26
}
```