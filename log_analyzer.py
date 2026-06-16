from brute_force import detect_bruteforce
from alert import generate_alert


def analyze_log():

    with open(
        "login_attempts.log",
        "r"
    ) as file:

        for line in file:

            parts = line.strip().split()

            if len(parts) != 2:
                continue

            ip = parts[0]
            status = parts[1]

            if status == "FAILED":

                attacker = detect_bruteforce(
                    ip
                )

                if attacker:

                    generate_alert(
                        f"Brute Force Attack Detected from {attacker}",
                        "HIGH"
                    )