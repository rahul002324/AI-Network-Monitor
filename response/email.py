import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = "rahulramesh148@gmail.com"
SENDER_PASSWORD = "gyucogpmtvnuwogp"

RECEIVER_EMAIL = "rahulramesh148@gmail.com"


def send_alert(ip, attack_type, severity):

    try:
        subject = "🚨 Smart IDS Alert: Attack Detected"

        body = f"""
Attack Detected!

Attack Type : {attack_type}
Attacker IP : {ip}
Severity    : {severity}
Time        : {datetime.now()}

Smart IDS Response: IP Blocked
"""

        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        print("📧 Email alert sent successfully")

    except Exception as e:
        print("Email alert failed:", e)