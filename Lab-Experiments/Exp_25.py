
import hashlib
from datetime import datetime

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Simulated evidence records
records = [
    {"event": "Evidence Collected",
     "time": "2026-11-20 10:00:00"},
    {"event": "Evidence Transferred",
     "time": "2026-11-20 11:00:00"},
    {"event": "Evidence Analyzed",
     "time": "2026-11-20 12:00:00"}
]

# Create hash chain
previous_hash = "0"

for record in records:
    record["previous_hash"] = previous_hash
    data = record["event"] + record["time"] + previous_hash
    record["hash"] = generate_hash(data)
    previous_hash = record["hash"]

# Verify hash and timestamp chain
def verify_chain(records):
    previous_hash = "0"
    previous_time = None

    for record in records:
        current_time = datetime.strptime(
            record["time"], "%Y-%m-%d %H:%M:%S"
        )

        data = record["event"] + record["time"] + previous_hash
        expected_hash = generate_hash(data)

        if record["previous_hash"] != previous_hash:
            return "FAILED: Hash chain broken"

        if record["hash"] != expected_hash:
            return "FAILED: Evidence record modified"

        if previous_time and current_time < previous_time:
            return "FAILED: Timestamp order invalid"

        previous_hash = record["hash"]
        previous_time = current_time

    return "SUCCESS: Chain of custody verified"


print("--- Chain of Custody Verification ---")
print(verify_chain(records))
