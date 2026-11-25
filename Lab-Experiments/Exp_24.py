baseline = {
    "Firewall": True,
    "Antivirus": True,
    "Encryption": True,
    "Multi-Factor Authentication": True,
    "Regular Backup": True
}

# Current security configuration
current = {
    "Firewall": True,
    "Antivirus": True,
    "Encryption": False,
    "Multi-Factor Authentication": False,
    "Regular Backup": True
}

print("--- Security Baseline Assessment ---")

failed = []

for control, required in baseline.items():
    status = current.get(control, False)

    if status == required:
        print(control, ": PASS")
    else:
        print(control, ": FAIL")
        failed.append(control)

print("\n--- Assessment Report ---")

print("Total Controls:", len(baseline))
print("Passed Controls:", len(baseline) - len(failed))
print("Failed Controls:", len(failed))

if failed:
    print("\nControls Requiring Improvement:")
    for control in failed:
        print("-", control)
else:
    print("All security controls meet the baseline.")
