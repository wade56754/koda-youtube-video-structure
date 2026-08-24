# Koda Channel Contract — Minimal Bootstrap

## 已由冻结输入支持的合同

| 项目 | 值 | 状态 | 来源 |
|---|---|---|---|
| 默认输出语言 | 简体中文 | CONFIRMED | 冻结 PRD 元信息 |
| Skill 职责 | 完整逐字稿之前的编辑判断层 | CONFIRMED | 冻结 PRD 第一章 |
| 最终审批人 | Koda | CONFIRMED | 冻结 PRD 目标用户与 NFR-05 |
| AI 职责 | 分类、候选生成、逻辑检查、证据位置、风险识别、版本比较 | CONFIRMED | 冻结 PRD 原则七 |
| Koda 职责 | 决定 payoff、核心判断、包装、个人事实与最终结构 | CONFIRMED | 冻结 PRD 原则七与 NFR-05 |
| 主要任务枚举 | SEARCH_ACQUISITION / RECOMMENDATION_EXPANSION / RETURNING_VIEWER | CONFIRMED | 冻结 PRD 原则三 |
| 证据优先方向 | 自有后台数据与案例优先于外部研究与逻辑推演 | CONFIRMED | 冻结 PRD 原则六 |
| 反填充规则 | 无证明的主要章节删除、合并或阻塞；目标时长不构成保留理由 | CONFIRMED | 冻结 PRD 风险五与 AC-05 |

## 频道层信息

以下信息未在三份冻结输入中形成可直接落盘的正式频道合同：

| 项目 | 当前值 | 状态 |
|---|---|---|
| 频道一句话定位 | UNCONFIRMED | SETUP_REQUIRED |
| 频道使命 | UNCONFIRMED | SETUP_REQUIRED |
| 核心目标受众 | UNCONFIRMED | SETUP_REQUIRED |
| 内容支柱及优先级 | UNCONFIRMED | SETUP_REQUIRED |
| 第一季可公开承诺 | UNCONFIRMED | SETUP_REQUIRED |
| 禁止或暂缓的主题 | UNCONFIRMED | SETUP_REQUIRED |
| 频道层下一条承接策略 | UNCONFIRMED | SETUP_REQUIRED |

## 最小运行规则

频道层信息未补齐时，只要当前 task packet 明确提供以下内容，本 Skill 仍可处理单条视频：

- 一个主要任务；
- 具体受众处境；
- payoff 或足够生成候选的信息；
- 核心判断方向；
- 包装信息或足够生成真实包装假设的信息；
- 相关事实与 `source_ref`；
- Koda 个人事实所引用的台账 ID 或当前轮明确确认事件。

缺少其中任何一项时，按 `00_runtime_contract.md` 输出 `SETUP_REQUIRED`，不得猜测频道层默认值。
