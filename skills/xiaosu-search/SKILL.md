---
name: xiaosu-search
description: "智能联网搜索，使用小宿科技 API。Use when: user asks to search the web, find information online, look up news, research topics, or get current information. Supports query parameters: count, freshness, enableContent, contentType, mainText, sites, blockWebsites."
homepage: https://docs.cloudsway.net
metadata: { "openclaw": { "emoji": "🔍", "requires": { "bins": ["python3"], "pip": ["requests"] } } }
---

# 小宿搜索 Skill (Xiaosu Search)

使用小宿科技智能搜索 API 进行联网搜索。

## 何时使用

✅ **使用此 skill 当：**

- "搜索 XXX" / "搜一下 XXX"
- "网上找找 XXX 的信息"
- "最新的 XXX 新闻"
- "XXX 的教程/文档"
- 需要实时网络信息的查询
- 查找特定网站的内容

❌ **不使用此 skill 当：**

- 已有内置工具能解决的问题（如天气用 weather skill）
- 本地文件搜索
- 数据库查询

## 配置

在 `TOOLS.md` 中配置 API 凭证：

```markdown
## 小宿搜索 API

- **BasePath**: `searchapi.cloudsway.net`
- **Endpoint**: `ySaJRFdgTNnBtbzy`
- **AccessKey**: `I10FCz8GUYXVHA7g53WG`
```

## 命令

### 基本搜索

```bash
python3 /usr/lib/node_modules/openclaw/skills/xiaosu-search/xiaosu_search.py "查询词"
```

### 带参数搜索

```bash
# 指定结果数量
python3 xiaosu_search.py "AI 新闻" count=20

# 时间筛选（Day/Week/Month）
python3 xiaosu_search.py "科技新闻" freshness=Week

# 返回长摘要
python3 xiaosu_search.py "Python 教程" enableContent=true contentType=MARKDOWN

# 指定/排除站点
python3 xiaosu_search.py "机器学习" sites=zhihu.com
python3 xiaosu_search.py "AI" blockWebsites=baijiahao.baidu.com
```

### 参数说明

| 参数 | 类型 | 默认 | 说明 |
|------|------|------|------|
| q | String | 必填 | 搜索查询词 |
| count | Short | 10 | 结果数量 (1-50) |
| freshness | String | - | 时间筛选：Day/Week/Month |
| enableContent | bool | false | 返回长摘要 |
| contentType | String | TEXT | 摘要格式：HTML/MARKDOWN/TEXT |
| mainText | bool | false | 返回关键片段 |
| sites | String | - | 指定站点 (host 格式) |
| blockWebsites | String | - | 排除站点 |

## 示例响应

```
搜索 人工智能 count=5

1. **人工智能成为全民赋能的最强力量**
   来源：OpenAI | 相关性：0.78
   时间：2025-07-21
   人工智能可以解释实验室结果、解读医学术语...
   🔗 https://openai.com/zh-Hans-CN/index/...

2. **什么是人工智能 (AI)？**
   来源：Google Cloud | 相关性：0.93
   人工智能 (AI) 是一组技术，使计算机能够学习、推理...
   🔗 https://cloud.google.com/learn/what-is-artificial-intelligence
```

## 注意事项

- API 凭证存储在 `TOOLS.md`，不要提交到版本控制
- 搜索结果数量可能少于请求数量
- offset 设置过大会导致结果为空
- 长摘要读取超时默认 0s，最大 10s
