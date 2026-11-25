def firewall(packet, rules):
    for rule in rules:
        if (rule["protocol"] == packet["protocol"]
                and rule["port"] == packet["port"]):
            return rule["action"]

    return "DENY" 
packet = {"protocol": "TCP", "port": 80}

rules1 = [
    {"protocol": "TCP", "port": 80, "action": "ALLOW"},
    {"protocol": "TCP", "port": 80, "action": "DENY"}
]

rules2 = [
    {"protocol": "TCP", "port": 80, "action": "DENY"},
    {"protocol": "TCP", "port": 80, "action": "ALLOW"}
]

print("--- Firewall Rule Engine ---")

print("Packet:", packet)

print("\nRule Set 1 (ALLOW first):")
print("Result:", firewall(packet, rules1))

print("\nRule Set 2 (DENY first):")
print("Result:", firewall(packet, rules2))

# Test default-deny
unknown_packet = {"protocol": "TCP", "port": 9999}

print("\nUnknown Packet:", unknown_packet)
print("Result:", firewall(unknown_packet, rules1))
