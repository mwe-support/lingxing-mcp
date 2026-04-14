# 查询产品表现（旧）
支持查询系统【统计】>【产品表现】数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/sales_report/asinList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|asin_type|产品表现维度：【默认0】<br>0 asin<br>1 父asin|否|[int]|0|
|start_date|报表时间，格式：Y-m-d，闭区间|是|[string]|2024-08-01|
|end_date|报表时间，格式：Y-m-d，开区间|是|[string]|2024-08-01|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "asin_type": 0,
    "start_date": "2024-08-01",
    "end_date": "2024-08-01",
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
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|1|
|data>>id|id|是|[int]|179|
|data>>gmt_modified|更新时间|是|[string]|2020-10-15 14:17:12|
|data>>price|单价|是|[string]| |
|data>>asin|ASIN|是|[string]|B00NANNJLQ|
|data>>small_image_url|商品图片链接|是|[string]|https://m.media-amazon.com/images/I/51nhvPT08aL._SL75_.jpg|
|data>>item_name|标题|是|[string]|Tontec 3.5 Inches Touch Screen for Raspberry Pi Display TFT Monitor 480x320 LCD Touchscreen Kit with Transparent Case for Raspberry Pi 2 Model B and Raspberry Pi B+|
|data>>cid|种类id|是|[int]| |
|data>>bid|品牌id|是|[int]| |
|data>>avaiable_days|可售天数预估|是|[string]|0.0|
|data>>order_items|订单量|是|[string]| |
|data>>volume|销量|是|[string]| |
|data>>amount|销售额|是|[string]|0.00|
|data>>sessions_browser|Sessions_Browser|是|[string]| |
|data>>sessions_total|Sessions_Total|是|[string]| |
|data>>sessions_mobile|Sessions_Mobile|是|[string]| |
|data>>buy_box_percentage|Buybox|是|[string]|0.000000|
|data>>page_views_browser|PV_Browser|是|[string]| |
|data>>page_views_total|PV_Total|是|[string]| |
|data>>page_views_mobile|PV_Mobile|是|[string]| |
|data>>clicks|点击量|是|[string]| |
|data>>impressions|展示量|是|[string]| |
|data>>total_spend|广告花费|是|[string]|0.00|
|data>>ctr|CTR|是|[string]|0.0000|
|data>>avg_cpc|CPC|是|[string]|0.00|
|data>>rank|大类排名|是|[string]| |
|data>>reviews|评论数|是|[string]| |
|data>>avg_star|评分|是|[number]| |
|data>>conversion_rate|转化率|是|[string]|0.0000|
|data>>total_spend_rate|总转化率|是|[string]|0.000000|
|data>>afn_fulfillable_quantity|FBA可售|是|[string]| |
|data>>reserved_fc_transfers|待调仓|是|[string]| |
|data>>reserved_fc_processing|调仓中|是|[string]| |
|data>>reserved_customerorders|调仓|是|[string]| |
|data>>afn_inbound_shipped_quantity|入库中|是|[string]| |
|data>>afn_unsellable_quantity|不可售|是|[string]| |
|data>>afn_inbound_receiving_quantity|在途|是|[string]| |
|data>>afn_inbound_working_quantity|计划入库|是|[string]| |
|data>>acos|ACOS|是|[string]|0.0000|
|data>>acoas|ACoAS|是|[string]| |
|data>>order_quantity|广告订单量|是|[string]| |
|data>>category|类别|是|[string]| |
|data>>pid|商品id|是|[int]|58|
|data>>adv_rate|广告订单量占比|是|[string]| |
|data>>sales_amount|广告销售额|是|[string]|0.00|
|data>>ad_cvr|广告CVR|是|[string]|0.0000|
|data>>asoas|ASOAS|是|[string]| |
|data>>remark|asin备注数组，格式[{"date": "***", "content": "***"}]|是|[array]|                                                              |
|data>>smallRankList|小类排名数组，格式[{"smallRankName": "***", "rankValue": "***"}]|是|[array]| &nbsp; |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "E0DD8407-9B19-5D26-2E4D-47EE98F817AD",
    "response_time": "2024-08-08 19:07:27",
    "data": [
        {
            "sid": 109,
            "id": 171855,
            "status": 0,
            "gmt_modified": "2023-04-03 11:41:44",
            "price": "",
            "asin": "B07Q8WHQKC",
            "small_image_url": "https://m.media-amazon.com/images/I/41xlxlwEsXL._SL75_.jpg",
            "item_name": "Zontek MS001 Adjustable Monitor Stand - Ergonomic Desk Organizer",
            "cid": 0,
            "bid": 0,
            "currency_code": "USD",
            "avaiable_days": "0.0",
            "order_items": "0",
            "volume": "0",
            "amount": "0.00",
            "sessionsTotal": "0",
            "sessionsBrowser": "0",
            "sessionsMobile": "0",
            "PVTotal": "0",
            "PVBrowser": "0",
            "PVMobile": "0",
            "buy_box_percentage": "0.000000",
            "clicks": "0",
            "impressions": "0",
            "total_spend": "0.00",
            "ctr": "0.0000",
            "avg_cpc": "0.00",
            "rank": "0",
            "reviews": "0",
            "avg_star": 0,
            "conversion_rate": "0.0000",
            "total_spend_rate": "0.000000",
            "afn_fulfillable_quantity": "0",
            "reserved_fc_transfers": "0",
            "reserved_fc_processing": "0",
            "reserved_customerorders": "0",
            "afn_inbound_shipped_quantity": "0",
            "afn_unsellable_quantity": "0",
            "afn_inbound_receiving_quantity": "0",
            "afn_inbound_working_quantity": "0",
            "acos": "0.0000",
            "acoas": "0",
            "order_quantity": "0",
            "category": "",
            "pid": 32610,
            "adv_rate": "0",
            "sales_amount": "0.00",
            "asoas": "0",
            "ad_cvr": "0.0000",
            "remark": [],
            "smallRankList": []
        }
    ],
    "total": 3803
}
```