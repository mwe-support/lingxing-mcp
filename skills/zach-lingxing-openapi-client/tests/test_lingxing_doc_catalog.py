from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from lib.lingxing_openapi.doc_catalog import (  # noqa: E402
    build_local_filename,
    discover_doc_catalog,
    parse_sidebar_markdown,
)


SIDEBAR = """
* 授权
  * [获取接口令牌-access_token](docs/Authorization/GetToken)
* 基础数据
  * [查询亚马逊店铺列表](docs/BasicData/SellerLists)
  * [批量修改店铺名称](docs/BasicData/SellerBatchRename)
* 新广告
  * [SP 广告活动日报](docs/newAd/report/spCampaignReports)
"""

GET_TOKEN_DOC = """
# 获取接口令牌-access_token

| API Path | 请求协议 | 请求方式 |
| :--- | :--- | :--- |
| `/api/auth-server/oauth/access-token` | HTTPS | POST |
"""

SELLER_LISTS_DOC = """
# 查询亚马逊店铺列表

| API Path | 请求协议 | 请求方式 |
| :--- | :--- | :--- |
| `/erp/sc/data/seller/lists` | HTTPS | GET |
"""

BATCH_RENAME_DOC = """
# 批量修改店铺名称

| API Path | 请求协议 | 请求方式 |
| :--- | :--- | :--- |
| `/erp/sc/data/seller/batchRename` | HTTPS | POST |
"""

SP_REPORT_DOC = """
# SP 广告活动日报

| API Path | 请求协议 | 请求方式 |
| :--- | :--- | :--- |
| `/pb/openapi/newad/spCampaignReports` | HTTPS | POST |

| 参数名 | 说明 |
| :--- | :--- |
| offset | 偏移量 |
| length | 分页大小 |
"""


def fake_fetcher(path: str, doc_token: str | None = None) -> str:  # noqa: ARG001
    payloads = {
        "_sidebar.md": SIDEBAR,
        "docs/Authorization/GetToken.md": GET_TOKEN_DOC,
        "docs/BasicData/SellerLists.md": SELLER_LISTS_DOC,
        "docs/BasicData/SellerBatchRename.md": BATCH_RENAME_DOC,
        "docs/newAd/report/spCampaignReports.md": SP_REPORT_DOC,
    }
    return payloads[path]


class LingxingDocCatalogTests(unittest.TestCase):
    def test_parse_sidebar_markdown_normalizes_remote_paths(self) -> None:
        entries = parse_sidebar_markdown(SIDEBAR)
        self.assertEqual(entries[0].href, "docs/Authorization/GetToken.md")
        self.assertEqual(entries[1].href, "docs/BasicData/SellerLists.md")
        self.assertEqual(entries[2].module, "BasicData")

    def test_discover_doc_catalog_filters_to_read_only_docs(self) -> None:
        catalog, warnings = discover_doc_catalog(fetcher=fake_fetcher)
        self.assertEqual(warnings, [])
        remote_paths = [entry.remote_path for entry in catalog]
        self.assertIn("docs/BasicData/SellerLists.md", remote_paths)
        self.assertIn("docs/newAd/report/spCampaignReports.md", remote_paths)
        self.assertNotIn("docs/BasicData/SellerBatchRename.md", remote_paths)

        sp_entry = next(item for item in catalog if item.remote_path == "docs/newAd/report/spCampaignReports.md")
        self.assertEqual(sp_entry.pagination_mode, "offset")
        self.assertTrue(sp_entry.requires_api_version_2)

    def test_build_local_filename_preserves_legacy_docs(self) -> None:
        self.assertEqual(build_local_filename("docs/BasicData/SellerLists.md"), "03_SellerLists.md")
        self.assertEqual(build_local_filename("docs/newAd/report/spCampaignReports.md"), "newAd_report_spCampaignReports.md")


if __name__ == "__main__":
    unittest.main()
