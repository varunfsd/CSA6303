
# Signature-based IPS simulation

signatures = ["malware", "sql injection", "port scan"]

# Trusted IP whitelist
whitelist = ["192.168.1.10"]

# Simulated network traffic
traffic = [
    {"ip": "192.168.1.20", "data": "normal request"},
    {"ip": "192.168.1.30", "data": "malware detected"},
    {"ip": "192.168.1.10", "data": "port scan"},
    {"ip": "192.168.1.40", "data": "sql injection"}
]

def ips_check(packet):
    ip = packet["ip"]
    data = packet["data"].lower()

    if ip in whitelist:
        return "ALLOWED (Trusted Source)"

    for signature in signatures:
        if signature in data:
            return "BLOCKED (Threat: " + signature + ")"

    return "ALLOWED (Safe Traffic)"


print("--- Intrusion Prevention System ---")

for packet in traffic:
    result = ips_check(packet)
    print("IP:", packet["ip"])
    print("Traffic:", packet["data"])
    print("Action:", result)
    print()
