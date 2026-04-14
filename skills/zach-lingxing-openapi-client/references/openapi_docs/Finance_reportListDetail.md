# 应收报告-详情-列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/monthly/receivable/report/list/detail` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|6|
|currencyCode|币种code|是|[string]|CNY|
|settleMonth|结算月|是|[string]|2023-01|
|searchField|搜索值类型：<br>fid 结算编号 <br/>settlementId settlementId <br/>sellerSku Msku <br/>localSku sku<br/>localName 品名 <br/>abstractName 摘要|否|[string]|fid|
|searchValue|搜索值|否|[string]|UNOFZ3UMA1DZ|
|offset|偏移量|否|[int]|0|
|length|分页长度，默认20|否|[int]|200|

## 请求示例
```
{
    "settleMonth": "2023-01",
    "currencyCode": "CNY",
    "sid": 1,
    "searchFiled": "fid",
    "searchValue": "UNOFZ3UMA1DZ"
    "offset": 0,
    "length": 200
}
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|提示信息|是|[string]|操作成功|
|request_id|请求链路id|是|[string]|ad9c1a8625c74f3ea0525e216374e31a1676514819613|
|response_time|响应时间|是|[string]|2023-02-16 10:33:40|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>id|序号|是|[int]|1|
|data>>postedDateLocale|日期|是|[string]|2021-01-01|
|data>>fid|结算编号|是|[string]|UNOFZ3UMA1DZ|
|data>>currencyCode|币种code|是|[string]|CNY|
|data>>currencyIcon|币种icon|是|[string]|￥|
|data>>settlementId|settlement_id|是|[string]| |
|data>>sellerSku|MSKU|是|[string]| |
|data>>localSku|SKU|是|[string]| |
|data>>localName|品名|是|[string]| |
|data>>abstractName|摘要|是|[string]|期初余额|
|data>>increase|本期增加|是|[float]|0|
|data>>decrease|本期减少|是|[float]|0|
|data>>balance|余额|是|[float]|98102.5|

## 返回成功示例

```
{
    "code": 0,
    "data": [
        {
            "id": 1,
            "postedDateLocale": "2023-01-01",
            "fid": "17SOMTSKNQ07X",
            "currencyCode": "CNY",
            "currencyIcon": "￥",
            "settlementId": "17048824551",
            "sellerSku": null,
            "localSku": null,
            "localName": null,
            "abstractName": "期初余额",
            "increase": 0.00,
            "decrease": 0.00,
            "balance": -270.35
        }
    ],
    "response_time": "2024-04-03 11:15:32",
    "total": 5,
    "error_details": [],
    "message": "操作成功",
    "request_id": "cd8ec897-a6c4-4f7a-95dc-6620204c6e37.1712114132511"
}
```
