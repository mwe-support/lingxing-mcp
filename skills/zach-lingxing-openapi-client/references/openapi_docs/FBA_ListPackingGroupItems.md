# 查询包装组
## 接口信息


| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/amzStaServer/openapi/inbound-packing/listPackingGroupItems` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|inboundPlanId|STA任务编号,，对应[创建STA任务](docs/FBA/CreateSTATask)接口对应字段【inboundPlanId】|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05|
|sid|亚马逊店铺sid，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|是|[long]| ||


## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/amzStaServer/openapi/inbound-packing/listPackingGroupItems?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
    "sid": 1
}'
```

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| |是|[number]|0|
|message| |是|[string]|操作成功|
|errorDetails| |是|[null]| |
|requestId| |是|[string]|de66fa7000f34bbe892b8dbf2b7c9299.1732862641215|
|responseTime| |是|[string]|2024-11-29T14:44:01.215|
|data| |是|[object]| |
|data>>inboundPlanId|STA任务编号|是|[string]|wf0a914e89-d126-4ed9-a093-2078289fed05|
|data>>packingGroupList|包装组|是|[array]| |
|data>>packingGroupList>>packingGroupId|包装组ID|是|[string]|pge426cb1a-25db-4784-bd05-24e4de16d03b|
|data>>packingGroupList>>packingGroupItemList|包装组商品信息|是|[array]| |
|data>>packingGroupList>>packingGroupItemList>>msku|msku|是|[string]|STN0002|
|data>>packingGroupList>>packingGroupItemList>>fnsku|fnsku|是|[string]|X00489S34P|
|data>>packingGroupList>>packingGroupItemList>>asin|asin|是|[string]|B0D3F37ZPB|
|data>>packingGroupList>>packingGroupItemList>>parentAsin|父asin|是|[string]|B0D3F37ZPB|
|data>>packingGroupList>>packingGroupItemList>>productName|品名|是|[string]|成本|
|data>>packingGroupList>>packingGroupItemList>>sku|sku|是|[string]|117009ZZ|
|data>>packingGroupList>>packingGroupItemList>>title|标题|是|[string]|Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky|
|data>>packingGroupList>>packingGroupItemList>>url|图片url|是|[string]|https://m.media-amazon.com/images/I/61FW9bR5rKL._SL75_.jpg|
|data>>packingGroupList>>packingGroupItemList>>prepOwner|预处理提供方（AMAZON,SELLER,NONE）|是|[string]|SELLER|
|data>>packingGroupList>>packingGroupItemList>>labelOwner|标签类型（AMAZON,SELLER,NONE）|是|[string]|SELLER|
|data>>packingGroupList>>packingGroupItemList>>quantity|申报量|是|[number]|16|
|data>>packingGroupList>>packingGroupItemList>>expiration|有效期|是|[string]| | |


## 返回成功示例
```
{
    "code": 0,
    "message": "操作成功",
    "errorDetails": [],
    "requestId": "3b3d867e7d014971a580549f107c8c5a.1732773886069",
    "responseTime": "2024-11-28T14:04:46.069",
    "data": {
        "inboundPlanId": "wf0a914e89-d126-4ed9-a093-2078289fed05",
        "packingGroupList": [
            {
                "packingGroupId": "pge426cb1a-25db-4784-bd05-24e4de16d03b",
                "packingGroupItemList": [
                    {
                        "msku": "STN0002",
                        "fnsku": "X00489S34P",
                        "asin": "B0D3F37ZPB",
                        "parentAsin": "B0D3F37ZPB",
                        "productName": "成本",
                        "sku": "117009ZZ",
                        "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky",
                        "url": "",
                        "prepOwner": "SELLER",
                        "labelOwner": "SELLER",
                        "quantity": 16,
                        "expiration": ""
                    },
                    {
                        "msku": "20240122-GM",
                        "fnsku": "X0047Z5K5Z",
                        "asin": "B0CM59V6Y8",
                        "parentAsin": "B0CPSY8HFP",
                        "productName": "饭饭饭",
                        "sku": "ggggasda",
                        "title": "Note Grid, Note Paper, Minimalist and Creative, Cute Note Book, Non Sticky-GM",
                        "url": "",
                        "prepOwner": "SELLER",
                        "labelOwner": "SELLER",
                        "quantity": 8,
                        "expiration": ""
                    }
                ]
            }
        ]
    }
}
```

