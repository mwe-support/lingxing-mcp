# 编辑费用单
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/fee/management/open/feeManagement/otherFee/edit` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|id|费用单id，[查询费用明细列表](docs/Finance/feeManagementList) 接口对应字段【records>>id】|是|[string]|302272426688496447|
|submit_type|提交类型：1 暂存，2 提交|是|[int]|2|
|dimension|分摊维度：<br>1 msku<br>2 asin<br>3 店铺<br>4 父asin<br>5 sku<br>6 企业|是|[int]|2|
|apportion_rule|分摊规则：<br>0 无<br>1 按销售额<br>2 按销量<br>3 店铺均摊后按销售额占比分摊 <br>4 店铺均摊后按销量占比分摊|是|[int]|1|
|date|分摊日期，格式：Y-m-d 或 Y-m|是|[string]|2023-02|
|currency_code|币种代码|是|[string]|CNY|
|other_fee_type_id|费用类型id，[查询费用类型列表](docs/Finance/feeManagementType) 接口对应字段【id】|是|[int]|1000014|
|is_request_pool|是否请款：0 否，1 是|是|[int]|0|
|remark|单据备注|否|[string]|备注|
|fee_items|费用明细项|是|[array]| |
|fee_items>>fof_id|费用单子项id，[查询费用明细列表](docs/Finance/feeManagementList) 接口对应字段【fof_id】|是|[string]| |
|fee_items>>sids|店铺id，全部店铺传[99999999] ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[array]|[1,2]|
|fee_items>>dimension_value|纬度值，例如ASIN值|是|[string]|B0ABCD001|
|fee_items>>fee|金额|是|[number]|-100|
|fee_items>>remark|备注|否|[string]|备注|

## 请求示例
```
{
    "id": "304363977645646336",
    "submit_type": 2,
    "dimension": 1,
    "apportion_rule": 1,
    "date": "2023-09",
    "currency_code": "CNY",
    "other_fee_type_id": 1167,
    "is_request_pool": 0,
    "remark": "",
    "fee_items": [
        {
            "fof_id": "304363977645675520",
            "sids": [106],
            "dimension_value": "FO-F20Y-K0KC",
            "fee": -100,
            "remark": ""
        }
    ]
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|msg|消息提示|是|[string]|操作成功|
|data|响应数据|是|[string]|true|

## 返回成功示例
```
{
    "code": 0,
    "msg": "操作成功",
    "data": true
}
```

## 返回失败示例
```
{
    "code": 0,
    "msg": "ASIN[FO-F20Y-K0KC]不存在",
    "data": null,
    "traceId": "f5523f038e1240bb87f65795c45b5d3e.1696844832006"
}
```