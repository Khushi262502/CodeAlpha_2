blacklisted_ips = {
    "192.168.1.31",
    "185.220.101.1",
    "45.33.32.156",
    "103.21.244.0"
}

def check_blacklisted_ip(ip):

    print("BLACKLIST CHECK:", ip)

    if ip in blacklisted_ips:

        print("MATCH FOUND!")

        return True

    return False