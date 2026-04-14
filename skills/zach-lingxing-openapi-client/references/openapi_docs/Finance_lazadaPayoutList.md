# 回款明细-LazadaPayout

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/lazada/payout/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| compareLogic | 字段比较条件逻辑关系：<br>`AND` 所有条件都满足<br>`OR` 满足任一条件<br>默认 `AND` | 否 | [string] | AND |
| currencyCode | 目标货币代码（为空则使用原币种） | 否 | [string] | USD |
| endDate | 结束时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `23:59:59` | 否 | [string] | 2026-03-17 23:59:59 |
| envKey | 环境标识 | 否 | [string] | prod |
| exportFields | 导出字段值 | 否 | [array] | ["statementNumber","payoutAmount"] |
| fieldCompares | 字段比较条件列表（多个条件之间的逻辑关系由 `compareLogic` 指定） | 否 | [array] | [{"field":"payoutAmount","operator":"gte","value":100}] |
| hasDifference | 是否有差额：`true`=有差额，`false`=无差额，`null`=全部 | 否 | [boolean] | true |
| length | 分页大小，默认 `20`，最大不超过 `200` | 是 | [number] | 20 |
| offset | 分页偏移，默认 `0` | 是 | [number] | 0 |
| paid | 支付标志：<br>`0` 未支付<br>`1` 已支付 | 否 | [number] | 1 |
| platformCode | 平台码 | 否 | [string] | lazada |
| searchExactly | 是否精确匹配 | 否 | [boolean] | false |
| searchMultiValue | 多个搜索值（精确匹配） | 否 | [array] | ["ST20260317001","ST20260317002"] |
| searchSingleValue | 单个搜索值（支持模糊匹配，多个值用逗号分隔） | 否 | [string] | ST20260317001,ST20260317002 |
| searchType | 搜索类型：<br>`1` 回款编号 | 否 | [number] | 1 |
| sids | 店铺 ID 数组（全部店铺/指定店铺） | 否 | [array] | [10001,10002] |
| sites | 站点数组 | 否 | [array] | ["SG","MY"] |
| sortField | 排序字段 | 否 | [string] | payoutTime |
| sortType | 排序方向：<br>`1` 升序/ASC<br>`0` 降序/DESC<br>默认 `0` | 否 | [string] | 0 |
| startDate | 开始时间，支持 `yyyy-MM-dd` 或 `yyyy-MM-dd HH:mm:ss` 格式，仅日期时自动补充 `00:00:00` | 否 | [string] | 2026-03-01 00:00:00 |
| storeTypes | 店铺类型数组：<br>`1` 跨境店<br>`2` 本土店 | 否 | [array] | [1,2] |
| timeType | 时间类型：<br>`1` 回款时间<br>`2` 结算周期<br>默认 `1` | 否 | [number] | 1 |


## 请求cURL示例

```bash
curl --location 'https://openapi.lingxing.com/basicOpen/finance/lazada/payout/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "compareLogic": "AND",
    "currencyCode": "USD",
    "startDate": "2026-03-01 00:00:00",
    "endDate": "2026-03-17 23:59:59",
    "length": 20,
    "offset": 0,
    "paid": 1,
    "searchType": 1,
    "searchSingleValue": "ST20260317001",
    "sites": ["SG","MY"],
    "sids": [10001,10002],
    "storeTypes": [1,2],
    "timeType": 1,
    "hasDifference": true,
    "currencyCode": "USD"
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
| data>>totalSum>>payoutAmount | 回款金额汇总 | 是 | [string] | 1250.50 |
| data>>totalSum>>settlementDifference | 结算明细差额汇总 | 是 | [string] | 12.35 |
| data>>totalSum>>totalCount | 总记录数 | 是 | [number] | 2 |
| data>>totalSum>>currencyCode | 币种代码 | 是 | [string] | USD |
| data>>totalSum>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>payoutAmount | 回款金额（数值部分） | 是 | [string] | 650.20 |
| data>>list>>settlementDifference | 结算明细差额（回款金额-结算明细汇总金额） | 是 | [string] | 6.20 |
| data>>list>>gmtModified | 修改时间 | 是 | [string] | 2026-03-17 15:20:00 |
| data>>list>>settlementEndTime | 结算周期结束时间 | 是 | [string] | 2026-03-15 23:59:59 |
| data>>list>>settlementStartTime | 结算周期开始时间 | 是 | [string] | 2026-03-01 00:00:00 |
| data>>list>>payout | payout | 是 | [string] | Payout |
| data>>list>>closingBalance | 期末余额 | 是 | [string] | 120.00 |
| data>>list>>currencyIcon | 币种图标 | 是 | [string] | $ |
| data>>list>>payoutTime | 回款时间 | 是 | [string] | 2026-03-17 12:30:00 |
| data>>list>>storeName | 店铺名 | 是 | [string] | Lazada-SG |
| data>>list>>id | 主键 ID | 是 | [number] | 1001 |
| data>>list>>statementNumber | 回款编号 | 是 | [string] | ST20260317001 |
| data>>list>>openingBalance | 期初余额 | 是 | [string] | 50.00 |
| data>>list>>storeType | 店铺类型：1-跨境店, 2-本土店 | 是 | [number] | 1 |
| data>>list>>siteDisplay | 站点中文展示 | 是 | [string] | 新加坡 |
| data>>list>>storeId | 店铺 ID | 是 | [number] | 10001 |
| data>>list>>gmtCreate | 创建时间 | 是 | [string] | 2026-03-17 12:00:00 |
| data>>list>>site | 站点代码 | 是 | [string] | SG |
| data>>list>>storeTypeDisplay | 店铺类型展示 | 是 | [string] | 跨境店 |
| data>>list>>sourceType | 数据来源：1-接口, 2-报表导入 | 是 | [number] | 1 |
| data>>list>>paid | 支付标志 | 是 | [number] | 1 |
| data>>list>>feesOnRefundsTotal | 退款手续费 | 是 | [string] | 5.80 |
| data>>list>>statementPeriodOrigin | 结算周期原始解析值 | 是 | [string] | 2026-03-01~2026-03-15 |
| data>>list>>updatedAt | 回款更新时间 | 是 | [string] | 2026-03-17 15:30:00 |
| data>>list>>currencyCode | 币种 | 是 | [string] | USD |
| data>>list>>platformCode | 平台码 | 是 | [string] | lazada |

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
            "payoutAmount": "1250.50",
            "settlementDifference": "12.35",
            "totalCount": 2,
            "currencyCode": "USD",
            "currencyIcon": "$"
        },
        "list": [
            {
                "payoutAmount": "650.20",
                "settlementDifference": "6.20",
                "gmtModified": "2026-03-17 15:20:00",
                "settlementEndTime": "2026-03-15 23:59:59",
                "settlementStartTime": "2026-03-01 00:00:00",
                "payout": "Payout",
                "closingBalance": "120.00",
                "currencyIcon": "$",
                "payoutTime": "2026-03-17 12:30:00",
                "storeName": "Lazada-SG",
                "id": 1001,
                "statementNumber": "ST20260317001",
                "openingBalance": "50.00",
                "storeType": 1,
                "siteDisplay": "新加坡",
                "storeId": 10001,
                "gmtCreate": "2026-03-17 12:00:00",
                "site": "SG",
                "storeTypeDisplay": "跨境店",
                "sourceType": 1,
                "paid": 1,
                "feesOnRefundsTotal": "5.80",
                "statementPeriodOrigin": "2026-03-01~2026-03-15",
                "updatedAt": "2026-03-17 15:30:00",
                "currencyCode": "USD",
                "platformCode": "lazada"
            },
            {
                "payoutAmount": "600.30",
                "settlementDifference": "6.15",
                "gmtModified": "2026-03-17 16:10:00",
                "settlementEndTime": "2026-03-15 23:59:59",
                "settlementStartTime": "2026-03-01 00:00:00",
                "payout": "Payout",
                "closingBalance": "115.00",
                "currencyIcon": "$",
                "payoutTime": "2026-03-17 13:10:00",
                "storeName": "Lazada-MY",
                "id": 1002,
                "statementNumber": "ST20260317002",
                "openingBalance": "42.00",
                "storeType": 2,
                "siteDisplay": "马来西亚",
                "storeId": 10002,
                "gmtCreate": "2026-03-17 12:20:00",
                "site": "MY",
                "storeTypeDisplay": "本土店",
                "sourceType": 1,
                "paid": 0,
                "feesOnRefundsTotal": "4.20",
                "statementPeriodOrigin": "2026-03-01~2026-03-15",
                "updatedAt": "2026-03-17 16:20:00",
                "currencyCode": "USD",
                "platformCode": "lazada"
            }
        ]
    }
}
```
