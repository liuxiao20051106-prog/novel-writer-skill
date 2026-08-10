# 📖 Novel Writer Skill — 全平台 AI 写小说助手

一套完整的小说写作方法论，可适配 **Claude Code、ChatGPT、Cursor、GitHub Copilot、Gemini、DeepSeek、Kimi、豆包、通义千问、Ollama** 等主流 AI 平台。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/Platforms-7+-blue)](platforms/)
[![中文](https://img.shields.io/badge/语言-中文-red)](SKILL.md)
[![English](https://img.shields.io/badge/Lang-English-blue)](en/SKILL.md)

---

## 🚀 快速开始

选择你的平台，点击对应指南：

| 平台 | 配置指南 | 难度 |
|------|---------|------|
| **Claude Code** | [platforms/claude-code.md](platforms/claude-code.md) | ⭐ 一键安装 |
| **ChatGPT** | [platforms/chatgpt.md](platforms/chatgpt.md) | ⭐ Custom GPT |
| **Cursor** | [platforms/cursor.md](platforms/cursor.md) | ⭐ 规则文件 |
| **GitHub Copilot** | [platforms/copilot.md](platforms/copilot.md) | ⭐ 指令文件 |
| **Gemini** | [platforms/gemini.md](platforms/gemini.md) | ⭐ Gems / API |
| **DeepSeek** | [platforms/deepseek.md](platforms/deepseek.md) | ⭐ API / Web |
| **其他平台** | [platforms/generic.md](platforms/generic.md) | ⭐ 通用方法 |

核心文件就一个：**[SKILL.md](SKILL.md)**（中文版）或 [en/SKILL.md](en/SKILL.md)（English），把它加载到任意 AI 平台即可。

---

## ✨ 功能概览

### 完整创作流程

```
构思 → 章节写作 → 修改润色
```

| 阶段 | 涵盖内容 |
|------|---------|
| **构思** | 体裁选择 → 一句话梗概 → 主题与基调 → 世界观设定 → 角色设计（主角/配角/反派/关系网）→ 大纲规划（三幕结构 + 高潮排布） |
| **章节写作** | 写前检查（衔接上一章）→ 四段式单章结构 → 场景设计 → 对话写作 → 章首衔接 & 章尾勾连 → 写后自查 |
| **修改润色** | 宏观编辑（结构/弧线/跨章通读）→ 微观编辑（语言/句式/对话）→ 细节打磨（代入感审查） |

### 八大技法深度

| 技法 | 核心内容 |
|------|---------|
| **故事结构** | 三幕因果链 · 高潮排布规律 · 次要情节设计 |
| **角色塑造** | 五层设计法（原型→外在→创伤→矛盾→弧线）·「想要 vs 需要」框架 |
| **场景设计** | 场景即冲突 · 长度节奏控制 · 体裁配比（爽文 3:1 / 言情 2:2 / 悬疑 1:3） |
| **对话写作** | 六大目标 ·「阻力」核心原理 · 打破乒乓球问答 |
| **节奏控制** | 快慢交替机制 · 加速/减速手段 · 高潮「压制-释放」 |
| **文笔风格** | 五种风格定调 · 身体先于大脑 · 留白技巧 |
| **代入感** | 五层体系（视角锁定 + 感官沉浸 + 情感共振 + 处境设计 + 错误规避） |
| **章节衔接** | 四种桥接方式（情绪/动作/悬念/时空）· 多线叙事连续性 |

---

## 📁 项目结构

```
novel-writer-skill/
├── README.md                      # 项目总览（你正在看的）
├── SKILL.md                       # 核心 skill 文件（中文）
├── aily-cli-skill.json            # Claude Code 元数据
├── LICENSE                        # MIT 许可
│
├── platforms/                     # 各平台配置指南
│   ├── claude-code.md             # Claude Code 安装说明
│   ├── chatgpt.md                 # ChatGPT Custom GPT 配置
│   ├── cursor.md                  # Cursor Rules 配置
│   ├── copilot.md                 # GitHub Copilot 指令
│   ├── gemini.md                  # Google Gemini Gems/API
│   ├── deepseek.md                # DeepSeek API/Web
│   └── generic.md                 # 通用配置（Kimi/豆包/Ollama...）
│
├── en/                            # 英文版
│   └── SKILL.md                   # English version of core skill
│
└── templates/                     # 写作模板
    └── novel-project.md           # 小说项目追踪文件模板
```

---

## 🔧 三种通用安装方式

### 方式一：作为 AI System Prompt（最通用）

1. 打开 `SKILL.md`，去掉开头的 `---` 块（YAML frontmatter）
2. 将全部正文内容粘贴到 AI 平台的「系统提示词」「角色设定」或「Custom Instructions」栏
3. 开始对话

### 方式二：每次对话手动粘贴

直接将 `SKILL.md` 内容作为第一条消息发送给 AI。

### 方式三：Git Clone

```bash
git clone https://github.com/liuxiao20051106-prog/novel-writer-skill.git
```

---

## 🌐 英文版 / English Version

See [en/SKILL.md](en/SKILL.md) for the English version of the complete skill instructions.

---

## 🧠 设计理念

1. **代入感优先** — 一切技巧服务于「让读者忘记在读书」
2. **情感驱动** — 情节 + 情感旅程 = 好小说，缺一不可
3. **角色与情节互为因果** — 不同步生长就会互相拖累
4. **章节之间读得通** — 读者不需要每章重新适应
5. **初稿像慈爱的父母，修改时像无情的神** — Elizabeth McCracken

---

## 📊 Token 用量

`SKILL.md` 约 4000-5000 tokens。如果平台上下文窗口较小（< 8K），建议精简后使用，或分阶段加载不同部分。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- 新增平台适配指南 → `platforms/` 目录
- 翻译到其他语言 → 新建 `xx/` 目录
- 改进写作方法论 → 编辑 `SKILL.md`

---

## 📄 许可

MIT License — 详见 [LICENSE](LICENSE)
