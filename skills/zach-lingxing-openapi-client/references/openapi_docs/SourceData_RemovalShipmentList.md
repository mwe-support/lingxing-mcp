# 查询亚马逊源报表-移除货件（新）
查询 Reports-Fulfillment-Removal Shipment Detail 报表
> 报表为seller_id维度，按sid请求会返回对应seller_id下所有移除订单数据，同一个seller_id授权的店铺任取一个sid请求报表数据即可

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/statistic/removalShipment/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|sid|店铺id【seller_id同时传值时，以sid为准】 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[int]|109|
|seller_id|亚马逊店铺id ,对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【seller_id】|否|[string]|A1MQMW3JWPNCBX|
|start_date|开始日期【发货日期】，左闭右开|是|[string]|2020-01-01|
|end_date|结束日期【发货日期】，左闭右开|是|[string]|2024-08-05|
|offset|分页偏移量，默认0|否|[int]|0|
|length|分页长度，默认1000|否|[int]|1000|

## 请求示例
```
{
    "sid": 109,
    "seller_id": "A1MQMW3JWPNCBX",
    "start_date": "2020-01-01",
    "end_date": "2024-08-05",
    "offset": 0,
    "length": 1000
}
```

## 返回结果
Json Object

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code|响应code，0成功|是|[int]| 0|
|message|消息提示|是|[string]|success|
|error_details|错误信息|是|[array]| |
|request_id|请求链路id|是|[string]|509368B3-3460-EF95-6D53-279F2C853CB7|
|response_time|响应时间|是|[string]|2022-08-16 17:47:34|
|total|总数|是|[int]|1|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|1|
|data>>mid|站点id|是|[int]|1|
|data>>seller_id|亚马逊店铺id|是|[string]|A1MQMW3JWPNABC|
|data>>seller_account_name|店铺账号名称|是|[string]| |
|data>>marketplace|市场|是|[string]|美国|
|data>>uuid_new|业务标识【uuid_new+uuid_num_new可标记唯一移除货件行】|是|[string]|7895469d45e27ea311569893f39dab4c|
|data>>uuid_num_new|业务标识-序号【uuid_new+uuid_num_new可标记唯一移除货件行】|是|[int]|1|
|data>>order_id|移除订单号|是|[string]|21052612K0|
|data>>sku|seller_sku【MSKU】|是|[string]|BA-IP12-6.1Clear|
|data>>fnsku|fnsku|是|[string]|X002M1CWOD|
|data>>disposition|disposition|是|[string]|Sellable|
|data>>shipped_quantity|发货数量|是|[int]|1|
|data>>carrier|承运商|是|[string]|ogre|
|data>>tracking_number|运单号|是|[string]|XCET6_LGB7_060821_1|
|data>>seller_name|店铺名称|是|[array]|店铺1|
|data>>seller_name>>sid|店铺id|是|[string]| |
|data>>seller_name>>name|店铺名称|是|[string]| |
|data>>seller_name>>mid|站点id|是|[string]| |
|data>>seller_name>>marketplace|市场|是|[string]| |
|data>>removal_order_type|移除货件类型|是|[string]| |
|data>>overseas_removal_order_no|移除入库单号|是|[string]| |
|data>>shipment_date|发货日期|是|[string]|2022-06-10T01:21:10-07:00|
|data>>shipment_date_timestamp|发货日期（时间戳）|是|[int]|1654849270|
|data>>request_date|创建时间|是|[string]|2021-11-04T12:47:10+00:00|
|data>>local_info|本地产品信息|是|[array]||
|data>>local_info>>local_sku|sku|是|[string]| |
|data>>local_info>>local_name|品名|是|[string]| |
|data>>delivery_info|配送信息|是|[object]| |
|data>>delivery_info>>ship_postal_code|邮编|是|[string]| |
|data>>delivery_info>>ship_state|配送地区|是|[string]| |
|data>>delivery_info>>ship_city|配送城市|是|[string]| |
|data>>delivery_info>>ship_country|配送国家|是|[string]| |
|data>>delivery_info>>district|街道|是|[string]| |
|data>>delivery_info>>county|县|是|[string]| |
|data>>delivery_info>>phone|电话|是|[string]| |
|data>>delivery_info>>address_line1|地址1|是|[string]| |
|data>>delivery_info>>address_line2|地址2|是|[string]| |
|data>>delivery_info>>address_line3|地址3|是|[string]| |
|data>>delivery_info>>name|名称|是|[string]| |
|data>>delivery_info>>address|配送地址|是|[string]| |
## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "7BD81461-BF0E-396E-47B5-8742673811DF",
    "response_time": "2022-08-29 19:32:31",
    "data": [
        {
            "sid": 0,
            "uuid": "4981415d45e24ea351566863f39dab5c",
            "uuid_num": 1,
	        "uuid_new": "7895469d45e27ea311569893f39dab4c",
            "uuid_num_new": 1,
            "order_id": "8P_US_0415",
            "sku": "Black_ Head_Rope",
            "fnsku": "B09MT39ABC",
            "disposition": "Return",
            "shipped_quantity": 2,
            "carrier": "",
            "tracking_number": "",
            "removal_order_type": "Return",
            "seller_id": "A1MQMWXXXPNABC",
            "mid": null,
            "seller_name": [
                {
                    "sid": 16,                  
                    "name": "test1",
                    "mid": 1,
                    "marketplace": "美国"
                }, 
                {
                    "sid": 18,
                    "name": "test2",
                    "mid": 3,
                    "marketplace": "墨西哥"
                }, 
                {
                    "sid": 3387,
                    "name": "test3",
                    "mid": 2,
                    "marketplace": "加拿大"
                }   
            ],
            "marketplace": null,
            "seller_account_name": "TEST",
            "overseas_removal_order_no": "OWR220804000005",
            "shipment_date": "2022-06-02T19:01:19+10:00",
            "shipment_date_timestamp": 1654160479,
            "request_date":"2022-08-04T12:47:10+00:00",
            "delivery_info": {
                "ship_postal_code": "",
                "ship_state": "",
                "ship_city": "",
                "ship_country": "",
                "district": "",
                "county": "",
                "phone": "",
                "address_line1": "",
                "address_line2": "",
                "address_line3": "",
                "name": "",
                "address": ""
            },
            "local_info": [
                {
                    "local_sku": "16",                  
                    "local_name": "test1"
                }
        }
    ],
    "total": 1
}
```


## 返回失败示例
```
{
    "code": 102,
    "message": "参数不合法",
    "error_details": [
        "sid => sid不能为空"
    ],
    "request_id": "5DBA1950-9910-9202-0A91-A9E451D1691B",
    "response_time": "2022-08-16 17:54:06",
    "data": [],
    "total": 0
}
```
