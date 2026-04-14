"""Helpers for discovering and cataloging LingXing OpenAPI docs."""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Callable


DOC_BASE_URL = "https://apidoc.lingxing.com"
ROOT_SIDEBAR_PATH = "_sidebar.md"

AMAZON_READONLY_MODULES = {
    "Authorization",
    "BasicData",
    "Statistics",
    "Sale",
    "newAd",
    "SourceData",
    "Finance",
    "FBA",
    "FBASug",
    "FBALimit",
}

LEGACY_LOCAL_NAMES = {
    "docs/Authorization/GetToken.md": "01_GetToken.md",
    "docs/Authorization/RefreshToken.md": "02_RefreshToken.md",
    "docs/BasicData/SellerLists.md": "03_SellerLists.md",
    "docs/BasicData/AllMarketplace.md": "04_AllMarketplace.md",
    "docs/Statistics/StoreSales.md": "05_StoreSales.md",
    "docs/Statistics/AsinDailyLists.md": "06_AsinDailyLists.md",
    "docs/Sale/Orderlists.md": "07_Orderlists.md",
    "docs/Sale/promotionListingList.md": "08_PromotionListingList.md",
    "docs/Sale/promotionalActivitiesSecKillList.md": "09_PromotionalActivitiesSecKillList.md",
    "docs/Sale/promotionalActivitiesManageList.md": "10_PromotionalActivitiesManageList.md",
    "docs/Sale/promotionalActivitiesVipDiscountList.md": "11_PromotionalActivitiesVipDiscountList.md",
    "docs/Sale/promotionalActivitiesCouponList.md": "12_PromotionalActivitiesCouponList.md",
}

READ_ONLY_TITLE_DENY_TERMS = (
    "创建",
    "新增",
    "修改",
    "删除",
    "取消",
    "提交",
    "保存",
    "导入",
    "上传",
    "同步",
    "批量修改",
    "批量更新",
    "设置",
    "绑定",
    "解绑",
)
READ_ONLY_TITLE_ALLOW_TERMS = (
    "查询",
    "获取",
    "列表",
    "汇总",
    "统计",
    "报表",
    "日报",
    "小时",
    "详情",
    "信息",
    "下载",
    "结果",
    "分析",
)
READ_ONLY_API_DENY_TERMS = (
    "/add",
    "/create",
    "/update",
    "/delete",
    "/remove",
    "/submit",
    "/save",
    "/import",
    "/batchRename",
)


@dataclass(frozen=True)
class SidebarEntry:
    title: str
    href: str
    module: str
    sections: tuple[str, ...]


@dataclass(frozen=True)
class DocCatalogEntry:
    module: str
    title: str
    remote_path: str
    local_file: str
    api_path: str | None
    request_method: str | None
    request_protocol: str | None
    explicit_read_only: bool
    pagination_mode: str
    requires_api_version_2: bool

    def to_manifest(self) -> dict[str, str | bool | None]:
        return {
            "module": self.module,
            "title": self.title,
            "remote_path": self.remote_path,
            "local_file": self.local_file,
            "api_path": self.api_path,
            "request_method": self.request_method,
            "request_protocol": self.request_protocol,
            "explicit_read_only": self.explicit_read_only,
            "pagination_mode": self.pagination_mode,
            "requires_api_version_2": self.requires_api_version_2,
        }


def _request(req: urllib.request.Request, timeout: int = 30, redirects: int = 3) -> bytes:
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        if exc.code in {301, 302, 307, 308} and redirects > 0:
            location = exc.headers.get("Location")
            if location:
                redirected = urllib.request.Request(
                    url=location,
                    data=req.data,
                    method=req.get_method(),
                    headers=dict(req.header_items()),
                )
                return _request(redirected, timeout=timeout, redirects=redirects - 1)
        detail = exc.read().decode("utf-8", errors="ignore")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc


def exchange_doc_token(doc_access_key: str) -> str:
    body = json.dumps({"docAccess": doc_access_key}).encode("utf-8")
    request = urllib.request.Request(
        url=f"{DOC_BASE_URL}/api/openapi-manage/account/check/doc_access",
        data=body,
        method="PUT",
        headers={
            "Content-Type": "application/json",
            "X-HTTP-Method-Override": "PUT",
        },
    )
    payload = json.loads(_request(request).decode("utf-8"))
    token = ((payload.get("data") or {}).get("can_access")) or ""
    if not token:
        raise RuntimeError(f"文档密钥校验失败: {payload}")
    return str(token)


def fetch_markdown(relative_path: str, doc_token: str | None = None) -> str:
    path = relative_path.lstrip("/")
    headers = {"Cookie": f"doc_access_token={doc_token}"} if doc_token else {}
    request = urllib.request.Request(
        url=f"{DOC_BASE_URL}/{path}",
        headers=headers,
        method="GET",
    )
    return _request(request).decode("utf-8")


def normalize_remote_path(href: str) -> str | None:
    value = str(href or "").strip()
    if not value:
        return None
    value = value.split("#", 1)[0].lstrip("/")
    if not value.startswith("docs/"):
        return None
    if not value.endswith(".md"):
        value = f"{value}.md"
    return value


def _indent_width(text: str) -> int:
    return len(text.replace("\t", "    "))


def parse_sidebar_markdown(markdown: str) -> list[SidebarEntry]:
    entries: list[SidebarEntry] = []
    stack: list[tuple[int, str]] = []
    for raw_line in markdown.splitlines():
        link_match = re.match(r"^(?P<indent>\s*)\*\s+\[(?P<title>[^\]]+)\]\((?P<href>[^)]+)\)\s*$", raw_line)
        if link_match:
            indent = _indent_width(link_match.group("indent"))
            while stack and indent <= stack[-1][0]:
                stack.pop()
            href = normalize_remote_path(link_match.group("href"))
            if not href:
                continue
            module = href.split("/", 2)[1] if "/" in href else ""
            entries.append(
                SidebarEntry(
                    title=link_match.group("title").strip(),
                    href=href,
                    module=module,
                    sections=tuple(item[1] for item in stack),
                )
            )
            continue
        section_match = re.match(r"^(?P<indent>\s*)\*\s+(?P<title>[^\[].+?)\s*$", raw_line)
        if section_match:
            indent = _indent_width(section_match.group("indent"))
            while stack and indent <= stack[-1][0]:
                stack.pop()
            stack.append((indent, section_match.group("title").strip()))
    return entries


def is_amazon_relevant_doc(remote_path: str) -> bool:
    parts = remote_path.split("/")
    if len(parts) < 3:
        return False
    return parts[1] in AMAZON_READONLY_MODULES


def is_explicit_read_only(title: str, api_path: str | None, request_method: str | None) -> bool:
    clean_title = str(title or "").strip()
    lower_api_path = str(api_path or "").lower()
    for term in READ_ONLY_TITLE_DENY_TERMS:
        if term in clean_title:
            return False
    for term in READ_ONLY_API_DENY_TERMS:
        if term.lower() in lower_api_path:
            return False
    method = str(request_method or "").upper()
    if method == "GET":
        return True
    if any(term in clean_title for term in READ_ONLY_TITLE_ALLOW_TERMS):
        return True
    if any(marker in lower_api_path for marker in ("/query", "/list", "/report", "reports", "/download", "/open/")):
        return True
    return False


def detect_pagination_mode(markdown: str) -> str:
    lower_text = markdown.lower()
    if "next_token" in lower_text:
        return "next_token"
    if ("|offset|" in lower_text or "`offset`" in lower_text or "| offset |" in lower_text) and (
        "|length|" in lower_text or "`length`" in lower_text or "| length |" in lower_text
    ):
        return "offset"
    return "none"


def parse_doc_metadata(remote_path: str, markdown: str, fallback_title: str) -> DocCatalogEntry:
    title_match = re.search(r"^#\s+(.+?)\s*$", markdown, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else fallback_title
    info_match = re.search(
        r"\|\s*`?(?P<api_path>/[^`|]+)`?\s*\|\s*(?P<protocol>HTTPS?)\s*\|\s*(?P<method>[A-Z]+)\s*\|",
        markdown,
        flags=re.IGNORECASE,
    )
    api_path = info_match.group("api_path").strip() if info_match else None
    request_protocol = info_match.group("protocol").upper() if info_match else None
    request_method = info_match.group("method").upper() if info_match else None
    module = remote_path.split("/", 2)[1] if "/" in remote_path else ""
    return DocCatalogEntry(
        module=module,
        title=title,
        remote_path=remote_path,
        local_file=build_local_filename(remote_path),
        api_path=api_path,
        request_method=request_method,
        request_protocol=request_protocol,
        explicit_read_only=is_explicit_read_only(title, api_path, request_method),
        pagination_mode=detect_pagination_mode(markdown),
        requires_api_version_2=module == "newAd" or str(api_path or "").startswith("/pb/openapi/newad/"),
    )


def build_local_filename(remote_path: str) -> str:
    legacy_name = LEGACY_LOCAL_NAMES.get(remote_path)
    if legacy_name:
        return legacy_name
    short_path = remote_path.removeprefix("docs/").removesuffix(".md")
    safe_name = re.sub(r"[^A-Za-z0-9]+", "_", short_path).strip("_")
    return f"{safe_name}.md"


def discover_doc_catalog(
    doc_token: str | None = None,
    *,
    fetcher: Callable[[str, str | None], str] | None = None,
) -> tuple[list[DocCatalogEntry], list[str]]:
    fetch = fetcher or fetch_markdown
    sidebar = fetch(ROOT_SIDEBAR_PATH, doc_token)
    entries = parse_sidebar_markdown(sidebar)
    catalog: list[DocCatalogEntry] = []
    warnings: list[str] = []
    seen: set[str] = set()
    for entry in entries:
        if entry.href in seen or not is_amazon_relevant_doc(entry.href):
            continue
        seen.add(entry.href)
        try:
            markdown = fetch(entry.href, doc_token)
        except Exception as exc:  # pragma: no cover - network-dependent
            warnings.append(f"{entry.href}: {exc}")
            continue
        metadata = parse_doc_metadata(entry.href, markdown, entry.title)
        if not metadata.explicit_read_only:
            continue
        catalog.append(metadata)
    catalog.sort(key=lambda item: (item.module, item.remote_path))
    return catalog, warnings


def build_index(entries: list[DocCatalogEntry], warnings: list[str] | None = None) -> str:
    lines = [
        "# 领星 OpenAPI 本地文档索引",
        "",
        "这些文档由 `scripts/sync_docs.py` 从官方 `_sidebar.md` 自动发现，只同步当前仓库需要的 Amazon 相关只读接口页面。",
        "",
        "| 本地文件 | 模块 | 请求方式 | 分页 | V2 头 | 官方路径 | API Path | 标题 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| `{entry.local_file}` | `{entry.module}` | `{entry.request_method or ''}` | "
            f"`{entry.pagination_mode}` | `{str(entry.requires_api_version_2).lower()}` | "
            f"`{entry.remote_path}` | `{entry.api_path or ''}` | {entry.title} |"
        )
    if warnings:
        lines.extend(["", "## Warnings", ""])
        for warning in warnings:
            lines.append(f"- {warning}")
    lines.append("")
    return "\n".join(lines)
