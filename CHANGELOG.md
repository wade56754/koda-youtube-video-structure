# Changelog

## 0.1.1 — 2026-08-25

- 保持 `DESIGN`、`AUDIT`、`REBUILD` 三种模式及既有五主状态、六类 blockers、双段包装门和证据门不变。
- 明确 `AUDIT` 为只读独立复核：输入中的 `review_rounds` 与 `review_inputs_complete` 均非权威，失败时输出修复路径而不自行改写。
- 将 `DATA_PRECONDITION_CHECK_ONLY` 定义为可覆盖任一输入 mode 的 operation-scope 层；缺数据进入 `missing_data[]` 与 `UNDETERMINED`，不复用 `EVIDENCE_GAP`。
- 补齐 AUDIT / task packet 输入键与权威边界；Public Experiment 命中后只生成预注册包。
- 修正 fixtures 06、07、08、12，并新增自报 PASS 违规、setup 缺失、稻草人反方三项对抗测试。
- 行为验收 fixtures 精确增加到 18 个。
- 修复 README 在真实 Git 仓库中的空目录与 grep 验证边界。
