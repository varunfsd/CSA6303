
from collections import defaultdict
from datetime import datetime, timedelta

# Simulated web server logs
logs = [
    ("192.168.1.10", "10:00:01"),
    ("192.168.1.10", "10:00:02"),
    ("192.168.1.10", "10:00:03"),
    ("192.168.1.10", "10:00:04"),
    ("192.168.1.10", "10:00:05"),
    ("192.168.1.20", "10:00:06"),
    ("192.168.1.20", "10:00:07")
]

threshold = 4
time_window = timedelta(seconds=10)

def detect_dos(logs):
    requests = defaultdict(list)

    for ip, timestamp in logs:
        time = datetime.strptime(timestamp, "%H:%M:%S")
        requests[ip].append(time)

    print("--- DoS Attack Detection ---")

    for ip, times in requests.items():
        times.sort()
        start = 0
        detected = False

        for end in range(len(times)):
            while times[end] - times[start] > time_window:
                start += 1

            count = end - start + 1

            if count > threshold:
                print("ALERT: Possible DoS Attack!")
                print("IP Address:", ip)
                print("Requests:", count)
                detected = True
                break

        if not detected:
            print("IP:", ip, "- Normal Traffic")

detect_dos(logs)
