
# Signature-based IDS

signatures = [
    {"protocol": "TCP", "port": 80, "pattern": "sql injection"},
    {"protocol": "TCP", "port": 21, "pattern": "unauthorized login"},
    {"protocol": "UDP", "port": 53, "pattern": "malicious dns"}
]

# Simulated network packets
packets = [
    {"protocol": "TCP", "port": 80, "data": "sql injection attempt"},
    {"protocol": "TCP", "port": 443, "data": "sql injection attempt"},
    {"protocol": "TCP", "port": 21, "data": "unauthorized login"},
    {"protocol": "UDP", "port": 53, "data": "malicious dns query"},
    {"protocol": "TCP", "port": 80, "data": "normal request"}
]

def detect_intrusion(packet):
    for rule in signatures:
        if (packet["protocol"] == rule["protocol"]
            and packet["port"] == rule["port"]
            and rule["pattern"] in packet["data"].lower()):
            return "ALERT: Intrusion Detected"

    return "SAFE: No Threat Detected"


print("--- Signature-Based IDS ---")

for packet in packets:
    print("Protocol:", packet["protocol"])
    print("Port:", packet["port"])
    print("Data:", packet["data"])
    print("Result:", detect_intrusion(packet))
    print()
