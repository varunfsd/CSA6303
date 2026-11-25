
def analyze_report(report):
    report = report.lower()

    improvements = {
        "Patch Management": [
            "patch", "update", "vulnerability"
        ],
        "Security Awareness": [
            "training", "awareness", "phishing"
        ],
        "Monitoring": [
            "monitoring", "logs", "alert", "detection"
        ],
        "Backup Strategy": [
            "backup", "recovery", "restore"
        ],
        "Access Control": [
            "password", "authentication", "permission", "access"
        ]
    }

    tags = []

    for area, keywords in improvements.items():
        if any(word in report for word in keywords):
            tags.append(area)

    return tags


report = input("Enter post-incident report: ")

result = analyze_report(report)

print("\n--- Post-Incident Report Analysis ---")

if result:
    print("Identified Improvement Areas:")
    for area in result:
        print("-", area)
else:
    print("No improvement areas identified.")
