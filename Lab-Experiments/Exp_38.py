
def calculate_risk(likelihood, impact):
    score = likelihood * impact

    if score <= 5:
        level = "Low"
    elif score <= 10:
        level = "Medium"
    elif score <= 15:
        level = "High"
    else:
        level = "Critical"

    return score, level


likelihood = int(input("Enter likelihood (1-5): "))
impact = int(input("Enter impact (1-5): "))

if 1 <= likelihood <= 5 and 1 <= impact <= 5:
    score, level = calculate_risk(likelihood, impact)

    print("\n--- Risk Assessment ---")
    print("Likelihood:", likelihood)
    print("Impact:", impact)
    print("Risk Score:", score)
    print("Risk Level:", level)
else:
    print("Invalid input! Enter values between 1 and 5.")
