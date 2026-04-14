# 查询销量统计列表v2

## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/platformStatisticsV2/saleStat/pageList` | HTTPS | POST | 1 |


## 请求参数

| 参数名| 说明| 必填 | 类型 | 示例|
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| :------------ | :------------ |:-------------|
| start_date| 开始日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天|是|[string]| 2022-10-03|
| end_date | 结束日期【下单时间】，格式：Y-m-d，时间间隔最长不超过90天|是|[string]| 2022-12-23|
| result_type | 汇总类型： <br>1 销量 <br>2 订单量<br> 3 销售额|是|[string]| 2|
| date_unit| 统计时间指标：<br>1 年 <br>2 月 <br>3 周 <br>4 日|是|[string]| 4|
| page| 分页页码，默认1|否|[int]| 1|
| length| 分页大小，默认20|否|[int]| 20|
| data_type| 统计数据维度： <br>1 ASIN <br>2 父体 <br>3 MSKU <br>4 SKU <br>5 SPU <br>6 店铺|是|[string]| 4|
| sids| 店铺id，多个使用英文逗号分隔。<br>如果id属于亚马逊店铺id，则对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】 <br>如果id属于多平台店铺id，则对应[查询多平台店铺信息](docs/MultiPlatform/V2/StoreInfoV2)接口对应字段【store_id】 |否|[array]| ["123","35"] |

## 请求cURL示例
```
curl --location --request POST 'https://openapi.lingxing.com/basicOpen/platformStatisticsV2/saleStat/pageList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data-raw '{
 "start_date": "2022-10-03",
 "end_date": "2022-12-23",
 "data_type": "4",
 "result_type": "1",
 "date_unit": "2",
 "page": 1,
 "length": 20,
 "sids":
[
"110000000018005095",
"110000000018006001",
"110000000018006003",
"110000000018006002"
]
}'

```

## 返回结果

| 参数名| 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :---------- |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]||
|response_time|响应时间|是|[string]|2024-12-02 09:29:46|
|data|响应数据|是|[array]| |
|data>>pic_url|图片地址|否|[string]||
|data>>sku|SKU|否|[array]|["wjc0_sku"]|
|data>>spu|SPU|否|[array]| |
|data>>spu_name|SPU名称|否|[array]| |
|data>>msku|MSKU|否|[array]||
|data>>mskuId|MSKU_id|否|[array]||
|data>>sid|店铺id|是|[array]| |
|data>>skuAndProductName|品名/SKU|否|[array]||
|data>>product_name|品名|是|[array]|["w_pm"]|
|data>>develop_name|开发人名称|是|[array]||
|data>>platform_code|平台编码|是|[array]|["10006"]|
|data>>platform_name|平台名称|是|[array]|["Walmart"]|
|data>>attribute|单体属性|否|[array]||
|data>>parentAsin|父体|否|[array]||
|data>>site_code|站点编码|是|[array]||
|data>>site_name|站点名称|是|[array]||
|data>>store_name|店铺名称|是|[array]|["10006-SG"]|
|data>>currency_code|币种|是|[string]|USD|
|data>>icon|币种符号|是|[string]||
|data>>date_collect|数据明细|是|[string]|{"2022-12-16":"1","2022-12-27":"1","2022-12-26":"1","2022-12-15":"3","2022-12-29":"3","2022-12-07":"1"}|
|data>>volumeTotal|明细小计|是|[string]|10|
|data>>platform_product_id|平台商品id|是|[array]| |
|data>>platform_product_title|标题|是|[array]| |
|total|总数|是|[int]|1|

## 返回成功示例
```
{
 "code": 0,
 "message": "success",
 "error_details": [],
 "request_id": "8b0547c62b8d4255ab606572a4fb756e.1733102982114",
 "response_time": "2024-12-02 09:29:46",
 "data": [{
"pic_url": "https://image.distributetop.com/erp-vue/901157321452879872/20230109/81436529358845e3837c508bd97094f5.jpeg",
"sku": ["wjc0_sku"],
"spu": [],
"spu_name": [],
"msku": "[\"TVS001-V2-YW180-RR\"]",
"mskuId": ["BF003-GY-Q-RR"],
"sid": [],
"skuAndProductName": ["ueeshop1111"],
"product_name": ["wjc0_pm"],
"develop_name": ["吴玖橙"],
"platform_code": ["10006"],
"platform_name": ["Walmart"],
"attribute": [],
"parentAsin": [],
"site_code": ["10006-SG"],
"site_name": ["[Shopee].新加坡"],
"store_name": ["test18自创Shopee测试店铺01号2"],
"currency_code": "USD",
"icon": "\"￥\"",
"date_collect": "{\"2022-12-16\":\"1\",\"2022-12-27\":\"1\",\"2022-12-26\":\"1\",\"2022-12-15\":\"3\",\"2022-12-29\":\"3\",\"2022-12-07\":\"1\"}",
"volumeTotal": 10,
"platform_product_id": [],
"platform_product_title": []
 }],
 "total": 1
}
```