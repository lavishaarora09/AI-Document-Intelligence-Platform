from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(stats, summary, keywords):

    doc = SimpleDocTemplate("AI_Report.pdf")

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI DOCUMENT INTELLIGENCE REPORT</b>", styles["Title"]))

    story.append(Paragraph(f"Pages : {stats['Pages']}", styles["BodyText"]))
    story.append(Paragraph(f"Characters : {stats['Characters']}", styles["BodyText"]))
    story.append(Paragraph(f"Words : {stats['Words']}", styles["BodyText"]))
    story.append(Paragraph(f"Sentences : {stats['Sentences']}", styles["BodyText"]))
    story.append(Paragraph(f"Keywords : {stats['Keywords']}", styles["BodyText"]))
    story.append(Paragraph(f"Reading Time : {stats['Reading Time']} minutes", styles["BodyText"]))

    story.append(Paragraph("<br/><b>AI Summary</b>", styles["Heading2"]))
    story.append(Paragraph(summary, styles["BodyText"]))

    story.append(Paragraph("<br/><b>Top Keywords</b>", styles["Heading2"]))

    for word in keywords:
        story.append(Paragraph(f"• {word}", styles["BodyText"]))

    doc.build(story)

    return "AI_Report.pdf"