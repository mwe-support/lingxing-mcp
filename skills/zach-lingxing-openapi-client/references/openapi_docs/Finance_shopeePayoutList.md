# 回款明细-ShopeePayout

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/shopee/payout/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| compareLogic | 字段比较条件逻辑关系：<br>`AND` 所有条件都满足<br>`OR` 满足任一条件<br>默认 `AND` | 否 | [string] | AND |
| currencyCode | 目标货币代码（为空则使用原币种，切换后按打款时间汇率换算） | 否 | [string] | USD |
| endDate | 结束时间（拨款时间），格式 `yyyy-MM-dd`，默认当前日期 | 否 | [string] | 2026-03-17 |
| envKey | 环境标识 | 否 | [string] | prod |
| exportFields | 导出字段值 | 否 | [array] | ["payeeId","payoutAmount"] |
| fieldCompares | 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定） | 否 | [array] | [{"field":"payoutAmount","operator":"gte","value":100}] |
| length | 分页大小，默认 `20`，最大不超过 `200` | 是 | [number] | 20 |
| offset | 分页偏移，默认 `0` | 是 | [number] | 0 |
| platformCode | 平台码 | 否 | [string] | shopee |
| searchExactly | 是否精确匹配 | 否 | [boolean] | false |
| searchMultiValue | 多个搜索值（精确匹配） | 否 | [array] | ["PAY001","PAY002"] |
| searchSingleValue | 单个搜索值（支持模糊匹配，多个值用逗号分隔） | 否 | [string] | PAY001,PAY002 |
| searchType | 搜索类型：<br>`1` 付款ID | 否 | [string] | 1 |
| sids | 店铺 ID 数组 | 否 | [array] | [10001,10002] |
| sites | 站点数组 | 否 | [array] | ["SG","MY"] |
| sortField | 排序字段 | 否 | [string] | payoutTime |
| sortType | 排序方向：<br>`1` 升序/ASC<br>`0` 降序/DESC<br>默认 `0` | 否 | [string] | 0 |
| startDate | 开始时间（拨款时间），格式 `yyyy-MM-dd`，默认当前月份第一天 | 否 | [string] | 2026-03-01 |
| storeType | 店铺类型：<br>`1` 跨境店(CB) | 否 | [number] | 1 |


## 请求cURL示例

```bash
curl --location 'https://openapi.lingxing.com/basicOpen/finance/shopee/payout/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "compareLogic": "AND",
    "currencyCode": "USD",
    "startDate": "2026-03-01",
    "endDate": "2026-03-17",
    "length": 20,
    "offset": 0,
    "searchType": "1",
    "searchSingleValue": "PAY001",
    "sids": [10001,10002],
    "sites": ["SG","MY"],
    "storeType": 1
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
| data>>totalSum>>difference | 差额汇总 | 是 | [string] | 12.35 |
| data>>totalSum>>fromAmount | 结算金额汇总 | 是 | [string] | 980.50 |
| data>>totalSum>>fromCurrency | 结算币种代码 | 是 | [string] | USD |
| data>>totalSum>>fromCurrencyIcon | 结算币种图标 | 是 | [string] | $ |
| data>>totalSum>>payoutAmount | 拨款金额汇总 | 是 | [string] | 992.85 |
| data>>totalSum>>payoutCurrency | 拨款币种代码 | 是 | [string] | USD |
| data>>totalSum>>payoutCurrencyIcon | 拨款币种图标 | 是 | [string] | $ |
| data>>totalSum>>settlementAdjustmentTotal | 总调整金额汇总（Adjustment） | 是 | [string] | 52.35 |
| data>>totalSum>>settlementIncomeTotal | 总结算金额汇总（Income） | 是 | [string] | 940.50 |
| data>>totalSum>>settlementTotal | 结算明细总和汇总 | 是 | [string] | 992.85 |
| data>>totalSum>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>uniqueNo | 业务唯一键 | 是 | [string] | SHOPEE-PAYOUT-001 |
| data>>list>>payoutAmount | 拨款金额（拨款币种） | 是 | [string] | 520.30 |
| data>>list>>payoutCurrencyIcon | 拨款币种图标 | 是 | [string] | $ |
| data>>list>>settlementAdjustmentTotal | 总调整金额（Adjustment） | 是 | [string] | 20.00 |
| data>>list>>settlementTotal | 结算明细总和（Income + Adjustment） | 是 | [string] | 520.30 |
| data>>list>>fromCurrencyIcon | 结算币种图标 | 是 | [string] | $ |
| data>>list>>payoutCurrency | 拨款币种 | 是 | [string] | USD |
| data>>list>>payoutTime | 拨款时间 | 是 | [string] | 2026-03-17 12:30:00 |
| data>>list>>settlementIncomeTotal | 总结算金额（Income） | 是 | [string] | 500.30 |
| data>>list>>exchangeRate | 汇率 | 是 | [string] | 1.0000 |
| data>>list>>payService | 收款渠道 | 是 | [string] | Payoneer |
| data>>list>>storeName | 店铺名 | 是 | [string] | Shopee-SG |
| data>>list>>fromCurrency | 结算币种 | 是 | [string] | USD |
| data>>list>>id | 主键 ID | 是 | [number] | 1001 |
| data>>list>>payeeId | 付款ID | 是 | [number] | 99887766 |
| data>>list>>originalPayoutTime | 原始拨款时间戳 | 是 | [number] | 1742198400 |
| data>>list>>storeType | 店铺类型：1-跨境店(CB) | 是 | [number] | 1 |
| data>>list>>fromAmount | 结算金额（结算币种） | 是 | [string] | 500.30 |
| data>>list>>siteDisplay | 站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>storeId | 店铺 ID | 是 | [number] | 10001 |
| data>>list>>encryptedPayoutId | 付款加密ID | 是 | [number] | 1234567890 |
| data>>list>>site | 站点代码 | 是 | [string] | SG |
| data>>list>>storeTypeDisplay | 店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>difference | 差额（总拨款金额（结算）-总订单收入-总调整费） | 是 | [string] | 6.20 |
| data>>list>>platformCode | 平台码 | 是 | [string] | shopee |

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
            "difference": "12.35",
            "fromAmount": "980.50",
            "fromCurrency": "USD",
            "fromCurrencyIcon": "$",
            "payoutAmount": "992.85",
            "payoutCurrency": "USD",
            "payoutCurrencyIcon": "$",
            "settlementAdjustmentTotal": "52.35",
            "settlementIncomeTotal": "940.50",
            "settlementTotal": "992.85",
            "totalCount": 2
        },
        "list": [
            {
                "uniqueNo": "SHOPEE-PAYOUT-001",
                "payoutAmount": "520.30",
                "payoutCurrencyIcon": "$",
                "settlementAdjustmentTotal": "20.00",
                "settlementTotal": "520.30",
                "fromCurrencyIcon": "$",
                "payoutCurrency": "USD",
                "payoutTime": "2026-03-17 12:30:00",
                "settlementIncomeTotal": "500.30",
                "exchangeRate": "1.0000",
                "payService": "Payoneer",
                "storeName": "Shopee-SG",
                "fromCurrency": "USD",
                "id": 1001,
                "payeeId": 99887766,
                "originalPayoutTime": 1742198400,
                "storeType": 1,
                "fromAmount": "500.30",
                "siteDisplay": "新加坡",
                "storeId": 10001,
                "encryptedPayoutId": 1234567890,
                "site": "SG",
                "storeTypeDisplay": "跨境店",
                "difference": "6.20",
                "platformCode": "shopee"
            }
        ]
    }
}
```
