# 获取发货单头程物流信息-其他费类型
用于发货单新版头程物流信息创建其他费的枚举值
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/shipment/getHeadLogisticsFeeTypes` | HTTPS | POST | 1 |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]|  |
|data>>fee_type_id|其他费ID|是|[string]|241192037543649792|
|data>>name|其他费名称|是|[string]|xx其他费|
|data>>remark|其他费备注|是|[string]|我是备注|
|data>>created_at|其他费创建时间|是|[string]|2022-12-15 19:53:14|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "88E526D5-0D49-BF76-A914-3025AB9F9093",
    "response_time": "2023-04-20 17:20:03",
    "data": [
        {
            "fee_type_id": "0",
            "name": "其他费用",
            "remark": "",
            "created_at": "20223-03-15 19:53:14"
        }
    ],
    "total": 0
}
```
