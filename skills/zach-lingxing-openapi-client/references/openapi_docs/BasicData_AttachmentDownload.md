# 下载附件
支持下载产品附件

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/common/file/download` | HTTPS | POST | 1 |

## 请求参数
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|file_id|附件id【取对应功能接口返回结果中的附件id值】|是|[int]|1209|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示消息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|100CF568-0228-E962-B810-82EAA06EA7CC|
|response_time|响应时间|是|[string]|2023-05-24 10:21:07|
|total|总数|是|[int]|0|
|data|响应数据|是|[object]| |
|data>>file_name|文件名|是|[string]|16327122625224.xlsx|
|data>>mime_type|文件类型|是|[string]|application/vnd.openxmlformats-officedocument.spreadsheetml.sheet|
|data>>content|base64 编码的文件内容|是|[string]|UEsDBBQ2a9j72XrfcmVscysACwDRAgAAYBYAAAAAxxxxxxxxxxxxx|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "100CF568-0228-E962-B810-82EAA06EA7CC",
    "response_time": "2023-05-24 10:21:07",
    "data": {
        "file_name": "16327122625224.xlsx",
        "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "content": "UEsDBBQ2a9j72XrfcmVscysACwDRAgAAYBYAAAAAxxxxxxxxxxxxx"
    },
    "total": 0
}
```
