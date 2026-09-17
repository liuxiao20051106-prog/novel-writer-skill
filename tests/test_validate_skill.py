# -*- coding: utf-8 -*-
"""validate_skill.py 的单元测试：用临时目录搭一个最小 skill 再校验。"""

import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))

import validate_skill as vs  # noqa: E402


def build_skill(root: Path, *, name='novel-writer',
                description='AI 小说创作助手。用户说“写小说”“续写”“审稿”时触发。',
                body='# 总览\n\n正文。\n',
                with_en=True, en_refs=('a.md',), refs=('a.md',),
                link='(references/a.md)', name_dir=None) -> Path:
    skill = root / (name_dir or name)
    skill.mkdir(parents=True, exist_ok=True)
    (skill / 'SKILL.md').write_text(
        f'---\nname: {name}\ndescription: {description}\n---\n\n{body}',
        encoding='utf-8')
    (skill / 'references').mkdir(exist_ok=True)
    for ref in refs:
        (skill / 'references' / ref).write_text(f'# {ref}\n\n见 [SKILL.md](../SKILL.md)。\n', encoding='utf-8')
    if link:
        (skill / 'SKILL.md').write_text(
            (skill / 'SKILL.md').read_text(encoding='utf-8') + f'\n详见 [技法]{link}。\n',
            encoding='utf-8')
    if with_en:
        (skill / 'en').mkdir(exist_ok=True)
        (skill / 'en' / 'SKILL.md').write_text(
            f'---\nname: {name}\ndescription: English description long enough to pass checks.\n---\n\n{body}',
            encoding='utf-8')
        (skill / 'en' / 'references').mkdir(exist_ok=True)
        for ref in en_refs:
            (skill / 'en' / 'references' / ref).write_text(f'# {ref}\n', encoding='utf-8')
    return skill


def run(root: Path, warnings_as_errors=False) -> tuple:
    issues: list = []
    vs.check_frontmatter(root, issues)
    vs.check_links(root, issues)
    vs.check_structure(root, issues)
    vs.check_mirror(root, issues)
    vs.check_scripts(root, issues)
    errors = [msg for level, msg in issues if level == 'error']
    warnings = [msg for level, msg in issues if level == 'warning']
    return errors, warnings


class ValidateTests(unittest.TestCase):
    def test_healthy_skill_has_no_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp))
            errors, _ = run(skill)
            self.assertEqual(errors, [])

    def test_skill_suffix_directory_is_not_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), name_dir='novel-writer-skill')
            errors, warnings = run(skill)
            self.assertEqual(errors, [])
            self.assertFalse(any('不一致' in w for w in warnings))

    def test_missing_frontmatter_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = build_skill(root)
            (skill / 'SKILL.md').write_text('# 没有 frontmatter\n', encoding='utf-8')
            errors, _ = run(skill)
            self.assertTrue(any('frontmatter' in e for e in errors))

    def test_xml_in_description_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), description='写小说 <tag> 触发')
            errors, _ = run(skill)
            self.assertTrue(any('尖括号' in e for e in errors))

    def test_bad_name_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), name='Novel Writer')
            errors, _ = run(skill)
            self.assertTrue(any('kebab-case' in e for e in errors))

    def test_broken_link_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), link='(references/missing.md)')
            errors, _ = run(skill)
            self.assertTrue(any('失效' in e for e in errors))

    def test_missing_english_mirror_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), with_en=False)
            errors, _ = run(skill)
            self.assertTrue(any('en/' in e for e in errors))

    def test_unequal_reference_sets_are_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp), refs=('a.md', 'b.md'), en_refs=('a.md',))
            errors, _ = run(skill)
            self.assertTrue(any('en/references/b.md' in e for e in errors))

    def test_long_body_exceeding_limit_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            body = '\n'.join(f'第 {i} 行' for i in range(520))
            skill = build_skill(Path(tmp), body=body)
            errors, _ = run(skill)
            self.assertTrue(any('行上限' in e for e in errors))

    def test_script_syntax_error_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = build_skill(Path(tmp))
            (skill / 'scripts').mkdir()
            (skill / 'scripts' / 'broken.py').write_text('def oops(:\n', encoding='utf-8')
            errors, _ = run(skill)
            self.assertTrue(any('语法错误' in e for e in errors))

    def test_cli_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_skill(root, link='(references/missing.md)')
            buffer = StringIO()
            old = sys.stdout
            sys.stdout = buffer
            try:
                code = vs.main(['--root', str(root / 'novel-writer')])
            finally:
                sys.stdout = old
            self.assertEqual(code, 1)
            self.assertIn('ERROR', buffer.getvalue())


if __name__ == '__main__':
    unittest.main()
