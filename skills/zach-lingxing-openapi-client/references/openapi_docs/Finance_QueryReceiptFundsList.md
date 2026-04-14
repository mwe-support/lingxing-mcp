# 查询收款单列表
支持查询收款单列表

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/queryReceiptFundsList` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| endDate | 结束日期，必填，格式：yyyy-MM-dd | 否 | [string] | 2024-12-31 |
| length | 分页长度，默认20，最大200 | 否 | [int] | 20 |
| offset | 分页偏移量，默认0 | 否 | [int] | 0 |
| searchField | 搜索字段，必填，枚举值：supplier_name-供应商, order_sn-收款单号, purchase_order_sn-采购单号, purchase_return_order_sn-退货单号, create_user-创建人, remark-备注 | 否 | [string] | order_sn |
| searchFieldTime | 搜索时间字段，枚举值：create_time-申请时间, receipt_time-收款时间 | 否 | [string] | create_time |
| searchValue | 搜索值，搜索字段对应的值 | 否 | [string] | RK2024010001 |
| seniorSearchList | 高级筛选，JSON字符串格式 | 否 | [string] | [] |
| startDate | 开始日期，必填，格式：yyyy-MM-dd | 否 | [string] | 2024-01-01 |
| status | 状态筛选，String数组，枚举值：1-待收款, 2-已完成, 3-已作废, 121-待审批, 122-已驳回, 124-已作废 | 否 | [array] | ["1","2"] |

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/finance/queryReceiptFundsList?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "endDate": "2024-12-31",
    "length": 20,
    "offset": 0,
    "searchField": "order_sn",
    "searchFieldTime": "create_time",
    "searchValue": "RK2024010001",
    "seniorSearchList": [],
    "startDate": "2024-01-01",
    "status": ["1","2"]
}'
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 响应码 | 是 | [int] |  |
| data | 返回数据 | 是 | [object] |  |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>amount | 收款金额 | 是 | [string] | 15000 |
| data>>list>>createTime | 创建时间，格式：yyyy-MM-dd HH:mm:ss | 是 | [string] | 2024-01-10 10:20:30 |
| data>>list>>createUser | 创建人 | 是 | [string] | 张三 |
| data>>list>>currency | 币种代码 | 是 | [string] | CNY |
| data>>list>>icon | 收款金额币种符号 | 是 | [string] | ¥ |
| data>>list>>objectId | 应收对象ID | 是 | [long] | 1234567890 |
| data>>list>>objectName | 应收对象名称 | 是 | [string] | XX供应商 |
| data>>list>>objectType | 应收对象类型 | 是 | [string] | supplier |
| data>>list>>opTypes | 操作类型权限控制 | 是 | [object] |  |
| data>>list>>opTypes>>audit | 审批按钮控制，1-显示, 0-隐藏 | 是 | [int] | 1 |
| data>>list>>opTypes>>businessId | 业务ID | 是 | [string] | 12345 |
| data>>list>>opTypes>>cancel | 作废按钮控制，1-显示, 0-隐藏 | 是 | [int] | 1 |
| data>>list>>opTypes>>del | 删除按钮控制，1-显示, 0-隐藏 | 是 | [int] | 0 |
| data>>list>>opTypes>>edit | 编辑按钮控制，1-显示, 0-隐藏 | 是 | [int] | 1 |
| data>>list>>orderSn | 收款单号 | 是 | [string] | RK2024010001 |
| data>>list>>receiptTime | 收款时间，格式：yyyy-MM-dd HH:mm:ss | 是 | [string] | 2024-01-15 14:30:00 |
| data>>list>>remark | 备注信息 | 是 | [string] | 采购退货退款 |
| data>>list>>status | 状态，枚举值：1-待收款, 2-已完成, 3-已作废, 121-待审批, 122-已驳回, 124-已作废 | 是 | [int] | 2 |
| data>>list>>statusText | 状态文本 | 是 | [string] | 已完成 |
| data>>list>>type | 收款类型，枚举值：1-采购退款 | 是 | [int] | 1 |
| data>>list>>typeText | 收款类型文本 | 是 | [string] | 采购退款 |
| data>>total | 总记录数 | 是 | [int] | 100 |
| error_details | 错误详情 | 是 | [array] |  |
| message | 提示信息 | 是 | [string] |  |
| request_id | 请求id | 是 | [string] |  |
| response_time | 响应时间 | 是 | [string] |  |
| total | 总记录数 | 是 | [int] |  |

## 返回成功示例
```
{
    "code": 0,
    "message": "success",
    "error_details": [],
    "request_id": "a0d54debf93140f3b58d1ed81e8e3583.178.17255922733991817",
    "response_time": "2024-11-12 16:00:00",
    "data": {
        "list": [
            {
                "amount": "15000",
                "createTime": "2024-01-10 10:20:30",
                "createUser": "张三",
                "currency": "CNY",
                "icon": "¥",
                "objectId": 1234567890,
                "objectName": "XX供应商",
                "objectType": "supplier",
                "opTypes": {
                    "audit": 1,
                    "businessId": "12345",
                    "cancel": 1,
                    "del": 0,
                    "edit": 1
                },
                "orderSn": "RK2024010001",
                "receiptTime": "2024-01-15 14:30:00",
                "remark": "采购退货退款",
                "status": 2,
                "statusText": "已完成",
                "type": 1,
                "typeText": "采购退款"
            },
            {
                "amount": "5000",
                "createTime": "2024-02-01 09:00:00",
                "createUser": "李四",
                "currency": "USD",
                "icon": "$",
                "objectId": 2345678901,
                "objectName": "YY客户",
                "objectType": "customer",
                "opTypes": {
                    "audit": 0,
                    "businessId": "67890",
                    "cancel": 0,
                    "del": 1,
                    "edit": 0
                },
                "orderSn": "SK2024020002",
                "receiptTime": "2024-02-05 11:00:00",
                "remark": "销售订单预付款",
                "status": 121,
                "statusText": "待审批",
                "type": 2,
                "typeText": "销售收款"
            }
        ],
        "total": 2
    },
    "total": 2
}

```
