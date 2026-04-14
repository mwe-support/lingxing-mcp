# 账单明细-ShopeeAdjustment

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/shopee/adjustment/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| adjDimensions | 调整维度数组（下拉多选）：<br>`Order`<br>`Shop`<br>`other` 其他维度 | 否 | [array] | ["Order","Shop"] |
| adjTypes | 调整类型数组（下拉多选）：<br>`Refund Amount`<br>`Marketing Fee`<br>`Warehouse Fee`<br>`Other` 其他类型 | 否 | [array] | ["Refund Amount","Marketing Fee"] |
| compareLogic | 字段比较条件逻辑关系：<br>`AND` 所有条件都满足<br>`OR` 满足任一条件<br>默认 `AND` | 否 | [string] | AND |
| currencyCode | 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算） | 否 | [string] | USD |
| endDate | 结束时间（结算时间），格式 `yyyy-MM-dd`，默认当前日期 | 否 | [string] | 2026-03-17 |
| envKey | 环境标识 | 否 | [string] | prod |
| exportFields | 导出字段值 | 否 | [array] | ["orderNo","amount"] |
| fieldCompares | 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定） | 否 | [array] | [{"field":"amount","operator":"gte","value":100}] |
| length | 分页大小，默认 `20`，最大不超过 `200` | 是 | [number] | 20 |
| offset | 分页偏移，默认 `0` | 是 | [number] | 0 |
| platformCode | 平台码 | 否 | [string] | shopee |
| searchExactly | 是否精确匹配 | 否 | [boolean] | false |
| searchMultiValue | 多个搜索值（精确匹配） | 否 | [array] | ["240301A001","240301A002"] |
| searchSingleValue | 单个搜索值（支持模糊匹配，多个值用逗号分隔） | 否 | [string] | 240301A001,240301A002 |
| searchType | 搜索类型：<br>`1` 平台单号 | 否 | [number] | 1 |
| sids | 店铺 ID 数组 | 否 | [array] | [10001,10002] |
| sites | 站点数组 | 否 | [array] | ["SG","MY"] |
| sortField | 排序字段 | 否 | [string] | payoutTime |
| sortType | 排序方向：<br>`1` 升序/ASC<br>`0` 降序/DESC<br>默认 `0` | 否 | [string] | 0 |
| startDate | 开始时间（结算时间），格式 `yyyy-MM-dd`，默认当前月份第一天 | 否 | [string] | 2026-03-01 |
| storeTypes | 店铺类型数组：<br>`1` 跨境店(CB)<br>`2` 本土店(Local) | 否 | [array] | [1,2] |


## 请求cURL示例

```bash
curl --location 'https://openapi.lingxing.com/basicOpen/finance/shopee/adjustment/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "adjDimensions": ["Order"],
    "adjTypes": ["Refund Amount"],
    "compareLogic": "AND",
    "currencyCode": "USD",
    "startDate": "2026-03-01",
    "endDate": "2026-03-17",
    "length": 20,
    "offset": 0,
    "searchType": 1,
    "searchSingleValue": "ORDER20260317001",
    "sites": ["SG","MY"],
    "sids": [10001,10002],
    "storeTypes": [1,2]
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
| data>>totalSum>>amount | 调整金额汇总 | 是 | [string] | 320.50 |
| data>>totalSum>>currency | 币种代码 | 是 | [string] | USD |
| data>>totalSum>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>totalSum>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>uniqueNo | 业务唯一键 | 是 | [string] | SHOPEE-ADJ-001 |
| data>>list>>originalPayoutTime | 原始结算时间戳 | 是 | [number] | 1742198400 |
| data>>list>>storeType | 店铺类型：1-跨境店, 2-本土店 | 是 | [number] | 1 |
| data>>list>>amount | 调整金额 | 是 | [string] | 120.50 |
| data>>list>>orderNo | 平台订单号 | 是 | [string] | ORDER20260317001 |
| data>>list>>adjDimension | 调整维度 | 是 | [string] | Order |
| data>>list>>adjNumber | 调整明细序号 | 是 | [number] | 1 |
| data>>list>>adjRemark | 调整备注 | 是 | [string] | 订单售后差异调整 |
| data>>list>>adjScenario | 调整场景 | 是 | [string] | After Sales |
| data>>list>>billingTransactionType | 账单交易类型 | 是 | [string] | adjustment |
| data>>list>>siteDisplay | 站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>list>>storeId | 店铺 ID | 是 | [number] | 10001 |
| data>>list>>payoutSn | 账期 ID | 是 | [string] | P20260317001 |
| data>>list>>encryptedPayoutId | 账期加密 ID（仅CB有） | 是 | [number] | 1234567890 |
| data>>list>>transactionId | 交易 ID（仅Local有） | 是 | [number] | 987654321 |
| data>>list>>transactionType | 交易类型（仅Local有） | 是 | [string] | SALE |
| data>>list>>payoutTime | 结算时间 | 是 | [string] | 2026-03-17 12:00:00 |
| data>>list>>site | 站点代码 | 是 | [string] | SG |
| data>>list>>storeTypeDisplay | 店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>storeName | 店铺名 | 是 | [string] | Shopee-SG |
| data>>list>>currency | 币种 | 是 | [string] | USD |
| data>>list>>id | 主键 ID | 是 | [number] | 1001 |
| data>>list>>platformCode | 平台码 | 是 | [string] | shopee |
| data>>list>>adjType | 调整类型 | 是 | [string] | Refund Amount |

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
            "amount": "320.50",
            "currency": "USD",
            "currencyIcon": "$",
            "totalCount": 2
        },
        "list": [
            {
                "uniqueNo": "SHOPEE-ADJ-001",
                "originalPayoutTime": 1742198400,
                "storeType": 1,
                "amount": "120.50",
                "orderNo": "ORDER20260317001",
                "adjDimension": "Order",
                "adjNumber": 1,
                "adjRemark": "订单售后差异调整",
                "adjScenario": "After Sales",
                "billingTransactionType": "adjustment",
                "siteDisplay": "新加坡",
                "currencyIcon": "$",
                "storeId": 10001,
                "payoutSn": "P20260317001",
                "encryptedPayoutId": 1234567890,
                "transactionId": 987654321,
                "transactionType": "SALE",
                "payoutTime": "2026-03-17 12:00:00",
                "site": "SG",
                "storeTypeDisplay": "跨境店",
                "storeName": "Shopee-SG",
                "currency": "USD",
                "id": 1001,
                "platformCode": "shopee",
                "adjType": "Refund Amount"
            }
        ]
    }
}
```
