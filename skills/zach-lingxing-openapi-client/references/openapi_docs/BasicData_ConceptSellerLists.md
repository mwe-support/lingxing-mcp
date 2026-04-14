# 查询亚马逊概念店铺列表
## 接口信息

**API Path**

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/seller/conceptLists` | HTTPS | GET | 1 |

**返回结果**<br>
Json Object

|参数名|说明|必填| 类型       |示例|
| :------------ | :------------ | :------------ |:---------| :------------ |
|code|状态码，0 成功|是| [int]    |0|
|message|消息提示|是| [string] |success|
|error_details|错误信息|是| [array]  ||
|request_id|请求链路id|是| [string] |C3D9F541-8083-E376-EB5C-606A872F5C89|
|response_time|响应时间|是| [string] |2022-12-08 18:27:13|
|total|总数|是| [int]    |0|
|data|响应数据|是| [array]  ||
|data>>id|概念店铺ID【唯一标识】|是| [number] |122167567747313660|
|data>>mid|概念市场ID|是| [number] |1000000|
|data>>name|概念店铺名称|是| [string] |-NA|
|data>>seller_id|亚马逊卖家记号|是| [string] |A303OEQ77COZA82|
|data>>seller_account_name|店铺账号名称|是| [string] |  |
|data>>seller_account_id|店铺账号ID|是| [number] |3275|
|data>>region|站点简称 |是| [string] |NA|
|data>>country|店铺所在国家名称|是| [string] |北美共享|
|data>>status|概念店铺状态：<br> 1 启用<br> 2 禁用|是| [number] |1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "A02474FC-787B-4A35-A287-C8029A46EE68",
    "response_time": "2024-09-19 09:57:54",
    "data": [
        {
            "id": 122202095001055744,
            "mid": 1000003,
            "name": "AK-EU(1)",
            "seller_id": "AN05PRUL7R796",
            "seller_account_name": "AK-quanqiu-EU11",
            "seller_account_id": 82,
            "region": "EU",
            "country": "欧洲共享",
            "status": 1
        } 
    ],
    "total": 1
}
```