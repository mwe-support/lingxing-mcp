"""Excel layouts aligned with Lingxing ERP web exports."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Iterable


@dataclass(frozen=True)
class ExportColumn:
    header: str
    number_format: str | None = None


@dataclass(frozen=True)
class ExportProfile:
    name: str
    sheet_name: str
    columns: tuple[ExportColumn, ...]
    prepare_rows: Callable[[Iterable[dict[str, Any]]], list[dict[str, Any]]]
    group_header: str | None = None
    merge_order_columns: int = 0
    unavailable_columns: tuple[str, ...] = ()


_COUNTRY_NAMES = {
    "US": "美国",
    "CA": "加拿大",
    "MX": "墨西哥",
    "BR": "巴西",
    "UK": "英国",
    "GB": "英国",
    "DE": "德国",
    "FR": "法国",
    "IT": "意大利",
    "ES": "西班牙",
    "NL": "荷兰",
    "SE": "瑞典",
    "PL": "波兰",
    "TR": "土耳其",
    "JP": "日本",
    "AU": "澳大利亚",
    "IN": "印度",
    "AE": "阿联酋",
    "SA": "沙特阿拉伯",
    "SG": "新加坡",
}

_SETTLEMENT_STATUS = {
    "OPEN": "待结算",
    "PENDING": "结算中",
    "CLOSED": "已结算",
    "RECONCILED": "已对账",
}

_TRANSFER_STATUS = {
    "SUCCEEDED": "已转账",
    "PROCESSING": "转账中",
    "FAILED": "失败",
    "UNKNOWN": "未知",
}

_CURRENCY_ICONS = {
    "CNY": "￥",
    "USD": "$",
    "GBP": "￡",
    "EUR": "€",
    "JPY": "¥",
    "CAD": "C$",
    "AUD": "A$",
    "MXN": "MX$",
}


def _value(record: dict[str, Any], *names: str) -> Any:
    for name in names:
        value = record.get(name)
        if value not in (None, ""):
            return value
    return None


def _text(value: Any) -> str | None:
    if value in (None, ""):
        return None
    return str(value)


def _number(value: Any) -> float | int | None:
    if value in (None, ""):
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return int(number) if number.is_integer() else number


def _json_value(value: Any, fallback: Any) -> Any:
    if not isinstance(value, str):
        return value if value is not None else fallback
    text = value.strip()
    if not text:
        return fallback
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return fallback


def _translated(value: Any, mapping: dict[str, str]) -> Any:
    if value in (None, ""):
        return None
    text = str(value)
    return mapping.get(text.upper(), text)


def _country_name(record: dict[str, Any]) -> Any:
    explicit = _value(record, "country", "countryName")
    if explicit:
        return explicit
    code = str(_value(record, "countryCode", "country_code") or "").upper()
    return _COUNTRY_NAMES.get(code, code or None)


def _settlement_type(record: dict[str, Any]) -> str | None:
    shipped = _value(record, "shipmentsDateLocale")
    settled = _value(record, "financePostedDateLocale")
    if not shipped or not settled:
        return None
    try:
        ship_date = datetime.fromisoformat(str(shipped)[:19])
        settle_date = datetime.fromisoformat(str(settled)[:19])
    except ValueError:
        return None
    months = (settle_date.year - ship_date.year) * 12 + settle_date.month - ship_date.month
    if months <= 0:
        return "已发货本月结算"
    return f"已发货{months:02d}月后结算"


def _settlement_rows(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for record in records:
        rows.append(
            {
                "店铺名称": _value(record, "sellerName"),
                "国家": _country_name(record),
                "订单号": _text(_value(record, "amazonOrderId")),
                "配送编号": _text(_value(record, "shipmentId")),
                "自定义订单编号": _text(_value(record, "merchantOrderId")),
                "msku": _text(_value(record, "msku")),
                "SKU": _text(_value(record, "localSku")),
                "品名": _value(record, "localName"),
                "品牌": _value(record, "brandName"),
                "分类": _value(record, "categoryName"),
                "listing负责人": _value(record, "listing"),
                "产品开发负责人": _value(record, "productDeveloper"),
                "数量": _number(_value(record, "quantity")),
                "下单时间": _value(record, "purchaseDateLocale"),
                "付款时间": _value(record, "paymentsDateLocale"),
                "发货时间": _value(record, "shipmentsDateLocale"),
                "结算时间": _value(record, "financePostedDateLocale"),
                "结算编号": _text(_value(record, "settlementId")),
                "发货与结算的时间间隔": _value(record, "daysBetweenShipAndFiance"),
                "结算类型": _settlement_type(record),
                "转账时间": _value(record, "fundTransferDateLocale"),
                "结算状态": _translated(_value(record, "processingStatus"), _SETTLEMENT_STATUS),
                "转账状态": _translated(_value(record, "fundTransferStatus"), _TRANSFER_STATUS),
                "到账状态": None,
                "币种": _value(record, "currencyCode"),
                "销售金额": _number(_value(record, "itemPrice")),
                "销售税额": _number(_value(record, "itemTax")),
                "买家运费": _number(_value(record, "shippingPrice")),
                "买家运费税额": _number(_value(record, "shippingTax")),
                "礼品包装金额": _number(_value(record, "giftWrapPrice")),
                "礼品包装税额": _number(_value(record, "giftWrapTax")),
                "促销折扣（商品）": _number(_value(record, "itemPromotionDiscount")),
                "促销折扣（运费））": _number(_value(record, "shipPromotionDiscount")),
                "平台费": None,
                "发货费": None,
                "其他订单费用": None,
                "采购成本": None,
                "头程成本": None,
                "其他成本": None,
                "订单毛利润": None,
                "含税订单毛利润": None,
                "订单毛利率": None,
                "含税订单毛利率": None,
                "销售国家": _value(record, "saleCountryName"),
                "销售地区": _value(record, "region"),
                "销售城市": _value(record, "shipCity"),
                "邮编": _text(_value(record, "shipPostalCode")),
                "物流方式": _value(record, "logisitcsMode"),
                "物流追踪编号": _text(_value(record, "trackingNumber")),
                "运营中心": _value(record, "fulfillmentCenterId"),
                "配送方式": _value(record, "fulfillment"),
                "销售渠道": _value(record, "salesChannel"),
            }
        )
    return rows


def _percentage(value: Any) -> str | None:
    number = _number(value)
    if number is None:
        return None
    return f"{float(number) * 100:.2f}%"


def _transaction_rows(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    field_map = {
        "店铺": "storeName",
        "国家": "country",
        "币种": "currencyCode",
        "下单时间": "orderDatetimeLocale",
        "付款时间": "paymentDatetimeLocale",
        "发货时间": "shipmentDatetimeLocale",
        "结算时间": "postedDatetimeLocale",
        "转账时间": "fundTransferDatetimeLocale",
        "订单号": "orderId",
        "Settlement Id": "settlementId",
        "结算编号": "fid",
        "MSKU": "msku",
        "FNSKU": "fnsku",
        "ASIN": "asin",
        "父asin": "parentAsin",
        "品名": "localName",
        "SKU": "localSku",
        "账单类型": "accountType",
        "费用类型": "eventSource",
        "订单类型": "fulfillment",
        "描述": "description",
        "交易状态": "transactionStatus",
        "数量": "quantity",
        "Listing负责人": "principalRealname",
        "开发负责人": "productDeveloperRealname",
        "销售额": "productSales",
        "销售税": "productSalesTax",
        "买家运费": "shippingCredits",
        "买家运费税": "shippingCreditsTax",
        "礼品包装": "giftwrapCredits",
        "礼品包装税": "giftwrapCreditsTax",
        "积分": "amazonPointFee",
        "促销折扣": "promotionalRebates",
        "促销折扣税": "promotionalRebatesTax",
        "代扣代缴增值税": "salesTaxCollected",
        "低价值商品税": "lowValueGoods",
        "市场预扣税": "marketplaceWithheldTax",
        "TCS_CGST": "tcsCgst",
        "TCS_SGST": "tcsSgst",
        "TCS_IGST": "tcsIgst",
        "平台费": "sellingFees",
        "FBA费": "fbaFees",
        "其他交易费": "otherTransactionFees",
        "其他": "other",
        "隐藏税": "hiddenTax",
        "亚马逊结算小计": "settlementTotal",
        "采购成本": "purchaseCostsTotal",
        "头程费用": "logisticsCostsTotal",
        "其他成本": "otherCostsTotal",
        "站外推广费": "customOrderFeeTotal",
        "结算订单毛利润": "settlementGrossProfit",
        "促销编码": "promotionId",
    }
    numeric_headers = {column.header for column in TRANSACTION_COLUMNS if column.number_format}
    text_headers = {"订单号", "Settlement Id", "结算编号", "MSKU", "FNSKU", "ASIN", "父asin", "SKU"}
    rows: list[dict[str, Any]] = []
    for record in records:
        row = {header: _value(record, field) for header, field in field_map.items()}
        row["延迟时间"] = None
        row["结算状态"] = _translated(_value(record, "settlementStatus"), _SETTLEMENT_STATUS)
        row["转账状态"] = _translated(_value(record, "fundTransferStatus"), _TRANSFER_STATUS)
        row["结算订单毛利润率"] = _percentage(_value(record, "settlementGrossProfitRate"))
        for header in numeric_headers:
            row[header] = _number(row.get(header))
        for header in text_headers:
            row[header] = _text(row.get(header))
        rows.append(row)
    return rows


def _currency_text(value: Any, currency: Any = "CNY", decimals: int = 2) -> str | None:
    number = _number(value)
    if number is None:
        return None
    currency_text = str(currency or "").upper()
    icon = _CURRENCY_ICONS.get(currency_text, str(currency or ""))
    return f"{icon}{float(number):.{decimals}f}"


def _unit_text(value: Any, unit: Any, decimals: int) -> str | None:
    number = _number(value)
    if number is None:
        return None
    return f"{float(number):.{decimals}f}{unit or ''}"


def _bool_status(value: Any, positive: str, negative: str) -> str:
    return positive if str(value).lower() in {"1", "true", "yes"} else negative


def _order_type(value: Any) -> Any:
    return {1: "单品单件", 2: "多品多件", 3: "单品多件"}.get(int(value or 0), value)


def _declared_weight_text(value: Any) -> str | None:
    if value in (None, ""):
        return None
    try:
        return f"{float(value):.2f}g"
    except (TypeError, ValueError):
        return str(value)


def _declaration_currency(item: dict[str, Any]) -> Any:
    explicit = item.get("declared_currency_icon") or item.get("declared_currency_code")
    if explicit:
        return explicit
    declaration_fields = ("unit_price", "declared_weight", "declared_quantity", "cn_name", "en_name", "customs_code")
    has_declaration = any(item.get(field) not in (None, "") for field in declaration_fields)
    return item.get("currency_code") if has_declaration else None


def _outbound_rows(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for source_index, record in enumerate(records):
        products = _json_value(record.get("product_info"), [])
        if isinstance(products, dict):
            products = [products]
        if not isinstance(products, list) or not products:
            products = [{}]
        tags = _json_value(record.get("tag_names"), [])
        tag_text = ",".join(str(item) for item in tags) if isinstance(tags, list) else _text(tags)
        platform_numbers = _json_value(record.get("platform_order_no"), record.get("platform_order_no"))
        fallback_platform = (
            platform_numbers[0]
            if isinstance(platform_numbers, list) and platform_numbers
            else platform_numbers if not isinstance(platform_numbers, (list, dict)) else None
        )
        total_stock_cost = sum(float(_number(item.get("stock_cost")) or 0) for item in products)
        package_size = None
        if any(_number(record.get(name)) is not None for name in ("pkg_length", "pkg_width", "pkg_height")):
            unit = record.get("pkg_size_unit") or ""
            package_size = "*".join(
                f"{float(_number(record.get(name)) or 0):.2f}" for name in ("pkg_length", "pkg_width", "pkg_height")
            ) + str(unit)
        logistics_channel = "-".join(
            str(value) for value in (record.get("logistics_provider_name"), record.get("logistics_type_name")) if value
        ) or None
        delivery_status = record.get("delivery_status_name") or record.get("delivery_message")
        if not delivery_status and str(record.get("delivery_status")) == "20":
            delivery_status = "已配货"
        for item_index, item in enumerate(products):
            order_values = {
                "销售出库单号": _text(record.get("wo_number")),
                "系统单号": _text(record.get("order_number")),
                "状态": record.get("status_name"),
                "波次号": _text(record.get("batch_no")),
                "三方仓出库时间": record.get("delivered_at"),
                "发货员": record.get("deliverer"),
                "系统出库时间": record.get("stock_delivered_at"),
                "订单出库成本": _currency_text(total_stock_cost, "CNY", 2),
                "是否验货": _bool_status(record.get("is_check"), "已验货", "未验货"),
                "是否称重": _bool_status(record.get("is_weigh"), "已称重", "未称重"),
                "面单打印": _bool_status(record.get("is_surface_print"), "已打印", "未打印"),
                "发货单打印": _bool_status(record.get("is_order_print"), "已打印", "未打印"),
                "创建时间": record.get("create_at"),
                "订单类型": _order_type(record.get("order_type")),
                "加工单号": _text(record.get("process_sn")),
                "平台单号": _text(item.get("platform_order_no") or fallback_platform),
                "标签": tag_text,
                "店铺": record.get("seller_name"),
                "站点": record.get("site_text"),
                "平台": record.get("platform_name"),
                "目的地": record.get("target_country"),
                "税号": _text(record.get("recipient_tax_no") or record.get("sender_tax_no")),
                "收件人": record.get("consignee"),
                "电话": _text(record.get("consignee_phone")),
                "邮编": _text(record.get("consignee_postcode")),
                "收货地址": record.get("consignee_full_address") or record.get("consignee_address"),
                "订单金额": _currency_text(record.get("order_origin_amount"), record.get("order_currency_code"), 2),
                "发货时限": record.get("deliver_deadline"),
                "客服备注": record.get("order_customer_service_notes"),
                "买家留言": record.get("order_buyer_notes"),
                "订单来源": record.get("order_from"),
                "订单结算时间": record.get("platform_payment_time"),
                "参考号": _text(record.get("reference_no")),
                "买家邮箱": record.get("email"),
                "物流商": record.get("logistics_provider_name"),
                "物流渠道": logistics_channel,
                "海外仓单号": _text(record.get("owms_waybill_no")),
                "运单号": _text(record.get("waybill_no")),
                "跟踪号": _text(record.get("tracking_no")),
                "预估运费": _currency_text(
                    record.get("logistics_estimated_freight"),
                    record.get("logistics_estimated_freight_currency_code") or "CNY",
                    2,
                ),
                "物流运费": _number(record.get("logistics_freight")),
                "出库仓库": record.get("warehouse_name"),
                "配货情况": delivery_status,
                "包裹尺寸": package_size,
                "估算重量": _unit_text(record.get("pkg_weight"), record.get("pkg_weight_unit"), 2),
                "包裹实重": _unit_text(record.get("pkg_real_weight"), record.get("pkg_real_weight_unit"), 2),
                "包裹计费重": _unit_text(record.get("pkg_fee_weight"), record.get("pkg_fee_weight_unit"), 3),
                "包裹体积": _unit_text(record.get("pkg_volume"), "cm³", 2),
            }
            if item_index:
                order_values = {header: None for header in order_values}
            row = {
                **order_values,
                "SKU": _text(item.get("sku")),
                "MSKU": _text(item.get("seller_sku")),
                "品名": item.get("product_name"),
                "数量": _number(item.get("count")),
                "商品出库成本": _currency_text(item.get("stock_cost"), "CNY", 6),
                "货值": _number(item.get("purchase_fee_unit")),
                "费用": _number(item.get("other_fee_unit")),
                "头程": _number(item.get("head_fee_unit")),
                "商品备注": item.get("customization"),
                "库位": item.get("storage_position") or item.get("location_name"),
                "分摊运费": _number(item.get("apportion_freight")),
                "单个运费": _number(item.get("apportion_freight_single")),
                "申报单价": _number(item.get("unit_price")),
                "申报币种": _declaration_currency(item),
                "中文申报名": item.get("cn_name"),
                "英文申报名": item.get("en_name"),
                "申报重量": _declared_weight_text(item.get("declared_weight")),
                "海关编码": _text(item.get("customs_code")),
                "申报数量": _number(item.get("declared_quantity")),
                "产品属性": item.get("material"),
                "_merge_group": source_index,
            }
            rows.append(row)
    return rows


SETTLEMENT_COLUMNS = tuple(
    ExportColumn(header, "integer" if header == "数量" else "decimal2" if 26 <= index <= 41 else "decimal4" if index in {42, 43} else None)
    for index, header in enumerate(
        (
            "店铺名称", "国家", "订单号", "配送编号", "自定义订单编号", "msku", "SKU", "品名", "品牌", "分类",
            "listing负责人", "产品开发负责人", "数量", "下单时间", "付款时间", "发货时间", "结算时间", "结算编号",
            "发货与结算的时间间隔", "结算类型", "转账时间", "结算状态", "转账状态", "到账状态", "币种", "销售金额",
            "销售税额", "买家运费", "买家运费税额", "礼品包装金额", "礼品包装税额", "促销折扣（商品）", "促销折扣（运费））",
            "平台费", "发货费", "其他订单费用", "采购成本", "头程成本", "其他成本", "订单毛利润", "含税订单毛利润",
            "订单毛利率", "含税订单毛利率", "销售国家", "销售地区", "销售城市", "邮编", "物流方式", "物流追踪编号",
            "运营中心", "配送方式", "销售渠道",
        ),
        1,
    )
)

TRANSACTION_COLUMNS = tuple(
    ExportColumn(header, "integer" if header == "数量" else "decimal2" if 29 <= index <= 54 else None)
    for index, header in enumerate(
        (
            "店铺", "国家", "币种", "下单时间", "付款时间", "发货时间", "结算时间", "转账时间", "延迟时间", "订单号",
            "Settlement Id", "结算编号", "MSKU", "FNSKU", "ASIN", "父asin", "品名", "SKU", "账单类型", "费用类型",
            "订单类型", "描述", "结算状态", "转账状态", "交易状态", "数量", "Listing负责人", "开发负责人", "销售额", "销售税",
            "买家运费", "买家运费税", "礼品包装", "礼品包装税", "积分", "促销折扣", "促销折扣税", "代扣代缴增值税",
            "低价值商品税", "市场预扣税", "TCS_CGST", "TCS_SGST", "TCS_IGST", "平台费", "FBA费", "其他交易费", "其他",
            "隐藏税", "亚马逊结算小计", "采购成本", "头程费用", "其他成本", "站外推广费", "结算订单毛利润",
            "结算订单毛利润率", "促销编码",
        ),
        1,
    )
)

OUTBOUND_COLUMNS = tuple(
    ExportColumn(
        header,
        "integer" if header in {"数量", "申报数量"} else "decimal4" if header in {"分摊运费", "单个运费"} else "decimal2" if header in {"物流运费", "货值", "费用", "头程", "申报单价"} else None,
    )
    for header in (
        "销售出库单号", "系统单号", "状态", "波次号", "三方仓出库时间", "发货员", "系统出库时间", "订单出库成本",
        "是否验货", "是否称重", "面单打印", "发货单打印", "创建时间", "订单类型", "加工单号", "平台单号", "标签", "店铺",
        "站点", "平台", "目的地", "税号", "收件人", "电话", "邮编", "收货地址", "订单金额", "发货时限", "客服备注", "买家留言",
        "订单来源", "订单结算时间", "参考号", "买家邮箱", "物流商", "物流渠道", "海外仓单号", "运单号", "跟踪号", "预估运费",
        "物流运费", "出库仓库", "配货情况", "包裹尺寸", "估算重量", "包裹实重", "包裹计费重", "包裹体积", "SKU", "MSKU",
        "品名", "数量", "商品出库成本", "货值", "费用", "头程", "商品备注", "库位", "分摊运费", "单个运费", "申报单价",
        "申报币种", "中文申报名", "英文申报名", "申报重量", "海关编码", "申报数量", "产品属性",
    )
)

EXPORT_PROFILES = {
    "shipment_settlement": ExportProfile(
        name="shipment_settlement",
        sheet_name="结算差异报告",
        columns=SETTLEMENT_COLUMNS,
        prepare_rows=_settlement_rows,
        unavailable_columns=(
            "到账状态",
            "平台费",
            "发货费",
            "其他订单费用",
            "采购成本",
            "头程成本",
            "其他成本",
            "订单毛利润",
            "含税订单毛利润",
            "订单毛利率",
            "含税订单毛利率",
        ),
    ),
    "profit_report_order_transaction": ExportProfile(
        name="profit_report_order_transaction",
        sheet_name="已发放订单",
        columns=TRANSACTION_COLUMNS,
        prepare_rows=_transaction_rows,
        group_header="基础信息",
        unavailable_columns=("延迟时间",),
    ),
    "sales_outbound_orders": ExportProfile(
        name="sales_outbound_orders",
        sheet_name="sheet1",
        columns=OUTBOUND_COLUMNS,
        prepare_rows=_outbound_rows,
        merge_order_columns=48,
        unavailable_columns=("库位",),
    ),
}


def get_export_profile(name: str) -> ExportProfile:
    try:
        return EXPORT_PROFILES[name]
    except KeyError as exc:
        raise ValueError(f"未知 Excel 导出模板: {name}") from exc
