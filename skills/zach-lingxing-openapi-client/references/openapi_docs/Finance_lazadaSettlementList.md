# 账单明细-LazadaSettlement

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/lazada/settlement/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| compareLogic | 字段比较条件逻辑关系：<br>`AND` 所有条件都满足<br>`OR` 满足任一条件<br>默认 `AND` | 否 | [string] | AND |
| currencyCode | 目标货币代码（为空则使用原币种） | 否 | [string] | USD |
| endDate | 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59` | 否 | [string] | 2026-03-17 23:59:59 |
| envKey | 环境标识 | 否 | [string] | prod |
| exportFields | 导出字段值 | 否 | [array] | ["orderNo","amount"] |
| feeNames | 费用名称数组 | 否 | [array] | ["Commission Fee","Shipping Fee"] |
| fieldCompares | 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定） | 否 | [array] | [{"field":"amount","operator":"gte","value":100}] |
| isInSettlement | 是否计入结算：<br>`0` 否<br>`1` 是<br>`null` 全部 | 否 | [number] | 1 |
| length | 分页大小，默认 `20`，最大不超过 `200` | 是 | [number] | 20 |
| offset | 分页偏移，默认 `0` | 是 | [number] | 0 |
| paidStatuses | 回款状态数组 | 否 | [array] | ["paid","not paid"] |
| platformCode | 平台码 | 否 | [string] | lazada |
| searchExactly | 是否精确匹配 | 否 | [boolean] | false |
| searchExactly1 | 商品搜索是否精确匹配 | 否 | [boolean] | false |
| searchMultiValue | 多个搜索值（精确匹配） | 否 | [array] | ["ORDER001","ORDER002"] |
| searchMultiValue1 | 商品搜索值（多个，精确匹配） | 否 | [array] | ["10001","MSKU001"] |
| searchSingleValue | 单个搜索值（支持模糊匹配，多个值用逗号分隔） | 否 | [string] | ORDER001,ORDER002 |
| searchSingleValue1 | 商品搜索值（单个，支持模糊匹配，多个值用逗号分隔） | 否 | [string] | MSKU001,示例商品 |
| searchType | 搜索类型：<br>`1` 平台单号<br>`2` 平台子单号<br>`3` 交易编号<br>`4` 支付参考编号<br>`5` 参考单号 | 否 | [number] | 1 |
| searchType1 | 商品搜索类型：<br>`11` MSKU ID<br>`12` MSKU<br>`13` 商品名称 | 否 | [number] | 12 |
| sids | 店铺 ID 数组 | 否 | [array] | [10001,10002] |
| sites | 站点数组 | 否 | [array] | ["SG","MY"] |
| sortField | 排序字段 | 否 | [string] | transactionDateOrigin |
| sortType | 排序方向：<br>`1` 升序/ASC<br>`0` 降序/DESC<br>默认 `0` | 否 | [string] | 0 |
| startDate | 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00` | 否 | [string] | 2026-03-01 00:00:00 |
| storeTypes | 店铺类型数组：<br>`1` 跨境店<br>`2` 本土店 | 否 | [array] | [1,2] |
| timeType | 时间类型：<br>`1` 结算日期<br>`2` 结算周期<br>默认 `1` | 否 | [number] | 1 |
| transactionTypes | 交易类型数组 | 否 | [array] | ["Payment","Refund"] |


## 请求cURL示例

```bash
curl --location 'https://openapi.lingxing.com/basicOpen/finance/lazada/settlement/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "compareLogic": "AND",
    "currencyCode": "USD",
    "startDate": "2026-03-01 00:00:00",
    "endDate": "2026-03-17 23:59:59",
    "length": 20,
    "offset": 0,
    "searchType": 1,
    "searchSingleValue": "ORDER001",
    "searchType1": 12,
    "searchSingleValue1": "MSKU001",
    "feeNames": ["Commission Fee"],
    "transactionTypes": ["Payment"],
    "sites": ["SG","MY"],
    "sids": [10001,10002],
    "storeTypes": [1,2],
    "timeType": 1
}'
```

## 返回结果

JSON Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 状态码，0：成功 | 是 | [number] | 0 |
| message | 消息提示 | 是 | [string] | success |
| error_details | 数据校验失败时的错误详情 | 是 | [array] | [] |
| request_id | 请求链路id | 是 | [string] | ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035 |
| response_time | 响应时间 | 是 | [string] | 2025-10-23 00:47:29 |
| data | 响应数据 | 是 | [object] |  |
| data>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>totalSum | 汇总数据 | 是 | [object] |  |
| data>>totalSum>>amount | 结算金额汇总 | 是 | [string] | 1200.50 |
| data>>totalSum>>currencyCode | 币种代码 | 是 | [string] | USD |
| data>>totalSum>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>totalSum>>refundQuantity | 退款数量汇总 | 是 | [number] | 2 |
| data>>totalSum>>saleQuantity | 销售数量汇总 | 是 | [number] | 10 |
| data>>totalSum>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>totalSum>>vatInAmount | 增值税金额汇总 | 是 | [string] | 18.60 |
| data>>totalSum>>whtAmount | 预提税金额汇总 | 是 | [string] | 9.50 |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>uniqueNo | 业务唯一键 | 是 | [string] | LAZADA-SETTLEMENT-001 |
| data>>list>>isInSettlement | 是否计入结算 | 是 | [number] | 1 |
| data>>list>>whtAmount | 预提税金额 | 是 | [string] | 4.50 |
| data>>list>>shippingSpeed | 配送时效 | 是 | [string] | Standard |
| data>>list>>gmtModified | 修改时间 | 是 | [string] | 2026-03-17 15:20:00 |
| data>>list>>whtIncludedInAmount | 是否已计入金额的预提税 | 是 | [string] | Y |
| data>>list>>statementStartTime | 结算周期开始时间 | 是 | [string] | 2026-03-01 00:00:00 |
| data>>list>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>list>>shipmentType | 发货类型 | 是 | [string] | Dropship |
| data>>list>>reference | 参考单号 | 是 | [string] | REF20260317001 |
| data>>list>>paidStatus | 回款状态值 | 是 | [string] | paid |
| data>>list>>orderItemStatus | 订单商品状态 | 是 | [string] | delivered |
| data>>list>>statement | 账单名称 | 是 | [string] | Statement |
| data>>list>>lazadaSku | Lazada SKU | 是 | [string] | LAZSKU001 |
| data>>list>>details | 明细说明 | 是 | [string] | Commission Fee |
| data>>list>>storeName | 店铺名 | 是 | [string] | Lazada-SG |
| data>>list>>id | 主键 ID | 是 | [number] | 1001 |
| data>>list>>transactionDateOrigin | 原始交易日期 | 是 | [string] | 2026-03-15 |
| data>>list>>sellerSku | 卖家 SKU | 是 | [string] | SELLER-SKU-001 |
| data>>list>>storeType | 店铺类型：1-跨境店, 2-本土店 | 是 | [number] | 1 |
| data>>list>>amount | 结算金额 | 是 | [string] | 600.25 |
| data>>list>>orderNo | 平台单号 | 是 | [string] | ORDER001 |
| data>>list>>refundQuantity | 退款数量 | 是 | [number] | 1 |
| data>>list>>saleQuantity | 销售数量 | 是 | [number] | 5 |
| data>>list>>vatInAmount | 增值税金额 | 是 | [string] | 9.30 |
| data>>list>>transactionNumber | 交易编号 | 是 | [string] | TXN20260317001 |
| data>>list>>paidStatusDisplay | 回款状态展示 | 是 | [string] | 已回款 |
| data>>list>>siteDisplay | 站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>feeType | 费用类型 | 是 | [string] | Commission |
| data>>list>>storeId | 店铺 ID | 是 | [number] | 10001 |
| data>>list>>transactionDate | 交易日期 | 是 | [string] | 2026-03-15 |
| data>>list>>gmtCreate | 创建时间 | 是 | [string] | 2026-03-17 12:00:00 |
| data>>list>>transactionType | 交易类型 | 是 | [string] | Payment |
| data>>list>>site | 站点代码 | 是 | [string] | SG |
| data>>list>>sourceType | 数据来源：1-接口, 2-报表导入 | 是 | [number] | 1 |
| data>>list>>storeTypeDisplay | 店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>orderItemNo | 平台子单号 | 是 | [string] | ORDER001-1 |
| data>>list>>feeName | 费用名称 | 是 | [string] | Commission Fee |
| data>>list>>comment | 备注 | 是 | [string] | 正常结算 |
| data>>list>>currencyCode | 币种代码 | 是 | [string] | USD |
| data>>list>>platformCode | 平台码 | 是 | [string] | lazada |
| data>>list>>statementEndTime | 结算周期结束时间 | 是 | [string] | 2026-03-15 23:59:59 |

## 返回成功示例

```json
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "ccafcc7d9a72484fac5a3889b5db2986.231.17611516492143035",
    "response_time": "2025-10-23 00:47:29",
    "data": {
        "totalCount": 2,
        "totalSum": {
            "amount": "1200.50",
            "currencyCode": "USD",
            "currencyIcon": "$",
            "refundQuantity": 2,
            "saleQuantity": 10,
            "totalCount": 2,
            "vatInAmount": "18.60",
            "whtAmount": "9.50"
        },
        "list": [
            {
                "uniqueNo": "LAZADA-SETTLEMENT-001",
                "isInSettlement": 1,
                "whtAmount": "4.50",
                "shippingSpeed": "Standard",
                "gmtModified": "2026-03-17 15:20:00",
                "whtIncludedInAmount": "Y",
                "statementStartTime": "2026-03-01 00:00:00",
                "currencyIcon": "$",
                "shipmentType": "Dropship",
                "reference": "REF20260317001",
                "paidStatus": "paid",
                "orderItemStatus": "delivered",
                "statement": "Statement",
                "lazadaSku": "LAZSKU001",
                "details": "Commission Fee",
                "storeName": "Lazada-SG",
                "id": 1001,
                "transactionDateOrigin": "2026-03-15",
                "sellerSku": "SELLER-SKU-001",
                "storeType": 1,
                "amount": "600.25",
                "orderNo": "ORDER001",
                "refundQuantity": 1,
                "saleQuantity": 5,
                "vatInAmount": "9.30",
                "transactionNumber": "TXN20260317001",
                "paidStatusDisplay": "已回款",
                "siteDisplay": "新加坡",
                "feeType": "Commission",
                "storeId": 10001,
                "transactionDate": "2026-03-15",
                "gmtCreate": "2026-03-17 12:00:00",
                "transactionType": "Payment",
                "site": "SG",
                "sourceType": 1,
                "storeTypeDisplay": "跨境店",
                "orderItemNo": "ORDER001-1",
                "feeName": "Commission Fee",
                "comment": "正常结算",
                "currencyCode": "USD",
                "platformCode": "lazada",
                "statementEndTime": "2026-03-15 23:59:59"
            }
        ]
    }
}
```
