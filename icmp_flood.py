from collections import defaultdict

icmp_counter = defaultdict(int)

alerted_ips = set()

def detect_icmp_flood(packet):

    try:

        src_ip = packet["IP"].src

        icmp_counter[src_ip] += 1

        print(
            f"ICMP Count for {src_ip}: {icmp_counter[src_ip]}"
        )

        if icmp_counter[src_ip] >= 20:

            if src_ip not in alerted_ips:

                alerted_ips.add(src_ip)

                return src_ip

    except:
        pass

    return None