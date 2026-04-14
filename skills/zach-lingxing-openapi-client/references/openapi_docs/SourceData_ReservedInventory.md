# 查询亚马逊源报表-预留库存
查询 FBA Reserved Inventory Report 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/reservedInventory` | HTTPS | POST | 5 |

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

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]| |
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sku|SKU|是|[string]|0A-TBHW-94FY0|
|data>>fnsku|FNSKU|是|[string]|X000Z8U9SPH|
|data>>asin|ASIN|是|[string]|B07NPK39V98|
|data>>product_name|品名|是|[string]|  |
|data>>reserved_qty|预留数量|是|[number]|6|
|data>>reserved_customerorders|为买家订单预留的商品数量|是|[number]|1|
|data>>reserved_fc_transfers|预留运营中心转运数量|是|[number]|3|
|data>>reserved_fc_processing|预留运营中心处理中数量|是|[number]|2|
|data>>gmt_modified|更新时间|是|[string]| &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "EEE3253E-2DB3-E6F5-5339-3D265EF5E836",
    "response_time": "2024-08-06 16:12:10",
    "data": [
        {
            "sku": "BLT0001-Green",
            "fnsku": "B0BBYP89RH",
            "asin": "B0BBYP89RH",
            "product_name": "Cute Little Bear Post It Notes Students Can Tear Messages N Times Paste Creative Cartoon Post It Notes2",
            "reserved_qty": 0,
            "reserved_customerorders": 0,
            "reserved_fc_transfers": 0,
            "reserved_fc_processing": 0,
            "gmt_modified": "2023-05-24 22:03:51"
        },
        {
            "sku": "BLT0001-Orange",
            "fnsku": "B0BBZ88H48",
            "asin": "B0BBZ88H48",
            "product_name": "Cute Little Bear Post It Notes Students Can Tear Messages N Times Paste Creative Cartoon Post It Notes",
            "reserved_qty": 0,
            "reserved_customerorders": 0,
            "reserved_fc_transfers": 0,
            "reserved_fc_processing": 0,
            "gmt_modified": "2023-05-24 22:03:49"
        }
    ],
    "total": 33
}
```