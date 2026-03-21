# 安装小宿搜索 Skill

## 步骤

### 1. 获取 API 凭证
从小宿科技控制台获取：
- BasePath
- Endpoint
- AccessKey

### 2. 配置凭证
编辑 `~/.openclaw/workspace/TOOLS.md`，填写你的凭证：

```markdown
## 小宿搜索 API

- **BasePath**: `your-base-path-here`
- **Endpoint**: `your-endpoint-here`
- **AccessKey**: `your-access-key-here`
```

### 3. 安装 Skill（需要管理员权限）

```bash
# 复制 skill 到系统目录
sudo cp -r ~/.openclaw/workspace/skills/xiaosu-search /usr/lib/node_modules/openclaw/skills/

# 或者创建软链接
sudo ln -s ~/.openclaw/workspace/skills/xiaosu-search /usr/lib/node_modules/openclaw/skills/xiaosu-search
```

### 4. 测试

```bash
# 直接运行 Python 脚本测试
python3 ~/.openclaw/workspace/skills/xiaosu-search/xiaosu_search.py "人工智能" count=5

# 或在 OpenClaw 中使用
搜索 人工智能 count=5
```

## 依赖

```bash
pip install requests
```
