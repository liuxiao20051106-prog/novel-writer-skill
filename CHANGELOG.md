# 更新日志

本项目的所有重要变更记录在此。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)。

## [Unreleased]

### 新增

- **英文版内容对齐**：`en/SKILL.md` 从约 40% 的缩略版扩充至与中文版完全对齐——补齐技法深度篇的场景设计（场景即冲突、四步场景结构、题材节奏配比表）、对话写作（六大目标、「阻力」原理、打破乒乓球问答）、节奏控制（快慢交替、高潮前压制）、文笔与风格（五种风格定调表、具体技法）、角色刻画七法、章节衔接失败模式与多线叙事提醒，以及构思/写章/修改三阶段的全部细节（梗概示例、章首衔接四方式带示例、字数控制、跨章通读清单等）。
- **英文版触发词**：`en/SKILL.md` 的 description 补充触发场景描述，降低欠触发概率。
- 新增 `platforms/zcode.md`：ZCode 平台配置指南（`.zcode/skills/` 与 `.agents/skills/` 发现路径、用户级/项目级安装、显式调用方式）。
- 新增本更新日志。

### 修复

- `platforms/claude-code.md` 安装命令此前只复制 `SKILL.md` 和 `aily-cli-skill.json`，导致 SKILL.md 中 `references/`、`templates/` 的按需加载链接失效；现补齐完整复制命令并在文件说明表中登记。

## [0.3.0]

### 新增

- 中英双语题材写作指南（`references/genre-playbooks.md`）与连载商业化指南（`references/serial-fiction-commercialization.md`），以及配套的市场定位、系列规划、发布终检模板。

## [0.2.0]

### 新增

- 多平台支持：Claude Code、ChatGPT、Cursor、Copilot、Gemini、DeepSeek 及通用平台配置指南。
- 英文版目录 `en/`（SKILL.md、references、templates）。
- AI 辅助创作工作方式与按需加载的专项指南体系。

## [0.1.0]

### 初始发布

- `novel-writer` skill 初始版本：构思、章节写作、修改润色三阶段工作流，八大技法深度篇，项目模板。
