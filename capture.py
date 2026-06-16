from scapy.all import *

from alert import generate_alert
from port_scan import detect_port_scan
from icmp_flood import detect_icmp_flood
from dns_detector import detect_dns_abuse

from scapy.layers.dns import DNS
from threat_intel import check_blacklisted_ip


def packet_callback(packet):

    try:

        

        if packet.haslayer(IP):
            src_ip = packet[IP].src

            dst_ip = packet[IP].dst
            print("Checking",src_ip,dst_ip)
            if check_blacklisted_ip(src_ip):

                generate_alert(
                f"Blacklisted IP Detected: {src_ip}",
                "CRITICAL"
    )

            if check_blacklisted_ip(dst_ip):

                generate_alert(
                f"Blacklisted IP Detected: {dst_ip}",
                "CRITICAL"
    )

            # -------------------------
            # DNS Detection
            # -------------------------

            if packet.haslayer(DNS):

                try:

                    if packet[DNS].qd:

                        domain = packet[DNS].qd.qname.decode(
                            errors="ignore"
                        ).rstrip(".")

                        print(
                            f"DNS Query: {domain}"
                        )

                        suspicious = detect_dns_abuse(
                            domain
                        )

                        if suspicious:

                            generate_alert(
                                f"Excessive DNS Queries for {domain}",
                                "MEDIUM"
                            )

                except Exception as e:

                    print(
                        "DNS Error:",
                        e
                    )

            # -------------------------
            # Port Scan Detection
            # -------------------------

            if packet.haslayer(TCP):

                attacker = detect_port_scan(
                    packet
                )

                if attacker:

                    generate_alert(
                        f"Port Scan Detected from {attacker}",
                        "MEDIUM"
                    )

            # -------------------------
            # Protocol Detection
            # -------------------------

            protocol = packet[IP].proto

            if protocol == 6:

                proto_name = "TCP"

            elif protocol == 17:

                proto_name = "UDP"

            elif protocol == 1:

                proto_name = "ICMP"

                attacker = detect_icmp_flood(
                    packet
                )

                if attacker:

                    generate_alert(
                        f"ICMP Flood Detected from {attacker}",
                        "HIGH"
                    )

            else:

                proto_name = "OTHER"

            # -------------------------
            # Packet Information
            # -------------------------

            print(
                f"Source: {packet[IP].src}"
            )

            print(
                f"Destination: {packet[IP].dst}"
            )

            print(
                f"Protocol: {proto_name}"
            )

            print(
                "-" * 40
            )

    except Exception as e:

        print(
            "Error:",
            e
        )


def start_capture():

    print(
        "Network IDS Started..."
    )

    sniff(
        prn=packet_callback,
        store=False,
        timeout=50
    )