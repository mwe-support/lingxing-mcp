# zach-lingxing-openapi-client

> **作者**：Zach ｜ 公众号「Zach的进化笔记」
>
> Learn in public！把领星 OpenAPI 的鉴权、签名、文档缓存和最小烟测整理成可复用的公开客户端底座。

领星 ERP OpenAPI 的接入底座，适用于固定出口网关模式，也适合给其他 `lingxing_*` 工具和脚本复用。

## 推荐安装方式：让 AI 帮你装

推荐在以下 IDE 中直接用自然语言安装：

- Claude Code
- Codex
- Cursor

把下面这句话直接发给你的 AI：

```text
帮我安装 `zach-lingxing-openapi-client` 这个 skill，来源仓库是 `lingxing-mcp`。直接装到当前工作区，并把依赖一起检查好。
```

手动安装仍然保留，但只作为降级方案：
[../../docs/manual-install.md](../../docs/manual-install.md)

如果你还没判断清楚整套方案适不适合自己，先看：

- [../../README.md](../../README.md)
- [../../docs/admin-setup.md](../../docs/admin-setup.md)
- [../../docs/tencent-cloud-buying-guide.md](../../docs/tencent-cloud-buying-guide.md)

## 它能做什么

这个 Skill 负责把领星 OpenAPI 的公共接入层整理好，避免每个脚本都重复处理一遍鉴权和签名。

- 获取与续约 `access_token`
- 生成官方 `sign`
- 请求店铺、站点、销量、订单、促销、广告、利润、源表、库存等只读 API
- 通过 `lib/lingxing_openapi/` 复用统一服务层
- 自动发现并缓存 Amazon 相关只读官方文档
- 运行基础链路与扩展只读接口烟测

## 前置提醒

- 本机直连仍受领星 IP 白名单限制
- 如已部署固定出口网关并将 `EIP` 加入白名单，可正常使用
- 不要把真实 `APP ID / AppSecret`、真实 Bearer 或文档密钥写回公开示例

## 关键脚本

```bash
python3 skills/zach-lingxing-openapi-client/scripts/sync_docs.py
python3 skills/zach-lingxing-openapi-client/scripts/smoke_check.py
```

## 共享代码位置

```text
lib/lingxing_openapi/
```

其中包含：

- `client.py`：鉴权、签名、请求封装
- `services.py`：业务型接口封装与高层聚合
- `endpoint_specs.py`：稳定层 / 实验层工具定义
- `doc_catalog.py`：官方 `_sidebar.md` 解析与文档目录生成
- `promotions.py`：促销标签归一化
- `mcp.py`：领星 MCP 工具注册与传输层

文档缓存位于：

```text
skills/zach-lingxing-openapi-client/references/openapi_docs/
```

完整说明见 [SKILL.md](./SKILL.md)

## 依赖

- `LINGXING_APP_ID`
- `LINGXING_APP_SECRET`
- `openssl`

## 使用方式

如果你只是想让 AI 帮你把底座接好，可以直接说：

```text
请帮我检查当前工作区里的领星 OpenAPI 接入底座是否完整，包括环境变量、文档缓存、烟测脚本和共享库路径。
```

如果你在写 Python 脚本，也可以直接复用：

```python
from lib.lingxing_openapi import LingxingOpenAPIClient, LingxingOpenAPIService
```

## 如果安装或运行出错，直接让 AI 帮你排查

把下面这段直接发给你的 AI，并把报错信息、截图或终端输出一起贴上：

```text
我已经安装了 `zach-lingxing-openapi-client`，但现在遇到了问题。请你直接帮我排查并尽量修复：

1. 先判断是 skill 文件缺失、依赖缺失、领星 OpenAPI 鉴权配置错误、路径错误，还是当前 IDE 没有正确加载
2. 自动检查当前工作区里和 `zach-lingxing-openapi-client` 相关的文件、配置、脚本和依赖
3. 如果可以自动修复，就直接修复
4. 修复后告诉我还需要重启 IDE、重新加载工作区，还是重新运行哪个命令
5. 最后给我一个最短的验证步骤，确认这个 skill 已经能用了
```

## 问题反馈

如果你在 `zach-lingxing-openapi-client` 的鉴权、文档同步或烟测环节遇到问题，也可以直接提交飞书问卷反馈：

- [Skill / MCP / 运营问题反馈收集](https://my.feishu.cn/share/base/form/shrcnAg1QaUD8SjBjqR8gjg8Ftf)

<img src="../../assets/traffic/feishu-feedback-form.png" width="260" alt="飞书问卷反馈二维码" />

## 关于作者

关注「**Zach的进化笔记**」，获取 AI x 跨境电商的实战经验、工具和方法论：

<img src="../../assets/traffic/wechat-official-account.jpg" width="200" alt="公众号二维码" />

扫码加入群聊「Zach的第二群朋友们👀」，一起交流 AI + 跨境电商的实战玩法：

<img src="../../assets/traffic/wechat-group.jpeg" width="200" alt="Zach的第二群朋友们二维码" />

如果群二维码过期，也可以通过上面的公众号二维码获取最新入口。
