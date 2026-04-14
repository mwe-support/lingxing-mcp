# 查询商品折扣列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/promotion/listingList` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|site_date|站点时间，格式：Y-m-d|是|[string]|2022-04-18|
|start_time|开始时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天|否|[string]|2023-02-18|
|end_time|结束时间【活动时间】，双闭区间，格式：Y-m-d，时间间隔最长不超过90天|否|[string]|2023-04-18|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20，上限200|否|[int]|20|
|is_overlay|是否优惠叠加：<br />0  否<br />1  是|否|[int]|1|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[103]|
|status|促销状态：<br />0  其他<br />1  进行中<br />2  已过期<br />3  未开始|否|[array]|[0,1]|
|product_status|商品状态：<br />-1  已删除<br />0  停售<br />1  在售|否|[array]|[0,1]|
|promotion_category|促销类型：<br />1  优惠券<br />2  秒杀<br />3  管理促销<br />4   会员折扣|否|[array]|[1,2]|

## 返回结果

Json Object

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[array]||
|data>>item_name|商品标题|是|[string]|wallet men's wallet|
|data>>sid|店铺id|是|[string]|119|
|data>>store_name|店铺名称|是|[string]|uboss-US|
|data>>region_name|国家/地区|是|[string]|美国|
|data>>currency_icon|货币符号|是|[string]|$|
|data>>small_image_url|商品缩略图地址|是|[string]|https://xxx.com/75.jpg|
|data>>asin|ASIN|是|[string]|B0xxxxDXBV|
|data>>asin_url|ASIN跳转地址|是|[string]|https://www.amazon.com/dp/B0xxxxDXBV|
|data>>seller_sku|MSKU|是|[string]|BN-Q83M-S7I3|
|data>>promotion_list|商品优惠券|是|[array]||
|data>>promotion_list>>promotion_id|优惠券id|是|[string]|f88a4358-695b-493d-81d5-9757b4afd715|
|data>>promotion_list>>name|优惠券名称|是|[string]|Save $2 on 1115满减类型（优惠券） BV|
|data>>promotion_list>>status|优惠券状态：<br />0  其他<br />1 进行中<br />2  已过期<br />3  未开始|是|[string]|0|
|data>>promotion_list>>origin_status|优惠券平台原始状态|是|[string]|FAILED|
|data>>promotion_list>>category|促销活动类别：<br/>1  优惠券<br/>2  秒杀<br/>3  管理促销<br/>4  促销折扣|是|[string]|1|
|data>>promotion_list>>category_text|促销活动类型说明|是|[string]|优惠券|
|data>>promotion_list>>promotion_type|促销类型|是|[string]|7|
|data>>promotion_list>>promotion_type_text|促销类型说明|是|[string]|金额|
|data>>promotion_list>>discount_price|折扣价格|是|[string]|0.00|
|data>>promotion_list>>discount_rate|折扣率|是|[string]|0.00|
|data>>promotion_list>>promotion_start_time|促销开始时间|是|[string]|2022-11-15 00:00:00|
|data>>promotion_list>>promotion_end_time|促销结束时间|是|[string]|2022-12-31 00:00:00|
|data>>promotion_combo_num|折扣叠加数量|是|[int]|1|
|data>>sales_price|优惠价|是|[string]|8.11|
|data>>sales_price_usd|优惠券【美元】|是|[string]|8.10|
|data>>avg_deal_price|平均成交价|是|[string]|0.00|
|data>>discount_price_min|最低折扣价|是|[string]|0.00|
|data>>discount_rate_rate|最低折扣率|是|[string]|0.00|
|data>>principal_list|listing负责人|是|[array]|["jack"]|
|data>>listing_tags|listing标签列表|是|[string]||
|data>>listing_tags>>global_tag_id|标签id|是|[string]|907202235307626941|
|data>>listing_tags>>tag_name|标签名|是|[string]|条目|
|data>>listing_tags>>color|标签颜色|是|[string]|#5A8BF0|
|data>>afn_fulfillable_quantity|FBA可售|是|[string]|0|
|data>>quantity|FBM可售|是|[string]|0|

## 返回成功示例

```
  
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "e320d07cd2b24dfd8e075677c0eee622.159.16982279070474519",
    "response_time": "2023-10-25 17:58:32",
    "data": [
        {
            "item_name": "Multifunctional short wallet antimagnetic wallet men's wallet",
            "sid": "119",
            "store_name": "uboss-US",
            "region_name": "美国",
            "currency_icon": "$",
            "small_image_url": "https://m.media-amazon.com/images/I/31geVbfb-UL._SL75_.jpg",
            "asin": "B09335DXBV",
            "asin_url": "https://www.amazon.com/dp/B0xxxxDXBV",
            "seller_sku": "BN-Q83M-S7I3",
            "promotion_list": [
                {
                    "promotion_id": "f88a4358-695b-493d-81d5-9757b4afd715",
                    "name": "Save $2 on 1115满减类型（优惠券） BV",
                    "status": "0",
                    "origin_status": "FAILED",
                    "category": "1",
                    "category_text": "优惠券",
                    "promotion_type": "7",
                    "promotion_type_text": "金额",
                    "discount_price": "0.00",
                    "discount_rate": "0.00",
                    "promotion_start_time": "2022-11-15 00:00:00",
                    "promotion_end_time": "2022-12-31 00:00:00"
                }
            ],
            "promotion_combo_num": "1",
            "sales_price": "8.11",
            "sales_price_usd": "8.10",
            "avg_deal_price": "0.00",
            "discount_price_min": "0.00",
            "discount_rate_rate": "0.00",
            "principal_list": [
                "jack"
            ],
            "listing_tags": [
                {
                    "global_tag_id": "907202235307626941",
                    "tag_name": "家电大卖",
                    "color": "#5A8BF0"
                }
            ],
            "afn_fulfillable_quantity": "0",
            "quantity": "0"
        }
	],
    "total": 1
}
```