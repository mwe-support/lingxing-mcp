# 查询补货限制列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/replenishmentRestriction/page/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| storage_type | 仓储类型：<br />Standard 标准<br />Oversize 大件<br />Apparel 服装<br />Footwear 鞋靴<br />ExtraLarge 超大 | 是 | [string] | Standard |
| offset | 分页偏移量，默认0 | 否 | [int] | 0 |
| length | 分页长度，默认20，上限200 | 否 | [int] | 20 |
|sids|店铺id，多个用英文逗号隔开 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[string]| 2,3,4 |

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功                                              |是|[int]|0|
|message| 消息提示 |是|[string]| success                              |
|error_details| 错误信息 |是|[array]||
|request_id| 请求链路id |是|[string]|38E88609-02F1-E7A0-8117-83B0BEB32861|
|total| 总数 |是|[int]|0|
|data| 响应数据 |是|[object]| |
|data>>data|月份数据|是|[object]||
|data>>data>>month| 月份【近4个月份】                                                |是|[array]| [ "8","9","10", "11" ]               |
|data>>list>>sid|店铺id|是|[string]|16|
|data>>list>>vol_unit_type|体积单位类型：<br />1 立方米 <br />2 立方英尺|是|[int]|1|
|data>>list>>ipi|IPI|是|[int]|0|
|data>>list>>update_type|更新类型：<br />1 插件 <br />2 手动 <br />3 导入|是|[int]|2|
|data>>list>>excess_inventory_rate|冗余库存率|是|[string]|0.000000|
|data>>list>>excess_inventory_color|冗余库存颜色：<br />1 dark-green<br />2 light-green<br />3 yellow<br />4 red|是|[int]|1|
|data>>list>>sell_through_rate|售出率|是|[string]|0.000000|
|data>>list>>sell_through_color|售出率颜色：<br />1 dark-green<br />2 light-green<br />3 yellow<br />4 red|是|[int]|1|
|data>>list>>stranded_inventory_rate|无在售信息的库存率|是|[string]|0.000000|
|data>>list>>stranded_inventory_color|无在售信息的库存率颜色：<br />1 dark-green<br />2 light-green<br />3 yellow<br />4 red|是|[int]|1|
|data>>list>>in_stock_rate|有存货库存率|是|[string]|0.000000|
|data>>list>>in_stock_color|有存货库存率颜色：<br />1 dark-green<br />2 light-green<br />3 yellow<br />4 red|是|[int]|1|
|data>>list>>create_time|创建时间|是|[string]|2022-02-25 15:11:01|
|data>>list>>update_time|更新时间|是|[string]|2023-05-19 14:25:50|
|data>>list>>update_time_report|报告更新时间|是|[string]|2023-08-07 11:36:32|
|data>>list>>items|子项数据|是|[array]| |
|data>>list>>items>>limit_name|近4个月的体积和数量|是|[string]|总容量限制|
|data>>list>>items>>月份-vol|体积【月份】|是|[string]|-|
|data>>list>>items>>月份-qty|数量【月份】|是|[string]|0|
|data>>list>>items>>月份-vol|体积【月份】|是|[string]|-|
|data>>list>>items>>月份-qty|数量【月份】|是|[string]|-|
|data>>list>>items>>月份-vol|体积【月份】|是|[string]|-|
|data>>list>>items>>月份-qty|数量【月份】|是|[string]|-|
|data>>list>>items>>月份-vol|体积【月份】|是|[string]|-|
|data>>list>>items>>月份-qty|数量【月份】|是|[string]|-|
|data>>list>>overview|当月数据 |是|[object]| |
|data>>list>>overview>>qty_stock_max|数量：总容量限制|是|[string]|0|
|data>>list>>overview>>qty_stock_used|数量：限额下的使用量|是|[string]|0|
|data>>list>>overview>>qty_predict_used|数量：预估使用量|是|[string]|0|
|data>>list>>overview>>qty_predict_remain|数量：预估剩余量|是|[string]|0|
|data>>list>>overview>>vol_stock_max|体积：总容量限制|是|[string]| 0                                    |
|data>>list>>overview>>vol_stock_used|体积：限额下的使用量|是|[string]| 0                                    |
|data>>list>>overview>>vol_predict_used|体积：预估使用量|是|[string]|0|
|data>>list>>overview>>vol_predict_remain|体积：预估剩余量|是|[string]| 1                                    |
|data>>list>>overview>>vol_unit_type|体积单位类型：<br />1 立方米 <br />2 立方英尺|是|[int]|1|
|data>>list>>sub_items|子项数据|是|[array]| |
|data>>list>>sub_items>>sid|店铺id|是|[string]|16|
|data>>list>>sub_items>>month|月份|是|[string]|2023-08-01|
|data>>list>>sub_items>>storage_type|库存类型|是|[string]|ExtraLarge|
|data>>list>>sub_items>>qty_stock_max|数量：总容量限制|是|[string]|-|
|data>>list>>sub_items>>qty_stock_basic|数量：基本容量|是|[int]|0|
|data>>list>>sub_items>>qty_stock_muiti_channel|数量：多渠道容量|是|[int]|0|
|data>>list>>sub_items>>qty_stock_limit_increase|数量：限制增加容量|是|[int]|0|
|data>>list>>sub_items>>qty_stock_granted_requests|数量：已批准请求|是|[int]|0|
|data>>list>>sub_items>>qty_stock_early_release|数量：提前发放|是|[int]|0|
|data>>list>>sub_items>>qty_stock_pending_requests|数量：待处理请求|是|[int]|0|
|data>>list>>sub_items>>qty_stock_used|数量：限额下的使用量|是|[int]|0|
|data>>list>>sub_items>>qty_stock_open_shipment|数量：在途占用|是|[int]|0|
|data>>list>>sub_items>>qty_stock_on_hand|数量：在库占用|是|[int]|0|
|data>>list>>sub_items>>qty_stock_remain|数量：实际剩余量|是|[int]|0|
|data>>list>>sub_items>>qty_predict_remain|数量：预估使用量|是|[string]|0|
|data>>list>>sub_items>>qty_predict_used|数量：预估使用量|是|[string]|0|
|data>>list>>sub_items>>vol_unit_type|体积单位：<br />1 立方米 <br />2 立方英尺|是|[int]|1|
|data>>list>>sub_items>>vol_stock_max|体积：总容量限制|是|[string]|-|
|data>>list>>sub_items>>vol_stock_basic|体积：基本容量|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_multi_channel|体积：多渠道容量|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_limit_increase|体积：限制增加容量|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_granted_requests|体积：已批准请求|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_early_release|体积：提前发放|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_pending_requests|体积：待处理请求|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_used|体积：限额下的使用量|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_open_shipment|体积：在途占用|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_on_hand|体积：在库占用|是|[string]|0.000000|
|data>>list>>sub_items>>vol_stock_remain|体积：实际剩余量|是|[string]|-1.000000|
|data>>list>>sub_items>>vol_predict_used|体积：预估使用量|是|[string]|0.000000|
|data>>list>>sub_items>>vol_predict_remain|体积：预估剩余量|是|[string]|-1.000000|
|data>>list>>sub_items>>fba_allocation_type|颜色：<br>1 预估<br>2 确定|是|[int]|0|


## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "5fac7b9fce57452abffd2aba45467192.153.16931862659299015",
    "response_time": "2023-08-28 09:31:07",
    "total": 1,
    "data": {
        "data": {
            "month": [
                "8",
                "9",
                "10",
                "11"
            ]
        },
        "list": [
            {
                "sid": "119",
                "vol_unit_type": 2,
                "ipi": -1,
                "update_type": 1,
                "update_time": "2023-05-19 14:25:50",
                "excess_inventory_rate": "-1.000000",
                "excess_inventory_color": 0,
                "sell_through_rate": "-1.000000",
                "sell_through_color": 0,
                "stranded_inventory_rate": "-1.000000",
                "stranded_inventory_color": 0,
                "in_stock_rate": "1.000000",
                "in_stock_color": 1,
                "create_time": "2023-04-19 14:25:50",
                "update_time_report": "2023-08-22 21:04:59",
                "overview": {
                    "qty_stock_max": -1,
                    "qty_stock_used": 0,
                    "qty_predict_used": 0,
                    "qty_predict_remain": -1,
                    "vol_stock_max": "-1.000000",
                    "vol_stock_used": "0.000000",
                    "vol_predict_used": "0.000000",
                    "vol_predict_remain": "-1.000000",
                    "vol_unit_type": 2
                },
                "items": [
                    {
                        "limit_name": "总容量限制",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "基本容量",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "多渠道容量",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "限制增加容量",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "已批准请求",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "提前发放",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "0.000000ft³",
                        "9-qty": "-",
                        "10-vol": "0.000000ft³",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "待处理请求",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "0.000000ft³",
                        "9-qty": "-",
                        "10-vol": "0.000000ft³",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "实际使用量",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "0.000000ft³",
                        "9-qty": "-",
                        "10-vol": "0.000000ft³",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "在途占用",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "在库占用",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "实际剩余量",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "预计占用量",
                        "8-vol": "0.000000ft³",
                        "8-qty": "-",
                        "9-vol": "0.000000ft³",
                        "9-qty": "-",
                        "10-vol": "0.000000ft³",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    },
                    {
                        "limit_name": "预计剩余量",
                        "8-vol": "-",
                        "8-qty": "-",
                        "9-vol": "-",
                        "9-qty": "-",
                        "10-vol": "-",
                        "10-qty": "-",
                        "11-vol": "-",
                        "11-qty": "-"
                    }
                ],
                "sub_items": [
                    {
                        "sid": "119",
                        "month": "2023-08-01",
                        "storage_type": "Standard",
                        "qty_stock_max": "-",
                        "qty_stock_basic": "-1",
                        "qty_stock_muiti_channel": "-1",
                        "qty_stock_limit_increase": "-1",
                        "qty_stock_granted_requests": "-1",
                        "qty_stock_early_release": "-1",
                        "qty_stock_pending_requests": "-1",
                        "qty_stock_used": 0,
                        "qty_stock_open_shipment": "-1",
                        "qty_stock_on_hand": "-1",
                        "qty_stock_remain": "-1",
                        "vol_unit_type": 2,
                        "vol_stock_max": "-",
                        "vol_stock_basic": "-1.000000",
                        "vol_stock_multi_channel": "-1.000000",
                        "vol_stock_limit_increase": "-1.000000",
                        "vol_stock_granted_requests": "-1.000000",
                        "vol_stock_early_release": "0.000000",
                        "vol_stock_pending_requests": "0.000000",
                        "vol_stock_used": "0.000000",
                        "vol_stock_open_shipment": "0.000000",
                        "vol_stock_on_hand": "0.000000",
                        "vol_stock_remain": "-1.000000",
                        "fba_allocation_type": 2,
                        "qty_predict_used": "0",
                        "vol_predict_used": "0.000000",
                        "qty_predict_remain": -1,
                        "vol_predict_remain": "-1.000000"
                    },
                    {
                        "sid": "119",
                        "month": "2023-09-01",
                        "storage_type": "Standard",
                        "qty_stock_max": "-",
                        "qty_stock_basic": "-1",
                        "qty_stock_muiti_channel": "-1",
                        "qty_stock_limit_increase": "-1",
                        "qty_stock_granted_requests": "-1",
                        "qty_stock_early_release": "-1",
                        "qty_stock_pending_requests": "-1",
                        "qty_stock_used": 0,
                        "qty_stock_open_shipment": "-1",
                        "qty_stock_on_hand": "-1",
                        "qty_stock_remain": "-1",
                        "vol_unit_type": 2,
                        "vol_stock_max": "-",
                        "vol_stock_basic": "-1.000000",
                        "vol_stock_multi_channel": "-1.000000",
                        "vol_stock_limit_increase": "-1.000000",
                        "vol_stock_granted_requests": "-1.000000",
                        "vol_stock_early_release": "0.000000",
                        "vol_stock_pending_requests": "0.000000",
                        "vol_stock_used": "0.000000",
                        "vol_stock_open_shipment": "-1.000000",
                        "vol_stock_on_hand": "-1.000000",
                        "vol_stock_remain": "-1.000000",
                        "fba_allocation_type": 1,
                        "qty_predict_used": "0",
                        "vol_predict_used": "0.000000",
                        "qty_predict_remain": -1,
                        "vol_predict_remain": "-1.000000"
                    },
                    {
                        "sid": "119",
                        "month": "2023-10-01",
                        "storage_type": "Standard",
                        "qty_stock_max": "-",
                        "qty_stock_basic": "-1",
                        "qty_stock_muiti_channel": "-1",
                        "qty_stock_limit_increase": "-1",
                        "qty_stock_granted_requests": "-1",
                        "qty_stock_early_release": "-1",
                        "qty_stock_pending_requests": "-1",
                        "qty_stock_used": 0,
                        "qty_stock_open_shipment": "-1",
                        "qty_stock_on_hand": "-1",
                        "qty_stock_remain": "-1",
                        "vol_unit_type": 2,
                        "vol_stock_max": "-",
                        "vol_stock_basic": "-1.000000",
                        "vol_stock_multi_channel": "-1.000000",
                        "vol_stock_limit_increase": "-1.000000",
                        "vol_stock_granted_requests": "-1.000000",
                        "vol_stock_early_release": "0.000000",
                        "vol_stock_pending_requests": "0.000000",
                        "vol_stock_used": "0.000000",
                        "vol_stock_open_shipment": "-1.000000",
                        "vol_stock_on_hand": "-1.000000",
                        "vol_stock_remain": "-1.000000",
                        "fba_allocation_type": 1,
                        "qty_predict_used": "0",
                        "vol_predict_used": "0.000000",
                        "qty_predict_remain": -1,
                        "vol_predict_remain": "-1.000000"
                    }
                ]
            }
        ]
    }
}
```
