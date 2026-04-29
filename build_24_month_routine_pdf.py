from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


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
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1F3D37"),
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KSub",
            fontName=FONT_NAME,
            fontSize=10.5,
            leading=15,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#5C675F"),
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KH1",
            parent=styles["Heading1"],
            fontName=FONT_BOLD_NAME,
            fontSize=15.5,
            leading=20,
            textColor=colors.HexColor("#21493F"),
            spaceBefore=12,
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
            textColor=colors.HexColor("#496B63"),
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
            textColor=colors.HexColor("#23313A"),
            spaceAfter=5,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KBodySmall",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=8.5,
            leading=12,
            textColor=colors.HexColor("#4E5A54"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KLead",
            parent=styles["BodyText"],
            fontName=FONT_NAME,
            fontSize=10.5,
            leading=16,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#33413A"),
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="KCardTitle",
            parent=styles["Heading2"],
            fontName=FONT_BOLD_NAME,
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#21493F"),
            spaceAfter=4,
        )
    )
    return styles


def p(text, style):
    return Paragraph(text, style)


def box(flowables, background, border, padding=10):
    table = Table([[flowables]], colWidths=[None])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 0.8, border),
                ("LEFTPADDING", (0, 0), (-1, -1), padding),
                ("RIGHTPADDING", (0, 0), (-1, -1), padding),
                ("TOPPADDING", (0, 0), (-1, -1), padding),
                ("BOTTOMPADDING", (0, 0), (-1, -1), padding),
            ]
        )
    )
    return table


def add_cover(story, styles):
    cover = box(
        [
            p("24개월 생활 루틴 가이드", styles["KTitle"]),
            p(
                "부모의 하루를 덜 지치게 만들고 아이의 하루를 조금 더 예측 가능하게 만드는 실전 가이드",
                styles["KSub"],
            ),
            p(
                "식사, 낮잠, 저녁 루틴, 떼쓰기 대응까지.<br/>검색보다 바로 적용할 수 있는 구조를 담았습니다.",
                styles["KLead"],
            ),
        ],
        colors.HexColor("#F7F1E6"),
        colors.HexColor("#D8C8A8"),
        padding=16,
    )
    story.append(cover)
    story.append(Spacer(1, 12))


def add_quick_start(story, styles):
    content = [
        p("바로 시작하기", styles["KCardTitle"]),
        p("이 가이드는 아래 순서로 쓰면 가장 편합니다.", styles["KBody"]),
        p("1. 전체 루틴을 먼저 본다.", styles["KBody"]),
        p("2. 지금 가장 힘든 구간 하나만 고른다.", styles["KBody"]),
        p("3. 그 구간의 대화 예시와 조정 팁을 적용한다.", styles["KBody"]),
        p("4. 일주일 흐름을 본 뒤 수정한다.", styles["KBody"]),
    ]
    story.append(box(content, colors.HexColor("#EEF5F2"), colors.HexColor("#9BB8AB")))
    story.append(Spacer(1, 10))


def add_bullet_list(story, items, styles):
    for item in items:
        story.append(p(f"• {item}", styles["KBody"]))


def add_numbered_list(story, items, styles):
    for idx, item in enumerate(items, start=1):
        story.append(p(f"{idx}. {item}", styles["KBody"]))


def add_labeled_block(story, label, lines, styles, background, border):
    content = [p(label, styles["KCardTitle"])]
    for line in lines:
        content.append(p(line, styles["KBody"]))
    story.append(box(content, background, border))
    story.append(Spacer(1, 8))


def split_sections(lines):
    sections = []
    current_title = None
    current_lines = []
    for line in lines:
        if line.startswith("## "):
            if current_title is not None:
                sections.append((current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title is not None:
        sections.append((current_title, current_lines))
    return sections


def render_section(title, lines, story, styles):
    clean = [line.rstrip() for line in lines]
    story.append(p(title, styles["KH1"]))

    if title == "이 가이드는 누구를 위한 문서인가":
        intro = []
        bullets = []
        tail = []
        mode = "intro"
        for line in clean:
            if not line:
                continue
            if line.startswith("- "):
                mode = "bullets"
                bullets.append(line[2:])
            elif mode == "bullets":
                tail.append(line)
            else:
                intro.append(line)
        for line in intro:
            story.append(p(line, styles["KBody"]))
        story.append(Spacer(1, 4))
        story.append(box([p("이런 부모에게 특히 잘 맞습니다", styles["KCardTitle"])] + [p(f"• {b}", styles["KBody"]) for b in bullets], colors.HexColor("#F8F4EC"), colors.HexColor("#D9C8A7")))
        story.append(Spacer(1, 8))
        for line in tail:
            story.append(p(line, styles["KBody"]))
        return

    if title == "먼저 기억할 것":
        paragraphs = []
        numbered = []
        for line in clean:
            if not line:
                continue
            if line[:2].isdigit() and line[1:3] == ". ":
                numbered.append(line[3:])
            else:
                paragraphs.append(line)
        for line in paragraphs[:2]:
            story.append(p(line, styles["KBody"]))
        story.append(Spacer(1, 4))
        story.append(box([p("핵심 3가지", styles["KCardTitle"])] + [p(f"{i+1}. {item}", styles["KBody"]) for i, item in enumerate(numbered)], colors.HexColor("#EEF5F2"), colors.HexColor("#9BB8AB")))
        return

    if title == "이 가이드의 사용법":
        numbered = [line[3:] for line in clean if line[:2].isdigit() and line[1:3] == ". "]
        intro = [line for line in clean if line and not (line[:2].isdigit() and line[1:3] == ". ")]
        for line in intro:
            story.append(p(line, styles["KBody"]))
        story.append(Spacer(1, 4))
        story.append(box([p("추천 사용 순서", styles["KCardTitle"])] + [p(f"{i+1}. {item}", styles["KBody"]) for i, item in enumerate(numbered)], colors.HexColor("#FFF8EE"), colors.HexColor("#E1C896")))
        return

    if title == "하루 기본 루틴 예시":
        sub_sections = []
        sub_title = None
        sub_lines = []
        for line in clean:
            if line.startswith("### "):
                if sub_title:
                    sub_sections.append((sub_title, sub_lines))
                sub_title = line[4:].strip()
                sub_lines = []
            else:
                sub_lines.append(line)
        if sub_title:
            sub_sections.append((sub_title, sub_lines))

        for sub_title, sub_lines in sub_sections:
            bullets = [line[2:] for line in sub_lines if line.startswith("- ")]
            body = [line for line in sub_lines if line and not line.startswith("- ")]
            card = [p(sub_title, styles["KCardTitle"])]
            for bullet in bullets:
                card.append(p(f"• {bullet}", styles["KBody"]))
            if body:
                card.append(Spacer(1, 4))
                for line in body:
                    card.append(p(line, styles["KBodySmall"]))
            story.append(box(card, colors.HexColor("#FAF7F1"), colors.HexColor("#D4DCCD")))
            story.append(Spacer(1, 8))
        return

    if title == "가장 많이 무너지는 5가지 지점":
        blocks = []
        current_name = None
        current_lines = []
        for line in clean:
            if line.startswith("### "):
                if current_name:
                    blocks.append((current_name, current_lines))
                current_name = line[4:].strip()
                current_lines = []
            else:
                current_lines.append(line)
        if current_name:
            blocks.append((current_name, current_lines))

        for name, block_lines in blocks:
            problem, adjust, talk = [], [], []
            target = None
            for line in block_lines:
                if not line:
                    continue
                if line == "문제:":
                    target = problem
                    continue
                if line == "조정:":
                    target = adjust
                    continue
                if line == "부모 대화 예시:":
                    target = talk
                    continue
                if line.startswith("- "):
                    if target is adjust:
                        adjust.append(line[2:])
                    else:
                        target.append(line[2:] if target is not None else line)
                elif target is not None:
                    target.append(line)
            flow = [p(name, styles["KH2"])]
            if problem:
                flow.append(box([p("문제", styles["KCardTitle"])] + [p(line, styles["KBody"]) for line in problem], colors.HexColor("#FFF5F0"), colors.HexColor("#E4B6A8"), padding=8))
                flow.append(Spacer(1, 6))
            if adjust:
                flow.append(box([p("조정", styles["KCardTitle"])] + [p(f"• {line}", styles["KBody"]) for line in adjust], colors.HexColor("#EEF5F2"), colors.HexColor("#9BB8AB"), padding=8))
                flow.append(Spacer(1, 6))
            if talk:
                flow.append(box([p("부모 대화 예시", styles["KCardTitle"])] + [p(line, styles["KBody"]) for line in talk], colors.HexColor("#F8F4EC"), colors.HexColor("#D9C8A7"), padding=8))
            story.append(KeepTogether(flow))
            story.append(Spacer(1, 8))
        return

    if title == "집에서 바로 할 수 있는 놀이 10가지":
        items = [line[3:] for line in clean if line[:2].isdigit() and line[1:3] == ". "]
        story.append(box([p("바로 해볼 놀이", styles["KCardTitle"])] + [p(f"{i+1}. {item}", styles["KBody"]) for i, item in enumerate(items)], colors.HexColor("#F7F1E6"), colors.HexColor("#D9C8A7")))
        tail = [line for line in clean if line and not (line[:2].isdigit() and line[1:3] == ". ")]
        story.append(Spacer(1, 8))
        for line in tail:
            story.append(p(line, styles["KBody"]))
        return

    if title == "부모가 자주 하는 실수":
        bullets = [line[2:] for line in clean if line.startswith("- ")]
        tail = [line for line in clean if line and not line.startswith("- ")]
        story.append(box([p("자주 하는 실수", styles["KCardTitle"])] + [p(f"• {line}", styles["KBody"]) for line in bullets], colors.HexColor("#FFF5F0"), colors.HexColor("#E4B6A8")))
        story.append(Spacer(1, 8))
        for line in tail:
            story.append(p(line, styles["KBody"]))
        return

    if title == "일주일 적용 체크리스트":
        bullets = [line[2:] for line in clean if line.startswith("- ")]
        story.append(box([p("일주일 체크리스트", styles["KCardTitle"])] + [p(f"□ {line}", styles["KBody"]) for line in bullets], colors.HexColor("#EEF5F2"), colors.HexColor("#9BB8AB")))
        return

    if title == "이런 경우는 따로 살펴보기":
        intro = [line for line in clean if line and not line.startswith("- ")]
        bullets = [line[2:] for line in clean if line.startswith("- ")]
        for line in intro:
            story.append(p(line, styles["KBody"]))
        story.append(Spacer(1, 4))
        story.append(box([p("전문가와 상의가 필요한 신호", styles["KCardTitle"])] + [p(f"• {line}", styles["KBody"]) for line in bullets], colors.HexColor("#FFF3EF"), colors.HexColor("#DDAE9F")))
        return

    for line in clean:
        if not line:
            story.append(Spacer(1, 6))
            continue
        if line.startswith("- "):
            story.append(p(f"• {line[2:]}", styles["KBody"]))
            continue
        if line[:2].isdigit() and line[1:3] == ". ":
            story.append(p(line, styles["KBody"]))
            continue
        story.append(p(line, styles["KBody"]))


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

    story = []
    add_cover(story, styles)
    add_quick_start(story, styles)

    with open("products/24-month-routine-guide.md", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    content_lines = lines[3:]
    for title, section_lines in split_sections(content_lines):
        render_section(title, section_lines, story, styles)
        story.append(Spacer(1, 6))
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
