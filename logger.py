from datetime import datetime


def log_alert(
    attack_type,
    severity
):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with open(
        "alerts.log",
        "a"
    ) as file:

        file.write(
            f"{timestamp} | {severity} | {attack_type}\n"
        )