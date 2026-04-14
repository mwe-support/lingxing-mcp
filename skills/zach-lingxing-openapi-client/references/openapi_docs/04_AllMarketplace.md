# 查询亚马逊市场列表
查询得到亚马逊所有市场列表数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/seller/allMarketplace` | HTTPS | GET | 1 |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|提示信息|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|AFD5AE05-EFB4-73F6-9C53-0AAD890298C5|
|response_time|响应时间|是|[string]|2021-04-10 16:11:16|
|data|响应数据|是|[array]| |
|data>>mid|站点id|是|[int]|1|
|data>>region|地区|是|[string]|NA|
|data>>aws_region|亚马逊地区|是|[string]|NA|
|data>>country|商城所在国家名称|是|[string]|美国|
|data>>code|亚马逊国家code|是|[string]|US|
|data>>marketplace_id|亚马逊市场id|是|[string]|xxxxxxxxxxxxxxxx|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "3BC60C99-6B35-B022-F712-8B57234ABA3C",
    "response_time": "2024-07-16 20:54:03",
    "data": [
        {
            "mid": 1,
            "region": "NA",
            "aws_region": "NA",
            "country": "美国",
            "code": "US",
            "marketplace_id": "xxxxxxxxxxxxxxxx"
        },
        {
            "mid": 2,
            "region": "NA",
            "aws_region": "NA",
            "country": "加拿大",
            "code": "CA",
            "marketplace_id": "A2EUQ1WTGCTBG2"
        },
        {
            "mid": 3,
            "region": "NA",
            "aws_region": "NA",
            "country": "墨西哥",
            "code": "MX",
            "marketplace_id": "A1AM78C64UM0Y8"
        },
        {
            "mid": 4,
            "region": "EU",
            "aws_region": "EU",
            "country": "英国",
            "code": "UK",
            "marketplace_id": "A1F83G8C2ARO7P"
        },
        {
            "mid": 5,
            "region": "EU",
            "aws_region": "EU",
            "country": "德国",
            "code": "DE",
            "marketplace_id": "A1PA6795UKMFR9"
        },
        {
            "mid": 6,
            "region": "EU",
            "aws_region": "EU",
            "country": "法国",
            "code": "FR",
            "marketplace_id": "A13V1IB3VIYZZH"
        },
        {
            "mid": 7,
            "region": "EU",
            "aws_region": "EU",
            "country": "意大利",
            "code": "IT",
            "marketplace_id": "APJ6JRA9NG5V4"
        },
        {
            "mid": 8,
            "region": "EU",
            "aws_region": "EU",
            "country": "西班牙",
            "code": "ES",
            "marketplace_id": "A1RKKUPIHCS9HS"
        },
        {
            "mid": 9,
            "region": "IN",
            "aws_region": "EU",
            "country": "印度",
            "code": "IN",
            "marketplace_id": "A21TJRUUN4KGV"
        },
        {
            "mid": 10,
            "region": "JP",
            "aws_region": "FE",
            "country": "日本",
            "code": "JP",
            "marketplace_id": "A1VC38T7YXB528"
        },
        {
            "mid": 11,
            "region": "CN",
            "aws_region": "",
            "country": "中国",
            "code": "CN",
            "marketplace_id": "AAHKV2X7AFYLW"
        },
        {
            "mid": 12,
            "region": "AU",
            "aws_region": "FE",
            "country": "澳洲",
            "code": "AU",
            "marketplace_id": "A39IBJ37TRP1C6"
        },
        {
            "mid": 13,
            "region": "AE",
            "aws_region": "EU",
            "country": "阿联酋",
            "code": "AE",
            "marketplace_id": "A2VIGQ35RCS4UG"
        },
        {
            "mid": 14,
            "region": "SG",
            "aws_region": "FE",
            "country": "新加坡",
            "code": "SG",
            "marketplace_id": "A19VAU5U5O7RUS"
        },
        {
            "mid": 15,
            "region": "EU",
            "aws_region": "EU",
            "country": "荷兰",
            "code": "NL",
            "marketplace_id": "A1805IZSGTT6HS"
        },
        {
            "mid": 16,
            "region": "SA",
            "aws_region": "EU",
            "country": "沙特阿拉伯",
            "code": "SA",
            "marketplace_id": "A17E79C6D8DWNP"
        },
        {
            "mid": 17,
            "region": "NA",
            "aws_region": "NA",
            "country": "巴西",
            "code": "BR",
            "marketplace_id": "A2Q3Y263D00KWC"
        },
        {
            "mid": 18,
            "region": "EU",
            "aws_region": "EU",
            "country": "瑞典",
            "code": "SE",
            "marketplace_id": "A2NODRKZP88ZB9"
        },
        {
            "mid": 19,
            "region": "EU",
            "aws_region": "EU",
            "country": "波兰",
            "code": "PL",
            "marketplace_id": "A1C3SOZRARQ6R3"
        },
        {
            "mid": 20,
            "region": "TR",
            "aws_region": "EU",
            "country": "土耳其",
            "code": "TR",
            "marketplace_id": "A33AVAJ2PDY3EV"
        },
        {
            "mid": 21,
            "region": "EU",
            "aws_region": "EU",
            "country": "比利时",
            "code": "BE",
            "marketplace_id": "AMEN7PMS3EDWL"
        }
    ],
}
```

## 附加说明  
1. 唯一键：marketplace_id或mid
2. 调用本接口，获取到领星ERP的站点ID【字段mid】对应的亚马逊市场ID映射关系；
3. 该接口数据变更频率较低，建议获取后本地保留数据；
4. mid将用于部分开放接口传入参数；
