# 查询FBA商品信息列表
创建货件计划需要的商品信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/shipment/getFbaProductList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[17]|
|search_field|模糊搜索字段：【搜索时支持以下单个字段】<br>msku=>MSKU<br>fnsku=>FNSKU<br>asin=>ASIN<br>sku=>SKU<br>title=>标题<br>product_name=>品名|否|[string]|msku|
|search_value|搜索值【对应搜索字段的值】|否|[string]|MSKU789fhdjk|
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认20|是|[int]|20|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2021-04-18 10:19:48|
|total|总数|是|[int]|11|
|data|响应数据|是|[array]| |
|data>>image|图片|是|[string]|https://m.media-amazon.com/images/I/xxxxx._SL75_.jpg|
|data>>msku|MSKU|是|[string]|xxxxxx|
|data>>fnsku|FNSKU|是|[string]|xxxxx|
|data>>asin|ASIN|是|[string]|xxxxx|
|data>>asin_url|ASIN对应亚马逊页面地址|是|[string]|https://www.amazon.com/dp/xxxx|
|data>>parent_asin|父ASIN|是|[string]|xxxxx|
|data>>title|标题|是|[string]|Lxxxxnding xxxxBand Hxxxx Black|
|data>>local_name|品名|是|[string]|123|
|data>>sku|sku|是|[string]|123|
|data>>product_id|产品id|是|[int]|6516|
|data>>sid|店铺id|是|[int]|17|

