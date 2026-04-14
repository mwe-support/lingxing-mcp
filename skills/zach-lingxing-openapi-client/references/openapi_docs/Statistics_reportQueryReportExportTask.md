# 报告导出-查询导出任务结果
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/report/query/reportExportTask` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| seller_id | 亚马逊店铺id，[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】| 是 | [string] | A1MQMWxxxJWPNCBX |
| task_id | 任务id | 是 | [string] | f5345297-07e2-4b08-becf-a4c29335246b |
| region | 店铺所在的地区【对应区域值支持国家见附加说明】：<br />na 北美<br />eu 欧洲<br />fe 远东 | 是 | [string] | na |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[object]| |
|data>>report_document_id | 报告文件id | 是  | [string] | amzn1.spdoc.1.4.eu.7d767cf6-07e4-4e93-8c58-f10d46b88984.T5VTxxxxx88M.2651 |
|data>>progress_status | 报表生成状态：<br />IN_PROGRESS 导出中<br/>CANCELLED 已取消<br/>DONE 已完成 <br/>FATAL 导出失败<br/>IN_QUEUE 排队中<br/>UNKNOWN 未知 | 是 | [string] | DONE  |
|data>>compression_algorithm|报表内容压缩方式|是|[string]|GZIP |
|data>>url|报表下载地址【有效期5min】|是|[string]|https://xxx.comeu-west/xxxx |
## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "842d7733ef5d4d968bc6877e06c34453.1697004896752",
    "response_time": "2023-10-11 14:14:56",
    "data": {
        "report_document_id": "amzn1.spdoc.1.4.eu.7d767cf6-07e4-4e93-8c58-f10d46b88984.T5VTxxxxx88M.2651",
        "progress_status": "DONE",
        "compression_algorithm":"GZIP",
        "url":"https://xxx.comeu-west/xxxx"
    },
    "total": 0
}
```
## 返回失败示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "8b2db18e302745d8b526cd2e04f9d917.1697096479664",
    "response_time": "2023-10-12 15:41:20",
    "data": {
        "report_document_id": null,
        "progress_status": "FATAL",
        "compression_algorithm":null,
        "url":null
    },
    "total": 0
}
```



## 附加说明
### region 说明如下：

1. na【North America】：包括国家为 CA、US、MX、BR <br >
2. eu【Europe】：包括国家为 ES、UK、FR、BE、NL、DE、IT、SE、ZA、PL、EG、TR、SA、AE、IN <br >
3. fe【Far East】：包括国家为 SG、AU、JP