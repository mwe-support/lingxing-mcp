# 查询亚马逊国家下地区列表
查询得到亚马逊对应国家的地区列表数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/worldState/lists` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|country_code|国家code，[查询亚马逊市场列表](docs/BasicData/AllMarketplace) 接口对应字段【code】|是|[string]|US|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示信息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|60CEFCDF-BF57-6E6E-541A-C31E83B266BE|
|response_time|响应时间|是|[string]|2023-04-10 16:11:16|
|data|响应数据|是|[array]| |
|data>>country_code|国家code|是|[string]|DE|
|data>>state_or_province_name|地区名称|是|[string]|Baden-Wurttemberg|
|data>>code|地区code|是|[string]|BW|
|total|总数|是|[int]|0|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "60CEFCDF-BF57-6E6E-541A-C31E83B266BE",
    "response_time": "2023-04-10 16:11:16",
    "data": [
        {
            "country_code": "DE",
            "state_or_province_name": "Baden-Wurttemberg",
            "code": "BW"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Bayern",
            "code": "BY"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Berlin",
            "code": "BE"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Brandenburg",
            "code": "BB"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Bremen",
            "code": "HB"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Hamburg",
            "code": "HH"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Hessen",
            "code": "HE"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Mecklenburg-Vorpommern",
            "code": "MV"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Niedersachsen",
            "code": "NI"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Nordrhein-Westfalen",
            "code": "NW"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Rheinland-Pfalz",
            "code": "RP"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Saarland",
            "code": "SL"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Sachsen",
            "code": "SN"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Sachsen-Anhalt",
            "code": "ST"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Schleswig-Holstein",
            "code": "SH"
        },
        {
            "country_code": "DE",
            "state_or_province_name": "Thuringen",
            "code": "TH"
        }
    ],
    "total": 16
}
```

## 附加说明
1. 唯一组合键：【country_code+state_or_province_name+code】
2. 该接口数据变更频率较低，建议获取后本地保留数据；