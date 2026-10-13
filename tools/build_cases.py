"""把 CASE-001/002 的 .md（英文）與 .zh.md（中文）預先轉成靜態 HTML（不在網頁載入 Markdown 渲染套件）。

用法：改完 docs/CASE_*.md 或 *.zh.md 後執行 `python tools/build_cases.py`（需要 `markdown` 套件；
OfficeMac 用 /opt/anaconda3/bin/python），再 commit 重新產生的 case-00x.html。
頁面外框與樣式在 tools/case_template.html。
"""
import re
from pathlib import Path
import markdown

REPO = Path(__file__).resolve().parent.parent  # 用相對位置，兩台電腦路徑不同也能跑

CASES = [
    dict(src="docs/CASE_001_Measurement_to_Decision.md", src_zh="docs/CASE_001_Measurement_to_Decision.zh.md", out="case-001.html",
         zh_title="從量測到決策", en_title="From Measurement to Decision"),
    dict(src="docs/CASE_002_Wearable_Strength_Training_Concept.md", src_zh="docs/CASE_002_Wearable_Strength_Training_Concept.zh.md", out="case-002.html",
         zh_title="穿戴式阻力訓練智慧", en_title="Wearable Strength Training Intelligence"),
]

TEMPLATE = (Path(__file__).parent / "case_template.html").read_text(encoding="utf-8")


def convert(md_text: str):
    # 第一行 "# CASE-00X | Title" 拆成編號與標題，其餘照原文轉換
    lines = md_text.splitlines()
    m = re.match(r"#\s+(CASE-\d+)\s*\|\s*(.+)", lines[0])
    case_id, title = m.group(1), m.group(2).strip()
    body = markdown.markdown("\n".join(lines[1:]), extensions=["tables", "fenced_code"])
    # 表格包一層，手機可橫向捲動而不撐破版面
    body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    return case_id, title, body


for c in CASES:
    case_id, title, body = convert((REPO / c["src"]).read_text(encoding="utf-8"))
    case_id_zh, _, body_zh = convert((REPO / c["src_zh"]).read_text(encoding="utf-8"))
    assert case_id == case_id_zh, "中英編號不一致"
    html = (TEMPLATE
            .replace("{{CASE_ID}}", case_id)
            .replace("{{TITLE_EN}}", c["en_title"])
            .replace("{{TITLE_ZH}}", c["zh_title"])
            .replace("{{BODY_EN}}", body)
            .replace("{{BODY_ZH}}", body_zh))
    (REPO / c["out"]).write_text(html, encoding="utf-8")
    print("wrote", c["out"], len(html))
