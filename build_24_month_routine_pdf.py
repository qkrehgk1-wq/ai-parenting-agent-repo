from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


OUTPUT_FILE = "products/24-month-routine-guide.pdf"
FONT_NAME = "MalgunGothic"
FONT_PATH = r"C:\Windows\Fonts\malgun.ttf"
FONT_BOLD_NAME = "MalgunGothicBold"
FONT_BOLD_PATH = r"C:\Windows\Fonts\malgunbd.ttf"


def register_fonts():
    pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))
    pdfmetrics.registerFont(TTFont(FONT_BOLD_NAME, FONT_BOLD_PATH))


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="KTitle",
            fontName=FONT_BOLD_NAME,
            fontSize=22,
            leading=28,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#17324D"),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KSub",
            fontName=FONT_NAME,
            fontSize=10,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#5B6573"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KH1",
            parent=styles["Heading1"],
            fontName=FONT_BOLD_NAME,
            fontSize=15,
            leading=20,
            textColor=colors.HexColor("#17324D"),
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KH2",
            parent=styles["Heading2"],
            fontName=FONT_BOLD_NAME,
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#294E70"),
            spaceBefore=6,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KBody",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=9.5,
            leading=15,
            textColor=colors.black,
            spaceAfter=5,
        )
    )
    return styles


def p(text, style):
    return Paragraph(text, style)


def add_lines(story, lines, style):
    for line in lines:
        if not line.strip():
            story.append(Spacer(1, 6))
            continue
        if line.startswith("# "):
            story.append(p(line[2:], style["KH1"]))
            continue
        if line.startswith("## "):
            story.append(p(line[3:], style["KH2"]))
            continue
        if line.startswith("- "):
            story.append(p(f"• {line[2:]}", style["KBody"]))
            continue
        if line[:2].isdigit() and line[1:3] == ". ":
            story.append(p(line, style["KBody"]))
            continue
        story.append(p(line, style["KBody"]))


def build_pdf():
    register_fonts()
    styles = build_styles()

    doc = SimpleDocTemplate(
        OUTPUT_FILE,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="24개월 생활 루틴 가이드",
        author="Codex",
    )

    story = [
        p("24개월 생활 루틴 가이드", styles["KTitle"]),
        p(
            "부모의 하루를 덜 지치게 만들고 아이의 하루를 조금 더 예측 가능하게 만드는 실전 가이드",
            styles["KSub"],
        ),
    ]

    with open("products/24-month-routine-guide.md", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # Skip top title/subtitle already rendered.
    content_lines = lines[3:]
    add_lines(story, content_lines, styles)
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
