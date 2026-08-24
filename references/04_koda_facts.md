# Koda Facts Ledger — Minimal Bootstrap

## 初始状态

本 Skill 的冻结输入没有提供可直接登记为“已批准个人事实”的完整确认事件，因此初始台账中没有可供视频引用的 Koda 个人事实。该缺失是有意的事实保护，不得用聊天记忆填补。

当前状态：`UNCONFIRMED` / `SETUP_REQUIRED`。

## 台账格式

新增任何事实时，必须使用一行记录：

| 字段 | 要求 |
|---|---|
| `fact_id` | 稳定 ID，不随改写变化 |
| `claim` | 可逐字核对的完整事实主张 |
| `status` | `CONFIRMED`、`HISTORICAL_BASELINE_RECHECK_REQUIRED` 或 `UNCONFIRMED` |
| `source_ref` | 正式项目文件、当前轮明确确认事件或原始后台数据 |
| `confirmation_event` | 谁在何处明确确认；没有则写 `NOT_PROVIDED` |
| `confirmed_date` | `YYYY-MM-DD`；没有则写 `NOT_PROVIDED` |
| `recheck_rule` | 拍摄前是否必须复核，以及复核条件 |
| `allowed_uses` | 可用于哪些视频或主张 |

## 使用规则

1. 只有 `CONFIRMED` 且在 `allowed_uses` 范围内的事实，可以作为 `FACT` 或 Koda 个人 `PROOF`。
2. `HISTORICAL_BASELINE_RECHECK_REQUIRED` 只能以“历史基线”表述，并在拍摄前复核；不得冒充当前数据。
3. `UNCONFIRMED` 不能进入标题、缩略图、核心判断或主要证据。
4. 当前轮 Koda 明确确认可临时使用，但 structure packet 必须保存其 `source_ref`，并要求后续落盘。
5. Koda 的感受、判断与事实分开登记。个人观点必须有 Koda 选择或批准事件，不能由模型从经历推断。
6. 外部事实不写入本文件；按 `07_claims_evidence_and_fact_gate.md` 记录 `source_ref` 与 `retrieved_date`。
