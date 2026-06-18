from alert_store import add_alert
def generate_alert(
    attack_type,
    severity
):
    add_alert(
        f"[{severity}] {attack_type}"

    )


    print("\n" + "=" * 50)

    print(
        f"[{severity}] {attack_type}"
    )

    print("=" * 50)