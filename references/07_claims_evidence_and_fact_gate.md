# Claims, Evidence, and Fact Gate

## 1. 最小 claim map

v0.1.1 每个核心主张只记录：

```text
claim:
claim_type:
evidence:
  role: PROOF | ILLUSTRATION
  proof:
  source_ref:
  retrieved_date:
```

`confidence` 与独立 `visual_proof` 字段延后到 v0.2，不在本版本添加。

## 2. 主张类型

- `FACT`：可由来源直接核对；
- `INFERENCE`：从已陈述前提推导，不得冒充事实；
- `KODA_VIEW`：Koda 明确选择或批准的观点；
- `NEEDS_VERIFICATION`：外部事实尚未核查；
- `USER_CONFIRM_REQUIRED`：个人事实、感受或立场需要 Koda 确认。

## 3. 证据角色

- `PROOF`：直接支持主张，计入章节证据门槛；
- `ILLUSTRATION`：帮助理解，但不能证明主张，不计入门槛。

比喻、假设性例子、类比和装饰性案例默认为 `ILLUSTRATION`，除非它们本身提供可核对事实并直接支持主张。

## 4. 来源与时效

- Koda 个人事实：只能引用 `04_koda_facts.md` 的 `fact_id` 或当前轮明确确认事件；
- 外部事实：必须有稳定 `source_ref` 与 `retrieved_date`；
- 当前数据：不能用历史基线替代；
- 历史数据：必须明确标记时间范围与复核要求；
- 没有来源的数字、经历、收入、感受或频道状态：标记 `UNCONFIRMED`，必要时加入 `FACT_UNVERIFIED`。

## 5. 核心证据门

- 每个核心主张至少一个 `PROOF`；
- 每个主要章节至少一个 `PROOF`，唯一纯逻辑推演章节除外；
- `ILLUSTRATION` 不能把证据覆盖率变成通过；
- 没有 `PROOF` 时，删除、合并、限定主张，或加入 `EVIDENCE_GAP`；
- 为了目标时长不得保留无证据章节。

## 6. 纯逻辑推演上限

每条视频至多一个纯逻辑推演章节，并且必须同时满足：

1. `claim_type=INFERENCE`；
2. 明确列出推演所依赖的前提；
3. 不独立承载核心判断；
4. 不被描述为数据事实；
5. 其余主要章节仍由 `PROOF` 支撑。

出现两个或以上纯逻辑章节时，加入 `EVIDENCE_GAP`，并删除、合并或补充证明。

## 7. 绝对化主张

包含“所有、一定、必然、永远、完全”等绝对量词的主张，若现有证据无法覆盖该范围：

- 不得原样登记为 `KODA_VIEW` 或 `FACT`；
- 提出缩小范围、增加条件或改为概率性判断的候选；
- 需要 Koda 选择时使用 `NEEDS_KODA_DECISION`；
- 缺证据时加入 `EVIDENCE_GAP`。

## 8. 包装事实门

包装中的每个事实性承诺都必须在 claim map 中有来源。传播力不能覆盖事实冲突：

- 已确认事实与包装冲突：`PACKAGING_CONFLICT`；
- 事实尚未确认：`FACT_UNVERIFIED`；
- 不得用更强、更绝对的标题替代缺失证据。
