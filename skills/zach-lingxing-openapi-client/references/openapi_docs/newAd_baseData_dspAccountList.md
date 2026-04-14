# 查询广告账号列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/baseData/account/list` | HTTPS | POST | 10 |

## 请求参数

|参数名|说明|必填|类型|示例|
|:------------|:------------|:------------|:------------|:------------|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|
|type|类型：<br/> dsp <br/> seller <br/> vendor |是|[string]|dsp|

## 返回结果

Json Object

|参数名|说明|必填|类型|示例|
|:------------|:------------|:------------|:------------|:------------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[array]||
|data>>sid|店铺id<br />1.type为seller时，返回sid <br />2.type为vendor时，sid的值暂时为profile_id(不建议使用，后续可能变更)<br /> 3.type为dsp时，为null|是|[string]||
|data>>profile_id|亚马逊店铺数字id	|是|[string]|1196801708955240|
|data>>country_code|国家code|是|[string]|US|
|data>>currency_code|币种|是|[string]|USD|
|data>>status|账号状态：<br />-1  删除<br />0  停止同步<br />1  正常<br />2  授权异常|是|[int]|1|
|data>>name|账号名称|是|[string]|北美dsp账号|
|data>>type|类型：<br/> dsp <br/> seller <br/> vendor|是|[string]|dsp|

## 返回成功示例

```

{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "d741f97136b642cdac66dbc83d0cfefa.1700102369668",
    "response_time": "2023-11-16 10:39:30",
    "data": [
        {
            "sid": "131213123123","
            "profile_id": “1196801708955240”,
            "country_code": "US",
            "currency_code": "USD",
            "status": 1,
            "name": "北美dsp账号",
            "type": "dsp"
        }
    ],
    "total": 1
}
```