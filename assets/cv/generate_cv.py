import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.units import mm

def build_pdf(filename):
    # A4: 210mm x 297mm. Target margins: 12mm left/right, 12mm top/bottom
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=12*mm,
        rightMargin=12*mm,
        topMargin=10*mm,
        bottomMargin=10*mm
    )

    PRIMARY = colors.HexColor('#16a34a')      # Emerald green
    DARK = colors.HexColor('#0f172a')         # Slate 900
    TEXT_MUTED = colors.HexColor('#475569')   # Slate 600
    LIGHT_BG = colors.HexColor('#f8fafc')     # Slate 50
    BORDER_COLOR = colors.HexColor('#e2e8f0') # Slate 200
    ACCENT_BG = colors.HexColor('#f0fdf4')    # Green 50
    ACCENT_BORDER = colors.HexColor('#86efac')# Green 300

    styles = getSampleStyleSheet()

    # Custom styles
    name_style = ParagraphStyle(
        'Name',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=22,
        textColor=DARK
    )
    title_style = ParagraphStyle(
        'Title',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=PRIMARY
    )
    contact_style = ParagraphStyle(
        'Contact',
        fontName='Helvetica',
        fontSize=7.8,
        leading=11,
        textColor=TEXT_MUTED
    )
    summary_style = ParagraphStyle(
        'Summary',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=DARK
    )
    section_h_style = ParagraphStyle(
        'SectionH',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=DARK,
        textTransform='uppercase'
    )
    role_style = ParagraphStyle(
        'Role',
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11,
        textColor=DARK
    )
    company_style = ParagraphStyle(
        'Company',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11,
        textColor=PRIMARY
    )
    date_style = ParagraphStyle(
        'Date',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=10,
        textColor=TEXT_MUTED,
        alignment=2 # Right
    )
    bullet_style = ParagraphStyle(
        'Bullet',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor('#334155')
    )
    skill_category_style = ParagraphStyle(
        'SkillCat',
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=TEXT_MUTED,
        textTransform='uppercase'
    )
    skill_desc_style = ParagraphStyle(
        'SkillDesc',
        fontName='Helvetica',
        fontSize=7.8,
        leading=10.5,
        textColor=DARK
    )

    story = []

    # 1. Header Table
    name_p = Paragraph('Shah Md. Arafatul <font color="#16a34a">Rahman</font>', name_style)
    subtitle_p = Paragraph('Senior Laravel &amp; Backend Engineer &nbsp;·&nbsp; ~5 Years Production Experience', title_style)
    badge_p = Paragraph('<font color="#15803d"><b>● AVAILABLE FOR HIRE (REMOTE)</b></font>', ParagraphStyle('B', fontName='Helvetica-Bold', fontSize=7.2, alignment=2, textColor=PRIMARY))

    header_data = [
        [[name_p, Spacer(1, 1*mm), subtitle_p], badge_p]
    ]
    t_header = Table(header_data, colWidths=[136*mm, 50*mm])
    t_header.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_header)
    story.append(Spacer(1, 2*mm))

    # Contact line
    contacts = (
        '📍 <b>Dhaka, Bangladesh (UTC+6)</b> &nbsp;·&nbsp; '
        '✉️ <b>arafatul985@gmail.com</b> &nbsp;·&nbsp; '
        '📞 <b>+880 1738020985</b> &nbsp;·&nbsp; '
        '🦊 <b>gitlab.com/Arafatul_Rahman</b> &nbsp;·&nbsp; '
        '🔗 <b>linkedin.com/in/shah-md-arafatul-rahman</b>'
    )
    story.append(Paragraph(contacts, contact_style))
    story.append(Spacer(1, 2*mm))
    story.append(HRFlowable(width="100%", thickness=1.2, color=PRIMARY, spaceBefore=0, spaceAfter=2.5*mm))

    # Summary box
    summary_text = (
        "<b>Executive Summary:</b> High-impact Backend Engineer with ~5 years of experience architecting resilient, production-grade applications using <b>Laravel, PHP 8, MySQL/PostgreSQL, and Redis</b>. Proven track record building enterprise shift scheduling systems with timezone engines for European workforces, high-traffic national portals (5,000+ daily searches), and Dockerized CI/CD cloud environments. Actively building <b>AI Agents (LangChain, OpenAI API)</b> and automated workflow pipelines (<b>n8n</b>)."
    )
    p_summary = Paragraph(summary_text, summary_style)
    t_summary = Table([[p_summary]], colWidths=[186*mm])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), ACCENT_BG),
        ('BOX', (0,0), (-1,-1), 0.8, ACCENT_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 2.5*mm),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5*mm),
        ('LEFTPADDING', (0,0), (-1,-1), 3.5*mm),
        ('RIGHTPADDING', (0,0), (-1,-1), 3.5*mm),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 3.5*mm))

    # 2. Main 2-Column Section
    # Left Column (118mm): Experience & Featured Architecture
    left_flow = []

    # Section: Experience
    left_flow.append(Paragraph('WORK EXPERIENCE', section_h_style))
    left_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))

    # Job 1: Dingi Dev
    j1_title = Paragraph('<b>Laravel Developer</b> &nbsp;·&nbsp; <font color="#16a34a">Dingi Dev</font> <font color="#64748b">(Remote)</font>', role_style)
    j1_date = Paragraph('2022 — Present', date_style)
    t_j1 = Table([[j1_title, j1_date]], colWidths=[84*mm, 34*mm])
    t_j1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flow.append(t_j1)
    left_flow.append(Spacer(1, 1*mm))
    left_flow.append(Paragraph('<font color="#15803d"><b>Stack:</b> Laravel 10/11 · Vue.js · Livewire · Redis Queues · Docker · Linux VPS</font>', ParagraphStyle('Stk', fontName='Helvetica-Bold', fontSize=7.2, leading=9, textColor=PRIMARY)))
    left_flow.append(Spacer(1, 1*mm))
    bullets_j1 = [
        "Architected distributed <b>shift-wise scheduling system</b> for European enterprise workforce with multi-country timezone support.",
        "Developed computation engines for <b>leave entitlement, vacation accrual, overtime pay</b>, and compensation according to European labor standards.",
        "Engineered background worker architecture with <b>Redis queues</b> for automated SMS/email reminders and calendar syncs.",
        "Configured and maintained containerized environments with <b>Docker Compose</b> and Nginx reverse-proxies on Linux cloud instances."
    ]
    for b in bullets_j1:
        left_flow.append(Paragraph(f"• {b}", bullet_style))
        left_flow.append(Spacer(1, 0.6*mm))

    left_flow.append(Spacer(1, 2*mm))

    # Job 2: Innovation Information System
    j2_title = Paragraph('<b>Full Stack Developer</b> &nbsp;·&nbsp; <font color="#16a34a">Innovation Info System</font>', role_style)
    j2_date = Paragraph('2019 — 2022', date_style)
    t_j2 = Table([[j2_title, j2_date]], colWidths=[84*mm, 34*mm])
    t_j2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flow.append(t_j2)
    left_flow.append(Spacer(1, 1*mm))
    left_flow.append(Paragraph('<font color="#15803d"><b>Stack:</b> Laravel · MySQL · REST APIs · Invoicing · Stock Tracking</font>', ParagraphStyle('Stk2', fontName='Helvetica-Bold', fontSize=7.2, leading=9, textColor=PRIMARY)))
    left_flow.append(Spacer(1, 1*mm))
    bullets_j2 = [
        "Built enterprise <b>POS and Inventory System</b> from scratch for Australian client (Banglatussie) managing catalog and orders.",
        "Engineered automated stock deduction, invoice generation, barcode scanning, and multi-warehouse product reconciliation.",
        "Designed normalized MySQL schema structures, indexes, and optimized heavy analytical sales reporting queries.",
        "Co-developed interactive online learning platform features with quiz evaluation engines and student progress dashboards."
    ]
    for b in bullets_j2:
        left_flow.append(Paragraph(f"• {b}", bullet_style))
        left_flow.append(Spacer(1, 0.6*mm))

    left_flow.append(Spacer(1, 2*mm))

    # Job 3: BdTender
    j3_title = Paragraph('<b>Software Developer</b> &nbsp;·&nbsp; <font color="#16a34a">BdTender (Part-Time)</font>', role_style)
    j3_date = Paragraph('2021 — 2025', date_style)
    t_j3 = Table([[j3_title, j3_date]], colWidths=[84*mm, 34*mm])
    t_j3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    left_flow.append(t_j3)
    left_flow.append(Spacer(1, 1*mm))
    bullets_j3 = [
        "Built dynamic search &amp; filter engine using <b>Laravel &amp; Ajax</b> for Bangladesh's premier tender aggregation portal.",
        "Implemented real-time notification dispatchers for government and private e-GP tenders across 64 districts."
    ]
    for b in bullets_j3:
        left_flow.append(Paragraph(f"• {b}", bullet_style))
        left_flow.append(Spacer(1, 0.6*mm))

    left_flow.append(Spacer(1, 2*mm))

    # Section: Key Projects
    left_flow.append(Paragraph('KEY ARCHITECTURAL PROJECTS', section_h_style))
    left_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))

    p1 = "<b>1. BdTender Procurement Portal:</b> National tender aggregation platform serving thousands of daily commercial users with sub-second Ajax search indexing and real-time SMS/email alerts."
    p2 = "<b>2. Enterprise Shift Management Engine:</b> Complex multi-tenant workforce scheduling system with custom timezone handlers, holiday rules, and compensation calculator."
    p3 = "<b>3. AI-Powered Workflow Automations:</b> Built intelligent lead scoring &amp; RAG document parsing bots integrating <b>LangChain, OpenAI API</b>, and <b>n8n</b> into Laravel backends."
    for p in [p1, p2, p3]:
        left_flow.append(Paragraph(p, bullet_style))
        left_flow.append(Spacer(1, 1*mm))

    # Right Column (64mm): Skills, Certifications, Education
    right_flow = []

    # Section: Skills
    right_flow.append(Paragraph('TECHNICAL ARSENAL', section_h_style))
    right_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))

    skills_data = [
        ("Backend", "<b>Laravel 10/11</b>, PHP 8.x, REST APIs, Sanctum, Passport, Queues, Horizon, Events, Jobs."),
        ("Databases", "<b>MySQL</b>, PostgreSQL, <b>Redis Caching</b>, Schema Optimization, Indexing."),
        ("DevOps & Cloud", "<b>Docker &amp; Compose</b>, GitHub Actions, GitLab CI, AWS (EC2, S3), Nginx, Linux VPS."),
        ("AI & Automation", "<b>AI Agents</b>, LangChain, OpenAI, <b>n8n Workflows</b>, RAG, Vector Search."),
        ("Frontend & Tools", "Vue.js, Livewire, JavaScript / Ajax, Tailwind CSS, Postman, Git.")
    ]
    for cat, desc in skills_data:
        right_flow.append(Paragraph(cat, skill_category_style))
        right_flow.append(Paragraph(desc, skill_desc_style))
        right_flow.append(Spacer(1, 1.4*mm))

    right_flow.append(Spacer(1, 1.5*mm))

    # Section: Certifications
    right_flow.append(Paragraph('CREDENTIALS &amp; CERTS', section_h_style))
    right_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))

    certs = [
        ("AWS Cloud Practitioner", "Amazon Web Services (In Progress)"),
        ("PHP & Laravel — Advanced", "Udemy · Completed 2022"),
        ("AI Agents & LangChain", "DeepLearning.AI · Completed 2025")
    ]
    for c_title, c_org in certs:
        p_c = Paragraph(f"<b>{c_title}</b><br/><font color='#64748b' size='7'>{c_org}</font>", bullet_style)
        t_c = Table([[p_c]], colWidths=[63*mm])
        t_c.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
            ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
            ('TOPPADDING', (0,0), (-1,-1), 1.5*mm),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1.5*mm),
            ('LEFTPADDING', (0,0), (-1,-1), 2*mm),
            ('RIGHTPADDING', (0,0), (-1,-1), 2*mm),
        ]))
        right_flow.append(t_c)
        right_flow.append(Spacer(1, 1.2*mm))

    right_flow.append(Spacer(1, 1.5*mm))

    # Section: Education
    right_flow.append(Paragraph('EDUCATION', section_h_style))
    right_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))
    edu_text = (
        "<b>B.Sc. in Computer Science &amp; Engineering</b><br/>"
        "<font color='#16a34a'>Dhaka, Bangladesh</font><br/>"
        "<font color='#64748b' size='7'>Algorithms, Data Structures, Database Architecture, OOP.</font>"
    )
    right_flow.append(Paragraph(edu_text, bullet_style))
    right_flow.append(Spacer(1, 2.5*mm))

    # Section: Languages & Style
    right_flow.append(Paragraph('LANGUAGES &amp; STYLE', section_h_style))
    right_flow.append(HRFlowable(width="100%", thickness=0.8, color=BORDER_COLOR, spaceBefore=1*mm, spaceAfter=2*mm))
    style_text = (
        "• <b>English</b>: Fluent (Professional working)<br/>"
        "• <b>Bengali</b>: Native<br/>"
        "• Async-first &amp; clean documentation<br/>"
        "• Timezone flexible for EU / US overlap"
    )
    right_flow.append(Paragraph(style_text, bullet_style))

    # Assemble 2-Column Table
    t_main = Table([[left_flow, right_flow]], colWidths=[119*mm, 67*mm])
    t_main.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_main)

    doc.build(story)
    print("PDF build complete:", filename)

if __name__ == '__main__':
    target = r"c:\laragon\www\newsite\portfolio\portfolio\assets\cv\Shah_Md_Arafatul_Rahman_CV.pdf"
    build_pdf(target)
