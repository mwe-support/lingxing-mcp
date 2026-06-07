# 领星 OpenAPI MCP

当前目录是 `lingxing-mcp` 公开仓库里的 MCP 服务端实现与部署入口。

它当前支持两种接法：

- 本地 `stdio`：适合个人验证
- 固定出口 `HTTP gateway`：适合团队共享和 IP 白名单场景

## 当前状态

- 已支持固定出口网关
- 已支持本地 `stdio` 和团队 `HTTP` 两种接入
- 已支持多人令牌模式
- 当前 MCP 工具保持只读，不提供写接口

## 推荐阅读顺序

- 仓库总入口：
  [`../../README.md`](../../README.md)
- 管理员部署说明：
  [`../../docs/admin-setup.md`](../../docs/admin-setup.md)
- 手动安装说明：
  [`../../docs/manual-install.md`](../../docs/manual-install.md)
- 公开示例配置说明：
  [`examples/public/README.md`](examples/public/README.md)
- 发布审计与发布前流程：
  [`../../docs/release-gate.md`](../../docs/release-gate.md)

## 核心文件

- `server.py`：本地 `stdio` MCP 入口
- `http_server.py`：团队 `HTTP` MCP 入口
- `deploy/manage_tokens.py`：多人令牌管理工具
- `deploy/`：固定出口网关部署脚本、systemd 模板、验证脚本
- `examples/public/`：公开版去敏示例配置

## 当前工具

保留原有基础工具：

- `lingxing_health_check`
- `lingxing_seller_lists`
- `lingxing_marketplaces`
- `lingxing_store_sales`
- `lingxing_asin_daily_lists`
- `lingxing_order_lists`
- `lingxing_promotion_listing`
- `lingxing_promotion_sec_kill`
- `lingxing_promotion_manage`
- `lingxing_promotion_vip_discount`
- `lingxing_promotion_coupon`
- `lingxing_resolve_daily_promotions`
- `lingxing_smoke_check`

新增稳定层只读工具：

- 广告账号与基础数据：`lingxing_ad_accounts`、`lingxing_ads_portfolios`、`lingxing_ads_sp_*`、`lingxing_ads_sd_*`、`lingxing_ads_sb_*`
- 广告报表与小时报表：SP/SD/SB 的 campaign、product ad、keyword、target、search term、hourly 工具
- 店铺分析：`lingxing_profit_seller`、`lingxing_profit_asin`、`lingxing_profit_parent_asin`
- 亚马逊源表：`lingxing_source_all_orders`、`lingxing_source_manage_inventory`、`lingxing_source_daily_inventory`、`lingxing_source_reserved_inventory`、`lingxing_source_transaction`
- FBA / 补货：`lingxing_fba_stock_aggregate`、`lingxing_fba_stock_detail`、`lingxing_replenishment_summary`、`lingxing_replenishment_asin_info`
- 报告导出：`lingxing_report_export_create`、`lingxing_report_export_query`、`lingxing_report_export_refresh_url`、`lingxing_report_export_download`
- 高层聚合：`lingxing_asin_ads_daily_rollup`、`lingxing_asin_weekly_rollup`

新增实验层只读工具：

- `lingxing_exp_*`

工具定义与入参以 [`lib/lingxing_openapi/endpoint_specs.py`](../../lib/lingxing_openapi/endpoint_specs.py) 为准。

## 多人令牌最小运维命令

初始化令牌文件：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json \
  init --id admin --description "Gateway admin bootstrap token"
```

新增成员令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json \
  add --id alice-mac --description "Alice MacBook Pro"
```

吊销成员令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json \
  revoke --id alice-mac
```

轮换成员令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json \
  rotate --id alice-mac
```

## 说明

- 当前目录只保留公开版接入材料、去敏示例和部署脚本。
- 如果你要在团队里长期使用，优先走固定出口 `HTTP gateway`，不要把本地 `stdio` 当长期共享主方案。
- 不要把真实 `APP ID / AppSecret`、真实 Bearer、真实服务器地址写进公开示例或截图里。

## 问题反馈

如果你在部署网关、配置 Bearer、接 MCP 或运行示例配置时遇到问题，也可以直接提交飞书问卷反馈：

- [Skill / MCP / 运营问题反馈收集](https://my.feishu.cn/share/base/form/shrcnAg1QaUD8SjBjqR8gjg8Ftf)

填写时建议补充当前接法、报错信息和卡住的步骤，方便后续排查。

<img src="../../assets/traffic/feishu-feedback-form.png" width="260" alt="飞书问卷反馈二维码" />


## OpenAPI rate limiting

The server does not require each MCP client to self-throttle. Business requests are throttled in the shared OpenAPI client by endpoint path before calling Lingxing. The default is enabled and conservative for unknown endpoints.

Useful environment variables:

```bash
LINGXING_OPENAPI_RATE_LIMIT_ENABLED=1
LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_RPS=1
LINGXING_OPENAPI_RATE_LIMIT_DEFAULT_BURST=1
LINGXING_OPENAPI_RATE_LIMIT_WAIT_TIMEOUT=60
LINGXING_OPENAPI_RATE_LIMIT_OVERRIDES=/bd/profit/report/open/report/asin/list=10:10
```

Use `LINGXING_OPENAPI_RATE_LIMIT_OVERRIDES` only after checking the official Lingxing token bucket capacity for the endpoint.
