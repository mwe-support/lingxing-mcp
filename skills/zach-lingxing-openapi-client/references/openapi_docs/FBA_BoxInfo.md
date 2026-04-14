# 查询货件装箱信息
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/fba/shipment/boxInfo` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[int]|16|
|shipment_id|货件编号|是|[string]|FBA174B1P511|

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|3A9BF998-54B2-37D8-D542-91CE363C734C|
|response_time|响应时间|是|[string]|2023-05-05 10:01:30|
|total|总数|是|[int]|1|
|data|响应数据|是|[object]| |
|data>>box_type|装箱类型：<br>SINGLE 每箱1款SKU<br>MULTIPLE 每箱多款SKU|是|[string]|MULTIPLE|
|data>>box_list|箱子信息|是|[array]| |
|data>>box_list>>box_length|箱子长|是|[string]|11|
|data>>box_list>>box_width|箱子宽|是|[string]|11|
|data>>box_list>>box_height|箱子高|是|[string]|11|
|data>>box_list>>box_weight|箱子重|是|[string]|11|
|data>>box_list>>box_dimensions_unit|长度单位，公制：cm，英制：in|是|[string]|cm|
|data>>box_list>>box_weight_unit|重量单位，公制：kg，英制：lb|是|[string]|kg|
|data>>box_list>>box_num|箱数|是|[number]|1|
|data>>box_list>>is_pile|LTL合作承运人是否允许箱子堆叠：0 否，1 是|否|[int]|1|
|data>>box_list>>box_mskus|箱内产品（LTL合作承运人时为空）|否|[array]| |
|data>>box_list>>box_mskus>>fulfillment_network_sku|货件FNSKU|否|[string]|B09MT3989W|
|data>>box_list>>box_mskus>>msku|货件MSKU|否|[string]|Black1_Head_Rope|
|data>>box_list>>box_mskus>>quantity_in_case|单箱数量|否|[string]|2|
|data>>is_partner|是否为亚马逊合作承运人:0 否，1 是|是|[number]|1|
|data>>carrier_name|承运方式|是|[string]|UNITED_PARCEL_SERVICE_INC|
|data>>transport_type|货件类型：SPD，LTL|是|[string]|SPD|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "3A9BF998-54B2-37D8-D542-91CE363C734C",
    "response_time": "2023-05-05 10:01:30",
    "data": {
        "box_type": "MULTIPLE",
        "box_list": [{
            "box_length": "11",
            "box_width": "11",
            "box_height": "11",
            "box_weight": "11",
            "box_num": 1,
            "is_pile": 1,
            "box_mskus": [{
                "fulfillment_network_sku": "B09MT3989W",
                "msku": "Black1_Head_Rope",
                "quantity_in_case": "2"
            }]
        }],
        "is_partner": 1,
        "carrier_name": "UNITED_PARCEL_SERVICE_INC",
        "transport_type": "SPD"
    },
    "total": 0
}
```