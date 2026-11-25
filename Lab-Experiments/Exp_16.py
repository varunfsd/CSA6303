
import random

def defense_in_depth():
    layers = {
        "Firewall": 0.60,
        "Intrusion Detection System": 0.50,
        "Antivirus": 0.70,
        "Access Control": 0.80,
        "Data Encryption": 0.90
    }

    print("\n--- Defense-in-Depth Simulation ---")

    for layer, protection in layers.items():
        print(f"\nChecking {layer}...")

        if random.random() < protection:
            print(f"Attack blocked by {layer}")
            print("Result: System Protected")
            return

        print(f"Attack bypassed {layer}")

    print("\nALERT: Attack passed all security layers!")
    print("Result: System Compromised")


defense_in_depth()
