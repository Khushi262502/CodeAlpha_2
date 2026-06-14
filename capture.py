from scapy.all import *
from alert import generate_alert
from port_scan import detect_port_scan



def packet_callback(packet):

    try:

        if packet.haslayer(IP):

            protocol = packet[IP].proto
            attacker = detect_port_scan(
                packet
            )

            if attacker:
                generate_alert(
                    f"Port Scan Detected from {attacker}",
                    "MEDIUM"
                )

            if protocol == 6:
                proto_name = "TCP"
                
                    
                

            elif protocol == 17:
                proto_name = "UDP"

            elif protocol == 1:
                proto_name = "ICMP"
                generate_alert(
                    "ICMP Packet Detected",
                    "LOW"
                )

            else:
                proto_name = "OTHER"
                generate_alert(
                    "Unknown Protocol Found",
                    "LOW"
                )

            print(
                f"Source: {packet[IP].src}"
            )

            print(
                f"Destination: {packet[IP].dst}"
            )

            print(
                f"Protocol: {proto_name}"
            )

            print("-" * 40)

    except Exception as e:

        print("Error:", e)

        
def start_capture():

    sniff(
        prn=packet_callback,
        store=False,
        timeout = 50

    )