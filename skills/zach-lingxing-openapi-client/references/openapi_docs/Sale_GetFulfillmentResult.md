# 查询亚马逊标发结果
此接口用于查询亚马逊标发操作的结果。单次请求最多可查询10条数据。
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/pb/mp/order/getFulfillmentResult` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|是|[string]|A1MQMW3JWPNCBX|
|task_id|任务id【提交标发接口返回】，单次请求最多支持查询10个任务ID。|是|[array]|[1003083]|

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|操作成功|
|request_id|请求链路id|是|[string]|fb53cd0f457f40c5951b8619b77776a8.151.16759105764670001|
|response_time|响应时间|是|[string]|2023-02-16 10:33:40|
|data|响应数据|是|[array]| |
|data>>result|多个订单结果集|是|[array]| |
|data>>result>>message_id|亚马逊返回，提交过来的记录id|是|[string]|2725|
|data>>result>>result_code|亚马逊返回，处理结果code|是|[string]|Error|
|data>>result>>result_message_code|亚马逊返回，消息code|是|[string]|25|
|data>>result>>result_description|亚马逊返回，错误描述|是|[string]|xxxx|
|data>>task_id|任务id|是|[string]|1003085|
|data>>status_code|任务状态|是|[string]|Complete|
|data>>ship_time|标发时间|是|[string]|1675848605|
|data>>processing_summary|结果汇总|是|[object]| |
|data>>processing_summary>>messages_processed|亚马逊返回，处理个数|是|[string]|1|
|data>>processing_summary>>messages_successful|亚马逊返回，成功个数|是|[string]| |
|data>>processing_summary>>messages_with_error|亚马逊返回，失败个数|是|[string]|1|
|data>>processing_summary>>messages_with_warning|亚马逊返回，告警个数|是|[string]| |
|data>>failure|请求失败原因|是|[string]|null|

## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "request_id": "fb53cd0f457f40c5951b8619b77776a8.151.16759105764670001",
    "response_time": "2023-02-16 10:33:40",
    "data": [
        {
            "result": [
                {
                    "message_id": "2725",
                    "result_code": "Error",
                    "result_message_code": "25",
                    "result_description": "We are unable to process the XML feed because one or more items are invalid."
                }
            ],
            "task_id": "1003085",
            "status_code": "Complete",
            "ship_time": "1675848605",
            "processing_summary": {
                "messages_processed": "1",
                "messages_successful": "0",
                "messages_with_error": "1",
                "messages_with_warning": "0"
            },
            "failure": null
        }
    ]
}
```

## 返回失败示例
```
{
    "code": 102,
    "message": "taskId任务id数组不能为空",
    "response_time": "2023-02-16 10:32:57",
    "request_id": "a740aa69a2fa4d2fb9cabfc81f15ccdd.149.16843781969788627",
    "data": null
}
```
