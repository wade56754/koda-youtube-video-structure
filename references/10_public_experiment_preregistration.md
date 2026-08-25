# Public Experiment Preregistration — v0.2.0

## 使用边界

仅用于实验执行前的季初预注册。`video_type=PUBLIC_EXPERIMENT`、`support_level=PREREGISTRATION_ONLY`。本模板不生成实验完成后的成片结构，也不声称任何指标已验证某种结构规律。

命中该路由后，普通 DESIGN 的公共命题化、payoff、包装、Hook 与 Section Card 步骤不执行；只生成下列预注册包。

## 预注册模板

```text
skill_version: 0.2.0
mode: DESIGN
operation_scope: STRUCTURE_WORK
status: DRAFT
blockers: []
setup_requirements: []

video_type: PUBLIC_EXPERIMENT
support_level: PREREGISTRATION_ONLY
personal_evidence: false

experiment_id:
registration_date:
owner: Koda
registration_status: PREREGISTERED

current_baseline:
  metric:
  value:
  measurement_window:
  source_ref:
  status: CONFIRMED | UNCONFIRMED

experiment_question:
viewer_relevance:
primary_hypothesis:
null_or_alternative_explanation:

rules_and_constraints:
  -

success_metrics:
  primary_metric:
  secondary_metrics:
  comparison_group_or_baseline:
  decision_rule:

data_window:
reporting_dates:

confounders_to_log:
  -

structure_hypothesis:
  hypothesis_id:
  structure_variable:
  expected_observable_signal:
  required_data:

facts_and_sources:
  - claim:
    source_ref:
    retrieved_date:

koda_decisions_required:
  -
```

## 硬性规则

- 基线、规则、指标、数据窗口和判断标准必须在执行前登记；
- 未确认基线标记 `UNCONFIRMED` / `SETUP_REQUIRED`，不得补造；
- 不得事后修改成功标准而不记录变更事件；
- 播放量不能单独宣布成功；
- 结果解释必须区分数据事实、可能解释、干扰因素和不能确认；
- 完整 Public Experiment 结果片结构延后，不在 v0.2.0 假装实现。
