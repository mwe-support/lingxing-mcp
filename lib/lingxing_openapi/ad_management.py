"""Amazon SP advertising management tool metadata."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AdManagementToolSpec:
    tool_name: str
    description: str
    endpoint: str
    docs_path: str
    item_arg: str | None = None
    body_key: str | None = None
    required_args: tuple[str, ...] = ()


@dataclass(frozen=True)
class AdManagementRequest:
    tool_name: str
    endpoint: str
    docs_path: str
    body: dict[str, Any]
    dry_run: bool
    confirm: bool


AD_MANAGEMENT_TOOL_SPECS: tuple[AdManagementToolSpec, ...] = (
    AdManagementToolSpec(
        tool_name="lingxing_ads_update_sp_campaign",
        description="修改 SP 广告活动和广告位，支持启停、预算、竞价策略和广告位比例；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/manage/putSpCampaign",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/adReportManagePutSpCampaign",
        item_arg="campaigns",
        body_key="campaigns",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_update_sp_ad_group",
        description="修改 SP 广告组，支持启停和默认竞价；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/manage/putSpAdGroup",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/adReportManagePutSpAdGroup",
        item_arg="ad_groups",
        body_key="adGroups",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_update_sp_keyword",
        description="修改 SP 关键词，支持启停和竞价；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/manage/putSpKeyword",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/adReportManagePutSpKeyword",
        item_arg="keywords",
        body_key="keywords",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_update_sp_target",
        description="修改 SP 商品投放，支持启停和竞价；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/manage/putSpTarget",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/adReportManagePutSpTarget",
        item_arg="targeting_clauses",
        body_key="targetingClauses",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_update_sp_product_ads",
        description="修改 SP 广告商品启用/暂停状态，单次最多 1000 个；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/manage/putSpProductAds",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/adReportManagePutSpProductAds",
        item_arg="product_ads",
        body_key="productAds",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_add_sp_keywords",
        description="添加 SP 关键词，单次最多 1000 个；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/spTarget/addKeywords",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/report/SpAddKeywords",
        item_arg="keywords",
        body_key="keywords",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_add_sp_negative_keywords",
        description="添加 SP 否定关键词，支持活动层级和广告组层级；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/spTarget/addNegativeKeywords",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/report/SpAddNegativeKeywords",
        item_arg="negative_keywords",
        body_key="negativeKeywords",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_add_sp_negative_targets",
        description="添加 SP 否定 ASIN，支持活动层级和广告组层级；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/spTarget/addNegativeTargets",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/report/SpAddNegativeTargets",
        item_arg="asins",
        body_key="asins",
    ),
    AdManagementToolSpec(
        tool_name="lingxing_ads_archive_sp_negatives",
        description="归档 SP 否定关键词或否定 ASIN，需传官方 target_id；默认 dry_run，不确认不执行。",
        endpoint="/basicOpen/adReport/spTarget/archiveNegatives",
        docs_path="https://apidoc.lingxing.com/#/docs/newAd/report/SpArchiveNegatives",
        required_args=("targetIds",),
    ),
)


AD_OPERATION_LOGS_ENDPOINT = "/pb/openapi/newad/apiLogStandard"
