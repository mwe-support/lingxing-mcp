# SB用户搜索词报表
## 基本信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/openapi/newad/hsaQueryWordReports` | HTTPS | POST | 10 |

## 请求头

| 标签 | 必填 | 说明 | 类型 | 示例 | 
| :------------ | :------------ | :------------ | :------------ | :------------ |
|X-API-VERSION|是|【兼容旧版本】<br>不添加标签：offset 为分页页码，从1开始<br>值为 2 时：offset 为分页偏移量，从0开始|[int]|2|

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|109|
|profile_id|VC广告店铺profile_id，对应[查询广告账号列表](docs/newAd/baseData/dspAccountList)接口对应字段【profile_id】，sid跟profile_id其中一个必填|是|[int]| 123456     |
|report_date|报表日期|是|[string]|2022-06-01|
|target_type|投放类型【默认 keyword】：keyword 关键词|是|[string]|keyword|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页条数，默认15|否|[int]|15|

## 请求示例
```
{
    "sid": 109,
    "report_date": "2022-06-01",
    "target_type": "keyword",
    "offset": 0,
    "length": 15
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|52688b81-2398-4e60-9617-619fc2cf5b1e|
|response_time|响应时间|是|[string]|2023-03-20 10:14:22|
|total|总数|是|[int]|3|
|data|响应数据|是|[array]| |
|data>>query|搜索词|是|[string]|laptop stand|
|data>>target_id|投放id（关键词/商品投放 根据target_type）|是|[number]|144272087511089300|
|data>>match_type|匹配类型|是|[string]|EXACT|
|data>>target_text|投放的内容|是|[string]|laptop stand|
|data>>ad_group_id|广告组id|是|[number]|144329503293620480|
|data>>impressions|展示量|是|[number]|224|
|data>>clicks|点击量|是|[number]|1|
|data>>cost|花费|是|[number]|1.03|
|data>>profile_id|亚马逊店铺数字id|是|[number]|121923590660074|
|data>>campaign_id|广告活动id|是|[number]|144264775656379200|
|data>>report_date|报表日期|是|[string]|2021-06-23|
|data>>same_orders|直接成交订单数|是|[number]|0|
|data>>orders|订单数|是|[number]|0 |
|data>>same_sales|直接成交销售额|是|[number]| 0|
|data>>sales|销售额|是|[number]|0 |
|data>>new_to_brand_orders|品牌新买家订单数量|是|[number]|0|
|data>>new_to_brand_order_percentage|品牌新买家订单百分比|是|[number]|0|
|data>>new_to_brand_order_rate|品牌新买家转换率|是|[number]|0|
|data>>new_to_brand_sales|品牌新买家销售额|是|[number]|0|
|data>>new_to_brand_units|品牌新买家销量|是|[number]|0|
|data>>video_first_quartile_views|播放25%的次数|是|[int]|0|
|data>>video_midpoint_views|播放50%的次数|是|[int]|0|
|data>>video_third_quartile_views|播放75%的次数|是|[int]|0|
|data>>video_complete_views|播放100%的次数|是|[int]|0|
|data>>video_5_second_views|观看完整视频或 5 秒（以较短者为准）的展示次数|是|[int]|0|
|data>>video_5_second_view_rate|观看完整视频或 5 秒（以较短者为准）的展示次数百分比|是|[int]|0|
|data>>video_unmutes|取消视频静音的展示次数|是|[int]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "error_details": [],
    "request_id": "52688b81-2398-4e60-9617-619fc2cf5b1e",
    "response_time": "2023-03-20 10:14:22",
    "total": 3,
    "data": [
        {
            "query": "laptop stand",
            "target_id": 144272087511089322,
            "match_type": "EXACT",
            "target_text": "laptop stand",
            "ad_group_id": 144329503293620476,
            "impressions": 224,
            "clicks": 1,
            "cost": 1.03,
            "profile_id": 121923590660074,
            "campaign_id": 144264775656379188,
            "report_date": "2021-06-23",
            "same_orders": 0,
            "orders": 0,
            "same_sales": 0.00,
            "sales": 0.00,
            "new_to_brand_orders": 0,
            "new_to_brand_order_percentage": 0.00,
            "new_to_brand_order_rate": 0.00,
            "new_to_brand_sales": 0.00,
            "new_to_brand_units": 0,
            "video_first_quartile_views": null,
            "video_midpoint_views": null,
            "video_third_quartile_views": null,
            "video_complete_views": null,
            "video_5_second_views": null,
            "video_5_second_view_rate": null,
            "video_unmutes": null
        }
    ]
}
```
