
def classify_action(description):
    description = description.lower()

    phases = {
        "Preparation": [
            "training", "policy", "planning", "drill"
        ],
        "Identification": [
            "detect", "identify", "analyze", "alert", "investigate"
        ],
        "Containment": [
            "isolate", "block", "disconnect", "restrict"
        ],
        "Eradication": [
            "remove", "delete malware", "eliminate", "clean"
        ],
        "Recovery": [
            "restore", "backup", "restart", "recover"
        ],
        "Lessons Learned": [
            "review", "report", "improve", "document"
        ]
    }

    scores = {}

    for phase, keywords in phases.items():
        scores[phase] = sum(
            1 for word in keywords if word in description
        )

    result = max(scores, key=scores.get)

    if scores[result] == 0:
        return "Unknown Phase"

    return result


action = input("Enter incident response action: ")

result = classify_action(action)

print("\n--- Incident Response Classification ---")
print("Action:", action)
print("Lifecycle Phase:", result)
