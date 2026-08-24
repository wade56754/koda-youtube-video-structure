# Audience and Content Map — Minimal Bootstrap

## 频道级受众

频道级默认受众尚未由冻结输入确认：`UNCONFIRMED`。在 Koda 补充正式受众地图前，不得从题材、平台或旧记忆推断年龄、职业、收入、地区、熟练度或购买意图。

## 每条视频必须提供的受众地图

当前 task packet 必须描述：

| 字段 | 必须回答的问题 |
|---|---|
| `who` | 这条视频具体写给哪类处境中的人，而不是宽泛人口标签 |
| `current_situation` | 他点击前正在做什么、卡在哪里 |
| `problem` | 他试图解决的单一主要问题 |
| `desired_change` | 看完后理解、判断、决策、行动，或经 Koda 签署的关系/身份回报发生什么变化 |
| `source_ref` | 该受众判断来自哪里：当前用户指令、用户研究、评论、搜索需求或其他正式来源 |
| `status` | `CONFIRMED`、`UNCONFIRMED` 或 `SETUP_REQUIRED` |

若 `who`、`current_situation`、`problem`、`desired_change` 中任一项无法从当前输入支持，标记 `UNCONFIRMED`，并把对应信息列入 `setup_requirements[]`。

## 内容与主要任务

主要任务只允许一个：

- `SEARCH_ACQUISITION`：解决明确、可搜索的问题；
- `RECOMMENDATION_EXPANSION`：用观点或问题扩大新观众；
- `RETURNING_VIEWER`：强化连续观看、信任或频道关系。

多个主题不等于多个主要任务。只有当内容同时试图完成两个或以上主要任务，或存在两个互不从属的 payoff，才加入 `MULTI_TASK`。

## RETURNING_VIEWER 的关系 / 身份回报

默认仍优先要求认知或行动回报。只有在 `primary_goal=RETURNING_VIEWER` 时，Skill 才能提出 `RELATIONSHIP_IDENTITY` payoff 候选，并必须：

1. 标记为候选；
2. 说明为什么无法提炼更强的公共认知回报；
3. 要求 Koda 明确选择；
4. 在选择前保持 `NEEDS_KODA_DECISION`；
5. 不把“了解近况”自动当成足够回报。
