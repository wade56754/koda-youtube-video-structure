# Changelog

## 0.2.0 — 2026-08-25

- DESIGN / REBUILD 改为先识别题材、提炼主题和观看回报，再比较候选结构并选择结构。
- 为观点论证型、行动教学型、执行前实验登记型及四种章节组织方式增加可审计来源卡，明确区分外部理论、方法改编和项目规则。
- 默认输出改为四段小白版创作说明；内部审计包只在明确要求技术包、审计详情或 debug 时展示。
- 新增可交给下游写作者继续工作的逐字稿大纲，同时保持不生成完整长视频逐字稿、不代替 Koda 审批和不绕过 handoff 的边界。
- 新增分享对话回归 fixture、golden contract tests 和公开仓库 CI；行为验收 fixtures 增加到 19 个。
- 默认创作者视图进一步禁止泄露内部状态、证据角色和交接英文词，并要求改写成普通中文。
- 默认结构来源必须给出可点击的完整网址；创作者视图不再叙述仓库、分支、模式或状态码。

## 0.1.1 — 2026-08-25

- 保持 `DESIGN`、`AUDIT`、`REBUILD` 三种模式及既有五主状态、六类 blockers、双段包装门和证据门不变。
- 明确 `AUDIT` 为只读独立复核：输入中的 `review_rounds` 与 `review_inputs_complete` 均非权威，失败时输出修复路径而不自行改写。
- 将 `DATA_PRECONDITION_CHECK_ONLY` 定义为可覆盖任一输入 mode 的 operation-scope 层；缺数据进入 `missing_data[]` 与 `UNDETERMINED`，不复用 `EVIDENCE_GAP`。
- 补齐 AUDIT / task packet 输入键与权威边界；Public Experiment 命中后只生成预注册包。
- 修正 fixtures 06、07、08、12，并新增自报 PASS 违规、setup 缺失、稻草人反方三项对抗测试。
- 行为验收 fixtures 精确增加到 18 个。
- 修复 README 在真实 Git 仓库中的空目录与 grep 验证边界。
