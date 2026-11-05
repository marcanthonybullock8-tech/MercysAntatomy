"""Mercy's Anatomy episode PDF builder (MA-009 package).

Usage: python3 ep_build.py <config.py>
The config defines OUT, PARTS, EP (date), CODE ("2x02"), SEASON_LINE, TITLE, COUNTERPART,
DATES, DEPENDS, CAST [(name, role, date)], ALSO, MEDIA [(head, sub, [paras])],
and CONT (list of flowables built with the helpers exported below).
Part files use the screenplay DSL: X: marker, H: heading, T: time, A: action,
C: NAME| (paren)| dialogue  or  C: NAME| dialogue, R: transition, I: boxed insert.
"""
import sys, re
from datetime import date
from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
                                KeepTogether, CondPageBreak, Flowable)

NAVY = colors.HexColor('#1F2A44'); RED = colors.HexColor('#9B1B30'); GREY = colors.HexColor('#F2F2F5')
BOXBG = colors.HexColor('#FBF3F4'); MEDBG = colors.HexColor('#FBFAF7')

# ---------- document styles ----------
T = ParagraphStyle('T', fontName='Times-Bold', fontSize=30, leading=36, alignment=1, textColor=NAVY, spaceAfter=6)
ST = ParagraphStyle('ST', fontName='Times-Italic', fontSize=13, leading=16, alignment=1, textColor=RED, spaceAfter=4)
TT = ParagraphStyle('TT', fontName='Times-BoldItalic', fontSize=20, leading=25, alignment=1, textColor=NAVY, spaceAfter=12)
C = ParagraphStyle('C', fontName='Times-Roman', fontSize=10.5, leading=14, alignment=1, spaceAfter=5)
B = ParagraphStyle('B', fontName='Times-Roman', fontSize=10.5, leading=14, spaceAfter=5)
H1 = ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=NAVY, spaceBefore=6, spaceAfter=8)
H2 = ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=11.5, leading=15, textColor=RED, spaceBefore=8, spaceAfter=5)
TC = ParagraphStyle('TC', fontName='Times-Roman', fontSize=9.5, leading=12)
TH = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.white)
BL = ParagraphStyle('BL', parent=B, leftIndent=14, bulletIndent=4)
MH = ParagraphStyle('MH', fontName='Times-Bold', fontSize=10.5, leading=13.5, spaceAfter=2)
MS = ParagraphStyle('MS', fontName='Times-Italic', fontSize=8.8, leading=11, textColor=colors.grey, spaceAfter=4)
MB = ParagraphStyle('MB', fontName='Times-Roman', fontSize=10, leading=13.5, spaceAfter=4)

def p(t, s=B): return Paragraph(t, s)
def bl(items): return [Paragraph(x, BL, bulletText='•') for x in items]
def box(t):
    tb = Table([[Paragraph(t, B)]], colWidths=[6.3*inch])
    tb.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 0.9, RED), ('BACKGROUND', (0,0), (-1,-1), BOXBG),
        ('LEFTPADDING', (0,0), (-1,-1), 7), ('RIGHTPADDING', (0,0), (-1,-1), 7), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
    return tb
def tbl(rows, widths):
    data = [[Paragraph(str(c), TH) for c in rows[0]]] + [[Paragraph(str(c), TC) for c in r] for r in rows[1:]]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), NAVY), ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, GREY]),
        ('GRID', (0,0), (-1,-1), 0.3, colors.HexColor('#BBBBC5')), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 4), ('RIGHTPADDING', (0,0), (-1,-1), 4), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3)]))
    return t
def media(head, sub, body):
    inner = [Paragraph(head, MH), Paragraph(sub, MS)] + [Paragraph(x, MB) for x in body]
    t = Table([[inner]], colWidths=[6.3*inch])
    t.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 0.6, colors.HexColor('#8A8A92')), ('BACKGROUND', (0,0), (-1,-1), MEDBG),
        ('LEFTPADDING', (0,0), (-1,-1), 8), ('RIGHTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 7), ('BOTTOMPADDING', (0,0), (-1,-1), 5)]))
    return [t, Spacer(1, 7)]

# ---------- screenplay styles (Courier 12; 1.5" left, 1" right margins) ----------
F = 'Courier'; FB = 'Courier-Bold'
SA = ParagraphStyle('SA', fontName=F, fontSize=12, leading=14, spaceAfter=12)
SH = ParagraphStyle('SH', fontName=FB, fontSize=12, leading=14, spaceBefore=0, spaceAfter=0)
STM = ParagraphStyle('STM', fontName=F, fontSize=12, leading=14, spaceAfter=12)
SC = ParagraphStyle('SC', fontName=F, fontSize=12, leading=14, leftIndent=2.2*inch, spaceAfter=0)
SP = ParagraphStyle('SP', fontName=F, fontSize=12, leading=14, leftIndent=1.6*inch, rightIndent=2.3*inch, spaceAfter=0)
SD = ParagraphStyle('SD', fontName=F, fontSize=12, leading=14, leftIndent=1.0*inch, rightIndent=1.5*inch, spaceAfter=12)
SR = ParagraphStyle('SR', fontName=F, fontSize=12, leading=14, alignment=2, spaceAfter=12)
SX = ParagraphStyle('SX', fontName=FB, fontSize=12, leading=14, alignment=1, spaceBefore=6, spaceAfter=18)
SI = ParagraphStyle('SI', fontName=F, fontSize=10.5, leading=13)

class Mark(Flowable):
    def __init__(self, key, store): Flowable.__init__(self); self.key = key; self.store = store
    def wrap(self, w, h): return (0, 0)
    def draw(self): self.store[self.key] = self.canv.getPageNumber()

def esc(t): return escape(t)

def script_flow(parts):
    out = []; n = 0
    lines = []
    for f in parts: lines += [l.rstrip('\n') for l in open(f, encoding='utf-8')]
    i = 0
    while i < len(lines):
        l = lines[i]; i += 1
        if not l.strip(): continue
        tag, _, body = l.partition(': ')
        body = body.strip()
        if tag == 'X':
            out.append(Paragraph(esc(body), SX))
            if body.startswith('END OF ACT') or body == 'END OF EPISODE':
                if body != 'END OF EPISODE': out.append(PageBreak())
        elif tag == 'H':
            n += 1
            head = Paragraph(f"{n}&nbsp;&nbsp;&nbsp;{esc(body)}", SH)
            nxt = []
            if i < len(lines) and lines[i].startswith('T: '):
                nxt.append(Paragraph(esc(lines[i][3:].strip()), STM)); i += 1
            out.append(KeepTogether([head] + nxt))
        elif tag == 'T': out.append(Paragraph(esc(body), STM))
        elif tag == 'A': out.append(Paragraph(esc(body), SA))
        elif tag == 'R': out.append(Paragraph(esc(body), SR))
        elif tag == 'I':
            tb = Table([[Paragraph(esc(body), SI)]], colWidths=[5.6*inch])
            tb.setStyle(TableStyle([('BOX', (0,0), (-1,-1), 0.8, colors.black), ('LEFTPADDING', (0,0), (-1,-1), 6), ('RIGHTPADDING', (0,0), (-1,-1), 6), ('TOPPADDING', (0,0), (-1,-1), 4), ('BOTTOMPADDING', (0,0), (-1,-1), 4)]))
            out += [tb, Spacer(1, 12)]
        elif tag == 'C':
            bits = [b.strip() for b in body.split('|')]
            name = bits[0]; paren = None
            if len(bits) == 3: paren, dlg = bits[1], bits[2]
            else: dlg = bits[-1]
            blk = [Paragraph(esc(name), SC)]
            if paren: blk.append(Paragraph(esc(paren), SP))
            blk.append(Paragraph(esc(dlg), SD))
            out.append(KeepTogether(blk))
        else:
            raise SystemExit(f"Unknown line in script: {l[:60]}")
    return out, n

def age(dob, on): return on.year - dob.year - ((on.month, on.day) < (dob.month, dob.day))

def build(cfg):
    marks = {}
    s = [Spacer(1, 1.6*inch), p("MERCY'S ANATOMY", T), p(cfg.SEASON_LINE, ST), p(f'"{cfg.TITLE}"', TT),
         p(cfg.COUNTERPART + " Narrator: Dr. Marc-Anthony Bullock", C), p("In-story dates: " + cfg.DATES, C),
         p("Script: Cold Open + 5 Acts + Tag. {SCENES} scenes. Standard: MA-009", C), p(cfg.DEPENDS, C), Spacer(1, 0.3*inch),
         box(f"<b>EPISODE PDF PACKAGE (MA-009 §6):</b> 1. Title page and cast (with ages on {cfg.AGES_ON}). 2. Script. 3. Media Companion. 4. Continuity Sheet."),
         PageBreak()]
    rows = [["Character", "Role in this episode", "Born", "Age"]]
    for nm, role, d in cfg.CAST: rows.append([esc(nm), esc(role), d.strftime("%b %-d, %Y"), str(age(d, cfg.EP))])
    s += [p(f"Cast in Order of Appearance (Ages on {cfg.AGES_ON})", H1), tbl(rows, [2.0*inch, 2.4*inch, 1.1*inch, 0.6*inch]),
          Spacer(1, 6), p(cfg.ALSO), PageBreak()]
    flow, n = script_flow(cfg.PARTS)
    s += [Mark('start', marks)] + flow + [Mark('end', marks), PageBreak()]
    s += [p(f"Media Companion: Episode {cfg.CODE}" + (f" ({cfg.TAGNAME})" if getattr(cfg, 'TAGNAME', '') else ''), H1),
          p("<i>Off-screen media around the episode, in chronological order. Not counted in page length (MA-009 §5).</i>")]
    for head, sub, body in cfg.MEDIA: s += media(head, sub, body)
    s.append(PageBreak())
    s += cfg.CONT
    s[6] = p(f"Script: Cold Open + 5 Acts + Tag. {n} scenes. Standard: MA-009", C)
    foot_txt = f"MERCY'S ANATOMY  {cfg.CODE}  \"{cfg.TITLE}\""
    def foot(c, d):
        c.saveState(); c.setFont('Courier', 8); c.setFillColor(colors.grey)
        c.drawString(1.0*inch, 0.5*inch, foot_txt); c.drawRightString(7.5*inch, 0.5*inch, f"{d.page}."); c.restoreState()
    doc = SimpleDocTemplate(cfg.OUT, pagesize=letter, leftMargin=1.5*inch, rightMargin=1.0*inch, topMargin=1.0*inch, bottomMargin=1.0*inch,
                            title=f"Mercy's Anatomy {cfg.CODE} - {cfg.TITLE}", author="Mercy's Anatomy")
    doc.build(s, onFirstPage=foot, onLaterPages=foot)
    print("scenes", n, "script pages", marks['end'] - marks['start'], marks)

if __name__ == '__main__':
    import importlib.util
    spec = importlib.util.spec_from_file_location('cfg', sys.argv[1]); cfg = importlib.util.module_from_spec(spec)
    sys.modules['cfg'] = cfg; spec.loader.exec_module(cfg); build(cfg)
