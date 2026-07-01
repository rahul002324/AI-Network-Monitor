from scapy.all import sniff
from capture.packet import process_packet

print("🚀 IDS Engine Running...\n")

try:
    sniff(prn=process_packet, store=False, timeout=10)
except KeyboardInterrupt:
    print("\n🛑 IDS stopped")

print("✅ Sniffing completed")
from detection.ai import train_model
import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    max([f for f in os.listdir("data") if f.endswith(".csv") and "attacks" not in f])
)

train_model(DATA_FILE)