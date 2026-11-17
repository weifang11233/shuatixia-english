# shuatixia-english · 小小刷题家 · 英语单元卷

外研版（三起）六年级上册英语单元测验的生成与题库转换脚本。

## 目录

| 路径 | 说明 |
|---|---|
| `英语单元卷/build_unit1.py` | Unit 1 测验生成器（47 小题 / 100 分：语音 5 · 词汇 10 · 单选 10 · 词形 5 · 连词成句 4 · 补全对话 5 · 阅读 7 · 写作 1） |
| `英语单元卷/to_bank.py` | 47 题转题库条目（题型映射 + chapter 打 `Unit1` 前缀） |
| `英语单元卷/六上全册/render.py` | 六上全册试卷渲染 |

## 口径

- A4 版式 6 页（试卷 4 + 答案 2）；听力音频 edge-tts en-GB
- 坑位记录：quiz-generator assemble 模式 assign_scores 全局均分需自控分；`<u>` 父容器禁 flex
