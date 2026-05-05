import logging
import os

LOG_FILE = "logs/email.log"

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)