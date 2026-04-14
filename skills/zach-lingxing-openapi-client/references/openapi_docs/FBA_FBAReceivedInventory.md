# 查询FBA到货接收明细
查询库存分类账里货件在FBA仓库的签收数据。

注意：请求后会返回该sid对应seller_id下的所有货件签收明细，具体sid与货件对应关系，请用 [查询货件列表](docs/FBA/FBAShipmentList) 确认；同一货件商品可能存在多行签收明细，可自行汇总计算

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/fba_report/receivedInventory` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|101|
|event_date|签收日期，格式：Y-m-d，未填写fba_shipment_id时必填|是|[string]|2019-07-12|
|fba_shipment_id|货件单号，未填写event_date时必填|否|[array]|["FBA1Y4ZJFZ"]|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|100|


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/data/fba_report/receivedInventory?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
  "sid": 101,
  "event_date": "2019-07-12",
  "fba_shipment_id":["FBA1Y4ZJFZ"],
  "offset": 0,
  "length": 1000
}'
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[string]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|data|响应数据|是|[array]| |
|data>>sid|店铺id, 等于入参sid，非货件实际对应的sid。字段即将下线，具体sid与货件对应关系，请用 [查询货件列表](docs/FBA/FBAShipmentList) 确认|否|[int]|101|
|data>>received_date|接收日期|是|[string]|2018-11-04T00:00:00+00:00|
|data>>received_date_locale|当地接收日期|是|[string]|2018-11-04T01:00:00+01:00|
|data>>received_date_timestamp|接收日期时间戳|是|[int]|1541289600|
|data>>fnsku|FNSKU|是|[string]| |
|data>>sku|MSKU|是|[string]| |
|data>>product_name|Listing标题|是|[string]| |
|data>>quantity|数量|是|[number]|-5|
|data>>fba_shipment_id|货件单号|是|[string]| |
|data>>fulfillment_center_id|物流中心编码|是|[string]|BHX4|
|data>>unique_index|单内签收日期索引|是|[int]|3|
|data>>unique_md5|与unique_index组成唯一索引|是|[string]|ad971e653ad89e2c94a939df63b8c884|
|data>>received_date_report|处理过的接收日期|是|[string]|2018-11-04|
|total|总数|是|[int]|1|

## 返回成功示例
```
{
  "code": 0,
  "message": "success",
  "error_details": "",
  "request_id": "C3D9F541-8083-E376-EB5C-606A872F5C89",
  "response_time": "2022-12-08 18:27:13",
  "data": [
    {
      "sid": 101,
      "received_date": "2018-11-04T00:00:00+00:00",
      "received_date_locale": "2018-11-04T01:00+01:00",
      "received_date_timestamp": 1541289600,
      "fnsku": "FBA1Y4ZJFZ",
      "sku": "MSKU-1",
      "product_name": "Product 1",
      "quantity": -5,
      "fba_shipment_id": "FBA1Y4ZJFZ",
      "fulfillment_center_id": "BHX4",
      "unique_index": 3,
      "unique_md5": "ad971e653ad89e2c94a939df63b8c884",
      "received_date_report": "2018-11-04"
    }
  ],
  "total": 1
}
```
