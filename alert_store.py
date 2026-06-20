alerts = []

def add_alert(alert):

    alerts.append(alert)

def get_alerts():

    return alerts

def get_stats():

    total = len(alerts)

    critical = sum(
        1 for alert in alerts
        if "[CRITICAL]" in alert
    )

    high = sum(
        1 for alert in alerts
        if "[HIGH]" in alert
    )

    medium = sum(
        1 for alert in alerts
        if "[MEDIUM]" in alert
    )

    return {
        "total": total,
        "critical": critical,
        "high": high,
        "medium": medium
    }