
def classify_threat(description):
    description = description.lower()

    threats = {
        "Phishing": [
            "phishing", "fake email", "fake link",
            "credential", "fraudulent"
        ],
        "DoS/DDoS": [
            "ddos", "dos", "traffic flood",
            "overload", "service unavailable"
        ],
        "Malware": [
            "malware", "virus", "trojan",
            "ransomware", "infected"
        ],
        "Man-in-the-Middle": [
            "intercept", "eavesdropping",
            "mitm", "packet sniffing", "spoofing"
        ]
    }

    scores = {}

    for threat, keywords in threats.items():
        scores[threat] = sum(
            1 for word in keywords if word in description
        )

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "Unknown Threat"

    return result


incident = input("Enter incident description: ")

result = classify_threat(incident)

print("\n--- Network Threat Analysis ---")
print("Incident:", incident)
print("Threat Category:", result)
