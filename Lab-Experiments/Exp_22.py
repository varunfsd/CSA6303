
# Simulated authentication log
logs = [
    "admin failed",
    "user1 success",
    "admin failed",
    "admin failed",
    "admin failed",
    "admin success",
    "user2 failed"
]

def detect_bruteforce(logs, username):
    failed = 0

    for log in logs:
        user, status = log.split()

        if user == username:
            if status == "failed":
                failed += 1

            elif status == "success":
                if failed >= 3:
                    print("\nALERT: Brute-force pattern detected!")
                    print("Username:", username)
                    print("Failed Attempts:", failed)
                    print("Status: Login succeeded after repeated failures")
                    return
                failed = 0

    print("\nNo brute-force pattern detected.")


username = input("Enter username to analyze: ")

detect_bruteforce(logs, username)
