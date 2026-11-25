
from collections import Counter

events = [
    {"ip": "192.168.1.10", "event": "failed login"},
    {"ip": "192.168.1.10", "event": "failed login"},
    {"ip": "192.168.1.10", "event": "failed login"},
    {"ip": "192.168.1.20", "event": "success login"},
    {"ip": "10.0.0.5", "event": "malware detected"}
]

threat_intelligence = ["192.168.1.10", "10.0.0.5"]

def hypothesis_based(events):
    print("\n--- Hypothesis-Based Hunting ---")
    for event in events:
        if event["event"] == "failed login":
            print("Suspicious Login:", event)

def intelligence_based(events):
    print("\n--- Intelligence-Based Hunting ---")
    for event in events:
        if event["ip"] in threat_intelligence:
            print("Known Threat IP:", event)

def analytics_based(events):
    print("\n--- Analytics-Based Hunting ---")
    counts = Counter(
        event["ip"] for event in events
        if event["event"] == "failed login"
    )

    for ip, count in counts.items():
        if count >= 3:
            print("ALERT: Repeated Failed Logins")
            print("IP:", ip, "Attempts:", count)

hypothesis_based(events)
intelligence_based(events)
analytics_based(events)
