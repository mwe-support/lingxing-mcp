# 应收报告-列表查询
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/monthly/receivable/report/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[109,123]|
|mids|国家id|否|[array]|[1]|
|currencyCode|币种code|否|[string]|US|
|archiveStatus|对账状态 ：<br>1   已对账，<br>0   未对账|否|[int]|0|
|settleMonth|结算月,格式：Y-m|是|[string]|2023-01|
|sortField|排序字段：<br>beginningBalanceCurrencyAmount 期初余额<br>incomeAmount 收入<br/>refundAmount 退款<br/>spendAmount 支出<br/>other 其他|否|[string]|beginningBalanceCurrencyAmount|
|sortType|排序规则：<br>asc  升序<br>desc  降序|否|[string]|desc|
|receivedState|转账/到账金额: <br>0  不相符<br>1  相符|否|[int]|1|
|offset|分页偏移量， 默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|

## 请求示例
```
{
    "sids": [109,123],
    "mids": [1],
    "currencyCode": "US",
    "archiveStatus": "0",
    "settleMonth": "2023-01",
    "sortField": "beginningBalanceCurrencyAmount",
    "sortType": "desc",
    "receivedState": 1,
    "offset": 0,
    "length": 20
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
|data>>country|站点|是|[string]|英国|
|data>>countryCode|国家编码|是|[string]|UK|
|data>>settlementDate|结算月|是|[string]|2021-01|
|data>>archiveStatus|对账状态：<br>已对账  1<br>未对账 0|是|[int]|0|
|data>>archiveStatusName|对账状态名称|是|[string]|未对账|
|data>>currencyCode|币种code|是|[string]|CNY|
|data>>currencyIcon|币种icon|是|[string]|￥|
|data>>beginningBalanceCurrencyAmount|期初余额|是|[float]|98102.5|
|data>>incomeAmount|收入|是|[float]|634711.85|
|data>>refundAmount|退款|是|[float]|-8548.59|
|data>>spendAmount|支出|是|[float]|-350595.94|
|data>>other|其他|是|[float]|0|
|data>>card|其他-信用卡（其他的子项）|是|[float]|0|
|data>>otherItem|其他-其他项目（其他的子项）|是|[float]|0|
|data>>convertedSuccessAmount|转账成功金额|是|[float]|167112.7|
|data>>convertedFailedAmount|转账失败金额|是|[float]|0|
|data>>receivedAmount|到账金额|是|[float]|0|
|data>>endingBalance|期末|是|[float]|206557.12|
|data>>remark|备注|否|[string]| this is a remark |

## 返回成功示例

```
{
    "code": 0,
    "data": [
        {
            "storeName": "8P-US-2024",
            "sid": 109,
            "country": "美国",
            "countryCode": "US",
            "settlementDate": "2023-01",
            "archiveStatus": 0,
            "archiveStatusName": "未对账",
            "currencyCode": "USD",
            "currencyIcon": "$",
            "beginningBalanceCurrencyAmount": -39.99,
            "incomeAmount": 0,
            "refundAmount": 0,
            "spendAmount": -41.47,
            "other": 40.03,
            "card": 40.03,
            "otherItem": 0,
            "convertedSuccessAmount": 0,
            "convertedFailedAmount": 0,
            "receivedAmount": 0,
            "endingBalance": -41.43,
            "remark": null
        }
    ],
    "response_time": "2024-04-03 11:11:43",
    "total": 9,
    "error_details": [],
    "message": "操作成功",
    "request_id": "eca49f3b-0b81-4cbc-a08c-de6e11420190.1712113903371"
}
```
