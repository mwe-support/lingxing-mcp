# Lingxing MCP

> **作者**：Zach ｜ 公众号「Zach的进化笔记」
>
> 把领星 ERP 的读取能力整理成可复用、可共享、可被 Claude Code / Codex / Cursor 直接调用的只读 MCP 基础设施，重点服务技术型卖家和 AI 协作用户。

---

## 一句话定位

`Lingxing MCP` 不是领星接口文档的搬运版，也不是 Amazon API 的替代品。  
它更像是一层稳定的访问基础设施：把领星 OpenAPI、IP 白名单、固定出口、团队共享、AI 工具调用这几件事收口成一套能真正跑起来的工程方案。

它当前公开定位非常明确：

- 面向 **技术型卖家**
- 面向 **AI 协作用户**
- 面向愿意配云服务器、配白名单、接 MCP 的团队

它不是“所有卖家都能零门槛一键用”的产品。

---

## 问题反馈

如果你在安装、配置、使用 Skill / MCP / 运营工作流时遇到问题，或者想提交改进建议，可以直接填写飞书问卷：

- [Skill / MCP / 运营问题反馈收集](https://my.feishu.cn/share/base/form/shrcnAg1QaUD8SjBjqR8gjg8Ftf)

建议把当前使用场景、卡住的步骤、报错信息和期望结果一起写上，后续更容易定位问题。

<img src="./assets/traffic/feishu-feedback-form.png" width="260" alt="飞书问卷反馈二维码" />

---

## 关于作者

关注「**Zach的进化笔记**」，获取 AI x 跨境电商的实战经验、工具和方法论：

<img src="./assets/traffic/wechat-official-account.jpg" width="200" alt="公众号二维码" />

扫码加入群聊「Zach的第二群朋友们👀」，一起交流 AI + 跨境电商的实战玩法：

<img src="./assets/traffic/wechat-group.jpeg" width="200" alt="Zach的第二群朋友们二维码" />

如果群二维码过期，也可以通过上面的公众号获取最新入口。

---

## 当前状态

**Status: Audit Passed / Not Pushed**

这个公开工作区当前承接的是已经去敏后的公开候选内容：

- 领星 OpenAPI 的公共客户端封装
- 本地 `stdio` 和共享 `HTTP` 两种 MCP 入口
- 多人令牌模式
- 固定出口网关的公共部署脚本
- 去敏后的示例配置和接入说明

---

## 先回答 4 个最重要的问题

### 1. 它能查什么

当前公开版聚焦只读能力，主要覆盖：

- 店铺列表
- 站点与时区信息
- 店铺销量
- ASIN 日级销量
- 产品表现汇总（浏览、会话、广告、销量）
- 广告账号、广告基础数据和 SP / SD / SB 报表
- 小时级广告报表
- 订单列表
- 促销列表与促销类型归一化
- 利润统计
- 亚马逊源表、FBA 库存和补货视图
- Amazon 报告导出与下载解析
- 高层聚合（ASIN 广告日汇总、周汇总）
- 实验层 `lingxing_exp_*` 只读工具
- 日常巡检和最小烟测

### 2. 它适合谁

更适合下面这几类团队：

- 已经在用领星 ERP 管多店铺
- 希望让 Claude Code、Codex、Cursor 直接查领星数据
- 团队成员经常换网络、开 VPN、异地办公
- 不想把 `APP ID` / `AppSecret` 散落到每个人电脑里

### 2.1 适合 / 不适合

**适合：**

- 已经在用领星 ERP 管理多店铺
- 愿意按文档购买腾讯云、配置白名单、部署固定出口
- 愿意让 Claude Code、Codex、Cursor 参与接入与排错

**不适合：**

- 希望零配置即开即用
- 不愿碰云服务器或白名单
- 不愿处理任何管理员动作，只想像 SaaS 一样一键开通

### 3. 为什么要固定出口云服务器

因为领星 OpenAPI 有 **IP 白名单限制**。  
如果你们多人、多地点、多 VPN 直接从各自电脑访问，白名单会很快失控。

固定出口云服务器的作用是：

- 让领星只看到一个稳定出口 IP
- 团队成员换网络时不需要反复改白名单
- 把主凭证只放在服务器，不放在每个人电脑里
- 让 HTTP gateway 成为团队统一入口

### 4. 为什么当前先做只读

因为大多数团队的第一道门槛不是“写接口不够多”，而是：

- 白名单没打通
- `APP ID / AppSecret` 没配好
- 固定出口没搭好
- IDE / MCP 没接起来

所以这个仓库当前优先把“读取链路先跑通”。  
先把访问、鉴权、白名单、网关、共享和 AI 调用打通，再讨论更高风险的写操作，会稳很多。

---

## Lingxing MCP 和 Amazon API 有什么区别

| 对比项 | Lingxing MCP | Amazon API |
| --- | --- | --- |
| 核心定位 | 领星 ERP 数据接入层 | Amazon 官方原始 API |
| 更适合谁 | 多店铺经营管理、团队共享、ERP 视角 | 单账号/单系统直连、官方数据链路 |
| 数据视角 | 更贴近店铺运营、销量、订单、促销、管理动作 | 更贴近 Amazon 平台原始能力 |
| 团队共享 | 更适合通过固定出口网关统一接入 | 一般更偏系统对系统接入 |
| 当前仓库重点 | 先把只读访问链路跑通 | 不在本仓库范围内 |

如果你的目标是：

- **让团队统一看多店铺数据**
- **让 AI 工具直接查询领星 ERP**
- **先把白名单和共享访问跑顺**

那 `Lingxing MCP` 往往比直接啃 Amazon API 更适合作为第一步。

---

## 给人看的：你需要做什么

### 领星侧必须由超级管理员完成

请使用 **领星超级管理员账号** 登录后台，然后进入：

`设置 -> 业务配置 -> 基础 -> 开放接口`

你至少需要完成这几件事：

1. 添加固定出口服务器的 IP 白名单
2. 添加 API 账号
3. 记录 `APP ID`
4. 记录 `AppSecret`

如果你只是想先跑通，权限可以先用较宽的只读范围验证；跑通后再收缩到最小权限集合。

### 服务器侧需要完成什么

你需要准备一台固定出口云服务器，然后：

1. 配置 `LINGXING_APP_ID`
2. 配置 `LINGXING_APP_SECRET`
3. 启动 `HTTP gateway`
4. 做最小健康检查
5. 把网关地址和成员令牌发给团队成员

如果你从没买过云服务器，直接看这份新手文档：

- [docs/tencent-cloud-buying-guide.md](./docs/tencent-cloud-buying-guide.md)

如果你已经买好了服务器，直接看管理员执行文档：

- [docs/admin-setup.md](./docs/admin-setup.md)

---

## 给 Agent / AI 看的：这套东西是什么

如果你是 Claude Code、Codex、Cursor 里的 Agent，可以这样理解这个仓库：

- 这是 **领星 ERP 的只读 MCP 接入层**
- 它不是 Amazon API 的替代品
- 团队共享模式下优先推荐 **固定出口云服务器 + HTTP gateway**
- 本地 `stdio` 更适合个人验证，不适合多人长期共享
- 当前仓库优先解决“访问链路跑通”，而不是扩写高风险写接口

更完整的 Agent 上下文见：

- [docs/agent-context.md](./docs/agent-context.md)

---

## 推荐安装方式：让 AI 帮你装

推荐在以下 IDE 中直接用自然语言安装：

- Claude Code
- Codex
- Cursor

把下面这段直接发给你的 AI：

```text
请从 GitHub 仓库 `lingxing-mcp` 接入领星 MCP 到当前工作区。主路线请采用“固定出口云服务器 + HTTP gateway + Claude Code / Codex / Cursor”方案；如果当前环境只是在我个人电脑上做临时验证，再改用 stdio。请同时检查示例配置、环境变量、依赖和最小健康检查是否完整。
```

如果你更喜欢自己一步一步安装，再看：

- [docs/manual-install.md](./docs/manual-install.md)

> 当前公开版只推荐一条主路线：
> **固定出口云服务器 + HTTP gateway + Claude Code / Codex / Cursor**
>
> 本地 `stdio` 会继续保留，但它是个人验证模式，不是团队共享主方案。

---

## 这个仓库当前支持什么

- 基础能力：`lingxing_health_check`、`lingxing_smoke_check`、`lingxing_seller_lists`、`lingxing_marketplaces`
- 店铺经营：`lingxing_store_sales`、`lingxing_asin_daily_lists`、`lingxing_orders`、`lingxing_product_performance`
- 促销：`lingxing_promotion_*`、`lingxing_resolve_daily_promotions`
- 广告：`lingxing_ad_accounts`、`lingxing_ads_sp_*`、`lingxing_ads_sd_*`、`lingxing_ads_sb_*`
- 利润：`lingxing_profit_seller`、`lingxing_profit_asin`、`lingxing_profit_parent_asin`
- 源表 / 库存 / 补货：`lingxing_source_*`、`lingxing_fba_*`、`lingxing_replenishment_*`
- 报告导出：`lingxing_report_export_create`、`lingxing_report_export_query`、`lingxing_report_export_refresh_url`、`lingxing_report_export_download`
- 高层聚合：`lingxing_asin_ads_daily_rollup`、`lingxing_asin_weekly_rollup`
- 实验层：`lingxing_exp_*`

这些工具当前全部是 **只读** 的，适合做：

- 数据查看
- 日常巡检
- 多店铺经营分析
- 广告和流量周报补数
- Amazon 报告下载解析
- 团队共享查询

---

## 文档入口

- 飞书补充文档： [docs/feishu-onboarding.md](./docs/feishu-onboarding.md)
- Agent 说明： [docs/agent-context.md](./docs/agent-context.md)
- 管理员执行清单： [docs/admin-setup.md](./docs/admin-setup.md)
- 腾讯云新手购买指南： [docs/tencent-cloud-buying-guide.md](./docs/tencent-cloud-buying-guide.md)
- 手动安装： [docs/manual-install.md](./docs/manual-install.md)
- 发布前闸门： [docs/release-gate.md](./docs/release-gate.md)

---

## 安全警示

> [!WARNING]
> 公开仓库、群聊、截图和文档里，都不要泄露以下信息：
>
> - 真实 `APP ID`
> - 真实 `AppSecret`
> - 真实 Bearer Token
> - 真实 `tokens.json`
> - 真实服务器 IP、团队接入地址、内网信息
>
> 传播截图前请先打码。  
> 一旦怀疑泄露，先轮换 API 账号或成员令牌，再继续使用。

---

## 可以直接发飞书群的短版说明

下面这段可以直接复制：

```text
这是一个把领星 ERP 接成 MCP 的只读基础设施方案，适合多店铺团队共享给 Claude Code、Codex、Cursor 直接查数据。它重点解决领星白名单、固定出口、团队共享和 AI 接入问题。当前先做只读，是为了先把访问链路稳定跑通，再逐步扩展。
```

---

## 如果安装或运行出错，直接让 AI 帮你排查

把下面这段直接发给你的 AI，并把报错信息、截图或终端输出一起贴上：

```text
我已经接入了 `lingxing-mcp`，但现在遇到了问题。请你直接帮我排查并尽量修复：

1. 先判断是领星白名单、APP ID / AppSecret、Bearer、HTTP gateway、MCP 配置，还是当前 IDE 没有正确加载
2. 自动检查当前工作区里和 `lingxing-mcp` 相关的配置、示例文件、脚本和依赖
3. 如果可以自动修复，就直接修复
4. 修复后告诉我还需要重启 IDE、重新加载工作区，还是重新运行哪个命令
5. 最后给我一个最短的验证步骤，确认这个 MCP 已经能用了
```

## License

MIT
