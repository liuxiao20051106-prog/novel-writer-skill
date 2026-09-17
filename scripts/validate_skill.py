#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Skill 自身的结构校验：frontmatter、链接、中英镜像、脚本语法。

这个仓库同时是「一份 skill」和「一个开源项目」，文件一多最容易坏在三处：
frontmatter 不合规导致加载不出来、改了结构忘了改链接、中英文版本悄悄走偏。
这些都能被机器检查，所以交给脚本，不靠人记。

用法：

    python scripts/validate_skill.py                 # 自动定位 skill 根目录
    python scripts/validate_skill.py --root .        # 显式指定根目录
    python scripts/validate_skill.py --warnings-as-errors

退出码：有 error 时为 1，否则为 0（warning 默认不阻断）。
"""

from __future__ import annotations

import argparse
import py_compile
import re
import sys
import tempfile
from pathlib import Path

FRONTMATTER_RE = re.compile(r'^---\s*\n(.*?)\n---\s*(?:\n|$)', re.DOTALL)
LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^#{1,6}\s+\S', re.MULTILINE)
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
RESERVED = ('anthropic', 'claude')

MAX_NAME_LEN = 64
MAX_DESCRIPTION_LEN = 1024
MAX_SKILL_LINES = 500
TOC_MIN_HEADINGS = 2
TOC_MIN_LINES = 100

MIRROR_DIRS = ('references', 'templates')
MIRROR_FILES = ('SKILL.md',)


# --------------------------------------------------------------------------- #
# 基础工具
# --------------------------------------------------------------------------- #
def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    key = None
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if ':' in line and not line.startswith((' ', '\t')):
            key, _, value = line.partition(':')
            data[key.strip()] = value.strip()
        elif key:
            data[key] += ' ' + line.strip()
    return data


def body_lines(text: str) -> int:
    match = FRONTMATTER_RE.match(text)
    body = text[match.end():] if match else text
    return len(body.splitlines())


def check_frontmatter(root: Path, issues: list) -> None:
    skill = root / 'SKILL.md'
    if not skill.is_file():
        issues.append(('error', 'SKILL.md 不存在'))
        return

    meta = parse_frontmatter(skill.read_text(encoding='utf-8'))
    if not meta:
        issues.append(('error', 'SKILL.md 缺少 YAML frontmatter'))
        return

    name = meta.get('name', '')
    if not name:
        issues.append(('error', 'frontmatter 缺少 name'))
    else:
        if len(name) > MAX_NAME_LEN:
            issues.append(('error', f'name 超过 {MAX_NAME_LEN} 字符：{len(name)}'))
        if not NAME_RE.match(name):
            issues.append(('error', f'name 需为 kebab-case（小写字母/数字/连字符）：{name}'))
        if any(word in name for word in RESERVED):
            issues.append(('error', f'name 含保留字 {RESERVED}：{name}'))
        # 仓库目录常带 -skill 后缀（如 novel-writer-skill），而 name 不带，属正常
        dir_name = root.name[:-len('-skill')] if root.name.endswith('-skill') else root.name
        if name != dir_name:
            issues.append(('warning', f'name({name}) 与目录名({root.name}) 不一致'))

    description = meta.get('description', '')
    if not description:
        issues.append(('error', 'frontmatter 缺少 description'))
    else:
        if len(description) > MAX_DESCRIPTION_LEN:
            issues.append(('error', f'description 超过 {MAX_DESCRIPTION_LEN} 字符：{len(description)}'))
        if '<' in description or '>' in description:
            issues.append(('error', 'description 不能包含 XML 尖括号'))
        if len(description) < 40:
            issues.append(('warning', 'description 过短，可能缺少触发场景描述'))

    lines = body_lines(skill.read_text(encoding='utf-8'))
    if lines > MAX_SKILL_LINES:
        issues.append(('error', f'SKILL.md 正文 {lines} 行，超过 {MAX_SKILL_LINES} 行上限'))


def iter_markdown(root: Path):
    for path in sorted(root.rglob('*.md')):
        if '.git' in path.parts:
            continue
        yield path


def check_links(root: Path, issues: list) -> None:
    for path in iter_markdown(root):
        text = path.read_text(encoding='utf-8')
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith(('http://', 'https://', '#', 'mailto:')):
                continue
            target = target.split('#')[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                rel = path.relative_to(root)
                issues.append(('error', f'{rel} 中的链接失效：{target}'))


def check_structure(root: Path, issues: list) -> None:
    for directory in ('references', 'templates', 'scripts'):
        path = root / directory
        if path.is_dir():
            # __pycache__ 是跑测试/导入脚本的产物，不算结构问题
            nested = [p for p in path.iterdir()
                      if p.is_dir() and p.name != '__pycache__' and not p.name.startswith('.')]
            if nested:
                issues.append(('warning', f'{directory}/ 下存在子目录，引用应保持一级深度：'
                                          f'{[p.name for p in nested]}'))

    for path in iter_markdown(root):
        rel = path.relative_to(root)
        if rel.parts[0] == 'en' and len(rel.parts) > 2 and rel.parts[1] in MIRROR_DIRS:
            continue
        text = path.read_text(encoding='utf-8')
        if len(text.splitlines()) >= TOC_MIN_LINES and len(HEADING_RE.findall(text)) < TOC_MIN_HEADINGS:
            issues.append(('warning', f'{rel} 超过 {TOC_MIN_LINES} 行但缺少分节标题，建议加目录'))


def check_mirror(root: Path, issues: list) -> None:
    en_root = root / 'en'
    if not en_root.is_dir():
        issues.append(('error', '缺少 en/ 英文镜像目录（本 skill 维护中英双语对等）'))
        return

    for name in MIRROR_FILES:
        if (root / name).is_file() and not (en_root / name).is_file():
            issues.append(('error', f'英文镜像缺失：en/{name}'))

    for directory in MIRROR_DIRS:
        zh_dir, en_dir = root / directory, en_root / directory
        if not zh_dir.is_dir():
            continue
        if not en_dir.is_dir():
            issues.append(('error', f'英文镜像缺失目录：en/{directory}'))
            continue
        zh_files = {p.name for p in zh_dir.glob('*.md')}
        en_files = {p.name for p in en_dir.glob('*.md')}
        for missing in sorted(zh_files - en_files):
            issues.append(('error', f'英文镜像缺失：en/{directory}/{missing}'))
        for extra in sorted(en_files - zh_files):
            issues.append(('warning', f'英文镜像多出文件：en/{directory}/{extra}'))


def check_scripts(root: Path, issues: list) -> None:
    scripts = root / 'scripts'
    if not scripts.is_dir():
        return
    with tempfile.TemporaryDirectory() as tmp:
        for path in sorted(scripts.glob('*.py')):
            try:
                py_compile.compile(str(path), cfile=str(Path(tmp) / f'{path.stem}.pyc'), doraise=True)
            except py_compile.PyCompileError as exc:
                issues.append(('error', f'{path.name} 语法错误：{exc}'))


# --------------------------------------------------------------------------- #
def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='校验 skill 结构与中英镜像一致性')
    parser.add_argument('--root', type=Path, default=None, help='skill 根目录，默认为脚本上级目录')
    parser.add_argument('--warnings-as-errors', action='store_true', help='把警告也视为失败')
    args = parser.parse_args(argv)

    root = (args.root or Path(__file__).resolve().parent.parent).resolve()

    issues: list = []
    check_frontmatter(root, issues)
    check_links(root, issues)
    check_structure(root, issues)
    check_mirror(root, issues)
    check_scripts(root, issues)

    errors = [msg for level, msg in issues if level == 'error']
    warnings = [msg for level, msg in issues if level == 'warning']

    print(f'校验根目录：{root}')
    for msg in errors:
        print(f'  [ERROR]   {msg}')
    for msg in warnings:
        print(f'  [WARNING] {msg}')
    print(f'合计：{len(errors)} 个错误，{len(warnings)} 个警告')

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
