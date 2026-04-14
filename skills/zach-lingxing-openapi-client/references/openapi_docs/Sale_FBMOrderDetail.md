# 查询亚马逊自发货订单详情
支持查询亚马逊自发货订单详情，对应系统【销售】>【订单管理】中订单详情

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/erp/sc/routing/order/Order/getOrderDetail` | HTTPS | POST | 1 |

## 请求参数

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ | 
|order_number|系统单号|是|[string]|123456789012345678|

## 返回结果
Json  Object

| 参数名  | 说明 | 必填 | 类型 |  示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|message|操作成功|是|[string]|操作成功|
|error_details|错误信息|是|[array]||
|request_id|请求链路id|是|[string]|052e20647c9c4622adb7576ae335211d.1687946868074|
|response_time|响应时间|是|[string]|2021-06-28 18:07:50|
|data|响应数据|是|[object]|  |
|data>>order_number|系统单号|是|[string]|103318489501696512|
|data>>order_status|订单状态|是|[string]|待发货|
|data>>order_from_name|订单类型|是|[string]|手工订单|
|data>>purchase_time|订购时间|是|[string]|2021-05-30 22:57:06|
|data>>platform|平台|是|[string]|AMAZON|
|data>>shop_name|店铺|是|[string]|81111-US|
|data>>buyer_choose_express|客选物流|是|[string]||
|data>>total_shipping_price|客付运费|是|[number]|0.00|
|data>>buyer_message|买家留言|是|[string]||
|data>>customer_comment|客服备注|是|[string]||
|data>>warehouse_name|发货仓库|是|[string]|xx|
|data>>wid|发货仓库id|是|[int]|130|
|data>>tracking_number|跟踪号|是|[string]|53434242|
|data>>logistics_type_name|物流方式|是|[string]|物流方式xx|
|data>>logistics_provider_name|物流商|是|[string]|物流商xx|
|data>>logistics_type_id|物流方式id|是|[int]|3295|
|data>>logistics_provider_id|物流商id|是|[int]|83|
|data>>logistics_pre_weight|估算重量|是|[number]|200.00|
|data>>logistics_pre_weight_unit|估算重量单位|是|[string]|g|
|data>>logistics_pre_price|预估运费|是|[number]|0.00|
|data>>logistics_freight|物流运费|是|[string]||
|data>>logistics_freight_currency_code|物流运费币种|是|[string]||
|data>>package_length|估算尺寸长|是|[number]|10.0|
|data>>package_width|估算尺寸宽|是|[number]|10.0|
|data>>package_height|估算尺寸高|是|[number]|10.0|
|data>>package_unit|估算尺寸单位|是|[string]|cm|
|data>>pkg_real_weight|包裹实重|是|[number]|0.00|
|data>>pkg_real_weight_unit|包裹实重单位|是|[string]||
|data>>pkg_length|包裹尺寸长|是|[number]|10.0|
|data>>pkg_width|包裹尺寸宽|是|[number]|10.0|
|data>>pkg_height|包裹尺寸高|是|[number]|10.0|
|data>>pkg_size_unit|包裹尺寸单位|是|[string]|cm|
|data>>order_price_amount|订单总金额|是|[number]|0.00|
|data>>gross_profit_amount|订单毛利润|是|[number]|0.00|
|data>>order_item| |是|[array]|  |
|data>>order_item>>platform_order_id|平台单号|是|[string]|113-57777756|
|data>>order_item>>MSKU|MSKU|是|[string]|xx|
|data>>order_item>>order_item_no|订单明细单号|是|[string]|xx|
|data>>order_item>>pic_url|图片连接|是|[string]|https://image.umaicloud.com/xxx/11.jpg |
|data>>order_item>>sku|SKU|是|[string]|xx|
|data>>order_item>>product_name|品名|是|[string]|xx|
|data>>order_item>>quality|数量|是|[int]|1|
|data>>order_item>>item_unit_price|单价|是|[number]|0.00|
|data>>order_item>>currency_code|单价币种|是|[string]|USD|
|data>>order_item>>customization|商品备注|是|[string]|商品备注|
|data>>order_item>>attachments|商品附件|是|[array]|["https://image.umaicloud.com/xxxxxx/0169e12f598.jpg"]|
|data>>order_item>>newAttachments|商品新附件信息|是|[array]||
|data>>order_item>>newAttachments>>file_id|[文件id](docs/Sale/attachmentDownFile)|是|[long]|103450663351412224|
|data>>order_item>>newAttachments>>file_name|文件名称|是|[string]|lADPBG1Q7eeWX_fNArLNArI_690_690.jpg|
|data>>order_item>>newAttachments>>file_type|文件类型：<br>1 图片 <br>2 压缩包|是|[int]|1|

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "438806AC-DF1A-8AD2-AC48-2D3426A12F67",
    "response_time": "2021-07-19 10:27:11",
    "data": {
        "order_number": "103318489501696512",
        "order_status": "待发货",
        "order_from_name": "手工订单",
        "purchase_time": "2021-05-30 22:57:06",
        "platform": "AMAZON",
        "shop_name": "81111-US",
        "buyer_choose_express": "",
        "total_shipping_price": "0.00",
        "buyer_message": "",
        "customer_comment": "",
        "warehouse_name": "HH",
        "wid": 130,
        "logistics_type_name": "HH",
        "logistics_provider_name": "HH",
        "logistics_type_id": 3295,
        "logistics_provider_id": 83,
        "tracking_number": "53434242",
        "logistics_pre_weight": "200.00",
        "logistics_pre_weight_unit": "g",
        "package_length": "10.0",
        "package_width": "10.0",
        "package_height": "10.0",
        "package_unit": "cm",
        "logistics_pre_price": "0.00",
        "pkg_real_weight": "0.00",
        "pkg_real_weight_unit": "",
        "pkg_length": "10.0",
        "pkg_width": "10.0",
        "pkg_height": "10.0",
        "pkg_size_unit": "cm",
        "logistics_freight": "",
        "logistics_freight_currency_code": "",
        "order_price_amount": "0.00",
        "gross_profit_amount": "0.00",
        "order_item": [
            {
                "platform_order_id": "543535",
                "MSKU": "",
                "order_item_no": "",
                "pic_url": "https://image.distribuxxxx/xxx.jpeg",
                "sku": "HH",
                "product_name": "HH",
                "quality": 1,
                "item_unit_price": "0.00",
                "currency_code": "USD",
                "customization": "",
                "attachments": [],
                "newAttachments": [
                    {
                        "file_id": 103450663351412224,
                        "file_name": "lADPBG1Q7eeWX_fNArLNArI_690_690.jpg",
                        "file_type": 1
                    }
                ]
            }
        ]
    },
    "total": 0
}
```
