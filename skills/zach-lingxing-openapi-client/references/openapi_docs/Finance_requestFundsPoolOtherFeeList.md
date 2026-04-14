# 查询请款池-其他费用

## 接口信息

| API Path | 请求协议 | 请求方式 | [令牌桶容量](/docs/Guidance/newInstructions?id=_5-限流算法说明) |
| :------------ |:-----| :------------ | :------------ |
| `/basicOpen/finance/requestFundsPool/otherFee/list` | HTTPS | POST | 1 |

## 请求参数

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| endTime | 结束时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度 | <font color="red">是</font> | [string] | 2024-12-31 |
| startTime | 开始时间，必填，格式：yyyy-MM-dd，根据searchFieldTime字段确定查询维度 | <font color="red">是</font> | [string] | 2024-01-01 |
| length | 分页长度 | 否 | [int] | 20 |
| offset | 分页偏移量 | 否 | [int] | 0 |
| purchaserIds | 采购方ID列表，筛选指定采购方的其他费用 | 否 | [array] | [1234567890,9876543210] |
| searchField | 搜索字段，枚举值：order_sn-采购单号, create_username-采购员，配合searchValue使用 | 否 | [string] | order_sn |
| searchFieldTime | 时间维度，枚举值：create_time-创建时间, close_time-付清时间，默认create_time | 否 | [string] | create_time |
| searchValue | 搜索值，根据searchField字段进行搜索，支持模糊查询 | 否 | [string] | PO20240101 |
| status | 付款状态，枚举值：0-查询未付清, 1-查询已付清，不传默认查询全部 | 否 | [int] | 0 |
| supplierIds | 应付对象ID列表，筛选指定供应商的其他费用 | 否 | [array] | [1234567890,9876543210] |

## 请求cURL示例
```
curl --location 'https://openapi.lingxing.com/basicOpen/finance/requestFundsPool/otherFee/list?access_token=value&timestamp=value&sign=value&app_key=value' \
--header 'Content-Type: application/json' \
--data '{
    "endTime": "2024-12-31",
    "startTime": "2024-01-01",
    "length": 20,
    "offset": 0,
    "purchaserIds": [1234567890,9876543210],
    "searchField": "order_sn",
    "searchFieldTime": "create_time",
    "searchValue": "PO20240101",
    "status": 0,
    "supplierIds": [1234567890,9876543210]
}'
```

## 返回结果
Json Object

| 参数名 | 说明 | 必填 | 类型 | 示例 |
| :------------ | :------------ | :------------ | :------------ | :------------ |
| code | 响应码 | 是 | [int] |  |
| data | 返回数据 | 是 | [object] |  |
| data>>list | 列表数据 | 是 | [array] |  |
| data>>list>>amountNotPaid | 未付金额，还需支付的金额 | 是 | [string] | 2500 |
| data>>list>>amountPaid | 已付金额，已完成支付的金额 | 是 | [string] | 1500.5 |
| data>>list>>applyedAmount | 已请款金额，已完成请款的金额 | 是 | [string] | 3500 |
| data>>list>>applyedDiscount | 已请款折扣，已完成请款的折扣金额 | 是 | [string] | 50 |
| data>>list>>applyedGoodsValue | 已请款货值，已完成请款的货物价值 | 是 | [string] | 4500 |
| data>>list>>applyingAmount | 申请中金额，正在请款流程中的金额 | 是 | [string] | 2000 |
| data>>list>>applyingDiscount | 请款中折扣，正在请款流程中的折扣金额 | 是 | [string] | 30 |
| data>>list>>applyingGoodsValue | 请款中货值，正在请款流程中的货物价值 | 是 | [string] | 3000 |
| data>>list>>applyingOrders | 请款中订单ID列表，正在请款流程中的订单 | 是 | [array] | [54321,98765] |
| data>>list>>closeDate | 结清日期，格式：yyyy-MM-dd，完成付清的日期 | 是 | [string] | 2024-11-15 |
| data>>list>>closeTime | 结清时间戳，完成付清的时间戳（秒） | 是 | [int] | 1700000000 |
| data>>list>>closedByUid | 结清操作人UID，完成付清的用户ID | 是 | [long] | 1234567890 |
| data>>list>>closedByUser | 结清操作人姓名，完成付清的操作人员 | 是 | [string] | 张三 |
| data>>list>>closedRemark | 结清备注，付清时填写的备注说明 | 是 | [string] | 已全额付清 |
| data>>list>>currency | 币种代码，费用金额使用的货币类型，如：CNY、USD | 是 | [string] | CNY |
| data>>list>>customOrderSn | 自定义单号，用户自定义的订单编号 | 是 | [string] | CUSTOM-2024-001 |
| data>>list>>discountAmount | 折扣金额，优惠折扣的金额 | 是 | [string] | 100 |
| data>>list>>fee | 费用金额，其他费用的总金额 | 是 | [string] | 5000 |
| data>>list>>feeTypeId | 费用类型ID，费用分类的唯一标识 | 是 | [long] | 1234567890 |
| data>>list>>feeTypeName | 费用类型名称，费用分类的名称 | 是 | [string] | 运输费 |
| data>>list>>icon | 图标标识，费用类型的图标地址或标识 | 是 | [string] | icon_other_fee.png |
| data>>list>>id | 其他费用记录ID，唯一标识 | 是 | [int] | 1001 |
| data>>list>>isAutoDone | 是否自动完成，枚举值：0-否, 1-是，标识是否系统自动结清 | 是 | [int] | 0 |
| data>>list>>notApplyAmount | 未请款金额，还未发起请款的金额 | 是 | [string] | 1000 |
| data>>list>>optRealname | 采购员 | 是 | [string] | 李四 |
| data>>list>>optUid | 创建操作人UID，创建该费用的用户ID | 是 | [long] | 1234567890 |
| data>>list>>orderSn | 订单编号，关联的采购单号 | 是 | [string] | PO202401010001 |
| data>>list>>paidOrders | 已付款请款单ID列表，记录已关联的付款单据 | 是 | [array] | [12345,67890] |
| data>>list>>payStatus | 付款状态，枚举值：0-未申请, 1-申请中, 2-已申请, 3-已付清 | 是 | [int] | 2 |
| data>>list>>payStatusText | 付款状态文本描述，如：未付清、已付清等 | 是 | [string] | 未付清 |
| data>>list>>payableAmount | 应付金额，需要支付的总金额 | 是 | [string] | 5000 |
| data>>list>>purchaserId | 采购方ID，发起采购的组织或个人ID | 是 | [long] | 1234567890 |
| data>>list>>purchaserName | 采购方名称，发起采购的组织或个人名称 | 是 | [string] | 深圳采购中心 |
| data>>list>>supplierId | 应付对象ID，供应商或应付方的ID | 是 | [long] | 1234567890 |
| data>>list>>supplierName | 应付对象名称，供应商或应付方的名称 | 是 | [string] | 顺丰物流 |
| data>>list>>unapplyGoodsValue | 未请款货值，还未发起请款的货物价值 | 是 | [string] | 1500 |
| data>>list>>updateUid | 更新操作人UID，最后修改该记录的用户ID | 是 | [long] | 1234567890 |
| data>>list>>wareHouseName | 仓库名称，关联的仓库名称 | 是 | [string] | 华南仓库 |
| data>>list>>wid | 仓库ID，关联的仓库唯一标识 | 是 | [long] | 1234567890 |
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
  "data": {
    "list": [
      {
        "amountNotPaid": "2500",
        "amountPaid": "1500.5",
        "applyedAmount": "3500",
        "applyedDiscount": "50",
        "applyedGoodsValue": "4500",
        "applyingAmount": "2000",
        "applyingDiscount": "30",
        "applyingGoodsValue": "3000",
        "applyingOrders": [
          54321,
          98765
        ],
        "closeDate": "2024-11-15",
        "closeTime": 1700000000,
        "closedByUid": 1234567890,
        "closedByUser": "张三",
        "closedRemark": "已全额付清",
        "currency": "CNY",
        "customOrderSn": "CUSTOM-2024-001",
        "discountAmount": "100",
        "fee": "5000",
        "feeTypeId": 1234567890,
        "feeTypeName": "运输费",
        "icon": "icon_other_fee.png",
        "id": 1001,
        "isAutoDone": 0,
        "notApplyAmount": "1000",
        "optRealname": "李四",
        "optUid": 1234567890,
        "orderSn": "PO202401010001",
        "paidOrders": [
          12345,
          67890
        ],
        "payStatus": 2,
        "payStatusText": "未付清",
        "payableAmount": "5000",
        "purchaserId": 1234567890,
        "purchaserName": "深圳采购中心",
        "supplierId": 1234567890,
        "supplierName": "顺丰物流",
        "unapplyGoodsValue": "1500",
        "updateUid": 1234567890,
        "wareHouseName": "华南仓库",
        "wid": 1234567890
      },
      {
        "amountNotPaid": "1000",
        "amountPaid": "500",
        "applyedAmount": "2000",
        "applyedDiscount": "20",
        "applyedGoodsValue": "2500",
        "applyingAmount": "500",
        "applyingDiscount": "10",
        "applyingGoodsValue": "1000",
        "applyingOrders": [
          11223,
          44556
        ],
        "closeDate": null,
        "closeTime": null,
        "closedByUid": null,
        "closedByUser": null,
        "closedRemark": null,
        "currency": "USD",
        "customOrderSn": "CUSTOM-2024-002",
        "discountAmount": "50",
        "fee": "3000",
        "feeTypeId": 2345678901,
        "feeTypeName": "关税",
        "icon": "icon_tariff.png",
        "id": 1002,
        "isAutoDone": 0,
        "notApplyAmount": "500",
        "optRealname": "王五",
        "optUid": 2345678901,
        "orderSn": "PO202401020002",
        "paidOrders": [
          99887
        ],
        "payStatus": 1,
        "payStatusText": "申请中",
        "payableAmount": "3000",
        "purchaserId": 2345678901,
        "purchaserName": "上海采购部",
        "supplierId": 2345678901,
        "supplierName": "UPS快递",
        "unapplyGoodsValue": "500",
        "updateUid": 2345678901,
        "wareHouseName": "华东仓库",
        "wid": 2345678901
      }
    ],
    "total": 2
  },
  "error_details": [],
  "message": "成功",
  "request_id": "some_request_id_123",
  "response_time": "2024-01-01 12:00:00",
  "total": 2
}

```
