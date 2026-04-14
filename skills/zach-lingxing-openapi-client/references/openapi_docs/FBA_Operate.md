# 查询异步任务状态
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/task-plan/operate` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|taskId|操作任务号|是|[string]| ||

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/task-plan/operate?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "taskId": "操作任务号"
}'
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功|是|[int]|	0 |
|message|消息提示 |是|[string]|success |
|errorDetails|错误信息 |是|[array]| |
|requestId| 请求链路id|是|[string]| |
|responseTime|响应时间 |是|[string]| 2020-05-18 11:23:47|
|data| 响应数据|是|[object]| |
|data>>errorMsg|错误信息|是|[string]| |
|data>>inboundPlanId|亚马逊任务编号|是|[string]| |
|data>>taskId|任务id|是|[string]| |
|data>>taskStatus|任务状态<br>process<br>success<br>failure<br>local_failure|是|[string]| ||


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": [],
    "requestId": "3b3d867e7d014971a580549f107c8c5a.1732773886069",
    "responseTime": "2024-11-28T14:04:46.069",
    "data": {
        "errorMsg": "错误信息",
        "inboundPlanId": "亚马逊任务编号",
        "taskId": "任务id",
        "taskStatus": "任务状态"
    }
}
```