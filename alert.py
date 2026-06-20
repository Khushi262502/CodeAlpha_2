from alert_store import add_alert
from email_alert import send_email_alert
from logger import log_alert
def generate_alert(
    attack_type,
    severity
):
    EMAIL_ENABLED = False
    if severity == "CRITICAL" and EMAIL_ENABLED:
        send_email_alert(
            attack_type,
            severity
        )
    add_alert(
        f"[{severity}] {attack_type}"

    )
    log_alert(
        attack_type,
        severity
    )


    print("\n" + "=" * 50)

    print(
        f"[{severity}] {attack_type}"
    )

    print("=" * 50)