# Video Patterns and Section Cards

## 1. Commentary — MVP_FULL

适用：反常识观点、常见说法的反驳、创作者判断、个人经历证明公共观点。

母结构候选：

```text
流行说法或公共问题
→ Koda 已确认的立场
→ 第一组 PROOF
→ 第二组 PROOF 或边界证据
→ 真实、最强反方
→ 反方哪部分成立
→ 修正、限定或深化后的判断
→ 观众可迁移的方法或判断
→ 下一条自然承接
```

要求：

- 有一个清晰公共问题和一个核心判断；
- 核心判断必须是 Koda 已选择或批准的，不由 Skill 补造；
- 反方应是目标观众或可信反对者真实会提出的主张，不得造稻草人；
- 必须回答“反方哪部分成立”；
- 结论应被证据修正、限定或深化，而不是机械重复开头；
- 个人经历只作为证据，`personal_evidence=true` 时仍不能用时间线替代公共命题。

## 2. Educational — MVP_FULL

适用：观众看完要完成一个具体动作、流程、操作或工作结果。

母结构候选：

```text
问题钩子
→ 成品 / 结果预览
→ 看完能完成什么
→ 前置条件
→ 3—5 个步骤
→ 每步例子、演示或项目证据
→ 常见错误
→ 最终结果
→ 下一课
```

要求：

- 尽早展示结果或工作流全貌；
- 每一步至少有一个 `PROOF`，例如真实操作、屏幕结果、项目文件或可靠事实；
- 不强制最强反方；
- 不写成工具清单；
- 观众看完应能执行一个明确动作。

## 3. Public Experiment — PREREGISTRATION_ONLY

MVP 只登记季初实验，不产出完整结果片母结构，也不声称已被频道数据验证。使用 `10_public_experiment_preregistration.md`。

## 4. 延后能力

`CASE_STUDY`、`TREND_JUDGMENT`、完整 `PUBLIC_EXPERIMENT` 结果片与 `RETENTION_REVIEW` 均不在 v0.1.1。遇到此类请求不得强行套进 Commentary 或 Educational；只说明延后边界，并在当前可做范围内提供 setup 或资料清单。

## 5. Section Card

每个章节必须选择且只选择一种内部组织方式：

- `STP`：Setup → Tension → Payoff。Commentary 的常用默认，但只有存在真实未解决问题时才使用 Tension。
- `PEIL`：Point → Explain → Illustrate → Lesson。Educational 的常用默认。
- `VALUE_LOOP`：Context → Application → Framing。适合把知识放入使用情境。
- `PLAIN`：直接陈述功能、证据和回报，不强造悬念。

禁止在同一 Section Card 内叠加两套或以上组织方式。

### 固定字段

```text
section_id:
section_function:
viewer_question:
organization: STP | PEIL | VALUE_LOOP | PLAIN
organization_fields:
core_claim:
claim_type:
evidence_items:
relation_to_previous:
transition_to_next:
estimated_duration_range:
delete_condition:
```

`organization_fields` 只填写所选方式对应的字段：

- STP：`setup` / `tension` / `payoff`
- PEIL：`point` / `explain` / `illustrate` / `lesson`
- VALUE_LOOP：`context` / `application` / `framing`
- PLAIN：`content` / `takeaway`

## 6. 章节推进与删除

每章只承担一个主要功能：暴露问题、推翻旧解释、提供证据、建立模型、处理反方、给出应用、说明边界或打开下一步。

相邻章节必须存在可说明的关系：原因、结果、矛盾、升级、证明、反驳、应用或边界。

以下情况必须给出删除、合并或补证路径；只有核心主张或必须保留的章节仍缺 `PROOF` 时才加入 `EVIDENCE_GAP`：

- 章节没有新的观众回报；
- 章节没有 `PROOF`，且不属于唯一允许的纯逻辑推演章节；
- 章节只为满足目标时长存在；
- 章节与主要任务或核心判断无关。

相邻两个章节都没有具体案例、数据、操作结果或画面可验证材料时，标记为“连续抽象风险”。这是待频道验证的结构假设，不得声称会导致流失。

`AUDIT` 只报告问题与修复路径，不得直接删除或合并输入结构。若无证据章节只是可移除的时长填充，Round 3 判 `FAIL`、状态保持 `DRAFT`，提出删除路径；在修订结构重新提交前不得宣告 `READY_FOR_KODA_APPROVAL`。

## 7. 前 30 秒计划

结构包只写开头结构，不写完整逐字稿：

- `0–8 秒`：对齐标题与缩略图的核心承诺；
- `8–20 秒`：明确观众能获得什么；
- `20–30 秒`：说明为什么值得继续，并安排首个真实证明的出现位置。

三段时间切分是工程组织方式，不是统一留存定律。禁止自我介绍、频道片头、空洞宏大背景、与标题无关铺垫、未经证实冲突和机械念目录。
