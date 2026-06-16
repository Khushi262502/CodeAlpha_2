from scapy.all import *

for i in range(30):

    send(
        IP(dst="192.168.56.1")/
        ICMP(),
        verbose=False
    )

print("ICMP Flood Sent")