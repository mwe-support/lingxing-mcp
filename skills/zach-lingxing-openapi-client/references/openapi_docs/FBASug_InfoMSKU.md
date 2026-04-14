# 查询建议信息-MSKU
支持查询FBA补货建议中MSKU维度的详细信息

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fbaSug/msku/getInfo` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|136|
|msku|MSKU|是|[string]|CNxxxx|
|mode|补货建议模式：<br>0 普通模式<br>1 海外仓中转模式<br>【不传默认取erp当前设置模式】|否|[int]|0|

## 请求示例
```
{
    "sid": 136,
    "msku": "CNxxxx",
    "mode": 0
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[string]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数 |是|[int]|0|
|data|响应数据|是|[object]| |
|data>>sid|店铺id|是|[int]|3|
|data>>msku|MSKU|是|[string]| xxx|
|data>>mode|补货建议模式：<br>0 普通<br>1 海外仓中转|是|[number]| |
|data>>quantity_sug_replenishment|建议采购量|是|[number]| |
|data>>quantity_sug_send|建议发货量|是|[number]| |
|data>>quantity_fba_valid|数量：FBA可售|是|[number]|7438|
|data>>msku_list|MSKU库存信息|是|[array]|  |
|data>>msku_list>>msku|MSKU|是|[string]| xxx|
|data>>msku_list>>afn_fulfillable_quantity|可售：FBA可售库存|是|[number]|7438|
|data>>msku_list>>reserved_fc_transfers|调仓中|是|[number]| |
|data>>msku_list>>reserved_fc_processing|待调仓|是|[number]| |
|data>>quantity_sug_purchase|建议采购量|是|[number]| |
|data>>quantity_sug_local_to_oversea|建议本地发海外仓量（海外仓中转模式）|是|[number]| |
|data>>quantity_sug_local_to_fba|建议本地发FBA量（普通模式）|是|[number]| |
|data>>quantity_sug_oversea_to_fba|建议海外仓发FBA量|是|[number]| |
|data>>sug_date_send_local|建议本地发货日|是|[string]| |
|data>>sug_date_send_oversea|建议海外仓发货日|是|[string]| |
|data>>sug_date_purchase|建议采购日|是|[string]| |
|data>>sales_avg_3|日均：3天|是|[number]| |
|data>>sales_avg_7|日均：7天|是|[number]| |
|data>>sales_avg_14|日均：14天|是|[number]| |
|data>>sales_avg_30|日均：30天|是|[number]| |
|data>>sales_avg_60|日均：60天|是|[number]| |
|data>>sales_avg_90|日均：90天|是|[number]| |
|data>>sales_total_3|3日总销量|是|[int]| |
|data>>sales_total_7|7日总销量|是|[int]| |
|data>>sales_total_14|14日总销量|是|[int]| |
|data>>sales_total_30|30日总销量|是|[int]| |
|data>>sales_total_60|60日总销量|是|[int]| |
|data>>sales_total_90|90日总销量|是|[int]||
|data>>suggest_sm_list|运输方式列表|是|[array]| |
|data>>suggest_sm_list>>sm_id|运输方式id|是|[string]| |
|data>>suggest_sm_list>>name|运输方式名称|是|[string]| |
|data>>suggest_sm_list>>quantity_sug_local_to_fba|建议本地仓发FBA量|是|[number]| |
|data>>suggest_sm_list>>quantity_sug_local_to_oversea|建议本地仓发海外仓量|是|[number]| |
|data>>suggest_sm_list>>quantity_sug_purchase|建议采购量|是|[number]|&nbsp;|
|data>>quantity_sug_purchase_air|已弃用（建议采购量（空运））|是|[number]| |
|data>>quantity_sug_purchase_sea|已弃用（建议采购量（海运））|是|[number]| |
|data>>quantity_sug_local_to_oversea_air|已弃用（建议本地发海外仓量（空运）（海外仓模式））|是|[number]| |
|data>>quantity_sug_local_to_oversea_sea|已弃用（建议本地发海外仓量（海运）（海外仓模式））|是|[number]| |
|data>>quantity_sug_local_to_fba_air|已弃用（建议本地发FBA量（空运））|是|[number]| |
|data>>quantity_sug_local_to_fba_sea|已弃用（建议本地发FBA量（海运））|是|[number]| |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "8C1AB940-1FBF-23F8-888A-540C57DB7AB5",
    "response_time": "2023-04-11 10:17:27",
    "data": {
        "sid": 119,
        "msku": "CN0001",
        "mode": 1,
        "quantity_fba_valid": 0,
        "quantity_sug_purchase": 411,
        "quantity_sug_purchase_air": 0,
        "quantity_sug_purchase_sea": 0,
        "quantity_sug_local_to_oversea": 0,
        "quantity_sug_local_to_oversea_air": 0,
        "quantity_sug_local_to_oversea_sea": 0,
        "quantity_sug_local_to_fba": 0,
        "quantity_sug_local_to_fba_air": 0,
        "quantity_sug_local_to_fba_sea": 0,
        "quantity_sug_oversea_to_fba": 0,
        "sug_date_send_local": "2023-01-30",
        "sug_date_purchase": "2023-01-03",
        "sug_date_send_oversea": "2023-02-08",
        "sales_avg_3": 0,
        "sales_avg_7": 0,
        "sales_avg_14": 0,
        "sales_avg_30": 0,
        "sales_avg_60": 2.34,
        "sales_avg_90": 1.67,
        "sales_total_3": 0,
        "sales_total_7": 0,
        "sales_total_14": 0,
        "sales_total_30": 0,
        "sales_total_60": 140,
        "sales_total_90": 150,
        "msku_list": [
             {
                 "msku": "CN0001",
                 "afn_fulfillable_quantity": 0,
                 "reserved_fc_transfers": 0,
                 "reserved_fc_processing": 1
             }
        ],
        "suggest_sm_list": [
            {
                "sm_id": "241241710888379395",
                "name": "快递",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 0
            },
            {
                "sm_id": "241384850192131072",
                "name": "自定义1",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 0
            },
            {
                "sm_id": "241241710888379396",
                "name": "铁运",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 30
            },
            {
                "sm_id": "241241710888379394",
                "name": "空派",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 30
            },
            {
                "sm_id": "241241710888379393",
                "name": "海卡",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 30
            },
            {
                "sm_id": "241241710888379392",
                "name": "海派",
                "quantity_sug_local_to_fba": 0,
                "quantity_sug_local_to_oversea": 0,
                "quantity_sug_purchase": 102
            }
        ]
    },
    "total": 0
}
```

## 附加说明
唯一键：【sid+msku+mode】