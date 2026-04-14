# 查询结算中心 - 结算汇总

支持查询亚马逊结算中心的结算汇总数据

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ | :------------ | :------------ | :------------ |
| `/bd/sp/api/open/settlement/summary/list` | HTTPS | POST | 10 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |
|offset|分页偏移量|[int]|否|0|
|length|分页长度|[int]|否|20|
|countryCodes|国家，[查询亚马逊市场列表](/docs/BasicData/AllMarketplace.md)接口对应字段mid|[array]|否|[1]|
|sids|店铺id ，对应[查询亚马逊店铺列表](docs/BasicData/SellerLists)接口对应字段【sid】|[array]|否|[136]|
|currencyCode|币种|[string]|否|"USD"|
|dateType|时间类型：<br>0 结算开始时间<br>1 结算结束时间<br>2 转账时间|[string]|是|1|
|startDate|开始时间【时间间隔最长不得超过90天】|[string]|是|2023-09-25|
|endDate|结束时间【时间间隔最长不得超过90天】|[string]|是|2023-12-24|
|searchField|搜索字段：<br> id 结算编号<br>settlement_id 账单编号|[string]|否|id|
|searchValue|搜索值|[array]|否|["LWCBG07Y55I3","D506VLLNX1VT"]|

## 请求示例
```
{
    "offset": 0,
    "length": 20,
    "countryCodes": [
        1
    ],
    "sids": [
        136
    ],
    "currencyCode": "USD",
    "dateType": 1,
    "startDate": "2023-9-25",
    "endDate": "2023-12-24",
    "searchField": "id",
    "searchValue": [
        "LWCBG07Y55I3",
        "D506VLLNX1VT"
    ]
}
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |  
| :------------ | :------------ | :------------ | :------------ | :------------ |  
|code|状态码，0 成功|是|[int]|0|
|msg|提示信息|是|[string]||
|data|响应数据|是|[array]||
|data>>total|总数|是|[int]||
|data>>records|列表|是|[array]||
|data>>records>>id|结算编号|是|[string]||
|data>>records>>sid|店铺|是|[int]||
|data>>records>>storeName|店铺名|是|[string]||
|data>>records>>countryCode|国家|是|[string]||
|data>>records>>customerCountryCode|国家code|是|[string]||
|data>>records>>sellerId|亚马逊账号id|是|[string]||
|data>>records>>accountType|报告类型|是|[string]||
|data>>records>>processingStatus|结算状态：<br>Open 待结算<br>Pending 结算中<br>Closed 已结算|是|[string]||
|data>>records>>fundTransferStatus|转账状态：<br>Succeeded 已转账<br>Failed 失败<br>Processing 转账中<br>Unknown 未知|是|[string]||
|data>>records>>reconciliationResult|对账结果|是|[string]||
|data>>records>>reconciliationResultMap|对账详情|是|[object]||
|data>>records>>reconciliationResultMap>>【月份值】>>checkStatus|对账状态|是|[string]||
|data>>records>>reconciliationResultMap>>【月份值】>>checkUser|对账人|是|[string]||
|data>>records>>reconciliationResultMap>>【月份值】>>checkDate|对账日期|是|[string]||
|data>>records>>originalTotalCurrencyCode|应收币种|是|[string]||
|data>>records>>originalTotalCurrencyAmount|应收金额|是|[number]||
|data>>records>>convertedTotalCurrencyCode|转账币种|是|[string]||
|data>>records>>convertedTotalCurrencyAmount|转账金额|是|[number]||
|data>>records>>comment|备注|是|[string]||
|data>>records>>financialEventGroupStartLocale|结算开始时间|是|[string]||
|data>>records>>financialEventGroupEndLocale|结算结束时间|是|[string]||
|data>>records>>fundTransferDate|转账日期|是|[string]||
|data>>records>>fundTransferDateLocale|转账日期-当地|是|[string]||
|data>>records>>settlementId|settlementId|是|[string]||
|data>>records>>accountTail|银行尾号|是|[string]||
|data>>records>>traceId|追踪编号|是|[string]||
|data>>records>>financialEventGroupId|财务事件组id|是|[string]||
|data>>records>>sale|销售|是|[object]||
|data>>records>>sale>>sale|销售金额|是|[number]||
|data>>records>>sale>>product|产品销售|是|[number]||
|data>>records>>sale>>freight|买家运费|是|[number]||
|data>>records>>sale>>packing|包装|是|[number]||
|data>>records>>sale>>other|其他|是|[number]||
|data>>records>>sale>>tax|税|是|[number]||
|data>>records>>refund|退款|是|[object]||
|data>>records>>refund>>refund|退款|是|[number]||
|data>>records>>refund>>saleRefund|收入退款|是|[number]||
|data>>records>>refund>>feeRefund|费用退款|是|[number]||
|data>>records>>refund>>tax|税退款|是|[number]||
|data>>records>>pay|支出|是|[object]||
|data>>records>>pay>>pay|支出|是|[number]||
|data>>records>>pay>>storage|仓储费用|是|[number]||
|data>>records>>pay>>amazon|亚马逊费用|是|[number]||
|data>>records>>pay>>ad|广告费|是|[number]||
|data>>records>>pay>>promotion|促销费|是|[number]||
|data>>records>>pay>>other|其他|是|[number]||
|data>>records>>transfer|转账|是|[object]||
|data>>records>>transfer>>convertedTotalCurrencyAmount|应收金额|是|[number]||
|data>>records>>transfer>>beginningBalanceCurrencyAmount|期初余额|是|[number]||
|data>>records>>transfer>>originalTotalCurrencyAmount|本期结算|是|[number]||
|data>>records>>transfer>>previousReserveAmount|预留退回|是|[number]||
|data>>records>>transfer>>currentReserveAmount|本期预留|是|[number]||
|data>>records>>transfer>>creditCardDeduction|信用卡扣款|是|[number]||
|data>>records>>bucket|bucket|是|[string]||
|data>>records>>s3FileKey|s3_file_key|是|[string]||
|data>>records>>originCurrencyIcon|应收币种符号|是|[string]||
|data>>records>>convertCurrencyIcon|转账币种符号|是|[string]|&nbsp;|

## 返回成功示例
```
{
    "code": 0,
    "msg": null,
    "data": {
        "total": 7,
        "records": [
            {
                "id": "1C6CP3QMDVLHW",
                "sid": 6,
                "storeName": "XinghaiDirect-1567",
                "countryCode": "US",
                "customerCountryCode": "",
                "sellerId": "xxxxxxxxxxxxxxxx",
                "accountType": "Standard",
                "processingStatus": "Closed",
                "fundTransferStatus": "Succeeded",
                "reconciliationResult": "未对账",
                "reconciliationResultMap": {
                    "2022-09": {
                        "checkStatus": "未对账",
                        "checkUser": null,
                        "checkDate": null
                    },
                    "2022-08": {
                        "checkStatus": "未对账",
                        "checkUser": null,
                        "checkDate": null
                    }
                },
                "originalTotalCurrencyCode": "USD",
                "originalTotalCurrencyAmount": 415.47,
                "convertedTotalCurrencyCode": "USD",
                "convertedTotalCurrencyAmount": 415.47,
                "comment": null,
                "financialEventGroupStartLocale": "2022-08-25T03:28:56-07:00",
                "financialEventGroupEndLocale": "2022-09-08T03:28:56-07:00",
                "fundTransferDate": "2022-09-09T10:37:53Z",
                "fundTransferDateLocale": "2022-09-09T03:37:53-07:00",
                "settlementId": "",
                "accountTail": "225",
                "traceId": "1BQR1QINCHA9LN9",
                "financialEventGroupId": "xJorkEeGz7nDQ0Ul-fGDf_LjO1EQOzJN_j4oTYmY-GU",
                "sale": {
                    "sale": 720.07,
                    "product": 718.91,
                    "freight": 3.81,
                    "packing": 0.00,
                    "other": -2.65,
                    "tax": 0.00
                },
                "refund": {
                    "refund": 0.00,
                    "saleRefund": 0.00,
                    "feeRefund": 0.00,
                    "tax": 0.00
                },
                "pay": {
                    "pay": -304.60,
                    "storage": 0.00,
                    "amazon": -304.60,
                    "ad": 0.00,
                    "promotion": 0.00,
                    "other": 0.00
                },
                "transfer": {
                    "convertedTotalCurrencyAmount": 415.47,
                    "beginningBalanceCurrencyAmount": 0.00,
                    "originalTotalCurrencyAmount": 415.47,
                    "previousReserveAmount": 0.00,
                    "currentReserveAmount": 0.00,
                    "creditCardDeduction": 0.00
                },
                "bucket": "",
                "s3FileKey": "",
                "originCurrencyIcon": "$",
                "convertCurrencyIcon": "$",
                "accountInfo": null
            }
        ]
    }
}
```