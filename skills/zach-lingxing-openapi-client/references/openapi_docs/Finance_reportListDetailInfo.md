# 应收报告-详情-基础信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/monthly/receivable/report/list/detail/info` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]|1|
|currencyCode|币种code|是|[string]|CNY|
|settleMonth|结算月|是|[string]|2023-01|

## 请求示例
```
{
    "sid": 1,
    "currencyCode": "CNY",
    "settleMonth": "2023-01"
}
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示信息|是|[string]|操作成功|
|request_id|请求链路id|是|[string]|ad9c1a8625c74f3ea0525e216374e31a1676514819613|
|response_time|响应时间|是|[string]|2023-02-16 10:33:40|
|data|响应数据|是|[array]| |
|data>>storeName|店铺名称|是|[string]|JHL Official-01|
|data>>sid|店铺id|是|[int]|8|
|data>>country|国家|是|[string]|英国|
|data>>countryCode|国家编号|是|[string]|UK|
|data>>settlementDate|结算月|是|[string]|2021-01|
|data>>archiveStatus|对账状态：<br>已对账  1<br>未对账 0|是|[int]|0|
|data>>archiveStatusName|对账状态名称|是|[string]|未对账|
|data>>currencyCode|币种code|是|[string]|CNY|
|data>>currencyIcon|币种icon|是|[string]|￥|
|data>>beginningBalanceCurrencyAmount|期初余额|是|[float]|98102.5|
|data>>increaseAmount|本期增加金额|是|[float]|284115.91|
|data>>decreaseAmount|本期减少金额|是|[float]|167112.7|
|data>>endingBalance|期末金额|是|[float]|206557.12|
|data>>remark|备注|是|[string]| |

## 返回成功示例

```
{
    "code": 0,
    "data": {
        "storeName": "8P-US-2024",
        "sid": 109,
        "country": "美国",
        "countryCode": "US",
        "settlementDate": "2023-01",
        "archiveStatus": 0,
        "archiveStatusName": "未对账",
        "currencyCode": "CNY",
        "currencyIcon": "￥",
        "beginningBalanceCurrencyAmount": -270.35,
        "increaseAmount": -280.35,
        "decreaseAmount": 0,
        "endingBalance": -280.08,
        "remark": null
    },
    "response_time": "2024-04-03 11:31:23",
    "total": 0,
    "error_details": [],
    "message": "操作成功",
    "request_id": "68ab134d-cad3-4b59-8bb8-450c73ab56d5.1712115083214"
}
```
