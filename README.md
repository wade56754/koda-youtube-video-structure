# koda-youtube-video-structure

## 用途

在完整逐字稿之前，使用 `DESIGN`、`AUDIT` 或 `REBUILD` 设计和审查 YouTube 长视频结构。v0.2.0 默认先判断题材与主题，再比较候选结构，解释结构的作用和可核查来源，最后输出普通创作者能继续使用的逐字稿大纲。

内部仍保留可审计的结构包，但只有用户明确要求“技术包、审计详情或 debug”时才展示。v0.2.0 不包含完整长视频逐字稿、完整 Public Experiment 结果片、Case Study、Trend Judgment 或 `RETENTION_REVIEW`，也不得代替 Koda 批准。

## 安装

将根目录 `koda-youtube-video-structure` 解压到以下任一路径，然后重启 Codex：

```text
~/.codex/skills/
$REPO_ROOT/.agents/skills/
```

## 最短调用例

```text
使用 $koda-youtube-video-structure，帮我设计“如何用 AI 完成一条 YouTube 视频”的结构。
先用普通中文说明题材、主题和目标观众，比较最相关的候选结构及来源，
再给逐字稿大纲。不要完整逐字稿；未知事实直接说还需要补充什么。
```

## 验证命令

在 Skill 根目录运行；该目录本身必须是已执行 `git init` 的真实 Git 仓库根目录。原样执行整段命令：

```bash
test -f SKILL.md \
  && test -f agents/openai.yaml \
  && test "$(find tests/fixtures -type f -name '*.yaml' | wc -l | tr -d ' ')" -eq 19 \
  && ! find . -path ./.git -prune -o -type d -empty -print | grep --exclude-dir=.git -q . \
  && ! grep -RInE --exclude-dir=.git 'BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|sk-[A-Za-z0-9]{20,}' .

python3 -m unittest discover -s tests -p 'test_*.py' -v
```

行为验收按 `tests/acceptance_protocol.md` 执行。
