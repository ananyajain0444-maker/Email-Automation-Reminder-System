import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT, DRY_RUN
from src.logger import log_info, log_error


def send_email(to_email, subject, body):
    try:
        if DRY_RUN:
            print(f"[DRY RUN] Sending email to {to_email}")
            log_info(f"[DRY RUN] Email to {to_email}")
            return "SUCCESS"

        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()

        log_info(f"Email sent to {to_email}")
        return "SUCCESS"

    except Exception as e:
        log_error(f"Failed for {to_email}: {str(e)}")
        return f"FAILED: {str(e)}"