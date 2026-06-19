from alert_store import add_alert
from email_alert import send_email_alert
def generate_alert(
    attack_type,
    severity
):
    if severity == "CRITICAL":
        send_email_alert(
            attack_type,
            severity
        )
    add_alert(
        f"[{severity}] {attack_type}"

    )


    print("\n" + "=" * 50)

    print(
        f"[{severity}] {attack_type}"
    )

    print("=" * 50)