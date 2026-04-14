# 地址簿-配送地址详情

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/fbaShipment/shoppingAddress` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明                                               | 必填 | 类型     | 示例 |
| :----- |:-------------------------------------------------| :--- | :------- | :--- |
| id     | 唯一记录id，[查询FBA列表](docs/FBA/FBAShipmentList)接口对应字段【id】 | 是 | [int] | 417  |

## 返回结果

| 参数名                      | 说明           | 必填 | 类型     | 示例                                               |
| :-------------------------- | :------------- | :--- | :------- | :------------------------------------------------- |
| code                        | 状态码，0 成功  | 是   | [int]    | 0                                                  |
| message                     | 消息提示       | 是   | [string] | success                                           |
| error_details               | 错误信息       | 是   | [array]  | []                                                 |
| request_id                  | 请求链路id     | 是   | [string] | ecfbe567-9abe-4dbd-9c4b-9a5929bcdee9.1677838481851 |
| data                        | 响应数据       | 是   | [object] |                                                    |
| data>>ship_to_address       | 收件人详细地址 | 是   | [string] |15201 Heritage Pkwy                                                    |
| data>>ship_to_postal_code   | 收件人邮政编码 | 是   | [string] |76177-2517                                                    |
| data>>ship_to_country       | 收件国家       | 是   | [string] |United States of America (USA)                                                    |
| data>>ship_to_province_code | 收件省份代码   | 是   | [string] |TX                                                    |
| data>>ship_to_city          | 收件城市       | 是   | [string] |Fort Worth                                                    |
| data>>ship_to_name          | 收件人姓名     | 是   | [string] |Amazon.com Services, Inc.                                                    |
| total                       | 总数           | 是   | [int]    | 0                                                  |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "2a78de97dda847feaeaabfd818743518.1692156761377",
    "response_time": "2023-08-16 11:32:41",
    "data": {
        "ship_to_address": "15201 Heritage Pkwy",
        "ship_to_postal_code": "76177-2517",
        "ship_to_country": "United States of America (USA)",
        "ship_to_province_code": "TX",
        "ship_to_city": "Fort Worth",
        "ship_to_name": "Amazon.com Services, Inc."
    },
    "total": 0
}
```
