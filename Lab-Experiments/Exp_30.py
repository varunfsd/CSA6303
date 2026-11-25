
# Simulated security logs

firewall_logs = [
    {"ip": "192.168.1.10", "event": "Multiple Connections"},
    {"ip": "192.168.1.20", "event": "Normal Traffic"}
]

windows_logs = [
    {"ip": "192.168.1.10", "user": "admin", "failed": 5},
    {"ip": "192.168.1.20", "user": "user1", "failed": 1}
]

vpn_logs = [
    {"ip": "192.168.1.10", "event": "Login Success"},
    {"ip": "192.168.1.20", "event": "Login Success"}
]

def correlate_logs():
    print("--- SIEM Correlation Analysis ---")

    for fw in firewall_logs:
        for win in windows_logs:
            for vpn in vpn_logs:

                if (fw["ip"] == win["ip"] == vpn["ip"]
                    and fw["event"] == "Multiple Connections"
                    and win["failed"] >= 3
                    and vpn["event"] == "Login Success"):

                    print("\nALERT: Possible Brute-Force Attack!")
                    print("IP Address:", fw["ip"])
                    print("Username:", win["user"])
                    print("Failed Logins:", win["failed"])
                    print("VPN Status:", vpn["event"])
                    return

    print("No suspicious activity detected.")


correlate_logs()
