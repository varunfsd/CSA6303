
def recommend_containment(incident):
    incident = incident.lower()

    if "ransomware" in incident or "malware" in incident:
        return "Isolate infected system from network"

    elif "phishing" in incident or "fake email" in incident:
        return "Block malicious links and reset credentials"

    elif "ddos" in incident or "dos attack" in incident:
        return "Enable traffic filtering and rate limiting"

    elif "data breach" in incident or "data leak" in incident:
        return "Revoke unauthorized access and secure data"

    elif "insider" in incident or "employee misuse" in incident:
        return "Disable suspicious user accounts"

    elif "unauthorized login" in incident or "brute force" in incident:
        return "Lock affected accounts and block suspicious IPs"

    else:
        return "Investigate incident and monitor network activity"


incident = input("Enter security incident description: ")

strategy = recommend_containment(incident)

print("\n--- Incident Containment Recommendation ---")
print("Incident:", incident)
print("Recommended Strategy:", strategy)
