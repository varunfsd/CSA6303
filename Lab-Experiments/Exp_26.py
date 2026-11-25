
import hashlib

# Simulated malware sample
sample = b"CreateRemoteThread VirtualAlloc WriteProcessMemory"

# Static Analysis
print("--- Static Malware Analysis ---")

file_hash = hashlib.sha256(sample).hexdigest()
print("SHA-256 Hash:", file_hash)

suspicious_apis = [
    "CreateRemoteThread",
    "VirtualAlloc",
    "WriteProcessMemory"
]

for api in suspicious_apis:
    if api.encode() in sample:
        print("Suspicious API Found:", api)

# Dynamic Analysis (Simulated)
print("\n--- Dynamic Malware Analysis ---")

behavior_logs = [
    "File created",
    "Registry modified",
    "Unauthorized network connection",
    "Process injection detected"
]

suspicious_behaviors = [
    "Registry modified",
    "Unauthorized network connection",
    "Process injection detected"
]

for behavior in behavior_logs:
    if behavior in suspicious_behaviors:
        print("Suspicious Behavior:", behavior)

print("\nMalware Analysis Completed")
