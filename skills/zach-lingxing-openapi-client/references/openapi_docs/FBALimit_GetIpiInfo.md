# 查询IPI信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fbaLimit/restock/getIpiInfo` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|
|seller_ids|亚马逊店铺id，多个使用英文逗号分隔 ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|否|[string]|ADA96FFC4BCB29|
|mids|站点id，多个使用英文逗号分隔 |否|[string]|2|
|sids|店铺id，多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]|2|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]||
|data>>seller_id|亚马逊店铺id|是|[string]|A18AAB8A278709|
|data>>seller_account_name|店铺账户名称|是|[string]|account2047-1|
|data>>seller_name|店铺名称|是|[string]|店铺11|
|data>>marketplace|国家|是|[string]|意大利|
|data>>update_date|更新时间|是|[string]|2022-11-30 17:30:46|
|data>>vol_unit_text|体积单位|是|[string]|立方米|
|data>>ipi|IPI|是|[number]|528|
|data>>excess_inventory_rate|冗余库存|是|[number]|0.554700|
|data>>sell_through_rate|售出率|是|[number]|2.500000|
|data>>stranded_inventory_rate|无在售信息的库存|是|[number]|0.000000|
|data>>in_stock_rate|有存货库存|是|[number]|0.680800|
|data>>sub_items| |是|[array]||
|data>>sub_items>>qty_predict_remain|预计剩余量（数量）|是|[number]|1000|
|data>>sub_items>>qty_predict_used|预计占用量（数量）|是|[number]||
|data>>sub_items>>qty_stock_max|最高库存水平（数量）|是|[number]|1000|
|data>>sub_items>>qty_stock_remain|实际剩余量（数量）|是|[number]|1000|
|data>>sub_items>>qty_stock_used|库存限额使用量（数量）|是|[number]||
|data>>sub_items>>storage_type|Standard标准尺寸 Oversize大件 Apparel服装 Footwear鞋靴|是|[string]|Apparel|
|data>>sub_items>>vol_predict_remain|预计剩余量（体积）|是|[string]||
|data>>sub_items>>vol_predict_used|预计占用量（体积）|是|[string]|0.000000|
|data>>sub_items>>vol_stock_max|最高库存水平（体积）|是|[string]||
|data>>sub_items>>vol_stock_remain|实际剩余量（体积）|是|[string]||
|data>>sub_items>>vol_stock_used|库存限额使用量（体积）|是|[string]||
|data>>sub_items>>vol_unit_type|单位：<br>1 立方米<br>2 立方英尺|是|[int]|1|

## 返回成功示例

```
{
	"code": 0,
	"message": "success",
	"error_details": [],
	"request_id": "A7D2A2C3-7C75-EE20-CB9C-5BB1EFE6B263",
	"response_time": "2023-01-06 11:40:20",
	"total": 1,
	"data": [{
		"seller_id": "A9373BD6015125",
		"seller_account_name": "account2051",
		"seller_name": "店铺1",
		"marketplace": "美国",
		"update_date": "2022-12-15 20:14:59",
		"vol_unit_text": "立方英尺",
		"ipi": 0,
		"excess_inventory_rate": "0.000000",
		"sell_through_rate": "0.000000",
		"stranded_inventory_rate": "0.000000",
		"in_stock_rate": "0.000000",
		"sub_items": [{
			"qty_predict_remain": -5579,
			"qty_predict_used": "5575",
			"qty_stock_max": 1,
			"qty_stock_remain": -4,
			"qty_stock_used": 5,
			"storage_type": "Standard",
			"vol_predict_remain": "-44.000000",
			"vol_predict_used": "0.000000",
			"vol_stock_max": "11.000000",
			"vol_stock_remain": "-44.000000",
			"vol_stock_used": "55.000000",
			"vol_unit_type": 2
		}, {
			"qty_predict_remain": -4,
			"qty_predict_used": 0,
			"qty_stock_max": 2,
			"qty_stock_remain": -4,
			"qty_stock_used": 6,
			"storage_type": "Oversize",
			"vol_predict_remain": "-44.000000",
			"vol_predict_used": "0.000000",
			"vol_stock_max": "22.000000",
			"vol_stock_remain": "-44.000000",
			"vol_stock_used": "66.000000",
			"vol_unit_type": 2
		}, {
			"qty_predict_remain": -4,
			"qty_predict_used": 0,
			"qty_stock_max": 3,
			"qty_stock_remain": -4,
			"qty_stock_used": 7,
			"storage_type": "Apparel",
			"vol_predict_remain": "-44.000000",
			"vol_predict_used": "0.000000",
			"vol_stock_max": "33.000000",
			"vol_stock_remain": "-44.000000",
			"vol_stock_used": "77.000000",
			"vol_unit_type": 2
		}, {
			"qty_predict_remain": -4,
			"qty_predict_used": 0,
			"qty_stock_max": 4,
			"qty_stock_remain": -4,
			"qty_stock_used": 8,
			"storage_type": "Footwear",
			"vol_predict_remain": "-44.000000",
			"vol_predict_used": "0.000000",
			"vol_stock_max": "44.000000",
			"vol_stock_remain": "-44.000000",
			"vol_stock_used": "88.000000",
			"vol_unit_type": 2
		}]
	}]
}
```

