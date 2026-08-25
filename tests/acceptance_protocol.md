# Behavior Acceptance Protocol — v0.2.0

## 目的

这 19 个 fixtures 验证 Skill 的行为契约，不评价具体文案是否好听，也不以固定句子逐字匹配代替语义检查。

## 执行方式

对每个 `tests/fixtures/*.yaml`：

1. 将 `input.user_request` 与 `input.task_packet` 原样交给安装了本 Skill 的 Agent；
2. 默认要求输出普通中文的创作者视图；只有 fixture 明确要求技术包时才输出 Markdown `structure_packet`；
3. 按 fixture 的 `expected` 做语义检查；内部审计包与默认创作者视图分别验收；
4. 记录每项 `PASS` / `FAIL`，不要因同义改写判失败。

兼容说明：fixtures 01—18 是 v0.1.x 的内部审计包契约。执行这些旧 fixture 时，验收 harness 必须附加“请输出技术包，用于审计验收”的明确请求；不得用它们推翻 v0.2.0 的默认创作者视图。fixture 19 不附加技术请求，专门验证默认输出。

## 必检字段

- `status` 必须等于 `expected.status`；
- `blockers[]` 作为集合比较，不要求自然语言顺序；
- `route.video_type`、`support_level`、`personal_evidence` 必须符合预期；
- 若 fixture 定义 `expected.operation_scope`，必须精确匹配；
- 若 fixture 定义 `expected.review_rounds`，三轮结果必须逐项精确匹配；
- 若 fixture 定义 `expected.missing_data`，按集合精确比较，不能用 `EVIDENCE_GAP` 替代；
- 若 fixture 定义 `expected.setup_requirements`，按 `path` 集合精确比较，并确认每项都标记 `SETUP_REQUIRED` 且包含原因；
- `required_behaviors` 必须在结构决策中成立；
- `prohibited_behaviors` 任何一项出现即失败；
- 不检查候选标题、钩子或段落的逐字文本；
- 不以字段齐全替代命题、证据与审批边界检查。

## 默认创作者视图

- 必须先说明题材和主题，再比较候选结构并说明来源，最后给逐字稿大纲；
- 必须按“这期视频是什么 → 为什么选这种结构 → 逐字稿大纲 → 还需要补充什么”的顺序；
- 逐字稿大纲每段包含作用、口语化要点、例子 / 证据 / 画面、衔接和预计时长，但不能形成完整可照念台词；
- 默认回复不得出现 YAML / JSON、内部字段表、内部状态枚举或未解释缩写；
- 技术包仍须保留原有事实门、审查和审批边界。

## AUDIT 权限与独立复核

- `review_rounds`、`review_inputs_complete`、`route`、`blockers` 和 `structure_summary` 都是非权威输入；Agent 必须从实际结构独立复核；
- `AUDIT` 只诊断提交版本并提出修复路径，不在同次运行中删除、合并、重排或补写；
- 任一独立审查轮 `FAIL` 时，提交版本不得 `READY_FOR_KODA_APPROVAL`；
- 修订必须由 `REBUILD` 或用户完成，并以新完整版本重新提交 AUDIT；
- fixture 06 与 16 专门检验该边界。

## 状态测试约束

- `DESIGN` / `REBUILD` 不得输出 `READY_FOR_KODA_APPROVAL` 或 `APPROVED_FOR_HANDOFF`；
- 普通 `AUDIT` 只有本次独立执行的三轮全 `PASS` 且 blockers 为空，才可 `READY_FOR_KODA_APPROVAL`；
- 没有 Koda 明确批准事件，不得 `APPROVED_FOR_HANDOFF`；
- 没有 Koda 明确拒绝事件，不得 `REJECTED`；
- 有可信 `RELATIONSHIP_IDENTITY` 候选但尚未选择时，状态为 `NEEDS_KODA_DECISION` 且不添加 `NO_PAYOFF`。

## 数据不足测试约束

- `DATA_PRECONDITION_CHECK_ONLY` 是 operation-scope 覆盖层，可从任一合法 mode 受理，不是第四种 mode；
- 覆盖层跳过普通 AUDIT 的结构包前置要求和三轮结构审查，主状态固定 `DRAFT`；
- 只要没有留存曲线，涉及开头原因或章节原因的结论必须是 `UNDETERMINED`；同义表达不能替代该明确标记；
- 缺失分析数据进入 `missing_data[]`，不得复用 `EVIDENCE_GAP`；
- 覆盖层不得升级结构规则。
