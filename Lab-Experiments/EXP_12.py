def assign_priority(alert):
    alert = alert.lower()

    if any(word in alert for word in [
        "ransomware", "data breach", "active attack",
        "privilege escalation", "critical server compromised",
        "mass data exfiltration"
    ]):
        return "P1"

    elif any(word in alert for word in [
        "malware", "unauthorized access", "brute force",
        "suspicious login", "multiple failed logins",
        "phishing attack"
    ]):
        return "P2"

    elif any(word in alert for word in [
        "port scanning", "suspicious activity",
        "unusual traffic", "policy violation",
        "outdated software"
    ]):
        return "P3"

    else:
        return "P4"


alert = input("Enter SOC Alert Description: ")

priority = assign_priority(alert)

print("SOC Alert:", alert)
print("Assigned Priority:", priority)