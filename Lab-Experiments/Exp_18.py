
import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()

# Sample malicious hash database
malicious_hashes = {
    hashlib.sha256(b"malware").hexdigest(),
    hashlib.sha256(b"virus").hexdigest()
}

filename = input("Enter file path: ")

if os.path.isfile(filename):
    file_hash = calculate_hash(filename)

    print("\n--- Malware Detection Result ---")
    print("File:", filename)
    print("SHA-256:", file_hash)

    if file_hash in malicious_hashes:
        print("ALERT: Known malicious hash detected!")
    else:
        print("No matching malicious hash found.")
else:
    print("Error: File not found!")
