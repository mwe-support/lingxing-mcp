# FBA费差异-异常订单-订单
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/sale/fbaFeeDifference/order/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名          | 说明                                       | 必填 | 类型 | 示例                  |
|:-------------|:-----------------------------------------| :------------ | :------------ |:--------------------|
| offset       | 分页偏移量，默认0                                |否|[int]| 0                   |
| length       | 分页长度，默认20，上限200                        |否|[int]| 20                  |
| start_date   | 开始时间【结算时间】，闭区间，格式：Y-m-d |否|[string]| 2022-04-18  |
| end_date     | 结束时间【结算时间】，闭区间，格式：Y-m-d |否|[string]| 2022-05-18  |
| sids         | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|否|[array]| [4,3]               |
| search_field | 搜索字段：order_id 订单号，msku MSKU              |否|[string]| msku                |
| search_value | 搜索值：多个使用英文逗号分隔，上限200                     |否|[string]| "21D9DBA"           |


## 返回结果
Json Object

| 参数名                                  | 说明         | 必填 | 类型 | 示例                                                 |
|:-------------------------------------|:-----------| :------------ | :------------ |:---------------------------------------------------|
| code                                 | 状态码，0 成功   |是|[int]| 0                                                  |
| message                              | 消息提示       |是|[string]| success                                            |
| error_details                        | 错误信息       |是|[array]|                                                    |
| request_id                           | 请求链路id     |是|[string]| ecfbe567-9abe-4dbd-9c4b-9a5929bcdee9.1677838481851 |
| response_time                        | 响应时间       |是|[string]| 2020-04-30 17:33:32                                |
| total                                | 总数         |是|[int]| 6                                                  |
| data                                 | 响应数据       |是|[array]|                                                    |
| data>>sid                            | 店铺id       |是|[int]| 17                                                 |
| data>>amazon_order_id                | 订单号        |是|[string]| 114-1821948-7841000                                |
| data>>title                          | 标题         |是|[string]| Love Pearl                                         |
| data>>asin                           | ASIN       |是|[string]| B09MT3989Q                                         |
| data>>asin_url                       | ASIN地址   |是|[string]| https://www.amazon.com/xxx.jpg      |
| data>>msku                           | MSKU       |是|[string]| Black_ Head_Rope                                   |
| data>>quantity                       | 数量         |是|[string]| 2                                                  |
| data>>sku                            | 本地产品sku    |是|[string]| SKUKT7XL                                           |
| data>>local_name                     | 品名         |是|[string]| KT7XL                                              |
| data>>small_image_url                | 图片地址       |是|[string]| https://XXX/images/SL75_.jpg        |
| data>>rule_name                      | 规则名称       |是|[string]| 规则1                                                |
| data>>chargeable                     | 应收费用       |是|[string]| 20.00                                              |
| data>>currency_chargeable            | 应收费用货币符号   |是|[string]| $                                                  |
| data>>currency_chargeables           | 应收费用货币     |是|[string]| USD                                                |
| data>>actual_fba_fee                 | 实收FBA费     |是|[string]| 20.00                                              |
| data>>currency_actual_fba_fee        | 实收FBA费货币符号 |是|[string]| $                                                  |
| data>>expected_compensation          | 预计赔偿金额     |是|[string]| 4.50                                               |
| data>>currency_expected_compensation | 预计赔偿金额货币符号 |是|[string]| $                                                  |
| data>>is_reparation                  | 是否赔偿       |是|[string]| 否                                                  |
| data>>compensation                   | 已赔偿金额      |是|[string]| 0.00                                               |
| data>>currency_compensation          | 已赔偿金额货币符号  |是|[string]| $                                                  |
| data>>compensation_date              | 赔偿时间       |是|[string]| 2023-03-03 14:00:00                                |
| data>>posted_date | 结算时间 |是|[string]| 2023-03-03 14:00:00 |


## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "6df5ce63ec85414c97b038ae83fb7887.97.16929533412085851",
    "response_time": "2023-08-25 16:49:02",
    "total": 1,
    "data": [
        {
            "sid": 17,
            "amazon_order_id": "205-9967953-3926766",
            "title": "Love Pearl Bottom Hair Circle",
            "asin": "B09MT9BKGH",
            "asin_url": "https://www.amazon.com/dp/B09MT9BKGH",
            "msku": "circle1",
            "quantity": "1",
            "local_name": "[演示数据]无线充电器 Qi认证 7.5W 兼容 iPhone",
            "small_image_url": "https://m.media-amazon.com/images/I/71y9Dp8vK1L._SL75_.jpg",
            "sku": "SKU21D9DBA",
            "rule_name": "规则1",
            "chargeable": "11.00",
            "currency_chargeable": "$",
            "currency_chargeables": "USD",
            "actual_fba_fee": "20.00",
            "currency_actual_fba_fee": "$",
            "expected_compensation": "9.00",
            "currency_expected_compensation": "$",
            "is_reparation": "是",
            "compensation": "4.50",
            "currency_compensation": "$",
            "compensation_date": "2021-04-29 11:02:18",
            "posted_date": "2023-03-03 00:00:00"
        }
    ]
}
```

