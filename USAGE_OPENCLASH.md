# OpenClash 使用指南

## 快速开始

本仓库提供的 `emby.list` 和 `tiktok.list` 文件是纯文本格式的规则文件，可以直接在 OpenClash 中使用。

## 在线引用方式

### 步骤 1: 配置规则提供者（Rule Providers）

在 OpenClash 的配置文件中添加以下内容：

```yaml
rule-providers:
  Emby:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/emby.list"
    path: ./ruleset/emby.yaml
    interval: 86400

  TikTok:
    type: http
    behavior: classical
    url: "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/tiktok.list"
    path: ./ruleset/tiktok.yaml
    interval: 86400
```

**注意**: 请将 `YOUR_USERNAME` 和 `YOUR_REPO` 替换为实际的 GitHub 用户名和仓库名。

### 步骤 2: 使用规则集

在 `rules` 部分添加规则：

```yaml
rules:
  - RULE-SET,Emby,Emby专用节点
  - RULE-SET,TikTok,TikTok专用节点
  # 其他规则...
  - MATCH,DIRECT
```

将 `Emby专用节点` 和 `TikTok专用节点` 替换为你的实际节点名称或策略组名称。

## 规则说明

### Emby 规则 (emby.list)

包含以下类型的域名：

1. **官方域名**
   - emby.media - Emby 官方网站
   - mb3admin.com - Emby 管理相关
   - embyserver.media - Emby 服务器域名

2. **社区服务器**
   - 包含多个公共 Emby 服务器域名
   - 如果你有自己的 Emby 服务器，可以在文件中添加

3. **关键词匹配**
   - `DOMAIN-KEYWORD,emby` - 匹配所有包含 "emby" 的域名

### TikTok 规则 (tiktok.list)

包含以下类型的域名：

1. **TikTok 主域名**
   - tiktok.com
   - musical.ly
   - tiktokcdn.com 等

2. **ByteDance 相关域名**
   - bytedapm.com
   - byteoversea.com
   - ibyteimg.com 等

3. **CDN 和媒体服务**
   - 各种 TikTok CDN 域名
   - 视频和图片服务域名

## 规则格式说明

每个 .list 文件遵循以下格式：

- `DOMAIN,example.com` - 完全匹配 example.com
- `DOMAIN-SUFFIX,example.com` - 匹配 example.com 及其所有子域名
- `DOMAIN-KEYWORD,keyword` - 匹配包含 keyword 的所有域名
- `# 注释` - 以 # 开头的行是注释

## 自定义规则

### 添加自己的 Emby 服务器

编辑 `emby.list` 文件，在合适的位置添加：

```
# 我的 Emby 服务器
DOMAIN,emby.example.com
DOMAIN-SUFFIX,myemby.net
```

### 添加额外的 TikTok 相关域名

编辑 `tiktok.list` 文件，添加新的域名规则。

## 更新频率

- 规则文件会根据社区反馈持续更新
- OpenClash 会根据 `interval` 设置自动更新规则（默认 86400 秒，即 24 小时）
- 你也可以在 OpenClash 界面手动更新规则

## 常见问题

### Q: 规则不生效怎么办？

1. 检查规则在配置文件中的位置，确保在 MATCH 规则之前
2. 确保规则集 URL 正确，可以正常访问
3. 在 OpenClash 日志中查看是否有错误信息
4. 尝试手动更新规则集

### Q: 如何验证规则是否命中？

在 OpenClash 的日志中可以看到规则匹配情况：

```
[rule] emby.media matched Emby rule
```

### Q: 可以同时使用 Emby 和 TikTok 规则吗？

可以，两个规则集是独立的，可以同时使用并指向不同的节点或策略组。

### Q: 如何处理规则冲突？

OpenClash 按顺序匹配规则，第一个匹配的规则会被使用。请根据需要调整规则的顺序。

## 贡献

如果你发现有遗漏的域名或错误，欢迎提交 Pull Request 或 Issue。

## 相关链接

- [OpenClash 官方文档](https://github.com/vernesong/OpenClash)
- [Clash 规则集文档](https://github.com/Dreamacro/clash/wiki/premium-core-features)
