# 立即重算-利润报表数据
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/profit/report/open/report/settle/compute/manual` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|date_month|重算月份，格式：yyyy-MM|是|[string]|2023-01|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示信息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|EF617C27-34B4-3596-BA2A-75F70F0B053C|
|response_time|响应时间|是|[string]|2023-04-13 14:38:53|
|data|响应数据|是|[array]| |
|total|总数|是|[int]|0|