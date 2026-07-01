import time
from collections import defaultdict

# Track ports per source IP
port_tracker = defaultdict(list)

# 🔥 Configuration
PORT_SCAN_THRESHOLD = 10   # 10 different ports
TIME_WINDOW = 10           # within 10 seconds

def detect_port_scan(src_ip, port):
    current_time = time.time()

    # Add new attempt
    port_tracker[src_ip].append((port, current_time))

    # Remove old attempts outside 10-second window
    port_tracker[src_ip] = [
        (p, t) for p, t in port_tracker[src_ip]
        if current_time - t <= TIME_WINDOW
    ]

    # Count unique ports
    unique_ports = {p for p, _ in port_tracker[src_ip]}

    if len(unique_ports) >= PORT_SCAN_THRESHOLD:
        port_tracker[src_ip].clear()  # prevent repeated alerts
        return True

    return False
