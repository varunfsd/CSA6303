
def assess_threat(data, context, confidence, action):
    print("\n--- Threat Intelligence Assessment ---")
    print("Collected Data:", data)
    print("Context:", context)
    print("Confidence:", confidence)
    print("Actionability:", action)

    if context.lower() == "yes" and confidence >= 70 and action.lower() == "yes":
        print("\nResult: Genuine Threat Intelligence")
    else:
        print("\nResult: Unprocessed Raw Data")

data = input("Enter collected data (IP/URL): ")
context = input("Is context available? (yes/no): ")
confidence = int(input("Enter confidence percentage (0-100): "))
action = input("Is data actionable? (yes/no): ")

if 0 <= confidence <= 100:
    assess_threat(data, context, confidence, action)
else:
    print("Invalid confidence percentage!")
