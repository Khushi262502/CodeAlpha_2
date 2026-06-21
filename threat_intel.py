alerted_ips = set()

def load_blacklist():

    try:

        with open(
            "blacklist.txt",
            "r"
        ) as file:

            return set(
                line.strip()
                for line in file
                if line.strip()
            )

    except FileNotFoundError:

        return set()


def check_blacklisted_ip(ip):

    blacklisted_ips = load_blacklist()

    if ip in blacklisted_ips:

        if ip not in alerted_ips:

            alerted_ips.add(ip)

            return True

    return False