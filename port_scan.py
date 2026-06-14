from collections import defaultdict

scanned_ports = defaultdict(set)

alerted_ips = set()

def detect_port_scan(packet):

    try:

        src_ip = packet["IP"].src

        dst_port = packet["TCP"].dport

        scanned_ports[src_ip].add(
            dst_port
        )

        print(
            f"{src_ip} -> Port {dst_port}"
        )

        print(
            f"Unique Ports: {len(scanned_ports[src_ip])}"
        )

        if len(scanned_ports[src_ip]) >= 10:

            if src_ip not in alerted_ips:

                alerted_ips.add(src_ip)

                return src_ip

    except Exception as e:

        print(e)

    return None