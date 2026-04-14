# 查询费用明细列表
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/fee/management/open/feeManagement/otherFee/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量，默认0|是|[int]|0|
|length|分页长度，默认20|是|[int]|20|
|date_type|时间类型：gmt_create 创建日期，date 分摊日期|是|[string]|gmt_create|
|start_date|开始时间，格式：Y-m-d|是|[string]|2022-12-01|
|end_date|结束时间，格式：Y-m-d|是|[string]|2023-12-01|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]|[100,113]|
|other_fee_type_ids|费用类型id|否|[array]|[1232,1246]|
|status_order|单据状态：<br>1 待提交<br>2 待审批<br>3 已处理<br>4 已驳回<br>5 已作废|否|[int]|3|
|dimensions|分摊维度id：<br>1 msku<br>2 asin<br>3 店铺<br>4 父asin<br>5 sku<br>6 企业|否|[array]|[1,2,3,4]|
|apportion_status|分摊状态【未设置新利润报表启用月使用该入参】：<br>1 未分摊<br>2 已分摊-新<br>3 已分摊-旧<br>4 已分摊|否|[array]|[1,2,3,4]|
|status_merge|分摊状态【已设置新利润报表启用月使用该入参】：<br>1 未分摊<br>2 已分摊|否|[int]|2|
|search_field|搜索类型：<br>number 单据编号<br>msku MSKU<br>asin ASIN<br>create_name 创建人<br>remark_order 单据备注<br>remark_item 明细备注|否|[string]|create_name|
|search_value|搜索值|否|[string]|何芳|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "date_type": "gmt_create",
    "start_date": "2022-12-01",
    "end_date": "2023-12-01",
    "sids": [
        100,
        113
    ],
    "other_fee_type_ids": [
        1232,
        1246
    ],
    "status_order": 3,
    "dimensions": [
        1,
        2,
        3,
        4
    ],
    "apportion_status": [
        1,
        2,
        3,
        4
    ],
    "status_merge": 2,
    "search_field": "create_name",
    "search_value": "何芳"
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|msg|消息提示|是|[string]|操作成功|
|data|响应数据|是|[object]| |
|data>>total|总数|是|[int]|1|
|data>>records|列表数据|是|[array]| |
|data>>records>>id|费用单id|是|[string]|304253905840791552|
|data>>records>>number|单据编号|是|[string]|FY20221129000008|
|data>>records>>dimension_id|分摊维度id：<br>1 msku<br>2 asin<br>3 店铺<br>4 父asin<br>5 sku<br>6 企业|是|[int]|5|
|data>>records>>dimension|分摊维度说明|是|[string]|SKU|
|data>>records>>apportion_rule_id|分摊规则id：<br>1 按销售额占比<br>2 按销量<br>3 店铺均摊后按销售额占比<br>4 店铺均摊后按销量占比|是|[int]|2|
|data>>records>>apportion_rule|分摊规则描述【msku场景下无】|是|[string]|按销售额占比|
|data>>records>>date|分摊日期|是|[string]|2022-11-29|
|data>>records>>fee|单据总费用金额|是|[number]|-4|
|data>>records>>rate|汇率|是|[number]|10|
|data>>records>>other_fee_type_id|费用类型id|是|[string]|1000015|
|data>>records>>other_fee_type|费用类型名称|是|[string]|分摊sku|
|data>>records>>currency_code|单据总费用(原始币种)币种|是|[string]|USD|
|data>>records>>currency_icon|单据总费用(原始币种)币符|是|[string]|$|
|data>>records>>allocation_status|分摊状态说明：<br>未分摊<br>已分摊<br>已分摊-新<br>已分摊-旧|是|[string]|已分摊|
|data>>records>>status_order_id|单据状态id：<br>1 待提交<br>2 待审批<br>3 已处理<br>4 已驳回<br>5 已作废|是|[int]|3|
|data>>records>>status_order|单据状态说明|是|[string]|已处理|
|data>>records>>create_name|创建人名称|是|[string]|XX|
|data>>records>>create_time|创建时间|是|[string]|2022-11-29 11:05:31|
|data>>records>>remark|备注|是|[string]|SKU维度请款|
|data>>records>>is_request_pool|是否请款：0 否，1 是|是|[int]|1|
|data>>records>>details|费用项明细|是|[array]| |
|data>>records>>details>>id|费用单子项id【旧】|是|[string]|304253905840903680|
|data>>records>>details>>fof_id|费用单子项id|是|[string]|304253905840857600|
|data>>records>>details>>sort|序号|是|[int]|1|
|data>>records>>details>>dimension_id|分摊维度id：<br>1 msku<br>2 asin<br>3 店铺<br>4 父asin<br>5 sku<br>6 企业|是|[int]|5|
|data>>records>>details>>dimension|分摊维度说明|是|[string]|SKU|
|data>>records>>details>>dimension_value|纬度值，例如ASIN值|是|[string]|B0ABCD001|
|data>>records>>details>>fee|原币金额|是|[number]|-2|
|data>>records>>details>>fee_sort|排序金额|是|[number]|-20|
|data>>records>>details>>store_type|店铺类型：<br>企业<br>单选店铺<br>全部店铺<br>多选店铺|是|[string]|单选店铺|
|data>>records>>details>>store_infos|店铺信息|是|[array]| |
|data>>records>>details>>store_infos>>id|店铺id|是|[string]|8|
|data>>records>>details>>store_infos>>name|店铺名称|是|[string]|xx-Official-1|
|data>>records>>details>>currency_icon|原始币种币符|是|[string]|$|
|data>>records>>details>>currency_icon_sort|排序币种符号|是|[string]|￥|
|data>>records>>details>>remark|费用子项备注|是|[string]|备注|

## 返回成功示例
```
{
    "code": 0,
    "msg": "操作成功",
    "data": {
        "total": 1
        "records": [
            {
                "id": "304264891485171712",
                "number": "FY221230000001",
                "date": "2022-01",
                "fee": 29999.00,
                "rate": 10.1235,
                "dimension_id": 2,
                "dimension": "ASIN",
                "apportion_rule_id": 1,
                "apportion_rule": "按销售额占比",
                "other_fee_type_id": "1165",
                "other_fee_type": "其他费",
                "currency_code": "USD",
                "currency_icon": "$",
                "allocation_status": "未分摊",
                "status_order_id": 3,
                "status_order": "已处理",
                "create_name": "超级管理员",
                "create_time": "2022-12-30 12:06:13",
                "is_request_pool": 0,
                "remark": "",
                "details": [
                    {
                        "id": "304264891485471232",
                        "sort": 1,
                        "fee": 29999.00,
                        "remark": "月",
                        "fof_id": "304264891485213184",
                        "store_type": "全部店铺",
                        "store_infos": null,
                        "dimension_id": 2,
                        "dimension": "ASIN",
                        "dimension_value": "B00J3JX1ZK",
                        "fee_sort": 303693.58,
                        "currency_icon": "$",
                        "currency_icon_sort": "￥"
                    }
                ]
            }
        ]
    }
}
```
