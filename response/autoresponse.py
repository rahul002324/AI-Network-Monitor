import subprocess
import socket


# ------------------------------
# Get own system IP
# ------------------------------
def get_own_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)


# ------------------------------
# Safety Check
# ------------------------------
def is_safe_ip(ip):

    own_ip = get_own_ip()

    # Do not block yourself
    if ip == own_ip:
        return False

    # Do not block localhost
    if ip.startswith("127."):
        return False

    # Do not block broadcast traffic
    if ip == "0.0.0.0" or ip == "255.255.255.255":
        return False

    return True


# ------------------------------
# Block IP using Windows Firewall
# ------------------------------
def block_ip(ip):

    if not is_safe_ip(ip):
        print(f"⚠ Skipping safe IP: {ip}")
        return

    try:
        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            f"name=Block_{ip}",
            "dir=in",
            "action=block",
            f"remoteip={ip}"
        ]

        subprocess.run(command, check=True)
        print(f"🚫 IP {ip} BLOCKED successfully")

    except Exception as e:
        print("❌ Blocking failed:", e)
# ------------------------------
# Unblock IP manually
# ------------------------------
def unblock_ip(ip):
    try:
        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "delete",
            "rule",
            f"name=Block_{ip}"
        ]

        subprocess.run(command, check=True)
        print(f"✅ IP {ip} UNBLOCKED successfully")

    except Exception as e:
        print("❌ Unblock failed:", e)