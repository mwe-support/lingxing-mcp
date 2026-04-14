# 获取国家下的州、省编码

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/multiplatform/profit/report/stateList` | HTTPS | POST | 1 |

## 请求参数
| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|countryCode|国家编码，二字码|是|[string]|AF|

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/multiplatform/profit/report/stateList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "countryCode":"AF"
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0：成功|是|[number]|0|
|message|消息提示|是|[string]|success|
|error_details|数据校验失败时的错误详情|是|[array]|[]|
|request_id|请求链路id|是|[string]|ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035|
|response_time|响应时间|是|[string]|2025-10-23 00:47:29|
|data|响应数据|是|[object]| |
|data>>states|州/省列表|是|[array]| |
|data>>states>>countryCode|国家编码|是|[string]|AF|
|data>>states>>stateOrProvinceName|州/省名称|是|[string]|Baghlan|
|data>>states>>code|州/省编码|是|[string]|BGL|
|total|总数|是|[number]|18|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035",
    "response_time": "2025-10-23 00:47:29",
    "data": {
        "states": [
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Baghlan",
                "code": "BGL"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Balkh",
                "code": "BAL"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Bamyan",
                "code": "BAM"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Faryab",
                "code": "FYB"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Helmand",
                "code": "HEL"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Herat",
                "code": "HER"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Kabul",
                "code": "KAB"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Kandahar",
                "code": "KAN"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Khost",
                "code": "KHO"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Kunduz",
                "code": "KDZ"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Logar",
                "code": "LOG"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Nangarhar",
                "code": "NAN"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Nimroz",
                "code": "NIM"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Paktika",
                "code": "PKA"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Paktiya",
                "code": "PIA"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Parwan",
                "code": "PAR"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Takhar",
                "code": "TAK"
            },
            {
                "countryCode": "AF",
                "stateOrProvinceName": "Uruzgan",
                "code": "URU"
            }
        ]
    },
    "total": 18
}
```