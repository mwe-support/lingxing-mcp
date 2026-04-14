# 查询Listing操作日志列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/listingManage/listingOperateLog/pageList` | HTTPS | POST | 1 |

## 请求参数

|参数名|说明|必填|类型|示例|
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[string]|17|
|msku|MSKU|是|[string]|JJ002|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认20|否|[int]|20|
|operate_uid|操作人id|否|[array]|[128620]|
|operate_type|操作类型：<br /> 1  调价 <br /> 2  调库存 <br /> 3  修改标题 <br /> 4  编辑商品 <br /> 5  B2B调价|否|[array]|[1,2,3,4,5]|
|operate_time_start|开始时间【操作时间】，格式：Y-m-d H:i:s|否|[string]|2021-09-01 01:22:00|
|operate_time_end|结束时间【操作时间】，格式：Y-m-d H:i:s|否|[string]|2022-10-01 11:22:00|

## 返回结果

Json Object

|参数名|说明|必填|类型|示例|
|:------------|:------------|:------------|:------------|:------------|
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是|[string]|2022-12-08 18:27:13|
|total|总数|是|[int]|0|
|data|响应数据|是|[array]||
|data>>operate_time|操作时间|是|[string]|2022-12-22 14:56:11|
|data>>operate_user|操作人名称|是|[string]|管理员|
|data>>operate_type|操作类型|是|[int]|1|
|data>>operate_type_text|操作类型说明|是|[string]|调价|
|data>>operate_detail|详情|是|[string]|手动调价：【价格】$20.00 -> $20.00|
|data>>sid|店铺id|是|[string]|17|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "7cd87731d2ee49e9be03f35f566bd372.93.16976777109634225",
    "response_time": "2023-10-19 09:08:33",
    "data": [
        {
            "operate_time": "2022-12-22 17:14:13",
            "operate_user": "0超级管理员01",
            "operate_type": 1,
            "operate_detail": "手动调价：【价格】$20.00 -> $20.00",
            "sid": "17",
            "operate_type_text": "调价"
        },
        {
            "operate_time": "2023-04-26 09:35:01",
            "operate_user": "jack",
            "operate_type": 4,
            "operate_detail": "[{\"title\":\"商品标题\",\"detail\":[\"High-quality for sale on Amazon\"]},{\"title\":\"商品图片\",\"detail\":[]}]",
            "sid": "17",
            "operate_type_text": "编辑商品"
        }
	],
    "total": 2
}
```