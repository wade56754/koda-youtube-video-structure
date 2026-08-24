# Router, Payoff, Core Judgment, and Packaging

## 1. 路由决胜顺序

严格按以下顺序判断，命中后停止向下竞争：

1. **预注册实验**：任务明确要在执行前登记基线、假设、规则、指标、数据窗口或干扰因素。输出 `video_type=PUBLIC_EXPERIMENT`、`support_level=PREREGISTRATION_ONLY`，只使用季初预注册模板。
2. **教学动作**：主要承诺是观众看完能完成一个可执行动作、流程或操作结果。输出 `video_type=EDUCATIONAL`、`support_level=MVP_FULL`。
3. **观点**：主要承诺是改变理解、判断或决策，并需要立场、证据、反方与限定。输出 `video_type=COMMENTARY`、`support_level=MVP_FULL`。

若同一题同时包含实验与教程，预注册实验优先；若同时包含教程与观点，以“观众看完主要要做什么”决胜。Koda 可以改判，但必须记录改判理由。

不得为 Commentary 的个人证据用法创建新的视频类型枚举。正确表示是：

```text
video_type: COMMENTARY
personal_evidence: true
```

仅当至少一项已核实的 Koda 经历在结构中承担证据角色时，`personal_evidence=true`。

## 2. 主要任务检查

只允许：`SEARCH_ACQUISITION`、`RECOMMENDATION_EXPANSION`、`RETURNING_VIEWER`。

- 多个素材、经历或章节可以共同服务一个主要任务和一个公共命题，不构成 `MULTI_TASK`。
- 两个以上互不从属的主要任务，或两个以上互不从属的 payoff，加入 `MULTI_TASK`。
- Skill 应先提出删减或拆分方案，不得自动拒绝。

## 3. payoff 流程

顺序固定：

1. 从受众处境和题材生成 1 个主候选，最多 2 个备选；
2. 标明 payoff 类型：`UNDERSTANDING`、`JUDGMENT`、`DECISION`、`ACTION`，或受限的 `RELATIONSHIP_IDENTITY`；
3. 说明每个候选会改变观众什么；
4. 由 Koda 明确选择；
5. 未选择时使用 `NEEDS_KODA_DECISION`；
6. 当前资料连可信候选都无法支持时，加入 `NO_PAYOFF`；
7. 只有 Koda 明确决定不做，才使用 `REJECTED`。

`RELATIONSHIP_IDENTITY` 只在 `RETURNING_VIEWER` 下允许，并须 Koda 明确签署。纯“了解近况”不能自动通过。只要当前资料足以支持一个可信的 `RELATIONSHIP_IDENTITY` 候选，等待 Koda 选择时使用 `NEEDS_KODA_DECISION` 且不触发 `NO_PAYOFF`；只有连允许类型的可信候选都无法形成时才加入 `NO_PAYOFF`。

## 4. 个人经历公共命题化

当输入以个人经历为主时，先逐项列出：

- 该经历能证明的公共问题候选；
- 该经历是 `PROOF`、`ILLUSTRATION`，还是目前不能使用；
- 哪些经历只是时间线信息；
- 哪个公共命题能统摄多个主题。

若无法提炼公共命题：

- `RETURNING_VIEWER` 可提出关系 / 身份回报候选并进入 `NEEDS_KODA_DECISION`；
- 其他主要任务加入 `NO_PAYOFF`；
- 不得直接写成个人时间线大纲。

## 5. 纯否定命题检查

类似“最大问题不是 X”“不要做 Y”“X 不成立”的句子，如果只排除错误答案、没有说明真正成立的判断，只能作为选题方向。

Skill 必须：

1. 保留原否定方向；
2. 生成 1—3 个肯定式、可证伪、可绑定证据的核心判断候选；
3. 不替 Koda 选定；
4. 主状态设为 `NEEDS_KODA_DECISION`；
5. 在 Koda 选择前，不用候选推进正式审查。

## 6. 包装双段门

包装状态只有：

- `HYPOTHESIS`：真实、可检验的工作标题与缩略图承诺。允许进入 `DRAFT` 结构，并可因结构或证据变化而修改。
- `LOCKED`：Koda 明确锁定，事实核查通过。只有该状态才可能进入 `APPROVED_FOR_HANDOFF`。

包装必须包含：

- 工作标题或锁定标题；
- 缩略图承诺；
- 二者分工；
- 点击时的观众预期；
- 前 30 秒兑现要求；
- `source_ref` 或事实依据。

包装不是单向门。结构工作发现 payoff、核心判断或事实不支持包装时，应回退到 `HYPOTHESIS` 并修改。

### 事实冲突优先

- 与已确认事实冲突：加入 `PACKAGING_CONFLICT`，不得锁定或交接。
- 事实本身未核实：加入 `FACT_UNVERIFIED`，不得用更强措辞补足。
- 缺少包装但足以生成候选：先生成 `HYPOTHESIS`，不必阻断所有结构工作。
- payoff 与核心判断明确后仍无法形成真实包装：加入 `PACKAGING_MISSING`。
