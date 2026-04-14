# 查询FBA货件箱子、卡板标签
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/storage/shipment/printFbaLabels` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|data|请求数据|是|[array]| |
|data>>shipment_id|货件编号|是|[string]|FBA16Q9LDF2X|
|data>>page_type|页面类型：<br>PackageLabel_A4_2 - 每张A4纸打印2个标签<br>PackageLabel_A4_4 - 每张A4纸打印4个标签<br>PackageLabel_Plain_Paper - 每张美国信纸打印1个标签<br>PackageLabel_Letter_2 - 每张美国信纸打印2个标签<br>PackageLabel_Letter_6 - 每张美国信纸打印6个标签<br>PackageLabel_Thermal_NonPCP - 热敏纸(108 x 152 mm)1个标签<br>PackageLabel_Thermal_AK100 - 热敏纸(100 x 100mm)1个标签<br>PackageLabel_Thermal_AK100_Mark - 热敏纸(100 x 100mm)1个标签(带水印)|是|[string]|PackageLabel_A4_2|
|data>>num|页数【非合作承运人货件必填；合作承运人标签无法指定页数，不需要填】|否|[int]|2|
|data>>page_start_index|箱子打印的起始页，默认为1|否|[int]|1|
|hide_ship_from_company_name|隐藏ship from公司名,默认不隐藏,非必填,传值1为开启|否|[int]|1|
|hide_ship_to_company_name|传值1为隐藏ship to公司名,默认不隐藏,非必填,传值1为开启|否|[int]|1|
|print_sta_name_page|传值1为新增任务名称页,默认不新增,非必填,仅打印box箱子标签时生效,传值1为开启|否|[int]|1|
|sort_label|传值1为按箱子顺序重排,默认不按箱子顺序重排,仅打印box箱子子标签时生效(说明:不按箱子顺序重排时,打印文件...|否|[int]|1|
|type|打印类型：box 箱子标签，card 卡板标签|是|[string]|card|


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/erp/sc/storage/shipment/printFbaLabels?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "data": [{
        "shipment_id": "FBA16Q9LDF2X",
        "page_type": "PackageLabel_Plain_Paper_CarrierBottom",
        "page_start_index": 1,
        "num": 2
    }],
    "hide_ship_from_company_name": 1,
    "hide_ship_to_company_name": 1,
    "print_sta_name_page": 1,
    "sort_label": 1,
    "type": "card"
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
|total|总数|是|[int]|0|
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
    "total": 0,
    "data": {
        "file_base64": "xxx"
    }
}
```
