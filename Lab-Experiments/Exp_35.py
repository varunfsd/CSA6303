
roles = {
    "Admin": {"read", "write", "delete"},
    "Manager": {"read", "write"},
    "Employee": {"read"}
}

users = [
    {"name": "Alice", "role": "Admin",
     "permissions": {"read", "write", "delete"}},
    {"name": "Bob", "role": "Manager",
     "permissions": {"read", "write", "delete"}},
    {"name": "Charlie", "role": "Employee",
     "permissions": {"read", "write"}},
    {"name": "David", "role": "Employee",
     "permissions": {"read"}}
]

print("--- Least Privilege Access Audit ---")

for user in users:
    required = roles[user["role"]]
    assigned = user["permissions"]

    excess = assigned - required

    print("\nUser:", user["name"])
    print("Role:", user["role"])

    if excess:
        print("Status: EXCESS ACCESS DETECTED")
        print("Excess Permissions:", ", ".join(sorted(excess)))
    else:
        print("Status: COMPLIANT")
