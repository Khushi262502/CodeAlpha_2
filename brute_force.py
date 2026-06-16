from collections import defaultdict

failed_attempts = defaultdict(int)

alerted_ips = set()


def detect_bruteforce(ip):

    failed_attempts[ip] += 1

    print(
        f"{ip} -> Failed Attempts: {failed_attempts[ip]}"
    )

    if failed_attempts[ip] >= 5:

        if ip not in alerted_ips:

            alerted_ips.add(ip)

            return ip

    return None