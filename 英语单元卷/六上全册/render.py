#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
外研版（三起）2026 新版 六年级上册 全册单元测试卷 · 通用渲染器
每套：47 小题 / 100 分 / 60 分钟；答案页独立分页；题号由程序推导，杜绝错位。
"""
import os

UNITS_META = {
    1: dict(sub="What do you do with money?", foot_l="本卷不含听力，语音以笔答形式考查 cr / cl 辅音连缀",
            phon=("cr", "cl", "/kr/", "/kl/")),
    2: dict(sub="What's your opinion?", foot_l="本卷不含听力，语音以笔答形式考查 dr / tr 辅音连缀",
            phon=("dr", "tr", "/dr/", "/tr/")),
    3: dict(sub="Wonderful nature", foot_l="本卷不含听力，语音以笔答形式考查 bl / br 辅音连缀",
            phon=("bl", "br", "/bl/", "/br/")),
    4: dict(sub="We can do it!", foot_l="本卷不含听力，语音以笔答形式考查 fr / fl 辅音连缀",
            phon=("fr", "fl", "/fr/", "/fl/")),
    5: dict(sub="Health matters", foot_l="本卷不含听力，语音以笔答形式考查 gl / gr 辅音连缀",
            phon=("gl", "gr", "/gl/", "/gr/")),
    6: dict(sub="See the world", foot_l="本卷不含听力，语音以笔答形式考查 pl / pr 辅音连缀",
            phon=("pl", "pr", "/pl/", "/pr/")),
}


# ---------------------------------------------------------------- 语音题生成
def mark(word, cluster):
    """给单词中的辅音连缀加下划线标记"""
    i = word.find(cluster)
    assert i >= 0, word + " 不含 " + cluster
    return word[:i] + "<u>" + cluster + "</u>" + word[i + len(cluster):]


def gen_phonics(words_a, words_b, unit_no, total=25):
    """生成 25 道语音题（每套 5 道）。words_a / words_b 为两个辅音连缀的单词池。"""
    ca, cb, pa, pb = UNITS_META[unit_no]["phon"]
    items = []
    seen = set()
    for q in range(total):
        odd_is_a = (q % 2 == 0)
        odd_pool, main_pool = (words_a, words_b) if odd_is_a else (words_b, words_a)
        odd = odd_pool[(q // 2) % len(odd_pool)]
        start = (q * 3) % len(main_pool)
        mains = [main_pool[(start + k) % len(main_pool)] for k in range(3)]
        if odd in mains:
            mains = [w for w in main_pool if w != odd][:3]
        pos = q % 4
        opts = mains[:]
        opts.insert(pos, odd)
        key = tuple(opts)
        assert key not in seen, "语音题重复: %s" % (key,)
        seen.add(key)
        odd_name, odd_pron = (ca, pa) if odd_is_a else (cb, pb)
        main_name, main_pron = (cb, pb) if odd_is_a else (ca, pa)
        stem = "　".join("%s. %s" % ("ABCD"[i], mark(w, ca if w in words_a else cb))
                         for i, w in enumerate(opts))
        items.append(dict(
            stem=stem, ans="ABCD"[pos],
            sol="%s 中 %s 读 %s，其余读 %s。" % (odd, odd_name, odd_pron, main_pron)))
    return items


# ---------------------------------------------------------------- 渲染
def opt_line(opts, cls="opts4"):
    cells = "".join('<span class="opt">%s. %s</span>' % ("ABCD"[i], o) for i, o in enumerate(opts))
    return '<div class="%s">%s</div>' % (cls, cells)


def render_paper(cfg):
    m = UNITS_META[cfg["unit_no"]]
    L = []
    a = L.append
    sec1, sec2a, sec2b = cfg["sec1"], cfg["sec2a"], cfg["sec2b"]
    sec3, sec4, sec5 = cfg["sec3"], cfg["sec4"], cfg["sec5"]
    dlg, read, wr = cfg["dlg"], cfg["read"], cfg["writing"]

    a('<!DOCTYPE html>')
    a('<html lang="zh-CN"><head><meta charset="utf-8">')
    a('<meta name="viewport" content="width=device-width, initial-scale=1">')
    a('<title>%s</title>' % cfg["title"])
    a(HTML_CSS)
    a('</head><body><div class="paper">')

    a('<header class="paper-head">')
    a('<div class="grade-line">外研版（三起）· 2026 新版 · 六年级上册　·　第 %s 套</div>' % cfg["set_no"])
    a('<h1>%s</h1>' % cfg["title"])
    a('<div class="sub">%s</div>' % m["sub"])
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
    for q in sec1:
        a('<li><span class="no">%d.</span><div class="stem"><div class="phon">%s</div></div></li>'
          % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 二、词汇
    a('<section class="sec"><h2>二、词汇<span class="req">（共 20 分）</span></h2>')
    a('<h3 class="sub-h">A. 根据中文提示写出单词或短语（每题 2 分，共 10 分）</h3><ol class="qs">')
    for q in sec2a:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol>')
    a('<h3 class="sub-h">B. 选出不同类的一项（每题 2 分，共 10 分）</h3><ol class="qs">')
    for q in sec2b:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 三、单项选择
    a('<section class="sec"><h2>三、单项选择<span class="req">每题 2 分，共 20 分</span></h2><ol class="qs">')
    for q in sec3:
        stem = q["stem"].replace("\n", "<br>")
        a('<li><span class="no">%d.</span><div class="stem">%s%s</div></li>'
          % (qno(), stem, opt_line(q["opts"])))
    a('</ol></section>')

    # ---- 四、词形填空
    a('<section class="sec"><h2>四、用所给词的适当形式填空<span class="req">每题 2 分，共 10 分</span></h2><ol class="qs">')
    for q in sec4:
        a('<li><span class="no">%d.</span><div class="stem">%s</div></li>' % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 五、连词成句
    a('<section class="sec"><h2>五、连词成句<span class="req">注意大小写和句末标点（每题 2 分，共 8 分）</span></h2><ol class="qs">')
    for q in sec5:
        a('<li><span class="no">%d.</span><div class="stem">%s<div class="wline"></div></div></li>'
          % (qno(), q["stem"]))
    a('</ol></section>')

    # ---- 六、补全对话
    a('<section class="sec"><h2>六、补全对话<span class="req">从方框中选择合适的句子，有一项多余（每题 2 分，共 10 分）</span></h2>')
    a('<div class="box"><div class="box-t">方框</div><div class="box-b">')
    for s in dlg["box"]:
        a('<span class="box-item">%s</span>' % s)
    a('</div></div>')
    a('<div class="dlg">')
    for who, line, _ in dlg["lines"]:
        line = line.replace("________", '<span class="bl">________</span>')
        a('<div class="dlg-row"><span class="who">%s:</span><span class="say">%s</span></div>' % (who, line))
    a('</div></section>')

    # ---- 七、阅读
    a('<section class="sec"><h2>七、阅读理解<span class="req">共 14 分</span></h2>')
    a('<h3 class="sub-h">A. 读短文，判断正（T）误（F）（每题 2 分，共 8 分）</h3>')
    a('<div class="passage">%s</div>' % read["pa"].replace("\n", " "))
    a('<ol class="qs">')
    for q in read["qa"]:
        a('<li><span class="no">%d.</span><div class="stem">%s <span class="tf">(&nbsp;&nbsp;&nbsp;)</span></div></li>'
          % (qno(), q["stem"]))
    a('</ol>')
    a('<div class="keep">')
    a('<h3 class="sub-h">B. 读短文，选择正确答案（每题 2 分，共 6 分）</h3>')
    a('<div class="passage">%s</div>' % read["pb"].replace("\n", " "))
    a('<ol class="qs">')
    for q in read["qb"]:
        a('<li><span class="no">%d.</span><div class="stem">%s%s</div></li>'
          % (qno(), q["stem"], opt_line(q["opts"], "opts2")))
    a('</ol></div></section>')

    # ---- 八、书面表达
    a('<section class="sec"><h2>八、书面表达<span class="req">共 8 分</span></h2>')
    a('<div class="prompt">%s</div>' % wr["prompt"])
    a('<div class="wgrid">')
    for _ in range(12):
        a('<div class="wrow"></div>')
    a('</div></section>')

    a('<div class="foot"><span>%s</span><span>%s</span></div>' % (m["foot_l"], "六年级英语 · Unit %d" % cfg["unit_no"]))

    # ================= 答案页（题号全部程序推导） =================
    # 各节起始题号
    n1 = 1
    n2a = n1 + len(sec1)
    n2b = n2a + len(sec2a)
    n3 = n2b + len(sec2b)
    n4 = n3 + len(sec3)
    n5 = n4 + len(sec4)
    n6 = n5 + len(sec5)
    n7 = n6 + 5
    n8 = n7 + len(read["qa"]) + len(read["qb"])

    a('<div class="answer-sec">')
    a('<h2>参考答案与评分说明</h2>')

    a('<h3>一、语音（每题 2 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (n1 + i, q["ans"]) for i, q in enumerate(sec1)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (n1 + i, q["sol"]) for i, q in enumerate(sec1)))

    a('<h3>二、词汇（每题 2 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (n2a + i, q["ans"]) for i, q in enumerate(sec2a)))
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (n2b + i, q["ans"]) for i, q in enumerate(sec2b)))
    a('<div class="sol">B 部分理由：%s</div>' % "<br>".join("%d. %s" % (n2b + i, q["sol"]) for i, q in enumerate(sec2b)))

    a('<h3>三、单项选择（每题 2 分，共 20 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (n3 + i, q["ans"]) for i, q in enumerate(sec3)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (n3 + i, q["sol"]) for i, q in enumerate(sec3)))

    a('<h3>四、用所给词的适当形式填空（每题 2 分，共 10 分）</h3>')
    a('<div class="ans-grid">%s</div>' % "　".join("%d. %s" % (n4 + i, q["ans"]) for i, q in enumerate(sec4)))
    a('<div class="sol">%s</div>' % "<br>".join("%d. %s" % (n4 + i, q["sol"]) for i, q in enumerate(sec4)))

    a('<h3>五、连词成句（每题 2 分，共 8 分）</h3>')
    a('<ol class="ans">')
    for i, q in enumerate(sec5):
        a('<li><b>%d.</b>%s<div class="sol">%s</div></li>' % (n5 + i, q["ans"], q["sol"]))
    a('</ol>')

    a('<h3>六、补全对话（每题 2 分，共 10 分）</h3>')
    used = [ans for _, _, ans in dlg["lines"] if ans]
    all_letters = [s.split(".")[0] for s in dlg["box"]]
    extra = [c for c in all_letters if c not in used]
    a('<div class="ans-grid">%s　　（%s 多余）</div>'
      % ("　".join("(%d) %s" % (i + 1, ans) for i, ans in enumerate(used)), "、".join(extra)))

    a('<h3>七、阅读理解（每题 2 分，共 14 分）</h3>')
    a('<div class="ans-grid">A：%s<br>B：%s</div>' % (
        "　".join("%d. %s" % (n7 + i, q["ans"]) for i, q in enumerate(read["qa"])),
        "　".join("%d. %s" % (n7 + len(read["qa"]) + i, q["ans"]) for i, q in enumerate(read["qb"]))))
    a('<div class="sol">%s</div>' % "<br>".join(
        "%d. %s" % (n7 + i, q["sol"]) for i, q in enumerate(read["qa"] + read["qb"])))

    a('<h3>八、书面表达（8 分）</h3>')
    a('<div class="sol">%s</div>' % wr["score_note"])
    a('<div class="sample"><div class="sample-t">范文</div>%s</div>' % wr["sample"].replace("\n", " "))

    a('<h3>易错点提醒</h3>')
    a('<ul class="tips">%s</ul>' % "".join("<li>%s</li>" % t for t in wr["tips"]))
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


# ---------------------------------------------------------------- 自检
def check_paper(cfg):
    """返回问题列表；空列表 = 通过"""
    problems = []
    sec1, sec2a, sec2b = cfg["sec1"], cfg["sec2a"], cfg["sec2b"]
    sec3, sec4, sec5 = cfg["sec3"], cfg["sec4"], cfg["sec5"]
    dlg, read, wr = cfg["dlg"], cfg["read"], cfg["writing"]

    counts = [len(sec1), len(sec2a), len(sec2b), len(sec3), len(sec4), len(sec5),
              5, len(read["qa"]), len(read["qb"]), 1]
    if sum(counts) != 47:
        problems.append("小题数 %d != 47" % sum(counts))
    score = 10 + 20 + 20 + 10 + 8 + 10 + (len(read["qa"]) + len(read["qb"])) * 2 + 8
    if score != 100:
        problems.append("总分 %d != 100" % score)

    # 选项与答案字母
    for name, sec in [("单选", sec3), ("阅读B", read["qb"])]:
        for i, q in enumerate(sec):
            if q["ans"] not in "ABCD" or len(q["opts"]) < 2:
                problems.append("%s 第 %d 题答案/选项异常" % (name, i + 1))
            elif "ABCD"[q["opts"].index(next(o for o in q["opts"] if "ABCD"[q["opts"].index(o)] == q["ans"]))] if False else False:
                pass
    for name, sec in [("语音", sec1), ("不同类", sec2b)]:
        for i, q in enumerate(sec):
            if q["ans"] not in "ABCD":
                problems.append("%s 第 %d 题答案字母异常" % (name, i + 1))
    # 判断题 T/F
    for i, q in enumerate(read["qa"]):
        if q["ans"] not in ("T", "F"):
            problems.append("阅读A 第 %d 题答案应为 T/F" % (i + 1))

    # 对话：5 空、方框 6 句、多余 1 句
    used = [ans for _, _, ans in dlg["lines"] if ans]
    if len(used) != 5:
        problems.append("对话空位数 %d != 5" % len(used))
    if len(dlg["box"]) != 6:
        problems.append("对话方框句数 %d != 6" % len(dlg["box"]))
    letters = [s.split(".")[0] for s in dlg["box"]]
    if sorted(used) != sorted([c for c in letters if c in used]):
        problems.append("对话答案字母与方框不一致")
    if len(set(letters)) != 6:
        problems.append("对话方框字母不唯一")

    # 题干唯一（前 60 字去空白，防应用去重冲突）
    stems = [q["stem"].replace(" ", "")[:60] for q in sec1 + sec2a + sec2b + sec3 + sec4 + sec5]
    for i, q in enumerate(read["qa"] + read["qb"]):
        stems.append(("R%d " % i) + q["stem"].replace(" ", "")[:40])
    if len(stems) != len(set(stems)):
        dup = [s for s in set(stems) if stems.count(s) > 1]
        problems.append("题干重复（前60字）: %s" % dup[:3])
    return problems


def save_paper(cfg, outdir):
    html = render_paper(cfg)
    fname = "六年级英语上册Unit%d单元测试_第%s套.html" % (cfg["unit_no"], cfg["set_no"])
    path = os.path.join(outdir, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path
