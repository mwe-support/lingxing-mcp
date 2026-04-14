# 查询汇率
查询得到亚马逊系统【设置】>【汇率管理】中的汇率数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/finance/currency/currencyMonth` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|date|汇率月份|是|[string]|2021-08|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|信息|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|6DB9CEC4-C9B6-9175-36C7-CE7A2CFC3968|
|response_time|响应时间|是|[string]|2021-09-03 10:38:21|
|data|数据集|是|[array]| |
|data>>date|汇率年月|是|[string]|2021-08|
|data>>code|币种|是|[string]|CNY|
|data>>icon|币种符号|是|[string]|￥|
|data>>name|币种名|是|[string]|人民币|
|data>>rate_org|官方汇率<br>数据来源中国银行官方汇率|是|[string]|1.0000|
|data>>my_rate|我的汇率<br>用户自定义汇率，系统首先使用该汇率数据|是|[string]|1.0000|
|data>>update_time|更新时间|是|[string]|2019-12-30 00:00:0|
|total|记录条数|是|[int]|17|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "6DB9CEC4-C9B6-9175-36C7-CE7A2CFC3968",
    "response_time": "2021-09-03 10:38:21",
    "data": [
        {
            "date": "2021-08",
            "code": "CNY",
            "icon": "￥",
            "name": "人民币",
            "rate_org": "1.0000",
            "my_rate": "1.0000",
            "update_time": "2019-12-30 00:00:0"
        },
        {
            "date": "2021-08",
            "code": "USD",
            "icon": "$",
            "name": "美元",
            "rate_org": "6.4679",
            "my_rate": "6.5376",
            "update_time": "2021-03-28 17:34:38"
        },
        {
            "date": "2021-08",
            "code": "TRY",
            "icon": "₺",
            "name": "土耳其里拉",
            "rate_org": "4.9922",
            "my_rate": "4.9922",
            "update_time": ""
        },
        {
            "date": "2021-08",
            "code": "SEK",
            "icon": "kr",
            "name": "瑞典克朗",
            "rate_org": "0.7497",
            "my_rate": "0.7664",
            "update_time": ""
        },
        {
            "date": "2021-08",
            "code": "SAR",
            "icon": "﷼",
            "name": "沙特里亚尔",
            "rate_org": "1.7243",
            "my_rate": "1.8146",
            "update_time": "2021-04-02 10:52:56"
        },
        {
            "date": "2021-08",
            "code": "PLN",
            "icon": "zł",
            "name": "波兰兹罗提",
            "rate_org": "1.7353",
            "my_rate": "1.7353",
            "update_time": ""
        },
        {
            "date": "2021-08",
            "code": "MXN",
            "icon": "Mex$",
            "name": "墨西哥比索",
            "rate_org": "0.3216",
            "my_rate": "0.3433",
            "update_time": "2020-05-28 10:29:5"
        },
        {
            "date": "2021-08",
            "code": "JPY",
            "icon": "JP¥",
            "name": "日元",
            "rate_org": "0.0588",
            "my_rate": "0.0588",
            "update_time": "2019-12-30 00:00:0"
        },
        {
            "date": "2021-08",
            "code": "INR",
            "icon": "₲",
            "name": "印度卢比",
            "rate_org": "0.0881",
            "my_rate": "0.1100",
            "update_time": "2020-03-02 16:39:5"
        },
        {
            "date": "2021-08",
            "code": "HKD",
            "icon": "HK$",
            "name": "港币",
            "rate_org": "0.8307",
            "my_rate": "0.8335",
            "update_time": "2021-02-04 11:52:13"
        },
        {
            "date": "2021-08",
            "code": "GBP",
            "icon": "￡",
            "name": "英镑",
            "rate_org": "8.8987",
            "my_rate": "8.7811",
            "update_time": "2020-11-27 19:51:3"
        },
        {
            "date": "2021-08",
            "code": "EUR",
            "icon": "€",
            "name": "欧元",
            "rate_org": "7.6303",
            "my_rate": "9.0000",
            "update_time": "2019-12-30 00:00:0"
        },
        {
            "date": "2021-08",
            "code": "CAD",
            "icon": "CA$",
            "name": "加元",
            "rate_org": "5.1304",
            "my_rate": "5.0041",
            "update_time": "2019-12-30 00:00:0"
        },
        {
            "date": "2021-08",
            "code": "BRL",
            "icon": "R$",
            "name": "巴西雷亚尔",
            "rate_org": "1.2473",
            "my_rate": "1.1909",
            "update_time": "2020-11-16 17:37:2"
        },
        {
            "date": "2021-08",
            "code": "AUD",
            "icon": "A$",
            "name": "澳元",
            "rate_org": "4.7173",
            "my_rate": "4.8853",
            "update_time": "2019-12-30 00:00:0"
        },
        {
            "date": "2021-08",
            "code": "AED",
            "icon": "د",
            "name": "迪拉姆",
            "rate_org": "1.7608",
            "my_rate": "1.8211",
            "update_time": "2020-05-13 15:23:4"
        },
        {
            "date": "2021-08",
            "code": "SGD",
            "icon": "S$",
            "name": "新加坡元",
            "rate_org": "4.8078",
            "my_rate": "5.0200",
            "update_time": "2020-05-13 15:23:3"
        }
    ],
    "total": 17
}
```

## 返回失败示例

```
{
    "code": 100,
    "message": "token为空",
    "error_details": [],
    "request_id": "BD4877EC-8C25-F082-609A-017EA3F6CFB5",
    "response_time": "2021-09-03 10:42:53",
    "data": [],
    "total": 0
}
```

## 附加说明
1. 唯一组合键：【date+code】
2. date、my_rate、code作为部分开放接口传入参数
