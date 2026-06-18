from flask import Flask

from alert_store import get_alerts

app = Flask(__name__)

@app.route("/")

def home():

    html = """

    <h1>Network IDS Dashboard</h1>

    """

    for alert in get_alerts():

        html += f"<p>{alert}</p>"

    return html


def start_dashboard():

    app.run(
        debug=False,
        use_reloader=False
    )