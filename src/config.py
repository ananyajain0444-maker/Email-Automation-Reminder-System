import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

DRY_RUN = True  # Set False to send real emails