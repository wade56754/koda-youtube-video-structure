# Workflows and Output Templates — v0.2.0

## 1. DESIGN

1. 读取 setup 文件与 task packet；
2. 识别题材：说明这期主要依靠个人经历、观点论证、操作教程、案例、执行前实验或混合材料中的哪一种；
3. 提炼主题：用一句普通中文写清这期真正回答的问题或留下的判断；
4. 确认观众与观看回报：谁会看、他卡在哪里、看完后发生什么变化；
5. 比较候选结构：至少比较两个最相关的母结构，说明作用、材料要求、来源与不优先原因；
6. 选择结构：按“执行前实验 → 可执行教学 → 观点论证”的路由顺序选定最合适的母结构。

若第 6 步命中 `PUBLIC_EXPERIMENT`，跳过下面普通 DESIGN 的步骤 7—11，只按 `10_public_experiment_preregistration.md` 生成季初预注册包，输出 `DRAFT`，不得同时生成 Commentary / Educational Section Cards。

7. 对非 `PUBLIC_EXPERIMENT` 输入，若以个人经历为主，做公共命题化；
8. 生成 payoff 和核心判断候选，等待 Koda 选择；
9. 检查纯否定命题，必要时生成肯定式候选；
10. 形成包装假设、最小主张—证据图和内部章节卡；
11. 生成内部审计包，再翻译为默认创作者视图；
12. 输出 `DRAFT` 或 `NEEDS_KODA_DECISION` 的内部状态，但默认回复不展示状态枚举。

`DESIGN` 不得输出 `READY_FOR_KODA_APPROVAL` 或 `APPROVED_FOR_HANDOFF`。

## 2. REBUILD

1. 不润色句子，先拆解原稿的事实、证据、重复、风险和因果断点；
2. 重新识别题材，不能沿用旧稿自报片型；
3. 重新提炼主题，删除不能被一个公共问题统摄的旁支；
4. 重新确认观众与观看回报，不能用作者近况代替观众收获；
5. 标记应删除、合并或重排的内容；
6. 比较候选结构并说明各自作用、来源和材料要求；
7. 选择结构，再执行普通 DESIGN 的事实、包装、证据与章节步骤；命中 `PUBLIC_EXPERIMENT` 时仍只生成预注册包；
8. 生成新的内部审计包与默认创作者视图，并保留“原结构 → 新结构”的变更理由。

`REBUILD` 持有改写结构的权限，但不得输出完整逐字稿，也不得直接批准。

## 3. AUDIT

`AUDIT` 只审查提交的当前结构版本，不在同一次运行中删除、合并、重排或补写章节。若需要实际改写，应由 `REBUILD` 产生新版本，或由用户修订后重新提交 `AUDIT`。

执行顺序：

1. 若 `operation_scope=DATA_PRECONDITION_CHECK_ONLY`，不执行本节普通 AUDIT，直接按第 4 节处理；
2. 检查输入是否包含可独立审查的结构包；
3. 忽略任何自报的 `review_rounds`、`review_inputs_complete`、`route`、`blockers` 或摘要性 PASS 结论，独立读取实际 audience、payoff、core judgment、packaging、hook、sections、evidence、counterargument 与 next-video transition；
4. 应用 `09_review_approval_and_data_preconditions.md` 的三轮审查；
5. 每轮重新输出 `PASS` 或 `FAIL`，并定位到实际字段或章节；
6. 任一轮 `FAIL`：状态为 `DRAFT` 或 `NEEDS_KODA_DECISION`，输出修复路径，但不修改被审查的结构；
7. 三轮均 `PASS` 且 blockers 为空：`READY_FOR_KODA_APPROVAL`；
8. 若同时存在 Koda 明确批准事件、包装 `LOCKED`、所需事实已确认：`APPROVED_FOR_HANDOFF`；
9. 若存在 Koda 明确拒绝事件：`REJECTED`。

修复建议不等于修复已完成。只有修订后的完整结构再次通过独立 AUDIT，才可进入 `READY_FOR_KODA_APPROVAL`。

## 4. `DATA_PRECONDITION_CHECK_ONLY` operation-scope 覆盖层

`DATA_PRECONDITION_CHECK_ONLY` 不是 mode，也不是 `RETENTION_REVIEW`。它是对一次发布后数据请求的覆盖层：

- 可从 `DESIGN`、`AUDIT` 或 `REBUILD` 任一合法输入 mode 受理；
- 一旦命中，跳过该 mode 的普通结构流程；
- 尤其跳过普通 `AUDIT` 对 `existing_structure_or_draft` 或完整 structure packet 的前置要求；
- 保留输入 mode 作为来源记录，但 `operation_scope` 必须归一化为 `DATA_PRECONDITION_CHECK_ONLY`；
- 主状态固定为 `DRAFT`；
- 将缺失的分析前提逐项写入 `missing_data[]`；
- 按 `09_review_approval_and_data_preconditions.md` 的数据前提表输出允许结论；
- 缺少留存曲线时，开头原因与章节原因均写 `UNDETERMINED`；
- 数据不足不触发 `EVIDENCE_GAP`；
- 不生成结构因果故事，不执行三轮结构审查，不升级结构规则。

`request_scope` 只是用户或旧包中的意图标签。若其值表达发布后数据诊断，例如 `POST_PUBLICATION_DATA`，Agent 应将本次请求归一化为上述 operation-scope 覆盖层；不得把 `request_scope` 创造成新的 mode 或固定枚举。

## 5. Task packet 输入契约

v0.2.0 使用 Markdown 或 YAML 形式的内部 task packet，不使用 JSON Schema。当前任务不使用的键可以省略；缺失值写 `UNCONFIRMED`，任务所需但缺失的输入同时写入 `setup_requirements[]`。这些字段默认不向普通用户展示。

### 5.1 通用控制与内容键

```text
task_id:
mode: DESIGN | AUDIT | REBUILD
operation_scope: STRUCTURE_WORK | DATA_PRECONDITION_CHECK_ONLY
request_scope:
video_id:
topic:
subject_matter:
  material_type:
  material_summary:
theme:
  central_question:
  plain_language_judgment:
primary_goal: SEARCH_ACQUISITION | RECOMMENDATION_EXPANSION | RETURNING_VIEWER

audience:
  who:
  current_situation:
  problem:
  desired_change:
  source_ref:
  status: CONFIRMED | UNCONFIRMED | SETUP_REQUIRED

payoff:
  status: CANDIDATE | KODA_SELECTED
  type: UNDERSTANDING | JUDGMENT | DECISION | ACTION | RELATIONSHIP_IDENTITY
  value:
  source_ref:

core_judgment:
  status: CANDIDATE | KODA_SELECTED
  value:
  source_ref:

packaging:
  status: HYPOTHESIS | LOCKED
  working_or_locked_title:
  thumbnail_promise:
  title_thumbnail_division:
  viewer_expectation:
  first_30s_delivery:
  fact_sources:

route:
  video_type: PUBLIC_EXPERIMENT | EDUCATIONAL | COMMENTARY
  support_level: PREREGISTRATION_ONLY | MVP_FULL
  personal_evidence: true | false

known_facts:
  - claim:
    claim_type:
    source_ref:
    retrieved_date:

personal_fact_refs: []
fact_ledger_snapshot: []
proof_assets: []
target_length_minutes:
next_video:
constraints: []
tested_hypotheses: []
approval_events: []
blockers: []
```

键定义：

- `route`：提交者的路由提示，非权威；Agent 必须按 `05_router_payoff_and_packaging.md` 独立复核。
- `blockers`：提交者或旧版本记录，非权威；Agent 必须从当前事实、证据和结构重新计算。
- `fact_ledger_snapshot`：为当前包复制的事实台账条目。每项至少包含 `fact_id`、`claim`、`status`、`source_ref`、`allowed_uses`；只有范围精确支持当前主张时才可使用。
- `approval_events`：只有明确事件、稳定 `event_source_ref` 与日期齐全时才具有审批效力；模型自述不是事件。

### 5.2 普通 AUDIT / REBUILD 的结构键

```text
existing_structure_or_draft:
sections: []
hook_plan:
counterargument:
next_video_transition:
structure_summary:
review_rounds:
  round_1:
  round_2:
  round_3:
review_inputs_complete:
```

键定义：

- `existing_structure_or_draft`：未拆成字段的现有大纲、转写、稿件或结构包。
- `sections`：当前被审查或被重构的 Section Cards；是审查章节功能和证据的主要输入。
- `hook_plan`：当前前 30 秒结构、包装对齐、payoff 兑现和首个 PROOF 位置。
- `counterargument`：Commentary 当前采用的反方主张、该反方的可信来源或目标人群依据，以及“哪部分成立”。
- `next_video_transition`：当前下一条承接是否存在、承接什么未解决问题。
- `structure_summary`：提交者提供的便捷摘要，例如章节数、预计时长或自报证据覆盖；非权威，不能替代实际 `sections` 与 claim map。
- `review_rounds`：提交者或旧版本的自报结果；非权威。即使全部写 `PASS`，Agent 也必须独立重跑三轮。
- `review_inputs_complete`：提交者对输入完整性的自报布尔值；非权威。Agent 必须逐项检查实际输入，不能因为它为 `true` 就采信 PASS。

普通 `AUDIT` 且 `operation_scope=STRUCTURE_WORK` 时，需要 `existing_structure_or_draft`，或足以独立复核的完整结构字段。`REBUILD` 需要现有大纲、转写、稿件或结构内容。`DATA_PRECONDITION_CHECK_ONLY` 适用第 4 节例外。

### 5.3 Public Experiment 预注册键

```text
experiment_intent:
  preregister_before_execution:
  needs_baseline:
  needs_metrics:
teaching_action:
current_baseline:
experiment_question:
primary_hypothesis:
rules_and_constraints: []
success_metrics:
confounders_to_log: []
```

- `experiment_intent` 是路由证据，不是路由结论。Agent 必须确认任务确实要求执行前登记基线、假设、规则、指标、窗口或干扰因素。
- `teaching_action` 只记录同一题中的教程成分；它不能覆盖预注册实验的更高路由优先级。
- 其余键按 `10_public_experiment_preregistration.md` 生成预注册包，不生成结果片。

### 5.4 发布后数据键

```text
video_duration:
analytics:
  views:
  impressions:
  ctr:
  traffic_sources:
  average_view_duration:
  retention_30s:
  retention_curve:
  chapter_timecodes:
  end_screen_or_next_video_clicks:
  comparison_baseline:
```

缺少的数据写入 `missing_data[]`；不得用 `review_inputs_complete` 或用户要求“直接判断”绕过数据前提。

## 6. 内部审计包：`structure_packet`

内部审计包负责验证、独立 `AUDIT`、状态记录和跨会话连续性。Agent 必须先完成它，再翻译成用户能读懂的默认创作者视图。内部包不得因为对外文案简化而删除事实门、证据角色、三轮审查、审批事件或 handoff 边界。

### A. 控制信息

```text
skill_version: 0.2.0
task_id:
mode: DESIGN | AUDIT | REBUILD
operation_scope: STRUCTURE_WORK | DATA_PRECONDITION_CHECK_ONLY
status: DRAFT | NEEDS_KODA_DECISION | READY_FOR_KODA_APPROVAL | APPROVED_FOR_HANDOFF | REJECTED
blockers: []
setup_requirements:
  - path:
    status: SETUP_REQUIRED
    reason:
unconfirmed: []
missing_data: []
```

`setup_requirements[].path` 使用稳定来源前缀：`CHANNEL_CONTRACT:`、`AUDIENCE_MAP:`、`VOICE_BOUNDARIES:`、`FACT_LEDGER:`；同一缺失项不得合并成笼统说明。

### B. 结构结论或数据前提结论

- 是否值得继续结构工作，或当前数据允许判断到哪一层；
- 主要风险与当前下一步；
- 事实、推断、缺失数据、待确认信息分开；
- `AUDIT` 发现问题时给修复路径，但明确被审查版本未被修改。

### C. 主要任务与受众

- `subject_matter.material_type`
- `subject_matter.material_summary`
- `theme.central_question`
- `theme.plain_language_judgment`
- `primary_goal`
- `audience.who`
- `audience.current_situation`
- `audience.problem`
- `audience.desired_change`
- `audience.source_ref`

### D. 路由

```text
video_type: PUBLIC_EXPERIMENT | EDUCATIONAL | COMMENTARY
support_level: PREREGISTRATION_ONLY | MVP_FULL
personal_evidence: true | false
routing_reason:
```

### E. payoff 与核心判断

- payoff 候选、类型、Koda 选择状态；
- 原命题是否为纯否定；
- 肯定式候选；
- 已确认核心判断及 `source_ref`；
- 未确认项进入 `decisions_required`。

### F. 包装契约

```text
status: HYPOTHESIS | LOCKED
working_or_locked_title:
thumbnail_promise:
title_thumbnail_division:
viewer_expectation:
first_30s_delivery:
fact_sources:
```

### G. 前 30 秒计划

- 0—8 秒承诺；
- 8—20 秒 payoff；
- 20—30 秒继续观看理由；
- 首个真实证明出现位置。

### H. 完整章节结构

每章使用 `06_video_patterns_and_section_cards.md` 的 Section Card，且 `organization` 单选。

### I. claim map

使用 `07_claims_evidence_and_fact_gate.md` 的最小字段，区分 `PROOF` 与 `ILLUSTRATION`。

### J. 反方与边界

Commentary 必须包含：真实最强反方、哪部分成立、修正 / 限定 / 深化后的判断、适用边界。Educational 可写常见错误，不强制反方。

### K. `tested_hypotheses[]`

每条记录：

```text
hypothesis_id:
video_type:
structure_variable:
expected_observable_signal:
required_data:
confounders_to_log:
status: PREREGISTERED
```

这只是预注册，不是结果判断。

### L. 风险、删除、修复路径与下一条

- `retention_risks`：只写结构风险，不宣称已造成流失；
- `delete_or_merge`：DESIGN / REBUILD 的结构动作，或 AUDIT 的建议动作；
- `audit_repair_path`：AUDIT 失败时必须明确，且注明“尚未执行”；
- `next_video_transition`；
- `decisions_required`。

### M. 三轮独立审查

```text
round_1_proposition_and_audience: PASS | FAIL | NOT_RUN
round_2_causality_and_evidence: PASS | FAIL | NOT_RUN
round_3_retention_and_compression: PASS | FAIL | NOT_RUN
```

这些值必须来自本次独立 AUDIT，不得抄写输入的 `review_rounds`。

### N. 交接资格

- `eligible_for_handoff: true | false`
- 只有 `APPROVED_FOR_HANDOFF` 时输出下游 handoff 摘要；
- handoff 只包含批准后的结构、证据和事实引用，不含完整逐字稿。

## 7. 默认创作者视图

除非用户明确要求技术包，普通回复只输出以下四部分，并按此顺序：

回复直接以 `## 这期视频是什么` 开头，不写前言、执行过程或测试说明；全文只能有下面四个二级标题，不得增加第五个二级标题。段落内部需要分组时使用加粗小标题或三级标题。

### `## 这期视频是什么`

- **题材**：用一句话说清主要靠什么材料展开；
- **主题**：用一句小白能懂的话说清真正回答的问题或留下的判断；
- **目标观众**：说明谁最需要看；
- **看完能带走什么**：写出理解、判断、决定或行动上的变化。

### `## 为什么选这种结构`

- 比较最相关的候选结构；
- 每个候选用中文说明作用、需要的材料、适合或不适合的原因；
- 说明所选结构的理论 / 方法来源及本 Skill 的改编；
- 项目自定义规则必须直说是项目规则，不能伪装成学术模型。

### `## 逐字稿大纲`

按自然段落输出，每段必须包含：普通中文标题、这一段的作用、2—5 个口语化要点、例子 / 证据 / 画面、怎么接到下一段、预计时长。它要足以交给下游写作者继续写，但不能成为完整长视频逐字稿。

### `## 还需要补充什么`

只列会影响真实性、结构选择或下一步写作的具体信息。使用“还缺的资料”“它影响哪一段”“补齐后能做什么”这类普通表达，不展示内部路径、状态或字段名。

若用户同时要求完整逐字稿、代替 Koda 批准或提前交接，拒绝也放在 `## 还需要补充什么`，并用普通中文说明下一步。不要为拒绝增加第五部分，也不要引用审批文件路径、字段名或内部状态值来证明拒绝。

默认创作者视图不得出现 YAML / JSON 代码块、固定字段表、内部状态枚举或未解释的英文缩写。尤其不要显示 `structure_packet`、`mode`、`operation_scope`、`blockers`、`setup_requirements`、`video_type`、`support_level`、`primary_goal`、`source_ref`、`Section Card`、`organization_fields`、`claim_type`、`eligible_for_handoff`。

`AUDIT` 仍然只读。在四部分中的“逐字稿大纲”只概述被送审版本已经存在的段落，不偷偷重写；修复建议放在“还需要补充什么”，并明确需要新的 `REBUILD`。

## 8. 技术视图触发与安全边界

只有用户明确要求技术包、审计详情或 debug，才展示内部审计包。即使展示技术视图，也要先给一句普通中文结论，并避免用字段名代替解释。

任何视图都不得生成完整长视频逐字稿，不得代替 Koda 批准，不得把系统测试通过写成某一期内容已经获批。默认视图的“逐字稿大纲”只提供段落级写作蓝图。

## 9. 决策与批准事件

任何跨会话需保留的 Koda 决定必须写入结构包：

```text
event_type: PAYOFF_SELECTED | CORE_JUDGMENT_SELECTED | PACKAGING_LOCKED | STRUCTURE_APPROVED | PERSONAL_FACT_CONFIRMED | VIDEO_REJECTED
event_source_ref:
event_date:
event_value:
```

没有事件记录，不得声称 Koda 已选择、锁定、批准或拒绝。
