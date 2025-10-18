# Sing-box & OpenClash 规则集

本仓库维护 Emby 和 TikTok 的规则集，同时支持 sing-box 和 OpenClash。

## 文件说明

### OpenClash 规则文件（纯文本格式）

- **emby.list** - Emby 服务规则，包含常见的 Emby 服务器域名
- **tiktok.list** - TikTok 服务规则，包含 TikTok 及其相关服务的域名

这些 `.list` 文件使用标准的 OpenClash 规则格式，可以直接在 OpenClash 中引用。

### Sing-box 规则文件（二进制格式）

- **emby.mrs** - 从 emby.list 编译生成的 sing-box 二进制规则集
- **tiktok.mrs** - 从 tiktok.list 编译生成的 sing-box 二进制规则集

这些 `.mrs` 文件是经过编译的二进制格式，用于 sing-box。

### 中间文件

- **emby-source.json** - 从 emby.list 转换的 JSON 格式（用于编译 .mrs）
- **tiktok-source.json** - 从 tiktok.list 转换的 JSON 格式（用于编译 .mrs）

## OpenClash 使用方法

### 方式一：在线引用（推荐）

在 OpenClash 规则配置中添加以下 URL：

```yaml
# Emby 规则
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

然后在规则中使用：

```yaml
rules:
  - RULE-SET,Emby,Emby节点
  - RULE-SET,TikTok,TikTok节点
```

### 方式二：本地使用

1. 下载对应的 `.list` 文件到 OpenClash 的规则目录
2. 在配置中引用本地文件路径

## Sing-box 使用方法

在 sing-box 配置中引用编译后的 `.mrs` 文件：

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "emby",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/emby.mrs",
        "download_detour": "direct"
      },
      {
        "tag": "tiktok",
        "type": "remote",
        "format": "binary",
        "url": "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/tiktok.mrs",
        "download_detour": "direct"
      }
    ],
    "rules": [
      {
        "rule_set": ["emby"],
        "outbound": "emby-proxy"
      },
      {
        "rule_set": ["tiktok"],
        "outbound": "tiktok-proxy"
      }
    ]
  }
}
```

## 规则格式

所有 `.list` 文件遵循标准的 OpenClash 规则格式：

- `DOMAIN,domain.com` - 精确匹配完整域名
- `DOMAIN-SUFFIX,domain.com` - 匹配域名后缀（包括子域名）
- `DOMAIN-KEYWORD,keyword` - 匹配包含关键词的域名
- `IP-CIDR,1.2.3.0/24` - 匹配 IP 段
- `#` 开头的行为注释

示例：
```
# Emby 基础规则
DOMAIN-SUFFIX,emby.media
DOMAIN-KEYWORD,emby
DOMAIN,media.nijigem.by
```

## 维护和更新

### 添加新规则

1. 编辑 `emby.list` 或 `tiktok.list` 文件
2. 添加新的规则行（遵循上述格式）
3. 提交更改

### 自动构建

当 `.list` 文件更新时，GitHub Actions 会自动：
1. 将 `.list` 转换为 JSON 格式
2. 使用 sing-box CLI 编译为 `.mrs` 二进制文件
3. 提交生成的文件

## 脚本说明

- `scripts/list2ruleset.py` - 将 `.list` 文件转换为 sing-box JSON 格式

手动运行：
```bash
python scripts/list2ruleset.py emby tiktok
```

## 许可证

本项目采用开源许可证，具体请查看 LICENSE 文件。

## 贡献

欢迎提交 Pull Request 来添加更多的规则或改进现有规则。

## 鸣谢

- TikTok 规则来源：[blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- Emby 规则基于社区收集整理
