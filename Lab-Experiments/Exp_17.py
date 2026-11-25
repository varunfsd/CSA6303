
def classify_control(description):
    description = description.lower()

    domains = {
        "Organizational Controls": [
            "policy", "risk", "audit", "compliance",
            "management", "supplier"
        ],
        "People Controls": [
            "employee", "training", "awareness",
            "staff", "screening"
        ],
        "Physical Controls": [
            "cctv", "door", "building", "security guard",
            "physical", "visitor"
        ],
        "Technological Controls": [
            "firewall", "encryption", "antivirus",
            "password", "network", "malware"
        ]
    }

    scores = {}

    for domain, keywords in domains.items():
        scores[domain] = sum(
            1 for word in keywords if word in description
        )

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "Unknown Control Domain"

    return result


control = input("Enter security control description: ")

result = classify_control(control)

print("\n--- ISO 27001 Control Classification ---")
print("Security Control:", control)
print("Annex A Domain:", result)
