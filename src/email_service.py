import random
from src.config import DRY_RUN

def send_email(to_email, subject, message):
    if DRY_RUN:
        print(f"[DRY RUN] Sending to {to_email}")
    
    # simulate success/failure
    status = random.choice(["SUCCESS", "FAILED"])
    return status