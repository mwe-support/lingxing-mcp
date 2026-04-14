# 库存报表-FBA-历史报表-汇总-明细
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/fbaStockReport/getList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|start_month|开始月份，默认当前月份|否|[string]|2023-08|
|end_month|截至月份，默认当前月份|否|[string]|2024-07|
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|否|[string]|A1R1A0FMFL8|
|dimention|数据维度：<br>1 汇总<br>2 明细【默认值】|否|[int]|1|
|offset|分页偏移量【dimention=2 明细维度生效】，默认0|否|[int]|0|
|length|分页长度【dimention=2 明细维度生效】，默认20，上限5000|否|[int]|20|
|attribute|可售状态：【dimention=2 明细维度生效】<br>0 不可售<br>1 可售<br>2 全部【默认值】|否|[int]|2|

## 请求示例
```
{
    "start_month": "2023-08",
    "end_month": "2024-07",
    "seller_id": "A1R1A0FMFL8",
    "dimention": 1,
    "offset": 0,
    "length": 20,
    "attribute": 2
}
```

## 返回结果 - 明细维度  
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|数据|是|[array]| |
|data>>ware_house_name|仓库名称|是|[string]|仓库1|
|data>>asin|ASIN|是|[string]|xxxxx|
|data>>sku|SKU|是|[string]|xxxxxxx|
|data>>fnsku|FNSKU|是|[string]|xxxxxx|
|data>>sku_name|品名|是|[string]|xxxxxx|
|data>>brand_name|品牌名称|是|[string]|xxxxxxx|
|data>>category_name1|一级类目-名称|是|[string]|xxx|
|data>>category_name2|二级类目-名称|是|[string]|xxxx|
|data>>category_name3|三级类目-名称|是|[string]|xxxxx|
|data>>is_saleable|库存属性：<br>全部<br>可售<br>不可售|是|[string]|全部|
|data>>global_tags_str|listing标签|是|[string]|xxxx|
|data>>seller_sku|MSKU|是|[string]|mskuxxxx|
|data>>person|负责人|是|[string]|xxxx|
|data>>year_month|月份|是|[string]|202206-202301|
|data>>first_stock_num|期初库存(数量)|是|[int]| |
|data>>first_stock_data|期初库存(总成本)|是|[string]|0.00|
|data>>first_stock_data_1|期初库存(商品成本）|是|[string]|0.00|
|data>>first_stock_data_2|期初库存(头程成本)|是|[string]|0.00|
|data>>shipment_num|货件补货(数量)|是|[int]| |
|data>>shipment_data|货件补货(总成本)|是|[string]|0.00|
|data>>shipment_data_1|货件补货(商品成本)|是|[string]|0.00|
|data>>shipment_data_2|货件补货(头程成本)|是|[string]|0.00|
|data>>order_num|订单发货(数量)|是|[int]| |
|data>>order_data|订单发货(总成本)|是|[string]|0.00|
|data>>order_data_1|订单发货(商品成本)|是|[string]|0.00|
|data>>order_data_2|订单发货(头程成本)|是|[string]|0.00|
|data>>refund_num|买家退货(数量)|是|[int]| |
|data>>refund_data|买家退货(总成本)|是|[string]|0.00|
|data>>refund_data_1|买家退货(商品成本)|是|[string]|0.00|
|data>>refund_data_2|买家退货(头程成本)|是|[string]|0.00|
|data>>adjust_num|库存调整(数量)|是|[int]| |
|data>>adjust_data|库存调整(总成本)|是|[string]|0.00|
|data>>adjust_data_1|库存调整(商品成本)|是|[string]|0.00|
|data>>adjust_data_2|库存调整(头程成本)|是|[string]|0.00|
|data>>stock_move_num|库存移除(数量)|是|[int]| |
|data>>stock_move_data|库存移除(总成本)|是|[string]|0.00|
|data>>stock_move_data_1|库存移除(商品成本)|是|[string]|0.00|
|data>>stock_move_data_2|库存移除(头程成本)|是|[string]|0.00|
|data>>stock_diff_num|库存差异(数量)|是|[int]| |
|data>>stock_diff_data|库存差异(总成本)|是|[string]|0.00|
|data>>stock_diff_data_1|库存差异(商品成本)|是|[string]|0.00|
|data>>stock_diff_data_2|库存差异(头程成本)|是|[string]|0.00|
|data>>end_stock_num|期末库存(数量)|是|[int]| |
|data>>end_stock_data|期末库存(总成本)|是|[string]|0.00|
|data>>end_stock_data_1|期末库存(商品成本)|是|[string]|0.00|
|data>>end_stock_data_2|期末库存(头程成本)|是|[string]|0.00|
|data>>end_shipping_num|期末在途(数量)|是|[string]| |
|data>>end_shipping_data|期末在途(总成本)|是|[string]|0.00|
|data>>end_shipping_data_1|期末在途(商品成本)|是|[string]|0.00|
|data>>end_shipping_data_2|期末在途(头程成本)|是|[string]|0.00|
|data>>cycle_rate|库存周转率(成本)|是|[number]|0.00|
|data>>cycle_rate_num|库存周转率(数量)|是|[int]| |
|data>>cycle_day|库存周转天数(成本)|是|[int]| |
|data>>cycle_day_num|库存周转天数(数量)|是|[int]| |
|data>>stock_use_rate|存销比(成本)|是|[number]| |
|data>>stock_use_num|存销比(数量)|是|[int]| |
|message|错误消息|是|[string]||
|request_id|请求链路id|是|[string]||
|response_time|响应时间|是|[string]||
|total|查询总数|是|[int]|1|


## 返回结果 - 汇总维度  
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]|  |
|request_id|请求链路id|是|[string]|8D680B8B-3C6F-3E16-F055-73DC70EAD977|
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|数据|是|[array]||
|data>>ware_house_name|仓库名称|是|[string]|仓库1|
|data>>year_month|月份|是|[string]|202206-202301|
|data>>first_stock_num|期初库存(数量)|是|[int]||
|data>>first_stock_data|期初库存(总成本)|是|[string]|0.00|
|data>>first_stock_data_1|期初库存(商品成本）|是|[string]|0.00|
|data>>first_stock_data_2|期初库存(头程成本)|是|[string]|0.00|
|data>>shipment_num|货件补货(数量)|是|[int]||
|data>>shipment_data|货件补货(总成本)|是|[string]|0.00|
|data>>shipment_data_1|货件补货(商品成本)|是|[string]|0.00|
|data>>shipment_data_2|货件补货(头程成本)|是|[string]|0.00|
|data>>order_num|订单发货(数量)|是|[int]||
|data>>order_data|订单发货(总成本)|是|[string]|0.00|
|data>>order_data_1|订单发货(商品成本)|是|[string]|0.00|
|data>>order_data_2|订单发货(头程成本)|是|[string]|0.00|
|data>>refund_num|买家退货(数量)|是|[int]||
|data>>refund_data|买家退货(总成本)|是|[string]|0.00|
|data>>refund_data_1|买家退货(商品成本)|是|[string]|0.00|
|data>>refund_data_2|买家退货(头程成本)|是|[string]|0.00|
|data>>adjust_num|库存调整(数量)|是|[int]||
|data>>adjust_data|库存调整(总成本)|是|[string]|0.00|
|data>>adjust_data_1|库存调整(商品成本)|是|[string]|0.00|
|data>>adjust_data_2|库存调整(头程成本)|是|[string]|0.00|
|data>>stock_move_num|库存移除(数量)|是|[int]||
|data>>stock_move_data|库存移除(总成本)|是|[string]|0.00|
|data>>stock_move_data_1|库存移除(商品成本)|是|[string]|0.00|
|data>>stock_move_data_2|库存移除(头程成本)|是|[string]|0.00|
|data>>stock_diff_num|库存差异(数量)|是|[int]||
|data>>stock_diff_data|库存差异(总成本)|是|[string]|0.00|
|data>>stock_diff_data_1|库存差异(商品成本)|是|[string]|0.00|
|data>>stock_diff_data_2|库存差异(头程成本)|是|[string]|0.00|
|data>>end_stock_num|期末库存(数量)|是|[int]||
|data>>end_stock_data|期末库存(总成本)|是|[string]|0.00|
|data>>end_stock_data_1|期末库存(商品成本)|是|[string]|0.00|
|data>>end_stock_data_2|期末库存(头程成本)|是|[string]|0.00|
|data>>end_shipping_num|期末在途(数量)|是|[string]||
|data>>end_shipping_data|期末在途(总成本)|是|[string]|0.00|
|data>>end_shipping_data_1|期末在途(商品成本)|是|[string]|0.00|
|data>>end_shipping_data_2|期末在途(头程成本)|是|[string]|0.00|
|data>>cycle_rate|库存周转率(成本)|是|[number]|0.00|
|data>>cycle_rate_num|库存周转率(数量)|是|[int]||
|data>>cycle_day|库存周转天数(成本)|是|[int]||
|data>>cycle_day_num|库存周转天数(数量)|是|[int]||
|data>>stock_use_rate|存销比(成本)|是|[number]||
|data>>stock_use_num|存销比(数量)|是|[int]||
|data>>shelf_sale_rate|动销率|是|[number]||
|message|错误消息|是|[string]||
|request_id|请求链路id|是|[string]||
|response_time|响应时间|是|[string]||
|total|查询总数|是|[int]|1|

## 返回成功示例
```
#明细
{
    "code": 0,
    "message": "success",
    "request_id": "557581a380f4447b959d4adf777dfa09",
    "response_time": "2022-12-21 18:45:50"
    "total": 2071,
    "data": [
        {
            "seller_sku": "MSKU0D9001E2",
            "asin": "",
            "fnsku": "",
            "sku": null,
            "sku_name": null,
            "ware_house_name": "8P-SPEED",
            "year_month": "202104-202112",
            "category_name1": "",
            "category_name2": "",
            "category_name3": "",
            "brand_name": "",
            "person": "",
            "is_saleable": "全部",
            "global_tags_str": "",
            "first_stock_num": 0,
            "first_stock_data": "0.00",
            "first_stock_data_1": "0.00",
            "first_stock_data_2": "0.00",
            "shipment_num": 0,
            "shipment_data": "0.00",
            "shipment_data_1": "0.00",
            "shipment_data_2": "0.00",
            "order_num": 0,
            "order_data": "0.00",
            "order_data_1": "0.00",
            "order_data_2": "0.00",
            "refund_num": 0,
            "refund_data": "0.00",
            "refund_data_1": "0.00",
            "refund_data_2": "0.00",
            "adjust_num": 0,
            "adjust_data": "0.00",
            "adjust_data_1": "0.00",
            "adjust_data_2": "0.00",
            "stock_move_num": 0,
            "stock_move_data": "0.00",
            "stock_move_data_1": "0.00",
            "stock_move_data_2": "0.00",
            "stock_diff_num": 0,
            "stock_diff_data": "0.00",
            "stock_diff_data_1": "0.00",
            "stock_diff_data_2": "0.00",
            "end_stock_num": 0,
            "end_stock_data": "0.00",
            "end_stock_data_1": "0.00",
            "end_stock_data_2": "0.00",
            "end_shipping_num": 0,
            "end_shipping_data": "0.00",
            "end_shipping_data_1": "0.00",
            "end_shipping_data_2": "0.00",
            "cycle_rate": 0,
            "cycle_rate_num": 0,
            "cycle_day": 0,
            "cycle_day_num": 0,
            "stock_use_rate": 0,
            "stock_use_num": 0
        }
    ]
}


#汇总
{
    "code": 0,
    "message": "success",
    "request_id": "557581a380f4447b959d4adf777dfa09",
    "response_time": "2022-12-21 18:44:54"
    "total": 12,
    "data": [
        {
            "ware_house_name": "8P-SPEED",
            "year_month": "202104-202112",
            "first_stock_num": 0,
            "first_stock_data": "0.00",
            "first_stock_data_1": "0.00",
            "first_stock_data_2": "0.00",
            "shipment_num": 0,
            "shipment_data": "0.00",
            "shipment_data_1": "0.00",
            "shipment_data_2": "0.00",
            "order_num": 0,
            "order_data": "0.00",
            "order_data_1": "0.00",
            "order_data_2": "0.00",
            "refund_num": 0,
            "refund_data": "0.00",
            "refund_data_1": "0.00",
            "refund_data_2": "0.00",
            "adjust_num": 0,
            "adjust_data": "0.00",
            "adjust_data_1": "0.00",
            "adjust_data_2": "0.00",
            "stock_move_num": 0,
            "stock_move_data": "0.00",
            "stock_move_data_1": "0.00",
            "stock_move_data_2": "0.00",
            "stock_diff_num": 0,
            "stock_diff_data": "0.00",
            "stock_diff_data_1": "0.00",
            "stock_diff_data_2": "0.00",
            "end_stock_num": 0,
            "end_stock_data": "0.00",
            "end_stock_data_1": "0.00",
            "end_stock_data_2": "0.00",
            "end_shipping_num": 0,
            "end_shipping_data": "0.00",
            "end_shipping_data_1": "0.00",
            "end_shipping_data_2": "0.00",
            "cycle_rate": 0,
            "cycle_rate_num": 0,
            "cycle_day": 0,
            "cycle_day_num": 0,
            "stock_use_rate": 0,
            "stock_use_num": 0,
            "shelf_sale_rate": 0
        }
    ]
}
```

## 返回失败示例

```
{
    "code": 500,
    "message": "系统错误",
    "data": null,
    "total": 0,
    "request_id": "557581a380f4447b959d4adf777dfa09",
    "response_time": "2022-12-21 18:44:54"
}
```
