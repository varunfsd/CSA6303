
properties = [
    ("Data Encryption", "Confidentiality", True),
    ("Access Control", "Confidentiality", False),
    ("Data Accuracy", "Integrity", True),
    ("File Integrity", "Integrity", False),
    ("Server Uptime", "Availability", True),
    ("Backup System", "Availability", False)
]

violations = set()

for name, principle, status in properties:
    if not status:
        violations.add(principle)

print("--- CIA Security Assessment ---")

for name, principle, status in properties:
    print(name, ":", "PASS" if status else "FAIL")

print("\nViolated CIA Principles:")

if violations:
    for principle in sorted(violations):
        print("-", principle)
else:
    print("No CIA violations detected")
