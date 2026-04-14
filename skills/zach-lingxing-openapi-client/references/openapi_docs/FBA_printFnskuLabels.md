# 查询FBA货件商品FNSKU标签
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/storage/shipment/printFnskuLabels` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|data| |是|[array]| |
|data>>shipment_id|货件编号|是|[string]|FBA16RKY2ZNR|
|data>>num|标签打印个数|是|[int]|20|
|data>>seller_sku|MSKU|是|[string]|Black_ Head_Rope|
|data>>fnsku|FNSKU|是|[string]|B09MT3989Q|
|page_type|标签页面类型：<br>SINGLE_COL_50_30 热敏纸【50X30】单排<br>SINGLE_COL_70_30 热敏纸【70X30】单排<br>DOUBLE_COL_100_30 热敏纸【100X30】双排<br>A4_FOUR_COL_40 A4纸【每页40个标签】四排<br>A4_FOUR_COL_44 A4纸【每页44个标签】四排<br>US_LETTER_THREE_COL_30 美国信纸【每页30个标签】三排|是|[string]|DOUBLE_COL_100_30|
|print_content|是否打印：【默认yes】<br>yes 是<br>no 否|否|[string]|yes|
|content_type|打印SKU/品名：【默认sku】<br>sku SKU<br>sku_name 品名|否|[string]|sku|
|print_custom|是否打印自定义内容：【默认yes】<br>yes 是<br>no 否|否|[string]|yes|
|custom_content|自定义内容，默认MADE IN CHINA|否|[string]| |
|new_tag|标签中是否显示‘new’字样：【默认yes】<br>yes 是<br>no 否|否|[string]|yes|


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/storage/shipment/printFnskuLabels?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
  "data": [{
      "shipment_id": "FBA16RKY2ZNR",
      "num": 20,
      "seller_sku": "Black_ Head_Rope",
      "fnsku": "B09MT3989Q",
  }],
  "page_type": "DOUBLE_COL_100_30",
  "print_content": "yes",
  "content_type": "sku",
  "print_custom": "yes",
  "custom_content": "MADE IN CHINA",
  "new_tag": "yes"
}'
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|17036564-84C9-554E-5225-BEFE9A3733EC|
|response_time|响应时间|是|[string]|2022-07-04 18:40:49|
|total|总数|是|[int]|1|
|data|响应数据|是|[object]| |
|data>>file_base64|成功时，将返回打印PDF文件的base64编码|是|[string]|xxx|


## 返回成功示例
```
{
  "code": 0,
  "message": "success",
  "error_details": [],
  "request_id": "17036564-84C9-554E-5225-BEFE9A3733EC",
  "response_time": "2022-07-04 18:40:49",
  "total": 1,
  "data": {
    "file_base64": "xxx"
  }
}
```