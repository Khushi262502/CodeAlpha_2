import smtplib

from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()


def send_email_alert(
    attack_type,
    severity
):

    sender_email = os.getenv("EMAIL")

    sender_password = os.getenv("EMAIL_PASSWORD")

    receiver_email = sender_email

    subject = f"[{severity}] Security Alert"

    body = f"""
Attack Detected: {attack_type}

Severity: {severity}
"""

    msg = MIMEText(body)

    msg["Subject"] = subject

    msg["From"] = sender_email

    msg["To"] = receiver_email

    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            sender_email,
            sender_password
        )

        server.sendmail(
            sender_email,
            receiver_email,
            msg.as_string()
        )

        server.quit()

        print(
            "Email Alert Sent!"
        )

    except Exception as e:

        print(
            "Email Error:",
            e
        )