
from collections import defaultdict

events = [
    {"source": "Firewall", "ip": "192.168.1.10", "event": "Failed Login"},
    {"source": "Server", "ip": "192.168.1.10", "event": "Failed Login"},
    {"source": "IDS", "ip": "192.168.1.10", "event": "Failed Login"},
    {"source": "Firewall", "ip": "192.168.1.20", "event": "Success Login"}
]

normalized = []

for e in events:
    normalized.append({
        "source": e["source"],
        "ip": e["ip"],
        "event": e["event"].lower()
    })

print("Normalized Events:")
for e in normalized:
    print(e)

count = defaultdict(int)

for e in normalized:
    if e["event"] == "failed login":
        count[e["ip"]] += 1

# Step 4: Generate alerts
print("\nSIEM Security Alerts:")

alert_found = False

for ip, attempts in count.items():
    if attempts >= 3:
        print(f"ALERT: Suspicious login activity from {ip}")
        print(f"Failed Attempts: {attempts}")
        alert_found = True

if not alert_found:
    print("No suspicious activity detected.")
