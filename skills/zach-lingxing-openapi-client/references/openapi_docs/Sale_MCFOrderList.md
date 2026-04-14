# 查询亚马逊多渠道订单列表-v2
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/order/amzod/api/orderList` | HTTPS | POST | 1 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[43,19,17,16,22]|
|start_date|订购时间-开始（不传默认最近6个月），格式：Y-m-d|否|[string]|2022-12-13|
|end_date|订购时间-结束（不传默认最近6个月），格式：Y-m-d|否|[string]|2022-12-14|
|date_type|查询日期类型：1 订购时间【默认值】，2 订单修改时间|否|[int]|1|
|order_status|订单状态列表，枚举值：NEW（待发货-待验证），RECEIVED（待发货-待处理），PLANNING（待发货-准备中），PROCESSING（待发货-处理中），CANCELLED（已取消），COMPLETE（已发货），COMPLETE_PARTIALLED（已发货-部分发货），UNFULFILLABLE（无法发货），INVALID（无法验证）；注意大小写敏感，请用大写枚举值|否|[array]|[NEW,RECEIVED,PLANNING]|
|offset|分页偏移量|是|[int]|0|
|length|分页长度，默认10，上限1000|是|[int]|20|

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|65b8587be2f545938d083d63280e1f81.93.16886966334816063|
|response_time|响应时间|是|[string]|2023-07-07 10:23:54|
|data|响应数据|是|[object]| |
|data>>total|总数|是|[int]|1|
|data>>records|记录|是|[array]| |
|data>>records>>remark|备注|是|[string]|备注|
|data>>records>>sid|店铺id|是|[int]|17|
|data>>records>>store_name|店铺名称|是|[string]|8speed-US|
|data>>records>>country|国家|是|[string]|美国|
|data>>records>>amazon_order_id|亚马逊订单号|是|[string]|S01-6274054-1946049|
|data>>records>>seller_fulfillment_order_id|卖家订单号|是|[string]|332565|
|data>>records>>gmt_modified|更新时间|是|[string]|2022-12-12 17:45:15|
|data>>records>>last_update_time|最近更新时间|是|[string]|2023-02-10 18:45:11|
|data>>records>>order_status|订单状态|是|[string]|Cancelled|
|data>>records>>purchase_date_local|订购时间|是|[string]|2023-02-07 20:48:19|
|data>>records>>ship_date|发货时间（站点时间）|是|[string]|2023-05-22 20:00:00|
|data>>records>>ship_date_utc|发货时间（UTC时间）|是|[string]|2023-05-23T03:00:00Z|
|data>>records>>listing_info|商品信息|是|[array]| |
|data>>records>>listing_info>>msku|msku|是|[string]|Pink_Head_Rope|
|data>>records>>listing_info>>quantity|数量|是|[int]|0|
|data>>records>>listing_info>>fnsku|fnsku|是|[string]| B08D3N9BK3 |
|data>>records>>listing_info>>local_sku|本地产品sku|是|[string]|yigexiangtong1|
|data>>records>>listing_info>>local_name|品名|是|[string]|有一个单品相同1|
|data>>records>>listing_info>>item_name|商品名称|是|[string]|Love Pearl Bottom Hair Circle |
|data>>records>>listing_info>>small_image_url|图片地址|是|[string]|https://xxx/K1L._SL75_.jpg|
|data>>records>>listing_info>>asin|asin|是|[string]|B09MERTKGH|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "65b8587be2f545938d083d63280e1f81.93.16886966334816063",
    "response_time": "2023-07-07 10:23:54",
    "data": {
        "total": 1,
        "records": [
            {
                "remark": "备注",
                "sid": 17,
                "store_name": "8speed-US",
                "country": "美国",
                "amazon_order_id": "S01-6274054-1946049",
                "seller_fulfillment_order_id": "332565",
                "last_update_time": "2023-02-10 18:45:11",
		        "gmt_modified": "2023-02-10 18:45:11",
                "order_status": "Cancelled",
                "purchase_date_local": "2023-02-07 20:48:19",
                "buyer_name": "Tena Nguyen",
                "ship_date": "2023-05-22 20:00:00",
                "ship_date_utc": "2023-05-23T03:00:00Z",
                "listing_info": [
                    {
                        "msku": "Pink_Head_Rope",
                        "quantity": 0,
                        "fnsku": "",
                        "local_sku": "yigexiangtong1",
                        "item_name": "Love Pearl Bottom Hair Circle Women's High Elastic Hair Binding Rope Jewelry Rubber Band Head Rope Pink kara tao.",
                        "local_name": "有一个单品相同1",
                        "small_image_url": "https://m.media-amazon.com/images/I/71y9Dp8vK1L._SL75_.jpg",
                        "asin": "B09MERTKGH"
                    }
                ]
            }
        ]
    }
}
```
