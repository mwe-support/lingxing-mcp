# 查询规则 - ASIN
支持查询系统FBA补货建议中ASIN的补货规则

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fbaSug/asin/getConfig` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|136|
|asin|ASIN|是|[string]|B0xxxxxxxx|

## 请求示例
```
{
    "sid": 136,
    "asin": "B0xxxxxxxx"
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[string]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|1|
|data|响应数据|是|[object]| |
|data>>info| |是|[object]||
|data>>info>>days_total|总备货时长（普通模式）|是|[number]|29|
|data>>info>>days_total2|总备货时长（海外仓中转模式）|是|[number]|51|
|data>>info>>days_plan|采购计划时长|是|[number]|2|
|data>>info>>days_purchase|采购时长|是|[number]| |
|data>>info>>days_qc|质检时长|是|[number]|3|
|data>>info>>days_oversea_to_fba|海外仓至FBA天数|是|[number]|1|
|data>>info>>days_frequency_purchase|采购频率|是|[number]| |
|data>>info>>days_frequency_local_send|本地仓发货频率|是|[number]| |
|data>>info>>days_frequency_oversea_send|海外仓发货频率|是|[number]| |
|data>>info>>safe_day|安全天数|是|[number]|14|
|data>>info>>is_ignore_certainly_short|建议量扣除必断货量：0 否，1 是|是|[int]||
|data>>info>>is_ignore_history_out_stock|历史销量排除断货数据：0 否，1 是|是|[int]||
|data>>info>>days_oversea|已弃用（原本地至海外仓天数-海运）|是|[number]| |
|data>>info>>days_toucheng|已弃用（原本地至FBA天数-海运）|是|[number]|10|
|data>>info>>days_toucheng_air|已弃用（原本地至FBA天数-空运）|是|[number]| |
|data>>info>>days_oversea_air|已弃用（原本地至海外仓天数-空运）|是|[number]| |
|data>>info>>days_frequancy|已弃用（原补货频率）|是|[number]| |
|data>>info>>sales_avg_3|已弃用（原日均销量：3天）|是|[number]| |
|data>>info>>sales_avg_7|已弃用（原日均销量：7天）|是|[number]| |
|data>>info>>sales_avg_14|已弃用（原日均销量：14天）|是|[number]| |
|data>>info>>sales_avg_30|已弃用（原日均销量：30天）|是|[number]| |
|data>>info>>sales_avg_60|已弃用（原日均销量：60天）|是|[number]| |
|data>>info>>sales_avg_90|已弃用（原日均销量：90天）|是|[number]| |
|data>>info>>default_type_toucheng|已弃用（原默认头程物流类型：0 否，1 是）|是|[int]| |
|data>>info>>default_type_oversea|已弃用（原默认本地发海外仓物流类型：0 否，1 是）|是|[int]| |
|data>>info>>sm_fba_list|本地仓至FBA时效|是|[array]| |
|data>>info>>sm_fba_list>>sm_id|运输方式id|是|[string]|241250000631390720|
|data>>info>>sm_fba_list>>code|运输方式编码|是|[string]|1|
|data>>info>>sm_fba_list>>name|运输方式名称|是|[string]|海派|
|data>>info>>sm_fba_list>>days|天数|是|[number]|30|
|data>>info>>sm_oversea_list|本地仓至海外仓时效|是|[array]| |
|data>>info>>sm_oversea_list>>sm_id|运输方式id|是|[string]|241250000631390722|
|data>>info>>sm_oversea_list>>code|运输方式编码|是|[string]|3|
|data>>info>>sm_oversea_list>>name|运输方式名称|是|[string]|空派|
|data>>info>>sm_oversea_list>>days|天数|是|[number]| |
|data>>list|日销量设置|是|[array]| |
|data>>list>>title|配置标题|是|[string]|默认配置|
|data>>list>>is_default|是否默认配置：<br>0 新增配置，<br>1 默认配置（动态权重）|是|[int]|1|
|data>>list>>type|【is_default=1时字段生效】：<br>0 自定义，<br>1 动态销量|是|[int]|1|
|data>>list>>date_start|配置起始日期|是|[string]|2021-07-20|
|data>>list>>date_end|配置结束日期|是|[string]|2022-01-16|
|data>>list>>weigth_3|权重：3天|是|[number]||
|data>>list>>weigth_7|权重：7天|是|[number]|10|
|data>>list>>weigth_14|权重：14天|是|[number]|30|
|data>>list>>weigth_30|权重：30天|是|[number]|20|
|data>>list>>weigth_60|权重：60天|是|[number]||
|data>>list>>weigth_90|权重：90天|是|[number]||
|data>>list>>volume|日销量（四舍五入，保留两位小数）|是|[number]| |
|data>>denoise|日销量去噪设置|是|[array]||
|data>>denoise>>title|配置名称|是|[string]||
|data>>denoise>>date_start|配置起始日期|是|[string]||
|data>>denoise>>date_end|配置结束日期|是|[string]||
|data>>denoise>>type|类型：1 固定值去噪，2 百分比去噪|是|[int]||
|data>>denoise>>percent|去噪百分比|是|[number]||
|data>>denoise>>volume|日销量|是|[number]|&nbsp;|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "6578BFD5-1559-089D-FDFC-C0051E35B9EA",
    "response_time": "2023-04-11 10:13:44",
    "data": {
        "info": {
            "days_plan": 2,
            "days_qc": 3,
            "days_purchase": 30,
            "days_oversea_to_fba": 0,
            "safe_day": 14,
            "sm_fba_list": [
                {
                    "sm_id": "241250000631390720",
                    "code": "1",
                    "name": "海派",
                    "days": 30
                }
            ],
            "sm_oversea_list": [
                {
                    "sm_id": "241250000631390722",
                    "code": "3",
                    "name": "空派",
                    "days": 0
                },
                {
                    "sm_id": "241250000631390720",
                    "code": "1",
                    "name": "海派",
                    "days": 0
                }
            ],
            "days_frequency_purchase": 0,
            "days_frequency_local_send": 0,
            "days_frequency_oversea_send": 0,
            "is_ignore_certainly_short": 0,
            "is_ignore_history_out_stock": 0,
            "sales_avg_3": 0,
            "sales_avg_7": 0,
            "sales_avg_14": 0,
            "sales_avg_30": 0,
            "sales_avg_60": 0,
            "sales_avg_90": 0,
            "days_total": 79,
            "days_total2": 64,
            "default_type_toucheng": 0,
            "default_type_oversea": 0,
            "days_toucheng": 30,
            "days_toucheng_air": 0,
            "days_oversea": 15,
            "days_oversea_air": 2
        },
        "list": [
            {
                "title": "默认配置",
                "is_default": 1,
                "type": 0,
                "date_start": "2023-04-11",
                "date_end": "2024-04-05",
                "volume": 10,
                "weigth_3": 0,
                "weigth_7": 0,
                "weigth_14": 0,
                "weigth_30": 0,
                "weigth_60": 0,
                "weigth_90": 0
            }
        ],
        "denoise": []
    },
    "total": 0
}
```

## 返回失败示例
```
{
    "code": 500,
    "message": "内部错误",
    "error_details": "补货建议规则不存在",
    "request_id": "B73460DB-F4A6-592F-0075-046E86FBD083",
    "response_time": "2023-04-11 10:11:54",
    "data": [],
    "total": 0
```
