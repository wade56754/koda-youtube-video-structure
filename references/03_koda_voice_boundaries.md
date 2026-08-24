# Koda Voice Boundaries — Minimal Bootstrap

## 当前状态

- Koda 已认可的长视频口播样本：`UNCONFIRMED` / `SETUP_REQUIRED`
- 可稳定复用的句式偏好：`UNCONFIRMED` / `SETUP_REQUIRED`
- 明确禁用表达清单：`UNCONFIRMED` / `SETUP_REQUIRED`
- 已确认的镜头表达、节奏与视觉语法：`UNCONFIRMED` / `SETUP_REQUIRED`

## 在样本缺失时允许做什么

- 使用简体中文、清晰、克制的编辑语言输出结构包；
- 区分“候选表达方向”与“Koda 已确认表达”；
- 记录每一处需要 Koda 提供原话、感受或立场的位置；
- 用章节功能、观众问题和证据位置描述结构，不代写完整口播。

## 禁止做什么

- 不得声称“这就是 Koda 的语气”；
- 不得仿写不存在的个人口头禅；
- 不得把模型生成的判断登记为 `KODA_VIEW`；
- 不得为了情绪强度虚构经历、数据、冲突或感受；
- 不得因为没有语音样本而拒绝结构工作，只能把语音相关项标记 `SETUP_REQUIRED`。

## Koda 补充语音资料时的最小格式

每个样本至少记录：

- `sample_id`
- `source_ref`
- `approved_by_koda`
- `approved_date`
- `accepted_traits`
- `rejected_traits`
- `allowed_scope`（结构说明 / 标题候选 / 口播句式）

未满足这些字段的材料只能作为阅读资料，不能升级为稳定语音规则。
