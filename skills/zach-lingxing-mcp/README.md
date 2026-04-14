# zach-lingxing-mcp

领星 ERP OpenAPI 的固定出口网关运维与 MCP 接入说明。

## 推荐安装方式：让 AI 帮你装

推荐在以下 IDE 中直接用自然语言安装：

- Claude Code
- Codex
- Cursor

把下面这句话直接发给你的 AI：

```text
帮我安装 `zach-lingxing-mcp` 这个 skill，来源仓库是 `lingxing-mcp`。直接装到当前工作区，并把依赖一起检查好。
```

手动安装仍然保留，但只作为降级方案：
[../../docs/manual-install.md](../../docs/manual-install.md)

如果你还没判断清楚这套方案适不适合自己，先看：

- [../../README.md](../../README.md)
- [../../docs/feishu-onboarding.md](../../docs/feishu-onboarding.md)
- [../../docs/admin-setup.md](../../docs/admin-setup.md)
- [../../docs/tencent-cloud-buying-guide.md](../../docs/tencent-cloud-buying-guide.md)

## 它具体能帮你解决什么问题

1. 帮你把领星 OpenAPI 接成可复用的 MCP
2. 帮你在固定出口网关和本地 `stdio` 两种模式之间选合适的接法
3. 帮你排查 Bearer、环境变量、权限和白名单问题
4. 帮你理解有哪些 `lingxing_*` 工具可用，包括广告、产品表现、利润、源表、报告导出和高层聚合能力

## 详细功能介绍

- **MCP 接入**
  支持本地 `stdio` 和共享 `HTTP` 两种接法。
- **固定出口网关说明**
  适合受 IP 白名单限制的团队环境。
- **Bearer / 多令牌排查**
  适合多人共享时做访问控制和问题定位。
- **最小工具链验证**
  通过 `lingxing_health_check` 和 `lingxing_smoke_check` 快速确认接口是否真正可用。
- **经营分析扩展面**
  支持产品表现、广告报表、利润统计、Amazon 源表、FBA/补货、报告导出与 ASIN 周汇总。

## 关键入口

```bash
python3 mcp-servers/lingxing-openapi/server.py
python3 mcp-servers/lingxing-openapi/http_server.py --host 127.0.0.1 --port 8099
bash mcp-servers/lingxing-openapi/deploy/deploy_gateway_via_ssh.sh --help
bash mcp-servers/lingxing-openapi/deploy/install_gateway_on_ubuntu.sh --help
bash mcp-servers/lingxing-openapi/deploy/open_ssh_tunnel.sh --help
```

详细说明见 [SKILL.md](./SKILL.md) 和 [mcp-servers/lingxing-openapi/README.md](../../mcp-servers/lingxing-openapi/README.md)

> [!WARNING]
> 不要把真实 `APP ID / AppSecret`、真实 Bearer、真实服务器地址写进工作区截图、公开仓库或群聊消息里。

## 如果安装或运行出错，直接让 AI 帮你排查

把下面这段直接发给你的 AI，并把报错信息、截图或终端输出一起贴上：

```text
我已经安装了 `zach-lingxing-mcp`，但现在遇到了问题。请你直接帮我排查并尽量修复：

1. 先判断是 MCP 配置错误、HTTP 网关未启动、Bearer 无效、环境变量缺失，还是当前 IDE 没有正确加载
2. 自动检查当前工作区里和 `zach-lingxing-mcp` 相关的配置、示例文件、脚本和依赖
3. 如果可以自动修复，就直接修复
4. 修复后告诉我还需要重启 IDE、重新加载工作区，还是重新运行哪个命令
5. 最后给我一个最短的验证步骤，确认这个 skill 已经能用了
```

## 问题反馈

如果你在接入或使用 `zach-lingxing-mcp` 时遇到问题，也可以直接提交飞书问卷反馈：

- [Skill / MCP / 运营问题反馈收集](https://my.feishu.cn/share/base/form/shrcnAg1QaUD8SjBjqR8gjg8Ftf)

<img src="../../assets/traffic/feishu-feedback-form.png" width="260" alt="飞书问卷反馈二维码" />

## 关于作者

关注「**Zach的进化笔记**」，获取 AI x 跨境电商的实战经验、工具和方法论：

<img src="../../assets/traffic/wechat-official-account.jpg" width="200" alt="公众号二维码" />

扫码加入群聊「Zach的第二群朋友们👀」，一起交流 AI + 跨境电商的实战玩法：

<img src="../../assets/traffic/wechat-group.jpeg" width="200" alt="Zach的第二群朋友们二维码" />

如果群二维码过期，也可以通过上面的公众号二维码获取最新入口。
