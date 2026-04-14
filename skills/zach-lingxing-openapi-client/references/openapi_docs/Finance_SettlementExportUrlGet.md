# 查询settlement下载URL
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/settlement/export/url/get ` | HTTPS | POST | 10 |


## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|[string] |是|xxxxxxxxxxxxxxxx|
|financial_event_group_id|结算汇总财务事件组ID【[结算汇总->financialEventGroupId](docs/Finance/settlementSummaryList)】|[string]|是|LWCBG07Y55I3|

## 请求示例
```
{
    "seller_id": "xxxxxxxxxxxxxxxx",
    "financial_event_group_id": "LWCBG07Y55I3"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|msg|提示信息|是|[string]|成功|
|data|响应结果|文件下载地址，有效期为1小时|[string]|http://xxxxxx/amzn1.spdoc.1.3.2a8d9758-20af-3de44f903d70.T3LIJA6M9UE7KF.1118.txt|

## 返回成功示例
```
{
  "code": 0,
  "msg": "",
  "data": http://xxxxxx/amzn1.spdoc.1.3.2a8d9758-20af-4c0b-aa07-3de44f903d70.T3LIJA6M9UE7KF.1118.txt
}
```
