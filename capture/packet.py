import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scapy.all import sniff, IP, TCP
from detection.rule import detect_port_scan
import csv
from datetime import datetime
from detection.ai import train_model, detect_anomaly, load_model
from response.autoresponse import block_ip
from response.email import send_alert

# ---------- FILE SETUP ----------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

today_date = datetime.now().strftime("%Y-%m-%d")
DATA_FILE = os.path.join(DATA_DIR, f"{today_date}.csv")
ATTACK_FILE = os.path.join(DATA_DIR, f"attacks_{today_date}.csv")


# Create CSV with header if not exists
if not os.path.exists(ATTACK_FILE):
    with open(ATTACK_FILE, "w", newline="") as af:
        writer = csv.writer(af)
        writer.writerow([
            "time",
            "src_ip",
            "attack_type",
            "description"
        ])

# ---------- PACKET PROCESSING ----------

def process_packet(packet):

    if packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        packet_size = len(packet)

        port = 0
        if packet.haslayer(TCP):
            port = packet[TCP].dport

        # 🚨 Rule-based detection
   # 🚨 Rule-based detection
        if detect_port_scan(src_ip, port):

            severity = "HIGH"

            print("\n" + "="*50)
            print(f"🚨 PORT SCAN DETECTED FROM {src_ip}")
            print(f"Severity: {severity}")
            print("="*50 + "\n")

            block_ip(src_ip)
            send_alert(src_ip, "Port Scan", severity)

        # 🤖 AI anomaly detection
        if detect_anomaly(port, packet_size):

            severity = "MEDIUM"

            print(f"🤖 AI ANOMALY DETECTED from {src_ip}")
            print(f"Severity: {severity}")

            block_ip(src_ip)
            send_alert(src_ip, "Port Scan", severity)

            with open(ATTACK_FILE, "a", newline="") as af:
                attack_writer = csv.writer(af)
                attack_writer.writerow([
                    datetime.now().strftime("%H:%M:%S"),
                    src_ip,
                    "AI Anomaly",
                    "Unusual traffic pattern"
                ])
        now = datetime.now().strftime("%H:%M:%S")

        print(f"[PACKET] {src_ip} → {dst_ip} | Port: {port} | Size: {packet_size}")

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "time",
            "src_ip",
            "dst_ip",
            "protocol",
            "port",
            "packet_size"
        ])


# ---------- START SNIFFER ----------

print("🚀 Packet Sniffer Started (10 sec window)...")
# 🤖 Try loading existing AI model
if not load_model():
    print("No saved model found. Training new model...")
    train_model(DATA_FILE)
try:
    sniff(prn=process_packet, store=False, timeout=10)
except KeyboardInterrupt:
    print("\n🛑 Sniffer stopped manually")

print("✅ Sniffing completed")
# 🤖 Train AI after collecting traffic
train_model(DATA_FILE)