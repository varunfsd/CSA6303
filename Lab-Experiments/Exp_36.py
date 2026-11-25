
def identify_compliance(description):
    description = description.lower()

    standards = {
        "PCI-DSS": [
            "credit card", "debit card", "payment",
            "cardholder", "transaction"
        ],
        "HIPAA": [
            "patient", "medical", "healthcare",
            "hospital", "health record"
        ],
        "GDPR": [
            "personal data", "privacy", "eu citizen",
            "european", "data protection"
        ],
        "SOX": [
            "financial report", "accounting",
            "audit", "financial statement", "public company"
        ]
    }

    scores = {}

    for standard, keywords in standards.items():
        scores[standard] = sum(
            1 for word in keywords if word in description
        )

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "Unknown Compliance Standard"

    return result


description = input("Enter system or data description: ")

result = identify_compliance(description)

print("\n--- Compliance Standard Identification ---")
print("Description:", description)
print("Applicable Standard:", result)
