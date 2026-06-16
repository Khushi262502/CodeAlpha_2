from collections import defaultdict

dns_counter = defaultdict(int)

alerted_domains = set()


def detect_dns_abuse(domain):

    dns_counter[domain] += 1

    print(
        f"{domain} -> {dns_counter[domain]}"
    )

    if dns_counter[domain] >= 10:

        if domain not in alerted_domains:

            alerted_domains.add(
                domain
            )

            return domain

    return None