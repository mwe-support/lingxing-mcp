# 查询采购报表列表 - 产品

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/basicOpen/report/purchase/product/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名       | 说明                                                         | 必填 | 类型     | 示例       |
| :----------- | :----------------------------------------------------------- | :--- | :------- | :--------- |
| offset       | 分页偏移量，默认0                                            | 否   | [int]    |0|
| length       | 分页长度，默认20，上限200                                    | 否   | [int]    |20|
| start_date   | 开始日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d    | 否   | [string] |2024-05-05|
| end_date     | 结束日期【时间间隔最长不得超过90天】，闭区间，格式：Y-m-d    | 否   | [string] |2024-08-01|
| time_type    | 时间类型：1 下单时间，2 到货时间                             | 否   | [int]    |1|
| sids         | 店铺id，多个使用英文逗号分隔 ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】| 否   | [string] |109,136|
| search_field | 搜索字段名：<br>product_name 品名<br />sku SKU<br />msku MSKU<br />fnsku FNSKU<br />spu_name 款名<br />spu SPU | 否   | [string] |sku|
| search_value | 搜索值                                                       | 否   | [string] |01|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "start_date": "2024-05-05",
    "end_date": "2024-08-01",
    "time_type": 1,
    "sids": "109,136",
    "search_field": "sku",
    "search_value": "01"
}
```

## 返回结果
Json Object

| 参数名                      | 说明           | 必填 | 类型     | 示例                                 |
| :-------------------------- | :------------- | ---- | :------- | :----------------------------------- |
| code                        | 状态码，0 成功 | 是   | [int]    | 0                                    |
| message                     | 消息提示       | 是   | [string] | success                              |
| error_details               | 错误信息       | 是   | [array]  |                                      |
| request_id                  | 请求链路id     | 是   | [string] | C3D9F541-8083-E376-EB5C-606A872F5C89 |
| response_time               | 响应时间       | 是   | [string] | 2022-12-08 18:27:13                  |
| total                       | 总数           | 是   | [int]    | 20                                   |
| data                        | 响应数据       | 是   | [array]  |                                      |
| data>>pic_url               | 图片URL        | 是   | [string] | https://image/xxx/A8.jpg             |
| data>>spu                   | SPU            | 是   | [string] |                                      |
| data>>spu_name              | 款名           | 是   | [string] |                                      |
| data>>sku                   | 本地SKU        | 是   | [string] | jobor000002                          |
| data>>product_name          | 品名           | 是   | [string] | jobor测试单品002                     |
| data>>attribute             | 属性           | 是   | [array]  |                                      |
| data>>attribute>>attr_name  | 属性名称       | 是   | [string] |                                      |
| data>>attribute>>attr_value | 属性值         | 是   | [string] |                                      |
| data>>fnsku                 | FNSKU          | 是   | [string] | FN477C98E                            |
| data>>msku                  | MSKU           | 是   | [string] |                                      |
| data>>purchase_quantity     | 采购量         | 是   | [string] | 2                                    |
| data>>receive_quantity      | 到货量         | 是   | [string] | 2                                    |
| data>>wait_quantity         | 待到货量       | 是   | [string] | 0                                    |
| data>>good_quantity         | 良品量         | 是   | [string] | 11                                   |
| data>>bad_quantity          | 次品量         | 是   | [string] | 1                                    |
| data>>return_quantity       | 退货量         | 是   | [string] | 0                                    |
| data>>price_avg             | 平均单价       | 是   | [string] | 0.00                                 |
| data>>purchase_amount       | 订单金额       | 是   | [string] | 0.00                                 |
| data>>receive_amount        | 到货金额       | 是   | [string] | 0.00                                 |
| data>>wait_amount           | 待到货金额     | 是   | [string] | 0.00                                 |
| data>>return_amount         | 退货金额       | 是   | [string] | 0.00                                 |
| data>>bad_rate              | 次品率         | 是   | [string] | 50.0000                              |
| data>>return_rate           | 退货率         | 是   | [string] | 0.0000                               |
| data>>category_name         | 分类名         | 是   | [string] | 商品分类c2                           |
| data>>brand_name            | 品牌名         | 是   | [string] | 品牌b1                               |
| data>>warehouse_name        | 仓库名称       | 是   | [string] | 拉美仓                               |
| data>>account_name          | 店铺名称       | 是   | [string] | 店铺2                                |
| data>>buyer_name            | 采购员名称     | 是   | [string] |                                      |
| data>>country               | 国家           | 是   | [string] | 美国                                 |
| data>>supplier_name         | 供应商         | 是   | [array]  | ["美国供应商s1"]                     |
| data>>director_name         | 负责人         | 是   | [array]  | ["0超级管理员01"]                    |
| data>>overdue_quantity      | 逾期数量       | 是   | [int]    | 0                                    |
| data>>overdue_time          | 逾期时长       | 是   | [string] | 0                                    |
| data>>overdue_quantity_rate | 逾期率         | 是   | [string] | 0.00%                                |
| data>>overdue_time_avg      | 平均逾期时长   | 是   | [string] | 2                                    |
| data>>exchange_quantity     | 换货量         | 是   | [int]    | 0                                    |

## 返回示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "08df995517c04bfa82fe65c2d79d7306.1723171585845",
    "response_time": "2024-08-09 10:46:26",
    "data": [
        {
            "pic_url": "https://image.distributetop.com/lingxing-erp/90128554873982976/20240523/d937bd94d48d4177ba7c1601e8ec8b54.jpg",
            "spu": "23131",
            "spu_name": "1112",
            "sku": "01",
            "product_name": "烤红薯",
            "attribute": [
                {
                    "attr_name": "测试属性",
                    "attr_value": "1"
                }
            ],
            "fnsku": "X0040T7HJP",
            "msku": "CN0001",
            "purchase_quantity": "10000",
            "receive_quantity": "100",
            "wait_quantity": "9900",
            "good_quantity": "0",
            "bad_quantity": "1",
            "return_quantity": "0",
            "price_avg": "10.0000",
            "purchase_amount": "100000.00",
            "receive_amount": "1000.00",
            "wait_amount": "99000.00",
            "return_amount": "0.00",
            "bad_rate": "1.00%",
            "return_rate": "0.00%",
            "category_name": "王",
            "brand_name": "蛋",
            "warehouse_name": "自发货仓库呀",
            "account_name": "renxiao-US",
            "buyer_name": "夏旺",
            "country": "美国",
            "supplier_name": [
                "揭阳市揭东区新亨镇婉佳服装店"
            ],
            "director_name": [],
            "overdue_quantity": 0,
            "overdue_time": "-",
            "overdue_quantity_rate": "0.00%",
            "overdue_time_avg": "-",
            "exchange_quantity": 0
        },
        {
            "pic_url": "https://image.distributetop.com/lingxing-erp/90128554873982976/20240523/d937bd94d48d4177ba7c1601e8ec8b54.jpg",
            "spu": "23131",
            "spu_name": "1112",
            "sku": "01",
            "product_name": "烤红薯",
            "attribute": [
                {
                    "attr_name": "测试属性",
                    "attr_value": "1"
                }
            ],
            "fnsku": "X0040T7HJP",
            "msku": "CN0001",
            "purchase_quantity": "1549",
            "receive_quantity": "1049",
            "wait_quantity": "500",
            "good_quantity": "599",
            "bad_quantity": "0",
            "return_quantity": "0",
            "price_avg": "10.0000",
            "purchase_amount": "15490.00",
            "receive_amount": "10490.00",
            "wait_amount": "5000.00",
            "return_amount": "0.00",
            "bad_rate": "0.00%",
            "return_rate": "0.00%",
            "category_name": "王",
            "brand_name": "蛋",
            "warehouse_name": "旺仔仓库测试",
            "account_name": "renxiao-US",
            "buyer_name": "夏旺",
            "country": "美国",
            "supplier_name": [
                "lx供应商",
                "ABC的"
            ],
            "director_name": [],
            "overdue_quantity": 0,
            "overdue_time": "-",
            "overdue_quantity_rate": "0.00%",
            "overdue_time_avg": "-",
            "exchange_quantity": 0
        }
    ],
    "total": 4
}
```