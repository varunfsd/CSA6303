
from collections import Counter

# Simulated event dataset
events = [
    {"source": "Firewall", "status": "Failed", "ip": "192.168.1.10"},
    {"source": "Server", "status": "Success", "ip": "192.168.1.20"},
    {"source": "Firewall", "status": "Failed", "ip": "192.168.1.10"},
    {"source": "IDS", "status": "Failed", "ip": "192.168.1.30"},
    {"source": "Server", "status": "Success", "ip": "192.168.1.20"}
]

# Step 1: Search filter
search = input("Enter status to search (Failed/Success): ")

filtered = [
    event for event in events
    if event["status"].lower() == search.lower()
]

print("\n--- Search Results ---")
for event in filtered:
    print(event)

# Step 2: Stats count by field
field = input("\nEnter field to count by (source/ip/status): ")

if field in ["source", "ip", "status"]:
    counts = Counter(event[field] for event in filtered)

    print("\n--- Stats Count by", field, "---")
    for key, count in counts.items():
        print(key, ":", count)
else:
    print("Invalid field!")
