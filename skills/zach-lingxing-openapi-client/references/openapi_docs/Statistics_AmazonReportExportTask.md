# 报告导出 - 报告下载链接续期

## 接口信息

| API Path | 请求协议  | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:------| :------------ | :------------ |
| `/basicOpen/report/amazonReportExportTask` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明      | 必填 | 类型 | 示例            |
| :------------ |:--------| :------------ | :------------ |:--------------|
|region| 店铺所在的地区【对应区域值支持国家见附加说明】：<br />na 北美<br />eu 欧洲<br />fe 远东 |是|[string]| na|
|seller_id| 亚马逊店铺id，[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|是|[string]| A1xxxxxxx |
|report_document_id| 报告文档Id,[报告导出-查询导出任务结果](docs/Statistics/reportQueryReportExportTask)接口对应字段【data>>report_document_id】|是|[string]| amzn1.xxxxxxxx |

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/report/amazonReportExportTask?access_token=value&sign=value&timestamp=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "region": "value",
    "seller_id": "value",
    "report_document_id": "value"
}'

```
## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例      |
| :------------ | :------------ | :------------ | :------------ |:--------|
|code|状态码，0：成功|是|[int]| 0       |
|message|消息提示|是|[string]| success |
|error_details|数据校验失败时的错误详情|是|[array]|         |
|request_id|请求链路Id|是|[string]|         |
|response_time|响应时间|是|[string]|         |
|data|响应数据|是|[object]|         |
|data>>url|亚马逊报告下载链接|是|[string]|         |
|data>>report_document_id|报告文档Id|是|[string]|         |
|total|总数|是|[int]| 0       |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "",
    "response_time": "",
    "data": {
        "url": "",
        "report_document_id": ""
    },
    "total": 0
}
```