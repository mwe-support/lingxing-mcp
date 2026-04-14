# 查询亚马逊多渠道订单详情-商品信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/order/amzod/api/orderDetails/productInformation` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|order_info|订单信息，上限200|是|[array]| |
|order_info>>sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|17|
|order_info>>seller_fulfillment_order_id|卖家订单号|是|[string]|quan332122-R|

## 请求示例
```
{
    "order_info": [
        {
            "sid": 109,
            "seller_fulfillment_order_id": "669-R-R"
        }
    ]
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|65b8587be2f545938d083d63280e1f81.93.16886972699286111|
|response_time|响应时间|是|[string]|2023-07-07 10:34:30|
|data|响应数据|是|[array]| |
|data>>remark|备注|是|[string]|商品备注|
|data>>phone|电话|是|[string]|暂停显示|
|data>>sid|店铺id|是|[int]|17|
|data>>store_name|店铺名称|是|[string]|8sxx-US|
|data>>amazon_order_id|平台订单号|是|[string]|S01-6631496-6928415|
|data>>seller_fulfillment_order_id|卖家订单号|是|[string]|WO103315548688220672|
|data>>displayable_order_comment|装箱单备注|是|[string]|Thank you for your order!|
|data>>order_status|订单状态|是|[string]|Processing|
|data>>sales_channel|销售渠道|是|[string]|Non-Amazon|
|data>>purchase_date_local|提交时间|是|[string]|2023-05-22 15:31:09|
|data>>ship_date|发货时间（北京时间）|是|[string]|2023-05-22 20:00:00|
|data>>ship_date_utc|发货时间（utc时间）|是|[string]|2023-05-23T03:00:00Z|
|data>>speed_category|配送服务|是|[string]|加急配送|
|data>>ship_date_locale_norm|发货时间（站点时间）|是|[string]|2023-05-22 20:00:00|
|data>>ship_date_locale_iso|发货时间ISO格式（站点时间）|是|[string]|2023-05-22T20:00:00-7:00|
|data>>listing_detail_info|商品信息|是|[array]| |
|data>>listing_detail_info>>asin|asin|是|[string]|B0BB300BKQ|
|data>>listing_detail_info>>fnsku|fnsku|是|[string]|fnsku123|
|data>>listing_detail_info>>quantity|数量|是|[int]|1|
|data>>listing_detail_info>>small_image_url|图片地址|是|[string]|https://m.media-amazon.com/images/I/41ow-ZIF5qL._SL75_.jpg|
|data>>listing_detail_info>>local_name|品名|是|[string]|HO|
|data>>listing_detail_info>>local_sku|本地产品sku|是|[string]|HO|
|data>>listing_detail_info>>msku|msku|是|[string]|HOLDER001|
|data>>listing_detail_info>>item_name|商品名称|是|[string]|Phone Holder|
|data>>listing_detail_info>>cancelled_quantity|已取消数量|是|[int]|0|
|data>>listing_detail_info>>unfulfillable_quantity|不可售数量|是|[int]|0|
|data>>listing_detail_info>>shipped_quantity|已发货数量|是|[int]|1|
|data>>listing_detail_info>>fba_fee|   FBA费 |  是 |  string |  -44.18|

## 返回成功示例

```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "65b8587be2f545938d083d63280e1f81.120.16887014368825201",
    "response_time": "2023-07-07 11:43:57",
    "data": [
        {
            "remark": "商品备注",
            "phone": "暂停显示",
            "sid": 17,
            "store_name": "8sxx-US",
            "amazon_order_id": "S01-6631496-6928415",
            "seller_fulfillment_order_id": "WO103315548688220672",
            "displayable_order_comment": "",
            "order_status": "Processing",
            "sales_channel": "",
            "purchase_date_local": "2023-05-22 15:31:09",
            "ship_date": null,
            "ship_date_utc": null,
            "speed_category": "加急配送",
            "listing_detail_info": [
                {
                    "asin": "B0BB300BKQ",
                    "fnsku": "",
                    "quantity": 1,
                    "small_image_url": "https://m.media-amazon.com/images/I/41ow-ZIF5qL._SL75_.jpg",
                    "local_name": "HO",
                    "local_sku": "HO",
                    "msku": "HOLDER001",
                    "item_name": "Phone Holder",
                    "cancelled_quantity": 0,
                    "unfulfillable_quantity": 0,
                    "shipped_quantity": 1,
                    "fba_fee": "-44.18"
                }
            ],
        }
    ]
}
```
