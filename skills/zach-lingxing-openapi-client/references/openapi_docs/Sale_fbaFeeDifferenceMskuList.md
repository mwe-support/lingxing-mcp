# FBA费差异-异常订单-MSKU
## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/openapi/sale/fbaFeeDifference/msku/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名       | 说明                                  | 必填 | 类型     | 示例       |
| :----------- | :------------------------------------ | :--- | :------- | :--------- |
| offset       | 分页偏移量，默认0                     | 否   | [int]    | 0          |
| length       | 分页长度，默认20，上限200           | 否   | [int]    | 20         |
| start_date   | 开始时间【结算时间】，闭区间，格式：Y-m-d          | 否   | [string] | 2022-04-18 |
| end_date     | 结束时间【结算时间】，闭区间，格式：Y-m-d          | 否   | [string] | 2022-05-18 |
| sids         | 店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [array]  | [4,3]      |
| search_field | 搜索字段：msku MSKU  | 否   | [string] | msku       |
| search_value | 搜索值：多个使用英文逗号分隔，上限200 | 否   | [string] | "21D9DBA"  |

## 返回结果

| 参数名  | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
|code| 状态码，0 成功|是|[int]|0|
|message| 消息提示 |是|[string]| success                                                      |
|error_details| 错误信息 |是|[array]||
|request_id| 请求链路id |是|[string]|ecfbe567-9abe-4dbd-9c4b-9a5929bcdee9.1677838481851|
|response_time| 响应时间 |是|[string]|2020-04-30 17:33:32|
|total|总数|是|[int]|6|
|data|响应数据|是|[array]| |
|data>>sid|店铺id|是|[int]|17|
|data>>title|标题|是|[string]| Love Pearl Bottom Hair Circle|
|data>>asin|ASIN|是|[string]|B09MT3989Q|
|data>>asin_url|ASIN地址|是|[string]|https://www.amazon.com/xxx|
|data>>msku|MSKU|是|[string]|Black_ Head_Rope|
|data>>sku|SKU|是|[string]|SKUKT7XL|
|data>>quantity|数量|是|[string]|2|
|data>>local_name|本地sku名称|是|[string]|KT7XL|
|data>>small_image_url|图片地址|是|[string]| https://www.xxx.com/xxx.jpg |
|data>>difference_order_quantity|异常订单量|是|[string]|1|
|data>>expected_compensation|预计赔偿金额|是|[string]|8.00|
|data>>currency_expected_compensation|预计赔偿金额货币符号|是|[string]|$|
|data>>currency_expected_compensations|预计赔偿金额货币|是|[string]|USD|
|data>>compensation|已赔偿金额|是|[string]|13.55|
|data>>currency_compensation|已赔偿金额货币符号|是|[string]| $ |

## 返回成功示例

```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "6df5ce63ec85414c97b038ae83fb7887.97.16929531440895659",
    "response_time": "2023-08-25 16:45:46",
    "data": [
        {
            "sid": "17",
            "title": "Love Pearl Bottom Hair Circle",
            "asin": "B09MT9BKGH",
            "asin_url": "https://www.amazon.com/d/GH",
            "msku": "circle1",
            "sku": "SKU21D9DBA",
            "quantity": "1",
            "local_name": "[演示数据]无线充电器 Qi认证 7.5W 兼容 iPhone",
            "small_image_url": "https://m.media-amazon.com/images/SL75_.jpg",
            "difference_order_quantity": "3",
            "expected_compensation": "10.00",
            "currency_expected_compensation": "$",
            "currency_expected_compensations": "USD",
            "compensation": "13.55",
            "currency_compensation": "$"
        }
    ],
    "total": 1
}
```

