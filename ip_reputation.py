import ipaddress
import json

def is_private_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return None

def load_indicators():
    with open("indicators.json", "r") as f:
        return json.load(f)

def check_ip_reputation(ip, indicators):
    return {
        "ip": ip,
        "is_private": is_private_ip(ip),
        "known_malicious": ip in indicators["malicious_ips"]
    }

def main():
    ip = input("Enter an IP address: ").strip()
    indicators = load_indicators()
    result = check_ip_reputation(ip, indicators)

    if result["is_private"] is None:
        print("Invalid IP address.")
        return

    print("\nIP Reputation Result")
    print("-------------------")
    print(f"IP Address: {result['ip']}")
    print(f"Private IP: {result['is_private']}")
    print(f"Known Malicious: {result['known_malicious']}")

if __name__ == "__main__":
    main()
