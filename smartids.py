import os
import pyfiglet
import pandas as pd
import subprocess
import time   # ← add this at top (if not already)
from rich.console import Console
from rich.table import Table

console = Console()

DATA_DIR = "data"

def banner():

    os.system("cls" if os.name == "nt" else "clear")

    title = pyfiglet.figlet_format("SMART IDS AI")
    console.print(f"[green]{title}[/green]")
    console.print("[cyan]AI Intrusion Detection Framework\n[/cyan]")


def help_menu():

    console.print("""
Available Commands

help        Show commands
start       Start IDS monitoring
traffic     Show captured traffic
attacks     Show detected attacks
blocked     Show blocked IPs
clear       Clear screen
exit        Exit framework
""")

def cleanup_old_files():

    DATA_DIR = "data"   # your data folder

    now = time.time()

    for file in os.listdir(DATA_DIR):

        path = os.path.join(DATA_DIR, file)

        if os.path.isfile(path):

            file_age = now - os.path.getmtime(path)

            # 30 days = 2592000 seconds
            if file_age > 2592000:

                os.remove(path)
                print(f"Deleted old file: {file}")

def show_traffic():

    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv") and "attacks" not in f]

    if files:

        latest = sorted(files)[-1]   # latest file
        df = pd.read_csv(os.path.join(DATA_DIR, latest))

        table = Table(title=f"Recent Traffic ({latest})")

        table.add_column("Source IP")
        table.add_column("Destination IP")
        table.add_column("Port")
        table.add_column("Size")

        for _, row in df.tail(10).iterrows():
            table.add_row(
                str(row["src_ip"]),
                str(row["dst_ip"]),
                str(row["port"]),
                str(row["packet_size"])
            )

        console.print(table)

    else:
        console.print("No traffic data found")

def show_attacks():

    files = [f for f in os.listdir(DATA_DIR) if "attacks" in f]

    if files:

        latest = sorted(files)[-1]

        df = pd.read_csv(f"{DATA_DIR}/{latest}")

        table = Table(title="Detected Attacks")

        table.add_column("IP")
        table.add_column("Type")

        for _, row in df.iterrows():

            ip = str(row.get("src_ip", "unknown"))
            attack = str(row.get("attack_type", "unknown"))

            table.add_row(ip, attack)

        console.print(table)

    else:

        console.print("No attacks logged")
def show_blocked():

    file = "data/blocked_ips.csv"

    if os.path.exists(file):

        df = pd.read_csv(file)

        table = Table(title="Blocked IPs")

        table.add_column("IP")

        for _, row in df.iterrows():
            table.add_row(str(row["ip"]))

        console.print(table)

    else:
        console.print("No blocked IPs found")


banner()
cleanup_old_files()

while True:

    cmd = console.input("[bold red]smartids > [/bold red]")

    if cmd == "help":

        help_menu()

    elif cmd == "start":
        console.print("Starting IDS engine...\n")
    
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        subprocess.run(
        ["python", os.path.join(BASE_DIR, "main.py")],
        cwd=BASE_DIR
    )
    elif cmd == "traffic":

        show_traffic()

    elif cmd == "attacks":

        show_attacks()

    elif cmd == "blocked":
        show_blocked()

    elif cmd == "clear":

        banner()

    elif cmd == "exit":

        console.print("Exiting Smart IDS AI")
        break

    else:

        console.print("Unknown command. Type help")

 