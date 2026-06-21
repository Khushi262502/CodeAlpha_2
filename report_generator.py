from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from alert_store import (
    get_alerts,
    get_stats
)


def generate_report():

    doc = SimpleDocTemplate(
        "incident_report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    stats = get_stats()

    elements.append(
        Paragraph(
            "Network IDS Incident Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(
            1,
            20
        )
    )

    elements.append(
        Paragraph(
            f"Total Alerts: {stats['total']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Critical Alerts: {stats['critical']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"High Alerts: {stats['high']}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Medium Alerts: {stats['medium']}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(
            1,
            20
        )
    )

    elements.append(
        Paragraph(
            "Recent Alerts",
            styles["Heading2"]
        )
    )

    for alert in get_alerts()[-20:]:

        elements.append(
            Paragraph(
                alert,
                styles["Normal"]
            )
        )

    doc.build(
        elements
    )

    print(
        "Incident Report Generated!"
    )