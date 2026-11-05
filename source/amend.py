import sys
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer
from pypdf import PdfReader, PdfWriter
sys.path.insert(0, '.')
from ep_build import p, bl, box, tbl, H1, H2, B
def page(path, size, doc_id):
    s = [p(f"{doc_id} Amendment A-1 (November 2026)", H1),
         box("<b>Creator-approved change.</b> This amendment page supersedes the billing and status shown elsewhere in this document wherever they differ."),
         Spacer(1, 8), p("Dr. Horace Whitlow: on-screen debut moved to Season 2", H2)]
    s += bl(["<b>Old:</b> RECURRING, Seasons 1-6.",
             "<b>New:</b> RECURRING, Seasons 2-6. Dr. Whitlow (b. September 19, 1949, Chief of Medicine and Natasha's political rival) does not appear in Season 1. "
             "His on-screen debut is <b>2x02 'Say When'</b> (Monday, October 3, 2005), where he moves that the Board review the Victor Donohue Foundation's relationships with QGH staff.",
             "<b>Season count:</b> 5 seasons (S2-S6), down from 6. Season 1 Recurring headcount drops by one.",
             "Age at his Season 2 debut (October 3, 2005): 56."])
    s.append(tbl([["ID", "Established fact", "Source"],
                  ["C-077", "Dr. Horace Whitlow debuts on screen in 2x02. Billing: RECURRING, Seasons 2-6.", "2x02; creator approval"]],
                 [0.7*inch, 4.6*inch, 1.3*inch]))
    m = 0.75*inch
    SimpleDocTemplate(path, pagesize=size, leftMargin=m, rightMargin=m, topMargin=m, bottomMargin=m).build(s)
for doc, size, did in [("MA-005_Character_Bible_Vol1.pdf", letter, "MA-005"), ("MA-006_Cast_Table.pdf", landscape(letter), "MA-006")]:
    src = "/home/user/MercysAntatomy/PDFs/" + doc
    page("amend_tmp.pdf", size, did)
    w = PdfWriter()
    for pg in PdfReader(src).pages: w.add_page(pg)
    for pg in PdfReader("amend_tmp.pdf").pages: w.add_page(pg)
    with open(src, "wb") as f: w.write(f)
    print(doc, len(PdfReader(src).pages))
