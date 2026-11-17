#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 Unit 1 单元卷（47 小题）转成小小刷题家的题库格式，追加进 build-banks.js 的英语库。

题型映射（应用只支持 single / multiple / judge / fill / solve 五类）：
  一、语音 5 题        -> single   （四个单词，划线字母以（cr）/（cl）标注）
  二A、词汇中译英 5 题 -> fill
  二B、选出不同类 5 题 -> single
  三、单项选择 10 题   -> single
  四、词形填空 5 题    -> fill
  五、连词成句 4 题    -> fill     （文本判分会忽略大小写/空格/标点）
  六、补全对话 5 空    -> single   （每空 4 个候选句，从原方框里取）
  七A、阅读判断 4 题   -> judge    （对/错）
  七B、阅读选择 3 题   -> single
  八、书面表达 1 题    -> solve    （主观题，答案存范文）
"""
import os

CH_SOUND = "Unit1 语音 cr/cl"
CH_WORD = "Unit1 词汇"
CH_CHOICE = "Unit1 单项选择"
CH_FORM = "Unit1 词形填空"
CH_ORDER = "Unit1 连词成句"
CH_DLG = "Unit1 补全对话"
CH_READ = "Unit1 阅读理解"
CH_WRITE = "Unit1 书面表达"

Q = []  # (type, stem, options, answer, explanation, chapter)


def add(t, stem, opts, ans, sol, ch):
    Q.append((t, stem, opts, ans, sol, ch))


# ---------------------------------------------------------------- 一、语音
# 题干里带上本题的四个词，保证题干唯一（题库去重按题干做，题干重复会被误删）
def sound_stem(words):
    return "选出划线部分发音不同的一项：" + " / ".join(words) + "（划线部分是 cr 或 cl）"


add("single", sound_stem(["crayon", "cream", "clang", "cry"]),
    ["crayon（cr）", "cream（cr）", "clang（cl）", "cry（cr）"], "C",
    "clang 中 cl 读 /kl/；crayon、cream、cry 中 cr 读 /kr/。", CH_SOUND)
add("single", sound_stem(["clock", "class", "clean", "cry"]),
    ["clock（cl）", "class（cl）", "clean（cl）", "cry（cr）"], "D",
    "cry 中 cr 读 /kr/；clock、class、clean 中 cl 读 /kl/。", CH_SOUND)
add("single", sound_stem(["clever", "cross", "cloud", "close"]),
    ["clever（cl）", "cross（cr）", "cloud（cl）", "close（cl）"], "B",
    "cross 中 cr 读 /kr/；clever、cloud、close 中 cl 读 /kl/。", CH_SOUND)
add("single", sound_stem(["cream", "clang", "class", "clock"]),
    ["cream（cr）", "clang（cl）", "class（cl）", "clock（cl）"], "A",
    "cream 中 cr 读 /kr/；clang、class、clock 中 cl 读 /kl/。", CH_SOUND)
add("single", sound_stem(["crayon", "clever", "clean", "cloud"]),
    ["crayon（cr）", "clever（cl）", "clean（cl）", "cloud（cl）"], "A",
    "crayon 中 cr 读 /kr/；clever、clean、cloud 中 cl 读 /kl/。", CH_SOUND)

# ---------------------------------------------------------------- 二A、词汇（中译英）
for cn, en in [("储蓄，存（钱）", "save"), ("用（钱），花费", "spend"),
               ("零花钱", "pocket money"), ("店主", "shopkeeper"), ("彩色蜡笔", "crayon")]:
    add("fill", "根据中文提示写出单词：%s" % cn, [], en,
        "本单元核心词：%s = %s。" % (cn, en), CH_WORD)

# ---------------------------------------------------------------- 二B、选出不同类
# 同理：题干写出四个词，保证题干唯一、被去重时不会互相覆盖
def odd_stem(words):
    return "选出不同类的一项：" + " / ".join(words)


add("single", odd_stem(["save", "crayon", "spend", "buy"]), ["save", "crayon", "spend", "buy"], "B",
    "crayon 是名词（蜡笔），其余三个都是动词。", CH_WORD)
add("single", odd_stem(["yuan", "dollar", "pocket", "pound"]), ["yuan", "dollar", "pocket", "pound"], "C",
    "yuan、dollar、pound 是货币单位，pocket 不是（pocket money 才是零花钱）。", CH_WORD)
add("single", odd_stem(["money", "buy", "sell", "share"]), ["money", "buy", "sell", "share"], "A",
    "money 是名词，buy、sell、share 都是动词。", CH_WORD)
add("single", odd_stem(["book", "robot", "ice cream", "shopkeeper"]), ["book", "robot", "ice cream", "shopkeeper"], "D",
    "shopkeeper 指人（店主），其余都是物品。", CH_WORD)
add("single", odd_stem(["happy", "surprised", "sad", "smile"]), ["happy", "surprised", "sad", "smile"], "D",
    "smile 是动词/名词（微笑），其余三个是形容词。", CH_WORD)

# ---------------------------------------------------------------- 三、单项选择
add("single", "— How much ______ the robot? — It's 35 yuan.",
    ["is", "are", "am", "be"], "A",
    "robot 是单数名词，be 动词用 is；答语 It's 也提示了单数。", CH_CHOICE)
add("single", "— How much ______ the cupcakes? — They're eight yuan each.",
    ["is", "are", "be", "has"], "B",
    "cupcakes 是复数，答语用 They're，问句用 are。", CH_CHOICE)
add("single", "Amy always ______ her pocket money in a saving box.",
    ["save", "saves", "saving", "saved"], "B",
    "always 表习惯用一般现在时；主语 Amy 是第三人称单数，动词加 -s。", CH_CHOICE)
add("single", "Sam always ______ his money on toys and ice creams.",
    ["spend", "spends", "spending", "spent"], "B",
    "主语 Sam 为第三人称单数，spend → spends。", CH_CHOICE)
add("single", "— I'll ______ the robot. Here's the money. — Thank you.",
    ["take", "takes", "taking", "took"], "A",
    "I'll = I will，will 后接动词原形 take。", CH_CHOICE)
add("single", "— How much are the ice creams? — ______ eight yuan.",
    ["It's", "They're", "There are", "He's"], "B",
    "ice creams 是复数，答语用 They're。", CH_CHOICE)
add("single", "The old man ______ at King Midas and said, \"Gold isn't everything.\"",
    ["smile", "smiles", "smiled", "smiling"], "C",
    "said 是过去式，and 前后时态一致，前面也用 smiled。", CH_CHOICE)
add("single", "I will save my money ______ the right things.",
    ["to", "for", "at", "of"], "B",
    "固定搭配 save money for sth.，表示为某事存钱。", CH_CHOICE)
add("single", "Everything ______ to gold after Midas made his wish.",
    ["turn", "turns", "turning", "turned"], "D",
    "故事发生在过去用过去式 turned；everything 作主语谓语用单数形式。", CH_CHOICE)
add("single", "— Do you want a golden ______? — Yes, I do. I want to turn everything to gold.",
    ["touch", "smile", "gold", "clang"], "A",
    "golden touch 点金术，是本单元固定短语。", CH_CHOICE)

# ---------------------------------------------------------------- 四、词形填空
add("fill", "用所给词的适当形式填空：Amy ________ (save) her pocket money every week.",
    [], "saves", "every week 表习惯，主语第三人称单数，save → saves。", CH_FORM)
add("fill", "用所给词的适当形式填空：Sam ________ (spend) all his money yesterday.",
    [], "spent", "yesterday 是过去时间状语，spend 的过去式是 spent。", CH_FORM)
add("fill", "用所给词的适当形式填空：Look! The children ________ (buy) books for the children's home.",
    [], "are buying", "Look! 提示此刻正在发生，用现在进行时 are buying。", CH_FORM)
add("fill", "用所给词的适当形式填空：I ________ (take) this robot. It's only 35 yuan.",
    [], "will take", "表示将要做的决定，用 will + 动词原形。", CH_FORM)
add("fill", "用所给词的适当形式填空：King Midas was very ________ (surprise) when his daughter turned to gold.",
    [], "surprised", "修饰人的感受用 -ed 形式的形容词 surprised（感到吃惊的）。", CH_FORM)

# ---------------------------------------------------------------- 五、连词成句
add("fill", "连词成句：is / how much / the / robot / ?", [], "How much is the robot?",
    "疑问词 How much 放句首，is 提到主语 the robot 之前。", CH_ORDER)
add("fill", "连词成句：are / how much / the / cupcakes / ?", [], "How much are the cupcakes?",
    "cupcakes 是复数，be 动词用 are。", CH_ORDER)
add("fill", "连词成句：always / Amy / her / saves / pocket money / .", [], "Amy always saves her pocket money.",
    "主语 + 频度副词 always + 实义动词 saves + 宾语。", CH_ORDER)
add("fill", "连词成句：will / my / I / save / money / for / the / right / things / .",
    [], "I will save my money for the right things.",
    "主语 I + will + 动词原形 save + 宾语 + for 短语。", CH_ORDER)

# ---------------------------------------------------------------- 六、补全对话
DLG = [
    ("Sam 到商店买机器人。Shopkeeper: Good morning. Can I help you? Sam: Yes. (1) ______",
     ["It's 35 yuan.", "How much is the robot?", "They're eight yuan each.", "Here you are."], "B",
     "Sam 想知道价钱，问 How much is the robot?；robot 是单数用 is。"),
    ("Shopkeeper: Good morning. Can I help you? Sam: Yes. How much is the robot? Shopkeeper: (2) ______",
     ["It's 35 yuan.", "I'll take it.", "Here you are.", "They're eight yuan each."], "A",
     "回答单数物品的价钱用 It's 35 yuan.。"),
    ("Sam: That's good. (3) ______ Shopkeeper: Here's your robot.",
     ["Here you are.", "I'll take it.", "It's 35 yuan.", "Thank you."], "B",
     "决定买下用 I'll take it.（我买了）。"),
    ("Shopkeeper: Here's your robot. Sam: (4) ______",
     ["I'll take it.", "Here you are.", "It's 35 yuan.", "How much is the robot?"], "B",
     "把要付的钱递过去说 Here you are.；Here's your robot. 是店主递东西。"),
    ("Sam: Here you are. Shopkeeper: (5) ______ Sam: Goodbye!",
     ["Here you are.", "Thank you.", "It's 35 yuan.", "They're eight yuan each."], "B",
     "收到钱后店主道谢 Thank you.。"),
]
for stem, opts, ans, sol in DLG:
    add("single", "补全对话（商店买机器人）：" + stem, opts, ans, sol, CH_DLG)

# ---------------------------------------------------------------- 七、阅读
PASSAGE_A = ("Sam and Amy are brother and sister. They get pocket money every week. "
             "Amy puts her money in a saving box. She likes buying books for the children's home. "
             "Sam is different. He spends his money on robots and ice creams. "
             "When the School Reading Week comes, Amy has many new books for the children. "
             "But Sam only has two coins. He says, \"I'll save my money for the right things from now on.\""
             "（saving box 存钱罐；children's home 儿童之家）")

READ_A = [
    ("Amy and Sam get pocket money every week.", "true",
     "短文第一句 They get pocket money every week."),
    ("Amy always spends all her money on toys.", "false",
     "Amy 把钱放进 saving box，还买书送给儿童之家，并非全买玩具。"),
    ("Sam buys many new books for the children's home.", "false",
     "买书的是 Amy；Sam 只剩两枚硬币。"),
    ("Sam wants to save his money from now on.", "true",
     "末句 Sam 自己说 I'll save my money for the right things from now on."),
]
for stem, ans, sol in READ_A:
    # 设问必须在短文之前：题库去重只比对题干前 60 字，同一段短文开头会让整组题被判重复
    add("judge", "阅读短文A，判断正误：" + stem + "　【短文A】" + PASSAGE_A,
        ["对", "错"], "A" if ans == "true" else "B",
        sol + ("（正确）" if ans == "true" else "（错误）"), CH_READ)

PASSAGE_B = ("Lily gets 50 yuan pocket money every month. She usually spends some of it on crayons and ice cream. "
             "This month she wants to do something different. Her classmate Xiaoming is ill and stays at home. "
             "Lily buys some books and a box of crayons for him. She also saves 20 yuan in her saving box. "
             "\"I can't buy a big robot now,\" she says with a smile, \"but Xiaoming is happy, and I'm happy, too.\""
             "（ill 生病的；classmate 同学）")

add("single", "阅读短文B，选择正确答案（Lily 每个月得到多少零花钱？）　【短文B】" + PASSAGE_B,
    ["15 yuan", "20 yuan", "50 yuan", "85 yuan"], "C",
    "第一句 gets 50 yuan pocket money every month。", CH_READ)
add("single", "阅读短文B，选择正确答案（Lily 给小明买了什么？）　【短文B】" + PASSAGE_B,
    ["A robot and a cake.", "Some books and a box of crayons.", "Ice cream and a pencil.", "A saving box."], "B",
    "文中 Lily buys some books and a box of crayons for him。", CH_READ)
add("single", "阅读短文B，选择正确答案（下面哪一句是正确的？）　【短文B】" + PASSAGE_B,
    ["Lily spends all her money this month.", "Lily saves 20 yuan this month.",
     "Xiaoming is Lily's brother.", "Lily buys a big robot."], "B",
    "文中 She also saves 20 yuan in her saving box；其余三项都与原文相反。", CH_READ)

# ---------------------------------------------------------------- 八、书面表达
WRITING_SAMPLE = ("I get 30 yuan pocket money every month. I will spend 10 yuan on books and crayons. "
                  "I will save 15 yuan in my saving box for a special day. I will share 5 yuan with people in need. "
                  "I think it is a good plan, and I will do it from now on.")
add("solve",
    "书面表达：以 My Pocket Money Plan 为题，写一段话，说说你打算怎样使用零花钱。"
    "要求：①不少于 5 句话；②用 will 表达打算，spend / save / share 三方面至少写到两方面；③不要出现真实姓名。"
    "提示词：spend ... on ...；save ... for ...；share ... with ...",
    [], WRITING_SAMPLE,
    "主观题：本题没有唯一答案。请先在纸上写，再对照参考范文检查三点——①will 后是否用动词原形；"
    "②有没有 use spend money on sth. / save money for sth. / share sth. with sb. 这三组搭配；"
    "③句数是否够 5 句、拼写与大小写是否正确。应用内无法自动评分，判分结果不作准。", CH_WRITE)

# ---------------------------------------------------------------- 生成 JS 片段
# 题库去重按题干做：题目数必须等于不同题干的个数，否则会被误删
stems = [q[1] for q in Q]
assert len(stems) == len(set(stems)), '题干重复：' + str([s for s in set(stems) if stems.count(s) > 1])

# 应用导入去重只比对「去空白+小写+前 60 字」，这里必须同样唯一，否则入库会被当成重复跳过
import re as _re
def norm_stem(s):
    return _re.sub(r'\s+', '', s).lower()[:60]
normed = [norm_stem(s) for s in stems]
if len(normed) != len(set(normed)):
    dup = [s for s in set(normed) if normed.count(s) > 1]
    raise SystemExit('前 60 字重复，入库会被去重跳过：%s' % dup)


def js_str(v):
    assert '`' not in v and '${' not in v, v
    return '`%s`' % v.replace('\\', '\\\\')


lines = []
for t, stem, opts, ans, sol, ch in Q:
    opt_js = '[' + ', '.join(js_str(o) for o in opts) + ']' if opts else '[]'
    lines.append("      { stem: %s, options: %s, answer: %s, explanation: %s, chapter: %s, type: '%s' },"
                 % (js_str(stem), opt_js, js_str(ans), js_str(sol), js_str(ch), t))
snippet = '\n'.join(lines)

here = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(here, '..', 'shuatixia-kids', 'sample-banks', 'build-banks.js')
src = open(target, encoding='utf-8').read()

MARK = "// ===== Unit1 单元卷（47 小题，外研版三起六上 2026 新版）====="
if MARK in src:
    raise SystemExit('已经插入过，先删除旧片段再跑')

anchor = "      { stem: `— Thank you very much! — ___`, options: [`You're welcome.`, 'No, thanks.', 'Yes, please.', `I'm fine.`], answer: 'A', explanation: '对感谢的礼貌回应是 You\\'re welcome.（不客气）。', chapter: '日常交际' },\n    ],"
assert anchor in src, '锚点没匹配到，先确认英语题库结尾'
src = src.replace(anchor, anchor.replace("\n    ],", "\n" + "      " + MARK + "\n" + snippet + "\n    ],"), 1)
open(target, 'w', encoding='utf-8').write(src)

from collections import Counter
print('已插入', len(Q), '题')
print('题型分布', dict(Counter(q[0] for q in Q)))
