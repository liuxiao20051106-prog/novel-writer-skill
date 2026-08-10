# 通用 AI 配置指南

适用于任何支持系统提示词（System Prompt）的 AI 平台，包括但不限于：

- **Kimi** (kimi.moonshot.cn)
- **豆包** (doubao.com)
- **通义千问** (tongyi.aliyun.com)
- **文心一言** (yiyan.baidu.com)
- **Poe** (poe.com)
- **Perplexity** (perplexity.ai)
- **Ollama** (本地模型)
- **LM Studio** (本地模型)
- 以及任何兼容 OpenAI API 格式的服务

## 通用配置步骤

1. 打开 `SKILL.md` 文件
2. 去掉开头的 YAML frontmatter 块（`---` 之间的几行）
3. 将剩余的全部内容作为「系统提示词」「角色设定」「自定义指令」或「Persona」粘贴
4. 开始对话

## Ollama / 本地模型

```bash
# 创建一个 Modelfile
cat > Modelfile << 'EOF'
FROM llama3.1:70b  # 或其他模型
SYSTEM """
（粘贴 SKILL.md 正文内容）
"""
PARAMETER temperature 0.8
PARAMETER top_p 0.9
EOF

# 创建自定义模型
ollama create novel-writer -f Modelfile

# 使用
ollama run novel-writer
```

## LM Studio

1. 加载模型后，在右侧 System Prompt 栏粘贴 `SKILL.md` 正文
2. 调整 Temperature 到 0.7-0.9（创意写作推荐范围）
3. 开始对话

## Poe

1. 创建 Bot → 选择模型
2. 在 Prompt 栏粘贴 `SKILL.md` 内容
3. 设置 Bot 名称和描述

## OpenAI 兼容 API 通用代码

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="https://your-api-endpoint"  # 替换为对应服务
)

with open("SKILL.md", "r", encoding="utf-8") as f:
    system_prompt = f.read()

response = client.chat.completions.create(
    model="your-model-name",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "你的写作需求"}
    ]
)
```

## 注意

不同平台的 token 限制不同，`SKILL.md` 约占用 ~4000-5000 tokens。如果平台上下文窗口较小（<8K），建议精简后再使用。
