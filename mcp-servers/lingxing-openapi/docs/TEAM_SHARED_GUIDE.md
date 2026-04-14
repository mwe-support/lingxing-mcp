# 团队共享接入手册

本手册面向公司内部成员，目标是让团队通过同一台固定出口云网关稳定拉取领星数据，而不用各自申请白名单 IP。

## 架构

团队成员客户端 → 本机 MCP 入口/桥接 → 公司固定出口网关 → 领星 OpenAPI

关键原则：

- 白名单只收敛到公司固定出口公网 IP
- 每位成员使用**单独令牌**
- 不把 `App ID / App Secret` 下发到成员电脑
- 成员侧只持有自己的访问令牌
- 网关可以先保留一个 bootstrap 单令牌，再逐步切到多人令牌分发

## 管理员侧准备

管理员至少准备这几项：

- 固定出口云网关已部署完成
- 领星白名单已放行该网关公网 IP
- 网关服务已启动
- 已创建团队令牌文件，例如 `/etc/lingxing-mcp/tokens.json`
- 已为每位成员签发单独令牌

网关环境变量建议：

```bash
LINGXING_APP_ID=replace-me
LINGXING_APP_SECRET=replace-me
LINGXING_TOKEN_CACHE_FILE=/var/lib/lingxing-mcp/token_cache.json
LINGXING_MCP_TOKENS_FILE=/etc/lingxing-mcp/tokens.json
LINGXING_MCP_HOST=127.0.0.1
LINGXING_MCP_PORT=8099
```

如果团队刚开始接入，可以先保持：

- `LINGXING_MCP_BEARER_TOKEN` 继续存在，保证老客户端不受影响
- `LINGXING_MCP_TOKENS_FILE` 作为多人令牌入口逐步启用

## 成员接入所需材料

管理员提供给每位成员：

- 网关访问地址
- 个人成员令牌
- 推荐的本地端口
- 对应 IDE 的接入片段

不要下发：

- `App ID`
- `App Secret`
- 服务器 root 权限
- 其他成员令牌

## macOS 接入

### 1. 建立本地 SSH Tunnel

```bash
ssh -N -L 18099:127.0.0.1:8099 user@gateway-host
```

如果公司使用 Tailscale，也可以把 `gateway-host` 换成 tailnet 主机名或 `100.x.y.z` 地址。

### 2. 写本机私有环境文件

```bash
mkdir -p ~/.config/lingxing-mcp
cp mcp-servers/lingxing-openapi/deploy/lingxing-client.env.example ~/.config/lingxing-mcp/client.env
```

把其中 `LINGXING_AUTH_HEADER` 改成你自己的成员令牌。

### 3. 配置客户端

- Claude Code / Codex / Cursor / Kiro：
  优先使用工作区内的项目配置或桥接脚本
- Claude App / Antigravity：
  使用薄入口指向工作区桥接脚本或本机 `18099`

### 4. 最小验证

```bash
curl http://127.0.0.1:18099/healthz
```

然后再执行一次 MCP `lingxing_health_check`。

## Windows 接入

### 1. 建立 SSH Tunnel

如果系统已安装 OpenSSH，可以在 PowerShell 中执行：

```powershell
ssh -N -L 18099:127.0.0.1:8099 user@gateway-host
```

### 2. 写本机私有配置

把 `lingxing-client.env.example` 复制到你自己的本地私有目录，例如：

```text
C:\Users\<你自己>\.config\lingxing-mcp\client.env
```

并把其中的成员令牌替换为你的个人令牌。

### 3. 验证

```powershell
curl http://127.0.0.1:18099/healthz
```

## 常见客户端接法

### Claude Code / Codex / Cursor / Kiro

- 优先项目级配置
- 通过工作区桥接脚本读取本机私有 env
- 不在项目文件里写成员令牌

### Claude App

- 用薄入口配置指向本机 `18099`
- 令牌仍放在本机私有文件

### Antigravity

- 用单独的 `mcp_config` 指向工作区桥接脚本或本机端口
- 不把真实令牌写进可提交的项目文件

## 令牌运维

查看令牌：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json list
```

新增成员：

```bash
python3 mcp-servers/lingxing-openapi/deploy/manage_tokens.py \
  --tokens-file /etc/lingxing-mcp/tokens.json \
  add --id alice-mac --description "Alice MacBook Pro"
```

吊销成员：

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

## 排错顺序

1. 先看 `curl http://127.0.0.1:18099/healthz`
2. 再看 `lingxing_health_check`
3. 再跑 `lingxing_smoke_check`
4. 如果是 `403`
   先检查领星授权有效期、接口权限、IP 白名单
5. 如果是 `missing_or_invalid_bearer`
   先检查是不是成员令牌错误、吊销或未更新

## 边界

- 这套共享方案当前是**只读**的
- 不提供库存修改、创建活动、改价格等写接口
- 团队成员使用的是领星读能力，不是领星后台替代品
