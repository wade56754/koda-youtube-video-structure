# koda-youtube-video-structure

## 用途

在完整逐字稿之前，使用 `DESIGN`、`AUDIT` 或 `REBUILD` 生成和审查 YouTube 长视频 `structure_packet`。v0.1.1 不包含 JSON Schema、Python 校验器、完整 Public Experiment 成片结构、Case Study、Trend Judgment 或 `RETENTION_REVIEW`。

## 安装

将根目录 `koda-youtube-video-structure` 解压到以下任一路径，然后重启 Codex：

```text
~/.codex/skills/
$REPO_ROOT/.agents/skills/
```

## 最短调用例

```text
使用 $koda-youtube-video-structure，mode=DESIGN。
选题：如何用 AI 完成一条 YouTube 视频。
主要任务：SEARCH_ACQUISITION。
只输出结构包，不写完整逐字稿；未知事实标记 UNCONFIRMED。
```

## 验证命令

在 Skill 根目录运行；该目录本身必须是已执行 `git init` 的真实 Git 仓库根目录。原样执行整段命令：

```bash
test -f SKILL.md \
  && test -f agents/openai.yaml \
  && test "$(find tests/fixtures -type f -name '*.yaml' | wc -l | tr -d ' ')" -eq 18 \
  && ! find . -path ./.git -prune -o -type d -empty -print | grep --exclude-dir=.git -q . \
  && ! grep -RInE --exclude-dir=.git 'BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|sk-[A-Za-z0-9]{20,}' .
```

行为验收按 `tests/acceptance_protocol.md` 执行。
