# 查询亚马逊店铺列表
查询得到企业已授权到领星ERP的全部亚马逊店铺信息

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/data/seller/lists` | HTTPS | GET | 1 |

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|code|状态码，0 成功|是|[int]|0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|response_time|响应时间|是|[string]|2020-05-18 11:23:47|
|data|响应数据|是|[array]||
|data>>sid|店铺id<br>领星ERP对企业已授权店铺的唯一标识|是|[number]|1519|
|data>>mid|站点id|是|[number]|1|
|data>>name|店铺名|是|[string]|test账号|
|data>>seller_id|亚马逊店铺id|是|[string]|AZTOL********|
|data>>account_name|店铺账户名称|是|[string]| |
|data>>seller_account_id|店铺账号id|是|[number]|1|
|data>>region|站点简称，例如NA指北美|是|[string]|EU|
|data>>country|商城所在国家名称|是|[string]|西班牙|
|data>>has_ads_setting|是否授权广告：<br>0 否<br>1 是|是|[int]| |
|data>>marketplace_id|市场id|是|[string]|xxxxxxxxxxxxxxxx|
|data>>status|店铺状态：<br>0 停止同步<br>1 正常<br>2 授权异常<br>3 欠费停服|是|[int]|1|

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "B34C8F27-F3CA-EE25-836C-32FABBD8B8CD",
    "response_time": "2021-11-10 17:28:33",
    "data": [
        {
            "sid": 1,
            "mid": 1,
            "name": "店铺1",
            "seller_id": "AZTOL********",
            "account_name": "account**",
            "seller_account_id": 2,
            "region": "EU",
            "country": "西班牙",
            "has_ads_setting": 0,
            "marketplace_id": xxxxxxxxxxxxxxxx,
	        "status": 1
        }
    ]
}
```
## 附加说明  
1. 唯一键：sid
2. 调用本接口，将一次性返回企业全部已授权到领星ERP的亚马逊SC店铺sid
3. sid将用于部分开放接口传入参数
