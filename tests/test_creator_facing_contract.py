from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_TEMPLATE = ROOT / "references" / "08_workflows_and_output_templates.md"
PATTERNS = ROOT / "references" / "06_video_patterns_and_section_cards.md"
GOLDEN = ROOT / "tests" / "golden" / "19_creator_friendly_rebuild.md"
FIXTURE = ROOT / "tests" / "fixtures" / "19_creator_friendly_rebuild.yaml"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
OPENAI_CONFIG = ROOT / "agents" / "openai.yaml"
NOTICES = ROOT / "THIRD_PARTY_NOTICES.md"
CI_WORKFLOW = ROOT / ".github" / "workflows" / "validate.yml"


class CreatorFacingContractTest(unittest.TestCase):
    def test_design_and_rebuild_diagnose_subject_matter_and_theme_before_routing(self):
        text = OUTPUT_TEMPLATE.read_text(encoding="utf-8")
        design = text[text.index("## 1. DESIGN") : text.index("## 2. REBUILD")]
        ordered_steps = ("识别题材", "提炼主题", "确认观众与观看回报", "比较候选结构", "选择结构")
        for step in ordered_steps:
            self.assertIn(step, design)
        if all(step in design for step in ordered_steps):
            positions = [design.index(step) for step in ordered_steps]
            self.assertEqual(positions, sorted(positions))

        rebuild = text[text.index("## 2. REBUILD") : text.index("## 3. AUDIT")]
        for step in ordered_steps:
            self.assertIn(step, rebuild)

    def test_each_structure_family_has_an_auditable_source_card(self):
        text = PATTERNS.read_text(encoding="utf-8")
        cards = re.findall(
            r"### 结构说明卡：([A-Z_]+)\n(.*?)(?=\n### 结构说明卡：|\n## |\Z)",
            text,
            flags=re.S,
        )
        by_name = {name: body for name, body in cards}
        expected = {
            "COMMENTARY",
            "EDUCATIONAL",
            "PUBLIC_EXPERIMENT",
            "STP",
            "PEIL",
            "VALUE_LOOP",
            "PLAIN",
        }
        self.assertEqual(expected, set(by_name))
        allowed_kinds = {"有外部理论依据", "由外部方法改编", "本项目工作规则"}
        for name, body in by_name.items():
            with self.subTest(name=name):
                for label in ("中文名", "作用", "适用场景", "不适用场景", "来源性质", "理论或方法来源", "本 Skill 改编"):
                    self.assertIn(f"- {label}：", body)
                source_kind = re.search(r"^- 来源性质：(.+)$", body, flags=re.M)
                self.assertIsNotNone(source_kind)
                self.assertIn(source_kind.group(1).strip(), allowed_kinds)
                self.assertRegex(body, r"https://|无外部理论来源")

    def test_default_creator_view_has_fixed_plain_language_order(self):
        self.assertTrue(GOLDEN.is_file(), "missing creator-facing golden output")
        if not GOLDEN.is_file():
            return
        text = GOLDEN.read_text(encoding="utf-8")
        headings = [
            "## 这期视频是什么",
            "## 为什么选这种结构",
            "## 逐字稿大纲",
            "## 还需要补充什么",
        ]
        self.assertTrue(text.startswith(headings[0]))
        self.assertEqual(re.findall(r"^## .+$", text, flags=re.M), headings)
        positions = [text.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))

        forbidden = (
            "structure_packet",
            "operation_scope",
            "blockers",
            "setup_requirements",
            "video_type",
            "support_level",
            "primary_goal",
            "source_ref",
            "Section Card",
            "organization_fields",
            "claim_type",
            "eligible_for_handoff",
            "UNCONFIRMED",
            "PROOF",
            "APPROVED_FOR_HANDOFF",
            "handoff",
            "DESIGN",
            "AUDIT",
            "REBUILD",
            "payoff",
            "main",
            "```yaml",
            "```json",
        )
        for token in forbidden:
            with self.subTest(token=token):
                self.assertNotIn(token, text)

        outline = text[text.index("## 逐字稿大纲") : text.index("## 还需要补充什么")]
        sections = re.findall(r"^### \d+\. .+$", outline, flags=re.M)
        self.assertGreaterEqual(len(sections), 5)
        self.assertIn("这一段的作用", outline)
        self.assertIn("例子、证据或画面", outline)
        self.assertIn("怎么接到下一段", outline)
        self.assertIn("预计时长", outline)

    def test_regression_fixture_records_the_shared_chat_failure(self):
        self.assertTrue(FIXTURE.is_file(), "missing shared-chat regression fixture")
        if not FIXTURE.is_file():
            return
        text = FIXTURE.read_text(encoding="utf-8")
        self.assertIn("6a8d8c9a-5100-83e8-b21b-1c9d964644c4", text)
        self.assertIn("题材", text)
        self.assertIn("主题", text)
        self.assertIn("结构来源", text)
        self.assertIn("逐字稿大纲", text)
        self.assertIn("默认回复不得出现", text)

    def test_internal_audit_packet_remains_available_but_is_not_the_default_reply(self):
        text = OUTPUT_TEMPLATE.read_text(encoding="utf-8")
        creator_view = text[text.index("## 7. 默认创作者视图") : text.index("## 8. 技术视图触发与安全边界")]
        self.assertIn("内部审计包", text)
        self.assertIn("默认创作者视图", text)
        self.assertIn("只有用户明确要求技术包、审计详情或 debug", text)
        self.assertIn("完整长视频逐字稿", text)
        self.assertIn("不得代替 Koda 批准", text)
        self.assertIn("回复直接以 `## 这期视频是什么` 开头", text)
        self.assertIn("不得增加第五个二级标题", text)
        self.assertIn("拒绝也放在 `## 还需要补充什么`", text)
        self.assertIn("至少写出一个完整的 `https://` 链接", creator_view)
        self.assertIn(
            "默认回复不得原样显示 `DESIGN`、`AUDIT`、`REBUILD`、`payoff`、`main`",
            creator_view,
        )
        for token in ("UNCONFIRMED", "PROOF", "APPROVED_FOR_HANDOFF", "handoff"):
            with self.subTest(token=token):
                self.assertIn(f"`{token}`", creator_view)
        for translation in ("待核实", "真实证明", "目前不能交给下游写稿"):
            with self.subTest(translation=translation):
                self.assertIn(translation, creator_view)

    def test_v020_release_metadata_and_ci_cover_the_new_contract(self):
        readme = README.read_text(encoding="utf-8")
        changelog = CHANGELOG.read_text(encoding="utf-8")
        openai_config = OPENAI_CONFIG.read_text(encoding="utf-8")
        notices = NOTICES.read_text(encoding="utf-8")

        self.assertIn("v0.2.0", readme)
        self.assertIn("-eq 19", readme)
        self.assertIn("python3 -m unittest discover", readme)
        self.assertIn("## 0.2.0", changelog)
        self.assertIn("题材", openai_config)
        self.assertIn("逐字稿大纲", openai_config)
        for source in ("Toulmin", "Merrill", "Loewenstein", "Nosek"):
            with self.subTest(source=source):
                self.assertIn(source, notices)

        self.assertTrue(CI_WORKFLOW.is_file(), "missing public repository CI")
        if CI_WORKFLOW.is_file():
            workflow = CI_WORKFLOW.read_text(encoding="utf-8")
            self.assertIn("python3 -m unittest discover", workflow)
            self.assertRegex(workflow, r"actions/checkout@[0-9a-f]{40}")
            self.assertRegex(workflow, r"actions/setup-python@[0-9a-f]{40}")


if __name__ == "__main__":
    unittest.main()
