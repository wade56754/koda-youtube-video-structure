# Runtime Contract — MVP v0.1.1

## 1. 覆盖边界

本 Skill 只覆盖：

```text
选题 / 现有结构 / 现有稿件
→ payoff 与公共命题
→ 包装假设
→ 片型路由
→ 结构与证据
→ 三轮结构审查
→ Koda 审批
```

不覆盖完整逐字稿、拍摄、发布、自动数据拉取或发布后因果诊断。

## 2. 模式与 operation scope

主模式只有：

- `DESIGN`
- `AUDIT`
- `REBUILD`

`HANDOFF` 是 `APPROVED_FOR_HANDOFF` 后生成的产物，不是模式。`RETENTION_REVIEW`、`CASE_STUDY`、`TREND_JUDGMENT` 均为延后能力。

`operation_scope` 与 mode 正交：

- `STRUCTURE_WORK`：执行所选 mode 的普通结构工作；
- `DATA_PRECONDITION_CHECK_ONLY`：发布后数据前提检查覆盖层，不是第四种 mode。它可从任一输入 mode 受理，跳过普通 `DESIGN` / `AUDIT` / `REBUILD` 前置条件，只执行数据前提检查，主状态固定 `DRAFT`，不得升级结构规则、生成 handoff 或作结构因果诊断。

## 3. 主状态

主状态只能取以下五值：

| 状态 | 含义 |
|---|---|
| `DRAFT` | 正在设计、重构、修复审查失败，或仅完成数据前提检查 |
| `NEEDS_KODA_DECISION` | 至少一个必须由 Koda 决定的候选尚未确认 |
| `READY_FOR_KODA_APPROVAL` | `AUDIT` 三轮均独立复核通过、blockers 为空，等待 Koda 对最终结构作明确批准 |
| `APPROVED_FOR_HANDOFF` | 三轮均通过、blockers 为空、包装已 `LOCKED`，且存在 Koda 明确批准事件 |
| `REJECTED` | 仅在存在 Koda 明确拒绝事件时使用 |

`DESIGN` 和 `REBUILD` 不得直接输出 `READY_FOR_KODA_APPROVAL` 或 `APPROVED_FOR_HANDOFF`。只有 `AUDIT` 持有这两个状态的判定权。

## 4. blockers[]

`blockers[]` 与主状态独立，可同时存在多个，按以下顺序排列：

1. `PACKAGING_CONFLICT`：包装承诺与已确认事实冲突；事实优先。
2. `FACT_UNVERIFIED`：核心主张或 Koda 个人事实未核实。
3. `EVIDENCE_GAP`：核心主张或必须保留的主要章节缺少可计入门槛的 `PROOF`。若无证据内容只是可直接删除且不影响主线的填充章节，`AUDIT` 应判相应审查轮 `FAIL` 并提出删除路径，不必把可删除填充复用为 `EVIDENCE_GAP`。
4. `MULTI_TASK`：同时存在多个主要频道任务，且尚未删减或拆分。
5. `NO_PAYOFF`：尚无可用 payoff，候选也无法被当前资料支持。`RETURNING_VIEWER` 下存在可支持的 `RELATIONSHIP_IDENTITY` 候选时不触发该 blocker，仍进入 `NEEDS_KODA_DECISION`。
6. `PACKAGING_MISSING`：在 payoff 与核心判断已明确后，仍无法形成一个真实、可检验的包装假设。

发布后分析数据缺失不属于 `EVIDENCE_GAP`；写入 `missing_data[]`，相关结论输出 `UNDETERMINED`。

blocker 不等于拒绝。Skill 必须先给修复路径；`REJECTED` 只由 Koda 的明确决定触发。

## 5. 其他固定枚举

- 主要任务：`SEARCH_ACQUISITION`、`RECOMMENDATION_EXPANSION`、`RETURNING_VIEWER`
- 包装状态：`HYPOTHESIS`、`LOCKED`
- 视频类型：`PUBLIC_EXPERIMENT`、`EDUCATIONAL`、`COMMENTARY`
- 支持级别：`PREREGISTRATION_ONLY`、`MVP_FULL`
- 操作范围：`STRUCTURE_WORK`、`DATA_PRECONDITION_CHECK_ONLY`
- Section Card 组织方式：`STP`、`PEIL`、`VALUE_LOOP`、`PLAIN`
- 主张类型：`FACT`、`INFERENCE`、`KODA_VIEW`、`NEEDS_VERIFICATION`、`USER_CONFIRM_REQUIRED`
- 证据角色：`PROOF`、`ILLUSTRATION`
- 审查轮结果：`PASS`、`FAIL`、`NOT_RUN`
- 数据结论：`UNDETERMINED`
- 缺失信息标记：`UNCONFIRMED`、`SETUP_REQUIRED`
- 候选选择状态（payoff / core judgment）：`CANDIDATE`、`KODA_SELECTED`
- payoff 类型：`UNDERSTANDING`、`JUDGMENT`、`DECISION`、`ACTION`、`RELATIONSHIP_IDENTITY`
- 事实状态：`CONFIRMED`、`HISTORICAL_BASELINE_RECHECK_REQUIRED`、`UNCONFIRMED`
- 决策事件：`PAYOFF_SELECTED`、`CORE_JUDGMENT_SELECTED`、`PACKAGING_LOCKED`、`STRUCTURE_APPROVED`、`PERSONAL_FACT_CONFIRMED`、`VIDEO_REJECTED`
- 假设登记状态：`PREREGISTERED`

不得临时创造同义枚举。

## 6. 来源优先级

1. 当前 task packet 中的明确用户指令；
2. 当前轮 Koda 明确确认、选择、锁定、批准或拒绝事件；
3. `01_koda_channel_contract.md` 与 `04_koda_facts.md`；
4. 用户为当前视频提供的原始资料；
5. 有 `source_ref` 和 `retrieved_date` 的外部来源；
6. 明确标注的 `INFERENCE`。

聊天记忆、模型常识、未落盘的旧数据，不得作为 Koda 事实或 Koda 观点。

输入中的自报审查结论不属于来源优先级：`review_rounds`、`review_inputs_complete`、`structure_summary` 只能作为待复核提示，不能证明合规。

## 7. SETUP_REQUIRED 处理

四个 setup 文件随 Skill 提供，但频道定位、受众、语音样本和个人事实仍可能为 `UNCONFIRMED`。若当前 task packet 已提供完成本次任务所需的信息，Skill 可以运行；否则：

- 主状态为 `DRAFT` 或 `NEEDS_KODA_DECISION`；
- 在 `setup_requirements[]` 中使用稳定来源前缀与缺失字段路径逐项标记 `SETUP_REQUIRED`，例如 `CHANNEL_CONTRACT:channel_positioning`、`AUDIENCE_MAP:who`、`VOICE_BOUNDARIES:approved_longform_samples`、`FACT_LEDGER:<fact_id>`；
- 若缺失直接影响事实或证据，再加入 `FACT_UNVERIFIED` 或 `EVIDENCE_GAP`；
- 不得以模型记忆填补。

## 8. 确定性边界

相同输入与相同 Skill 版本下，模式、operation scope、路由、状态、blockers、组织方式约束和审批边界应保持一致；自然语言表述允许变化。
