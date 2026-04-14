# 查询沃尔玛广告主列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/adReport/advertiser/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型       | 示例 |
| :------------ | :------------ | :------------ |:---------| :------------ |
| searchText | 广告主名称模糊搜索 | 否 | [string] |  |
| paging | 不分页传false  分页传true | 是 | [string] |  |
| limit | 分页条数 | 否 | [int]    |  |
| page | 页码 | 否 | [int]    |  ||

## 请求cURL示例

```
curl --location 'https://openapi.lingxing.com/basicOpen/adReport/advertiser/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{"paging":false,"limit":10,"page":1}'
```

## 返回结果

JSON Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 状态码，0：成功 | 是 | [int] | 0 |
| message | 消息提示 | 是 | [string] | success |
| error_details | 数据校验失败时的错误详情 | 是 | [array] | |
| request_id | 请求链路id | 是 | [string] | a0d54debf93140f3b58d1ed81e8e3583 |
| response_time | 响应时间 | 是 | [string] | 2026-04-03 12:00:00 |
| data | 响应数据 | 是 | [object] | |
| data>>total | 总数 | 是 | [int] | 1 |
| data>>list |  | 是 | [array] |  |
| data>>list>>advertiserId | 广告主id | 是 | [string] | 123456789 |
| data>>list>>advertiserName | 广告主名称 | 是 | [string] | 1 |
| data>>list>>status | 状态 0禁用, 1启用 | 是 | [int] | 1 |

## 返回成功示例

```
{
	"code":0,
	"message":"success",
	"error_details":[],
	"request_id":"a0d54debf93140f3b58d1ed81e8e3583",
	"response_time":"2026-04-03 12:00:00",
	"data":{
		"total":1,
		"list":[
			{
				"advertiserId":"123456789",
				"advertiserName":"1",
				"status":1,
			}
		]
	}
}```
