from flask import Flask

from alert_store import get_alerts,get_stats


app = Flask(__name__)

@app.route("/")

def home():

    stats = get_stats()

    html =  f"""

    <h1>Network IDS Dashboard</h1>

    <h2>Statistics</h2>

    <p>Total Alerts: {stats['total']}</p>

    <p>Critical Alerts: {stats['critical']}</p>

    <p>High Alerts: {stats['high']}</p>

    <p>Medium Alerts: {stats['medium']}</p>

    <p>Threat Intel Alerts: {stats['threat_intel']}</p>

    <hr>

    <h2>Recent Alerts</h2>

    """

    for alert in get_alerts():

        html += f"<p>{alert}</p>"

    return html


def start_dashboard():

    app.run(
        debug=False,
        use_reloader=False
    )