
import time
from collections import defaultdict

baseline = {
    "max_failed_attempts": 3,
    "allowed_ips": ["192.168.1.10", "192.168.1.20"]
}

login_events = [
    {"user": "admin", "ip": "192.168.1.10", "status": "success"},
    {"user": "admin", "ip": "192.168.1.10", "status": "failed"},
    {"user": "admin", "ip": "192.168.1.10", "status": "failed"},
    {"user": "admin", "ip": "192.168.1.10", "status": "failed"},
    {"user": "guest", "ip": "10.0.0.5", "status": "success"}
]

failed_counts = defaultdict(int)

print("--- Continuous Security Monitoring ---")

for event in login_events:
    time.sleep(1)

    user = event["user"]
    ip = event["ip"]
    status = event["status"]

    print("\nUser:", user, "| IP:", ip, "| Status:", status)

    if ip not in baseline["allowed_ips"]:
        print("ALERT: Login from unknown IP address!")

    if status == "failed":
        failed_counts[user] += 1

        if failed_counts[user] >= baseline["max_failed_attempts"]:
            print("ALERT: Multiple failed login attempts!")

    elif status == "success":
        failed_counts[user] = 0

print("\nSecurity Monitoring Completed")
