# 刊登管理-查询刊登结果
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/listing/publish/openapi/amazon/product/list` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|record_unique_id|批次唯一ID|否|[int]|613461486794178560|
|sku|sku|否|[string]|abced-1|
|store_id|store_id|否|[int]| |
|operate_time |操作时间|否|[object]| |
|operate_time >>start|开始时间|否|[string]| |
|operate_time >>end|结束时间|否|[string]| |
|operate_time >>end|结束时间|否|[string]| ||


## 请求示例
```
{
    "record_unique_id": 613461486794178560,
    "sku": "abced-1",
    "store_id": 0,
    "operate_time ": {
        "start": "",
        "end": ""
    }
}
```

## 返回结果
| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码|是|[number]|1|
|msg|消息提示|是|[string]|成功|
|data|响应数据|是|[array]||
|data>>record_unique_id|批次唯一ID|是|[number]|613461486794178600|
|data>>store_id|store_id|是|[number]|3690|
|data>>sku|sku|是|[string]|abced-1|
|data>>status|状态：<br>0 处理中<br>1 成功<br>2 失败|是|[number]|2|
|data>>failure_reason|失败原因|是|[string]||
|data>>warning|亚马逊返回warning|是|[string]||
|data>>operate_time|操作时间|是|[string]|2025-08-20 19:56:56|
|data>>finish_time|完成时间|是|[string]|2025-08-21 10:00:24|
|data >> operationType|刊登类型<br>0 刊登新品<br>1 更新已有商品信息|是|[int]| |
|request_id|请求链路id|是|[string]|0fb7e663-3db9-4f6e-aef9-86c79aaf3ed6|

## 返回成功示例
```
{
    "code": 1,
    "msg": "成功",
    "data": [
        {
            "record_unique_id": 613461486794178560,
            "store_id": 3690,
            "sku": "abced-1",
            "status": 2,
            "failure_reason": "",
            "operate_time": "2025-08-20 19:56:56",
            "finish_time": "2025-08-21 10:00:24"
        }
    ],
    "request_id": "0fb7e663-3db9-4f6e-aef9-86c79aaf3ed6|e154967c-7e32-11f0-a339-8e0180587c4d"
}
```
