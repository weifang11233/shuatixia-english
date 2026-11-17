#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外研版（三起）2026 新版 六年级上册 Unit 1 What do you do with money?
单元测试卷生成器 —— 100 分 / 60 分钟 / 47 小题
输出：A4 打印版 HTML（答案独立分页）
"""
import os

TITLE = "外研版（三起）六年级上册 Unit 1 单元测试卷"
SUBTITLE = "Unit 1 What do you do with money?"
META = "建议时长 60 分钟　|　满分 100 分　|　范围：Unit 1（2026 新版·孙有中主编）"
FOOT_L = "本卷不含听力，语音以笔答形式考查 cr / cl 辅音连缀"
FOOT_R = "六年级英语 · Unit 1"

# ---------------------------------------------------------------- 题目数据
# 一、语音（划线部分发音不同的一项）
SEC1 = [
    dict(stem="A. c<u>r</u>ayon　B. c<u>r</u>eam　C. <u>cl</u>ang　D. c<u>r</u>y",
         ans="C", sol="clang 划线部分读 /kl/，其余读 /kr/。"),
    dict(stem="A. <u>cl</u>ock　B. <u>cl</u>ass　C. <u>cl</u>ean　D. c<u>r</u>y",
         ans="D", sol="cry 读 /kr/，其余读 /kl/。"),
    dict(stem="A. <u>cl</u>ever　B. c<u>r</u>oss　C. <u>cl</u>oud　D. <u>cl</u>ose",
         ans="B", sol="cross 读 /kr/，其余读 /kl/。"),
    dict(stem="A. c<u>r</u>eam　B. <u>cl</u>ang　C. <u>cl</u>ass　D. <u>cl</u>ock",
         ans="A", sol="cream 读 /kr/，其余读 /kl/。"),
    dict(stem="A. c<u>r</u>ayon　B. <u>cl</u>ever　C. <u>cl</u>ean　D. <u>cl</u>oud",
         ans="A", sol="crayon 读 /kr/，其余读 /kl/。"),
]

# 二、词汇
SEC2A = [
    dict(stem="储蓄，存（钱）　________", ans="save"),
    dict(stem="用（钱），花费　________", ans="spend"),
    dict(stem="零花钱　________", ans="pocket money"),
    dict(stem="店主　________", ans="shopkeeper"),
    dict(stem="彩色蜡笔　________", ans="crayon"),
]
SEC2B = [
    dict(stem="A. save　B. crayon　C. spend　D. buy", ans="B", sol="crayon 是名词，其余是动词。"),
    dict(stem="A. yuan　B. dollar　C. pocket　D. pound", ans="C", sol="pocket 不表示货币单位。"),
    dict(stem="A. money　B. buy　C. sell　D. share", ans="A", sol="money 是名词，其余是动词。"),
    dict(stem="A. book　B. robot　C. ice cream　D. shopkeeper", ans="D", sol="shopkeeper 指人，其余指物品。"),
    dict(stem="A. happy　B. surprised　C. sad　D. smile", ans="D", sol="smile 是名词/动词，其余是形容词。"),
]

# 三、单项选择
SEC3 = [
    dict(stem="— How much ______ the robot?\n— It's 35 yuan.",
         opts=["is", "are", "am", "be"], ans="A",
         sol="robot 是单数名词，be 动词用 is；答语 It's 也提示了单数。"),
    dict(stem="— How much ______ the cupcakes?\n— They're eight yuan each.",
         opts=["is", "are", "be", "has"], ans="B",
         sol="cupcakes 是复数，答语用 They're，问句用 are。"),
    dict(stem="Amy always ______ her pocket money in a saving box.",
         opts=["save", "saves", "saving", "saved"], ans="B",
         sol="always 表习惯，用一般现在时；主语 Amy 是第三人称单数，动词加 -s。"),
    dict(stem="Sam always ______ his money on toys and ice creams.",
         opts=["spend", "spends", "spending", "spent"], ans="B",
         sol="同上，主语 Sam 为第三人称单数，spend → spends。"),
    dict(stem="— I'll ______ the robot. Here's the money.\n— Thank you.",
         opts=["take", "takes", "taking", "took"], ans="A",
         sol="I'll = I will，后接动词原形。"),
    dict(stem="— How much are the ice creams?\n— ______ eight yuan.",
         opts=["It's", "They're", "There are", "He's"], ans="B",
         sol="ice creams 是复数，答语主语用 They，be 动词用 are。"),
    dict(stem="The old man ______ at King Midas and said, \"Gold isn't everything.\"",
         opts=["smile", "smiles", "smiled", "smiling"], ans="C",
         sol="and 后的 said 是过去式，前面也用过去式 smiled，时态保持一致。"),
    dict(stem="I will save my money ______ the right things.",
         opts=["to", "for", "at", "of"], ans="B",
         sol="固定搭配 save money for sth.，表示为某事存钱。"),
    dict(stem="Everything ______ to gold after Midas made his wish.",
         opts=["turn", "turns", "turning", "turned"], ans="D",
         sol="故事发生在过去，用过去式 turned；everything 作主语时谓语用单数形式。"),
    dict(stem="— Do you want a golden ______?\n— Yes, I do. I want to turn everything to gold.",
         opts=["touch", "smile", "gold", "clang"], ans="A",
         sol="golden touch 点金术，是本单元固定短语。"),
]

# 四、用所给词的适当形式填空
SEC4 = [
    dict(stem="Amy ________ (save) her pocket money every week.", ans="saves",
         sol="every week 表习惯，主语第三人称单数。"),
    dict(stem="Sam ________ (spend) all his money yesterday.", ans="spent",
         sol="yesterday 是过去时间状语，spend 的过去式是 spent。"),
    dict(stem="Look! The children ________ (buy) books for the children's home.", ans="are buying",
         sol="Look! 提示此刻正在发生，用现在进行时 are buying。"),
    dict(stem="I ________ (take) this robot. It's only 35 yuan.", ans="will take",
         sol="表示将要做的决定，用 will + 动词原形。写成 'll take 也算对。"),
    dict(stem="King Midas was very ________ (surprise) when his daughter turned to gold.", ans="surprised",
         sol="修饰人的感受用 -ed 形式 surprised（吃惊的）。"),
]

# 五、连词成句
SEC5 = [
    dict(stem="is / how much / the / robot / ?", ans="How much is the robot?",
         sol="疑问词 How much 放句首，be 动词 is 提到主语 the robot 前。"),
    dict(stem="are / how much / the / cupcakes / ?", ans="How much are the cupcakes?",
         sol="cupcakes 为复数，be 动词用 are。"),
    dict(stem="always / Amy / her / saves / pocket money / .", ans="Amy always saves her pocket money.",
         sol="主语 + 频度副词 always + 实义动词 saves + 宾语。"),
    dict(stem="will / my / I / save / money / for / the / right / things / .",
         ans="I will save my money for the right things.",
         sol="主语 I + will + 动词原形 save + 宾语 + for 短语。"),
]

# 六、补全对话
DLG_BOX = ["A. It's 35 yuan.", "B. I'll take it.", "C. How much is the robot?",
           "D. Here you are.", "E. They're eight yuan each.", "F. Thank you."]
DLG_LINES = [
    ("Shopkeeper", "Good morning. Can I help you?", None),
    ("Sam", "Yes. (1) ________", "C"),
    ("Shopkeeper", "(2) ________", "A"),
    ("Sam", "That's good. (3) ________", "B"),
    ("Shopkeeper", "Here's your robot.", None),
    ("Sam", "(4) ________", "D"),
    ("Shopkeeper", "(5) ________", "F"),
    ("Sam", "Goodbye!", None),
]

# 七、阅读理解
PASSAGE_A = """Sam and Amy are brother and sister. They get pocket money every week.
Amy puts her money in a saving box. She likes buying books for the children's home.
Sam is different. He spends his money on robots and ice creams.
When the School Reading Week comes, Amy has many new books for the children.
But Sam only has two coins. He says, "I'll save my money for the right things from now on."
<i>（saving box 存钱罐；children's home 儿童之家）</i>"""

READ_A = [
    dict(stem="Amy and Sam get pocket money every week.", ans="T",
         sol="第一句 They get pocket money every week."),
    dict(stem="Amy always spends all her money on toys.", ans="F",
         sol="Amy 把钱存进 saving box，还用来买书，不是全买玩具。"),
    dict(stem="Sam buys many new books for the children's home.", ans="F",
         sol="买书的是 Amy，Sam 只剩下两枚硬币。"),
    dict(stem="Sam wants to save his money from now on.", ans="T",
         sol="最后一句他自己说 I'll save my money for the right things from now on."),
]

PASSAGE_B = """Lily gets 50 yuan pocket money every month. She usually spends some of it on
crayons and ice cream. This month she wants to do something different.
Her classmate Xiaoming is ill and stays at home. Lily buys some books and a box of
crayons for him. She also saves 20 yuan in her saving box.
"I can't buy a big robot now," she says with a smile, "but Xiaoming is happy, and
I'm happy, too."
<i>（ill 生病的；classmate 同学）</i>"""

READ_B = [
    dict(stem="How much pocket money does Lily get every month?",
         opts=["15 yuan", "20 yuan", "50 yuan", "85 yuan"], ans="C",
         sol="第一句 gets 50 yuan pocket money every month。"),
    dict(stem="What does Lily buy for Xiaoming?",
         opts=["A robot and a cake.", "Some books and a box of crayons.",
               "Ice cream and a pencil.", "A saving box."], ans="B",
         sol="Lily buys some books and a box of crayons for him。"),
    dict(stem="Which of the following is TRUE?",
         opts=["Lily spends all her money this month.",
               "Lily saves 20 yuan this month.",
               "Xiaoming is Lily's brother.",
               "Lily buys a big robot."], ans="B",
         sol="文中 She also saves 20 yuan in her saving box；A、C、D 均与原文相反。"),
]

WRITING_PROMPT = """以 <b>My Pocket Money Plan</b> 为题，写一段话，说说你打算怎样使用零花钱。
<br>要求：① 不少于 5 句话；② 用 <b>will</b> 表达打算，spend / save / share 三方面至少写到两方面；
③ 不要出现真实姓名。
<br>提示词：spend ... on ...　save ... for ...　share ... with ..."""

WRITING_SAMPLE = """I get 30 yuan pocket money every month. I will spend 10 yuan on books and crayons.
I will save 15 yuan in my saving box for a special day. I will share 5 yuan with people
in need. I think it is a good plan, and I will do it from now on."""

# ---------------------------------------------------------------- 渲染
def opt_line(opts, cls="opts4"):
    cells = "".join('<span class="opt">%s. %s</span>' % ("ABCD"[i], o) for i, o in enumerate(opts))
    return '<div class="%s">%s</div>' % (cls, cells)


def build():
    out = []
    A = out.append

    A('<div class="paper">')
    A('<header class="paper-head">')
    A('<h1>%s</h1>' % TITLE)
    A('<div class="sub">%s</div>' % SUBTITLE)
    A('<div class="meta">%s</div>' % META)
    A('</header>')
    A('<div class="idbar"><span>姓名：____________</span><span>班级：____________</span>'
      '<span>学号：__________</span><span>得分：____________</span></div>')

    # 一、语音
    A('<section class="sec"><h2>一、语音<span class="req">选出划线部分发音不同的一项（每题 2 分，共 10 分）</span></h2>')
    A('<ol class="qs">')
    for q in SEC1:
        A('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (0, q["stem"]))
    A('</ol></section>')
    # 修正序号
    A('')
    return out


# ---------------------------------------------------------------- 渲染
def render():
    L = []
    a = L.append

    a('<!DOCTYPE html>')
    a('<html lang="zh-CN"><head><meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width, initial-scale=1">')
    a('<title>%s</title>' % TITLE)
    a(HTML_CSS)
    a('</head><body><div class="paper">')

    # 卷头
    a('<header class="paper-head">')
    a('<div class="grade-line">外研版（三起）· 2026 新版 · 六年级上册</div>')
    a('<h1>Unit 1 单元测试卷</h1>')
    a('<div class="sub">What do you do with money?</div>')
    a('<div class="meta">建议时长 60 分钟　·　满分 100 分</div>')
    a('</header>')
    a('<div class="idbar"><span>姓名：____________</span><span>班级：____________</span>'
      '<span>学号：__________</span><span>得分：____________</span></div>')

    no = [0]

    def qno():
        no[0] += 1
        return no[0]

    # ---- 一、语音
    a('<section class="sec"><h2>一、语音<span class="req">选出划线部分发音不同的一项（每题 2 分，共 10 分）</span></h2><ol class="qs">')
    for q in SEC1:
        a('<li><span class="no">%d.</span><div class="stem"><div class="phon">%s</div></div></li>'
          % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 二、词汇
    a('<section class="sec"><h2>二、词汇<span class="req">（共 20 分）</span></h2>')
    a('<h3 class="sub-h">A. 根据中文提示写出单词（每题 2 分，共 10 分）</h3><ol class="qs">')
    for q in SEC2A:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol>')
    a('<h3 class="sub-h">B. 选出不同类的一项（每题 2 分，共 10 分）</h3><ol class="qs">')
    for q in SEC2B:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 三、单项选择
    a('<section class="sec"><h2>三、单项选择<span class="req">每题 2 分，共 20 分</span></h2><ol class="qs">')
    for q in SEC3:
        stem = q["stem"].replace("\n", "<br>")
        a('<li><span class="no">%d.</span><div class="stem">%s%s</div></li>'
          % (qno(), stem, opt_line(q["opts"])))
    a('</ol></section>')

    # ---- 四、词形填空
    a('<section class="sec"><h2>四、用所给词的适当形式填空<span class="req">每题 2 分，共 10 分</span></h2><ol class="qs">')
    for q in SEC4:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 五、连词成句
    a('<section class="sec"><h2>五、连词成句<span class="req">注意大小写和句末标点（每题 2 分，共 8 分）</span></h2><ol class="qs">')
    for q in SEC5:
        a('<li><span class="no">%d.</span><div class="stem">%s<div class="wline"></div></div></li>'
          % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 六、补全对话
    a('<section class="sec"><h2>六、补全对话<span class="req">从方框中选择合适的句子，有一项多余（每题 2 分，共 10 分）</span></h2>')
    a('<div class="box"><div class="box-t">方框</div><div class="box-b">')
    for i, s in enumerate(DLG_BOX):
        a('<span class="box-item">%s</span>' % s)
    a('</div></div>')
    a('<div class="dlg">')
    for who, line, _ in DLG_LINES:
        line = line.replace("________", '<span class="bl">________</span>')
        a('<div class="dlg-row"><span class="who">%s:</span><span class="say">%s</span></div>' % (who, line))
    a('</div></section>')

    # ---- 七、阅读
    a('<section class="sec"><h2>七、阅读理解<span class="req">共 14 分</span></h2>')
    a('<h3 class="sub-h">A. 读短文，判断正（T）误（F）（每题 2 分，共 8 分）</h3>')
    a('<div class="passage">%s</div>' % PASSAGE_A.replace("\n", " "))
    a('<ol class="qs">')
    for q in READ_A:
        a('<li><span class="no">%d.</span><div class="stem">%s <span class="tf">(&nbsp;&nbsp;&nbsp;)</span></div></li>'
          % (qno(), q["stem"]))
    a('</ol>')
    a('<div class="keep">')
    a('<h3 class="sub-h">B. 读短文，选择正确答案（每题 2 分，共 6 分）</h3>')
    a('<div class="passage">%s</div>' % PASSAGE_B.replace("\n", " "))
    a('<ol class="qs">')
    for q in READ_B:
        a('<li><span class="no">%d.</span><div class="stem">%s%s</div></li>'
          % (qno(), q["stem"], opt_line(q["opts"], "opts2")))
    a('</ol></div></section>')

    # ---- 八、书面表达
    a('<section class="sec"><h2>八、书面表达<span class="req">共 8 分</span></h2>')
    a('<div class="prompt">%s</div>' % WRITING_PROMPT)
    a('<div class="wgrid">')
    for _ in range(12):
        a('<div class="wrow"></div>')
    a('</div></section>')

    a('<div class="foot"><span>%s</span><span>%s</span></div>' % (FOOT_L, FOOT_R))

    # ================= 答案页 =================
    a('<div class="answer-sec">')
    a('<h2>参考答案与评分说明</h2>')

    a('<h3>一、语音（每题 2 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (i + 1, q["ans"]) for i, q in enumerate(SEC1)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (i + 1, q["sol"]) for i, q in enumerate(SEC1)))

    a('<h3>二、词汇（每题 2 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (i + 6, q["ans"]) for i, q in enumerate(SEC2A)))
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (i + 11, q["ans"]) for i, q in enumerate(SEC2B)))
    a('<div class="sol">B 部分理由：%s</div>' % "<br>".join("%d. %s" % (i + 11, q["sol"]) for i, q in enumerate(SEC2B)))

    a('<h3>三、单项选择（每题 2 分，共 20 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (i + 16, q["ans"]) for i, q in enumerate(SEC3)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (i + 16, q["sol"]) for i, q in enumerate(SEC3)))

    a('<h3>四、用所给词的适当形式填空（每题 2 分，共 10 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (i + 26, q["ans"]) for i, q in enumerate(SEC4)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (i + 26, q["sol"]) for i, q in enumerate(SEC4)))

    a('<h3>五、连词成句（每题 2 分，共 8 分）</h3>')
    a('<ol class="ans">')
    for i, q in enumerate(SEC5):
        a('<li><b>%d.</b>%s<div class="sol">%s</div></li>' % (i + 31, q["ans"], q["sol"]))
    a('</ol>')

    a('<h3>六、补全对话（每题 2 分，共 10 分）</h3>')
    a('<div class="ans-grid">(1) C　(2) A　(3) B　(4) D　(5) F　　（E 多余）</div>')

    a('<h3>七、阅读理解（每题 2 分，共 14 分）</h3>')
    a('<div class="ans-grid">A：%s<br>B：%s</div>' % (
        "　".join("%d. %s" % (i + 35, q["ans"]) for i, q in enumerate(READ_A)),
        "　".join("%d. %s" % (i + 39, q["ans"]) for i, q in enumerate(READ_B))))
    a('<div class="sol">%s</div>' % "<br>".join(
        "%d. %s" % (i + 35, q["sol"]) for i, q in enumerate(READ_A + READ_B)))

    a('<h3>八、书面表达（8 分）</h3>')
    a('<div class="sol">评分点：内容 4 分（写到 spend / save / share 中至少两方面）、语言 3 分'
      '（will + 动词原形、拼写、单复数）、书写 1 分（大小写、标点）。不足 5 句每少一句扣 1 分。</div>')
    a('<div class="sample"><div class="sample-t">范文</div>%s</div>' % WRITING_SAMPLE.replace("\n", " "))

    a('<h3>易错点提醒</h3>')
    a('<ul class="tips">'
      '<li>How much <b>is</b> the robot? / How much <b>are</b> the cupcakes? —— 看 be 动词后的名词是单数还是复数。</li>'
      '<li>Amy <b>saves</b> / Sam <b>spends</b> —— always 表习惯用一般现在时，主语是第三人称单数时动词要加 -s。</li>'
      '<li>Everything <b>turned</b> to gold. —— everything 作主语谓语用单数；故事叙述用过去式。</li>'
      '<li>I\'ll take <b>it</b>. / I\'ll take <b>one</b>. —— 指代前面提到的单数物品。</li>'
      '<li>cry / cream / crayon 读 /kr/，clang / class / clock 读 /kl/，注意区分。</li>'
      '</ul>')
    a('</div>')

    a('</div></body></html>')
    return "\n".join(L)


HTML_CSS = """<style>
:root{
  --ink:#1a1a1a; --ink-soft:#4a4a4a; --line:#c9ccd1; --line-soft:#e4e6e9;
  --paper:#fff; --accent:#2f6fb3; --accent-soft:#eef4fb;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#f2f3f5;color:var(--ink)}
body{font-family:"Times New Roman","SimSun","宋体",serif;font-size:15px;line-height:1.75}
.paper{width:210mm;min-height:297mm;margin:16px auto;padding:15mm 17mm 16mm;background:var(--paper);
  box-shadow:0 2px 12px rgba(0,0,0,.08)}
.paper-head{text-align:center;border-bottom:2px solid var(--ink);padding-bottom:9px}
.paper-head .grade-line{font-size:12.5px;color:var(--ink-soft);letter-spacing:3px}
.paper-head h1{margin:2px 0 1px;font-size:24px;letter-spacing:2px;font-weight:700;
  font-family:"KaiTi","楷体","SimHei","黑体",serif}
.paper-head .sub{font-size:14px;color:var(--accent);font-style:italic}
.paper-head .meta{font-size:12.5px;color:var(--ink-soft);letter-spacing:.5px;margin-top:2px}
.idbar{display:flex;justify-content:space-between;gap:8px;font-size:12.5px;color:var(--ink-soft);
  padding:7px 2px 10px;border-bottom:1px dashed var(--line)}
.idbar span{white-space:nowrap}
.sec{margin:14px 0 0}
.sec h2{font-size:16px;font-weight:700;margin:0 0 7px;font-family:"KaiTi","楷体","SimHei",serif;letter-spacing:.5px}
.sec h2 .req{font-size:12px;font-weight:400;color:var(--ink-soft);margin-left:8px;
  font-family:"SimSun",serif;letter-spacing:0}
.sub-h{font-size:13.5px;font-weight:700;margin:9px 0 5px;color:var(--ink)}
ol.qs{list-style:none;margin:0;padding:0}
ol.qs > li{display:flex;gap:6px;align-items:flex-start;margin:0 0 8px;page-break-inside:avoid}
ol.qs > li .no{flex:0 0 auto;min-width:24px;font-weight:700;font-size:14px;line-height:1.75}
ol.qs > li .stem{flex:1 1 auto}
.opts4{display:flex;flex-wrap:wrap;gap:1px 34px;margin-top:2px;font-size:14.5px}
.opts2{display:grid;grid-template-columns:max-content max-content;gap:1px 30px;margin-top:2px;font-size:14.5px}
.phon{display:block;font-size:14.5px;letter-spacing:.2px;white-space:nowrap}
.phon u{text-underline-offset:3px;text-decoration-thickness:1.5px}
.wline{border-bottom:1px solid #8d939b;height:22px;margin:2px 0 0}
.passage{background:#fafbfc;border:1px solid var(--line-soft);border-radius:4px;
  padding:9px 11px;margin:4px 0 7px;font-size:14.5px;line-height:1.85;text-align:justify}
.passage i{color:var(--ink-soft);font-size:12.5px}
.tf{letter-spacing:1px;color:var(--ink-soft)}
.box{border:1.5px solid var(--ink);border-radius:4px;padding:7px 10px;margin:5px 0 9px;background:#fcfcfd}
.box-t{font-size:11.5px;color:var(--ink-soft);letter-spacing:2px;margin-bottom:3px}
.box-b{display:flex;flex-wrap:wrap;gap:2px 22px;font-size:14.5px}
.dlg{margin:2px 0 0}
.dlg-row{display:flex;gap:8px;margin:0 0 5px;align-items:baseline}
.dlg-row .who{flex:0 0 92px;font-weight:700;font-size:14px}
.dlg-row .say{flex:1 1 auto;font-size:14.5px}
.bl{display:inline-block;min-width:70px;border-bottom:1px solid #8d939b;text-align:center}
.prompt{background:var(--accent-soft);border-left:3px solid var(--accent);padding:8px 11px;
  font-size:14px;line-height:1.8;margin:4px 0 8px}
.wgrid{margin-top:10px}
.keep{page-break-inside:avoid;break-inside:avoid}
.wrow{height:26px;border-bottom:1px solid #aab0b8}
.foot{margin-top:18px;padding-top:7px;border-top:1px dashed var(--line);
  font-size:11.5px;color:var(--ink-soft);display:flex;justify-content:space-between}
/* 答案页 */
.answer-sec{page-break-before:always;break-before:page;border-top:2px solid var(--ink);padding-top:12px;
  background:linear-gradient(180deg,var(--accent-soft),transparent 60px)}
.answer-sec h2{font-size:19px;letter-spacing:3px;color:var(--accent);margin:4px 0 10px;
  font-family:"KaiTi","楷体",serif}
.answer-sec h3{font-size:14px;margin:13px 0 5px;border-left:3px solid var(--accent);padding-left:8px}
.ans-grid{font-size:14.5px;font-weight:700;letter-spacing:.5px;margin-bottom:3px}
.sol{color:var(--ink-soft);font-size:12.5px;line-height:1.7}
ol.ans{list-style:none;margin:0;padding:0;font-size:14px}
ol.ans > li{margin:0 0 5px;display:flex;gap:6px;flex-wrap:wrap;align-items:baseline}
ol.ans > li b{min-width:22px}
.sample{background:#fafbfc;border:1px dashed var(--line);border-radius:4px;padding:9px 11px;
  font-size:14px;line-height:1.8;margin-top:5px}
.sample-t{font-size:11.5px;color:var(--accent);letter-spacing:2px;margin-bottom:3px}
ul.tips{margin:4px 0 0;padding-left:20px;font-size:13px;line-height:1.85;color:var(--ink-soft)}
ul.tips li{margin-bottom:2px}
@page{size:A4;margin:13mm}
@media print{
  html,body{background:#fff}
  .paper{width:auto;min-height:0;margin:0;padding:0;box-shadow:none}
  .foot{border-top:none}
}
</style>"""


if __name__ == "__main__":
    html_str = render()
    outdir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(outdir, "六年级英语上册Unit1测验.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_str)
    total = len(SEC1) + len(SEC2A) + len(SEC2B) + len(SEC3) + len(SEC4) + len(SEC5) + 5 + len(READ_A) + len(READ_B) + 1
    score = 10 + 20 + 20 + 10 + 8 + 10 + 14 + 8
    print("已生成:", path)
    print("小题数:", total, "总分:", score)
