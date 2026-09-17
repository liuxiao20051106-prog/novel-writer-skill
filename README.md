# 📖 Novel Writer Skill — 全平台 AI 写小说助手

一套完整的小说写作方法论，可适配 **Claude Code、ZCode、ChatGPT、Cursor、GitHub Copilot、Gemini、DeepSeek、Kimi、豆包、通义千问、Ollama** 等主流 AI 平台。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/Platforms-8+-blue)](platforms/)
[![中文](https://img.shields.io/badge/语言-中文-red)](SKILL.md)
[![English](https://img.shields.io/badge/Lang-English-blue)](en/README.md)

---

## 这是什么？

一个给 AI 用的「写小说系统指令」。把 [SKILL.md](SKILL.md) 加载到任意 AI 平台后，AI 就变成一个专业的小说写作助手——不是只会说"写得不错"的陪聊，而是真的能帮你：

- 从零构思一个故事（体裁、梗概、主题、世界观、角色、大纲）
- 按章写作，确保章节之间衔接流畅、情感连贯
- 写完自查（逻辑漏洞？角色降智？代入感够吗？）
- 逐层修改润色（结构 → 语言 → 细节）
- 按题材兑现读者承诺，并规划可持续连载与商业化路径
- 用可回滚、有人工作者门禁的流程批量协作，并以测试用例验收

## 为什么需要它？

直接对 AI 说「帮我写小说」，通常会得到一段还行的文字——但仅此而已。AI 不会主动帮你：

- ❌ 确认体裁和读者定位 → 写出来的东西不知道给谁看
- ❌ 设计有深度的角色 → 角色扁平、动机模糊
- ❌ 规划章节结构和高潮排布 → 写着写着就散了
- ❌ 保持章节之间的连贯性 → 上一章在哭下一章在笑
- ❌ 检查代入感 → 读者根本进不去
- ❌ 追踪伏笔和角色状态 → 写着写着就忘了前面埋了什么

这个 skill 把专业小说作者的完整工作流程写进了 AI 的系统指令，**让 AI 先成为合格的写作搭档，再开始动笔**。

## 核心特色

| 特色 | 说明 |
|------|------|
| 🎯 **方法论驱动** | 不是「写好看点」这种空泛指令，而是具体的技法：四段式单章结构、五层角色设计、四种章节桥接方式……每一项都有明确的「怎么做」和「为什么」 |
| 🔗 **章节连贯性** | 内置写前检查流程：写每章之前必须回顾上一章结尾，确保时间线、场景、POV、情绪四个维度都接得上 |
| 👁️ **代入感优先** | 五层代入体系：视角锁定 + 感官沉浸 + 情感共振 + 处境设计 + 常见错误规避，不是嘴上说「要有代入感」而是每一步都有检查点 |
| 🌍 **全平台通用** | 一套方法论，适配 Claude Code / ChatGPT / Cursor / Copilot / Gemini / DeepSeek / Kimi / 豆包 / Ollama 等 10+ 平台，每个平台都有具体配置指南 |
| 🧭 **题材与连载策略** | 覆盖玄幻、科幻、言情、悬疑等主要题材，并提供读者定位、平台核对、合同与权利检查框架 |
| 🧹 **去 AI 味** | 十类机器腔信号 + 中文高频词替换表 + 负面指令模板，写完直接扫一遍再交稿 |
| 🧪 **草稿量化体检** | `scripts/draft_diagnostics.py` 给出句长/段落变异系数、对话占比、感官密度、AI 腔密度、重复片段——用数据定位可疑段落 |
| 🤖 **可控 AI 工作流** | 用明确状态、人工审批、幂等重试和运行日志管理跨会话、批量章节与多人协作 |
| ✅ **质量评测** | 用硬性门禁、证据式评分和行为测试检查连续性、原创性、事实与发布风险 |
| 📋 **项目追踪模板** | 11 套中英文模板追踪角色、伏笔、风格锚、来源、市场假设、自动化运行和发布验收 |
| 🔒 **结构自检** | `scripts/validate_skill.py` 校验 frontmatter、链接有效性、中英镜像一致性与脚本语法，改动后跑一次就知道有没有改坏 |

## 适合谁用？

- 🖊️ **网文作者 / 小说创作者** — 需要 AI 真正理解写作流程，而不是只会写一段漂亮文字
- 🎓 **写作初学者** — 通过 AI 引导，系统学习小说创作的方法论
- 🔄 **多平台用户** — 你在 Claude Code 写大纲、在 DeepSeek 写正文、在 ChatGPT 润色——同一套方法论在所有平台保持一致的写作标准
- 📚 **长篇连载作者** — 项目追踪模板帮你管理角色、伏笔和情感节奏，不再写到后面忘了前面

---

## 🚀 快速开始

选择你的平台，点击对应指南：

| 平台 | 配置指南 | 安装方式 |
|------|---------|---------|
| **Claude Code** | [platforms/claude-code.md](platforms/claude-code.md) | 复制到 `~/.claude/skills/` |
| **ChatGPT** | [platforms/chatgpt.md](platforms/chatgpt.md) | 创建 Custom GPT |
| **Cursor** | [platforms/cursor.md](platforms/cursor.md) | 添加 `.cursorrules` |
| **GitHub Copilot** | [platforms/copilot.md](platforms/copilot.md) | 添加 `copilot-instructions.md` |
| **Gemini** | [platforms/gemini.md](platforms/gemini.md) | 创建 Gem / API |
| **DeepSeek** | [platforms/deepseek.md](platforms/deepseek.md) | System Prompt / Web |
| **ZCode** | [platforms/zcode.md](platforms/zcode.md) | `~/.agents/skills/` 或项目 `.zcode/skills/` |
| **其他平台** | [platforms/generic.md](platforms/generic.md) | 系统提示词粘贴 |

入口文件是 **[SKILL.md](SKILL.md)**（中文版）或 [en/SKILL.md](en/SKILL.md)（English）；专项指南与模板会按任务需要加载。

---

## ✨ 功能概览

### 完整创作流程

```
构思 → 题材与定位 → 章节/连载写作 → 修改润色 → 质量验收 → 发布准备
```

| 阶段 | 涵盖内容 |
|------|---------|
| **构思** | 体裁选择 → 一句话梗概 → 主题与基调 → 世界观设定 → 角色设计（主角/配角/反派/关系网）→ 大纲规划（三幕结构 + 高潮排布） |
| **章节写作** | 写前检查（衔接上一章）→ 四段式单章结构 → 场景设计 → 对话写作 → 章首衔接 & 章尾勾连 → 写后自查 |
| **修改润色** | 宏观编辑（结构/弧线/跨章通读）→ 微观编辑（语言/句式/对话）→ 细节打磨（代入感审查） |

### 十五项技法深度 + 长篇工程

每项技法的「必守底线」常驻 SKILL.md，完整方法论按需加载：

| 技法 | 核心内容 | 深度指南 |
|------|---------|---------|
| **故事结构** | 三幕因果链 · 节拍—场景—序列—幕—故事五级 · 十五节拍表 · 网文章/卷映射 | [打开](references/craft-story-structure.md) |
| **开篇钩子** | 黄金 300 字 · 黄金三章任务分配 · 四种章末钩子 · 开篇雷区 | [打开](references/craft-opening-hooks.md) |
| **角色塑造** | 五层设计法（原型→外在→创伤→矛盾→弧线）·「想要 vs 需要」· 三种弧线 · 语言指纹 | [打开](references/craft-character.md) |
| **情绪与潜台词** | 情绪三层（标签/身体/真相）· 三分栏写法 · 微观张力四手法 · 潜台词对照表 | [打开](references/craft-emotion-and-subtext.md) |
| **视角与叙述距离** | 人称/POV/时态四决策 · 叙述距离四档 · 视角越界与多线换线 | [打开](references/craft-pov-and-distance.md) |
| **场景设计** | 场景—续幕模型 · 四步结构 · 体裁配比（爽文 3:1 / 言情 2:2 / 悬疑 1:3） | [打开](references/craft-scene-design.md) |
| **对话写作** | 六大目标 ·「阻力」核心原理 · 打破乒乓球问答 · AI 三种典型病 | [打开](references/craft-dialogue.md) |
| **节奏控制** | 快慢交替机制 · 加速/减速手段 · 高潮「压制-释放」· 冷却章 | [打开](references/craft-pacing.md) |
| **悬念伏笔** | 信息差三种用法 · 悬念三层次 · 伏笔四模式与三段式回收 · 公平性原则 | [打开](references/craft-suspense-foreshadowing.md) |
| **文笔风格** | 五种风格定调 · 过滤词清除 · 动词优先 · 密度与句式控制 · 留白 | [打开](references/craft-prose-style.md) |
| **代入感** | 五层体系（视角锁定 + 感官沉浸 + 情感共振 + 处境设计 + 错误规避） | [打开](references/craft-immersion.md) |
| **章节衔接** | 四种桥接方式（情绪/动作/悬念/时空）· 时间跳跃 · 多线叙事连续性 | [打开](references/craft-chapter-bridging.md) |
| **网文节奏与追读** | 爽点三级 · 期待感管理 · 断章四型 · 三种章模板 · 毒点雷区 · 数据自查 | [打开](references/craft-webnovel-rhythm.md) |
| **修订工程** | 四轮修订法 · 反向提纲 · 冷却与通读 · 用 AI 修订的边界 · 停止信号 | [打开](references/craft-revision.md) |
| **去 AI 味** | 机器腔三根源 · 十类信号改法 · 叙事腔四类 · 中文高频词替换表 | [打开](references/craft-ai-tells.md) |
| **长篇一致性** | 上下文预算分配 · 分层摘要 · 两步生成法 · 每卷设定审计 · 会话交接 | [打开](references/context-budget.md) |

---

## 🧪 自带脚本

两个零依赖 Python 脚本（仅用标准库），输出纯文本或 JSON：

```bash
# 草稿量化体检：字数、句长/段落变异系数、对话占比、感官密度、AI 高频腔、重复片段、破折号密度
python scripts/draft_diagnostics.py 章节.md
python scripts/draft_diagnostics.py 章节.md --top 15 --json

# Skill 结构自检：frontmatter、链接有效性、中英镜像一致性、脚本语法
python scripts/validate_skill.py
python scripts/validate_skill.py --warnings-as-errors

# 跑脚本自身的单元测试（23 项）
python -m unittest discover -s tests
```

体检脚本给的是**线索不是判决**——指标超阈值先看上下文，别机械照改。`push`/`PR` 时 GitHub Actions 会自动跑测试与自检。

---

## 📁 项目结构

```
novel-writer-skill/
├── README.md                      # 项目总览（你正在看的）
├── CHANGELOG.md                   # 更新日志
├── SKILL.md                       # 核心 skill 文件（中文）
├── aily-cli-skill.json            # Claude Code 元数据
├── LICENSE                        # MIT 许可
│
├── scripts/                       # 零依赖 Python 脚本
│   ├── draft_diagnostics.py       # 草稿量化体检
│   └── validate_skill.py          # 结构与中英镜像自检
├── tests/                         # 脚本单元测试（23 项）
├── .github/workflows/validate.yml # push/PR 自动跑测试 + 自检
│
├── platforms/                     # 各平台配置指南
│   ├── claude-code.md             # Claude Code 安装说明
│   ├── zcode.md                   # ZCode 安装说明（原生 skill 发现）
│   ├── chatgpt.md                 # ChatGPT Custom GPT 配置
│   ├── cursor.md                  # Cursor Rules 配置
│   ├── copilot.md                 # GitHub Copilot 指令
│   ├── gemini.md                  # Google Gemini Gems/API
│   ├── deepseek.md                # DeepSeek API/Web
│   └── generic.md                 # 通用配置（Kimi/豆包/Ollama...）
│
├── en/                            # 完整英文版
│   ├── README.md                  # English project overview
│   ├── SKILL.md                   # English core skill
│   ├── references/                # 27 份 English specialist guides（含 15 份技法深度）
│   └── templates/                 # 11 套 English project templates
│
├── references/                    # 按需加载的专项指南（27 份）
│   ├── craft-*.md                 # 15 份技法深度（结构/开篇/角色/情绪/视角/场景/
│   │                              #   对话/节奏/悬念/文笔/代入/衔接/网文/修订/去AI味）
│   ├── context-budget.md          # 上下文预算与长篇记忆打包
│   ├── ai-collaboration.md        # AI 分工、提示方式与原创性
│   ├── project-continuity.md      # 长篇连续性与版本管理
│   ├── quality-review.md          # 分层审校与质量检查
│   ├── research-and-fact-checking.md # 事实核查与来源
│   ├── copyright-privacy-compliance.md # 版权、隐私与平台合规
│   ├── sensitive-content.md       # 敏感内容处理
│   ├── publishing-checklist.md    # 发布、翻译与改编
│   ├── genre-playbooks.md         # 主要题材写作指南
│   ├── serial-fiction-commercialization.md # 连载与商业化
│   ├── automation-workflow.md     # AI 自动化工作流
│   └── evaluation-and-test-cases.md # 质量评分与行为测试
│
└── templates/                     # 可直接复制的项目模板（11 套）
    ├── novel-project.md           # 小说项目总览
    ├── chapter-brief.md           # 章节任务卡
    ├── continuity-ledger.md       # 连续性台账
    ├── style-anchor.md            # 风格锚（防文风漂移）
    ├── reverse-outline.md         # 反向提纲（修订地图）
    ├── source-log.md              # 来源记录
    ├── release-checklist.md       # 发布终检
    ├── series-plan.md             # 系列与长篇规划
    ├── market-positioning.md      # 市场定位与连载假设
    ├── automation-run-log.md      # 自动化运行记录
    └── quality-scorecard.md       # 质量评分卡
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

英文版项目总览见 [en/README.md](en/README.md)；完整英文 skill 指令见 [en/SKILL.md](en/SKILL.md)。

For the English version of the complete skill instructions, see [en/SKILL.md](en/SKILL.md).

---

## 🧠 设计理念

1. **代入感优先** — 一切技巧服务于「让读者忘记在读书」
2. **情感驱动** — 情节 + 情感旅程 = 好小说，缺一不可
3. **角色与情节互为因果** — 不同步生长就会互相拖累
4. **章节之间读得通** — 读者不需要每章重新适应
5. **初稿像慈爱的父母，修改时像无情的神** — Elizabeth McCracken

---

## 📊 Token 用量

核心方法与 15 项技法的「必守底线」保留在 `SKILL.md`（正文 193 行）；技法完整展开（`references/craft-*.md`）与题材、长篇管理、商业化、自动化、事实核查、合规、质量测试等专项内容位于 `references/`，按任务需要加载，避免一次占用过多上下文。`en/` 提供同等范围的英文入口、指南和模板。

长篇写作时按 [上下文预算](references/context-budget.md) 打包：系统指令 15-25%、事实层 20-30%、前文 20-30%、本章任务卡 10-15%，至少留 20% 给生成。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- 新增平台适配指南 → `platforms/` 目录
- 翻译到其他语言 → 新建 `xx/` 目录
- 改进写作方法论 → 编辑 `SKILL.md`

---

## 📄 许可

MIT License — 详见 [LICENSE](LICENSE)
