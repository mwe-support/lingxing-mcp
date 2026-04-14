# 查询亚马逊源报表-FBA库存
查询 FBA Manage Inventory 报表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/mws_report/manageInventory` | HTTPS | POST | 5 |

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
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|2C1A1C68-395F-C1A0-5639-9AF0A5BE08A4|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>sku|MSKU|是|[string]|0A-TBHW-4FY0|
|data>>fnsku|FNSKU|是|[string]|X000Z98USPH|
|data>>asin|ASIN|是|[string]|B07NPK93V98|
|data>>product_name|品名|是|[string]|  |
|data>>condition|商品的状况|是|[string]|Unknown|
|data>>mfn_listing_exists|商品是否由卖家自行配送|是|[string]|  |
|data>>mfn_fulfillable_quantity|您的配送网络中可取件、包装和配送的商品数量|是|[number]| |
|data>>afn_listing_exists|商品是否由亚马逊物流配送|是|[string]|  |
|data>>afn_warehouse_quantity|亚马逊运营中心内某个 SKU 的已处理商品数量|是|[number]|198|
|data>>afn_fulfillable_quantity|亚马逊运营中心内某个 SKU 可取件、包装和配送的商品数量|是|[number]|197|
|data>>afn_unsellable_quantity|亚马逊运营中心内某个 SKU 处于不可售状况的商品数量|是|[number]|1|
|data>>afn_reserved_quantity|亚马逊运营中心内某个 SKU 目前正在进行内部处理（如取件、包装和配送或留作测量、取样等）的商品数量|是|[number]| |
|data>>afn_total_quantity|入库货件或亚马逊运营中心内某个 SKU 的商品总数量：(afn-total-quantity) = (afn-warehouse-quantity) + (afn-inbound-working-quantity) + (afn-inbound-shipped-quantity) + (afn-inbound-receiving-quantity)|是|[number]|198|
|data>>per_unit_volume| |是|[string]|0.00|
|data>>afn_inbound_working_quantity|您已通知亚马逊的入库货件中某个 SKU 的商品数量|是|[number]| |
|data>>afn_inbound_shipped_quantity|您已通知亚马逊并提供追踪编码的入库货件中某个 SKU 的商品数量|是|[number]| |
|data>>afn_inbound_receiving_quantity|某个 SKU 抵达亚马逊运营中心等待处理的商品数量|是|[number]| |
|data>>your_price|您当前的销售价格|是|[number]|0.00|
|data>>cg_price|采购：采购成本（人民币）|是|[number]|0.00|
|data>>landed_price|卖家自己产品的销售价格|是|[number]|0.00|
|data>>gmt_modified|更新时间|是|[string]| &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "7E6545C5-E5FB-A761-B405-80143E321385",
    "response_time": "2024-08-06 16:02:47",
    "data": [
        {
            "sku": "BLT0001-Green",
            "fnsku": "B0BBYP89RH",
            "asin": "B0BBYP89RH",
            "product_name": "Cute Little Bear Post It Notes Students Can Tear Messages N Times Paste Creative Cartoon Post It Notes2",
            "condition": "New",
            "mfn_listing_exists": "Yes",
            "mfn_fulfillable_quantity": 34,
            "afn_listing_exists": "No",
            "afn_warehouse_quantity": 0,
            "afn_fulfillable_quantity": 0,
            "afn_unsellable_quantity": 0,
            "afn_reserved_quantity": 0,
            "afn_total_quantity": 0,
            "per_unit_volume": "0.00",
            "afn_inbound_working_quantity": 0,
            "afn_inbound_shipped_quantity": 0,
            "afn_inbound_receiving_quantity": 0,
            "your_price": "5.00",
            "cg_price": "0.00",
            "landed_price": "8.35",
            "gmt_modified": "2023-05-24 21:42:09"
        },
        {
            "sku": "BLT0001-Orange",
            "fnsku": "B0BBZ88H48",
            "asin": "B0BBZ88H48",
            "product_name": "Cute Little Bear Post It Notes Students Can Tear Messages N Times Paste Creative Cartoon Post It Notes",
            "condition": "New",
            "mfn_listing_exists": "Yes",
            "mfn_fulfillable_quantity": 3,
            "afn_listing_exists": "No",
            "afn_warehouse_quantity": 0,
            "afn_fulfillable_quantity": 0,
            "afn_unsellable_quantity": 0,
            "afn_reserved_quantity": 0,
            "afn_total_quantity": 0,
            "per_unit_volume": "0.00",
            "afn_inbound_working_quantity": 0,
            "afn_inbound_shipped_quantity": 0,
            "afn_inbound_receiving_quantity": 0,
            "your_price": "6.01",
            "cg_price": "0.00",
            "landed_price": "3.01",
            "gmt_modified": "2023-05-24 21:42:06"
        }
    ],
    "total": 33
}
```