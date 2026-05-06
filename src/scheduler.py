import pandas as pd
import os
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

from src.utils import load_contacts, load_reminders, load_template, personalize
from src.email_service import send_email
from src.logger import log


def generate_charts(df):
    os.makedirs("images", exist_ok=True)

    # -----------------------------
    # 1. STATUS BAR CHART
    # -----------------------------
    status_count = df["status"].value_counts()
    plt.figure(figsize=(6,4))
    status_count.plot(kind="bar")
    plt.title("Email Status Report")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("images/report_chart.png", dpi=300)
    plt.close()

    # -----------------------------
    # 2. PIE CHART
    # -----------------------------
    plt.figure(figsize=(5,5))
    status_count.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Email Status Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("images/status_pie.png", dpi=300)
    plt.close()

    # -----------------------------
    # 3. EMAILS PER USER
    # -----------------------------
    user_count = df["email"].value_counts()
    plt.figure(figsize=(6,4))
    user_count.plot(kind="bar")
    plt.title("Emails per User")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("images/emails_per_user.png", dpi=300)
    plt.close()

    # -----------------------------
    # 4. 🔥 TIME DISTRIBUTION (3 PATTERNS - BEST)
    # -----------------------------
    times = ["10:00", "11:00", "12:00", "13:00"]

    # Example patterns
    increasing = [1, 2, 3, 4]
    decreasing = [4, 3, 2, 1]
    random_pattern = [random.randint(1, 4) for _ in times]

    plt.figure(figsize=(8,5))

    plt.plot(times, increasing, marker="o", label="Increasing Load")
    plt.plot(times, decreasing, marker="o", label="Decreasing Load")
    plt.plot(times, random_pattern, marker="o", label="Random Activity")

    plt.title("Email Traffic Patterns Over Time")
    plt.xlabel("Time")
    plt.ylabel("Number of Emails")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig("images/time_distribution.png", dpi=300)
    plt.close()


def process_emails():
    contacts = load_contacts("data/contacts.csv")
    reminders = load_reminders("data/reminders.csv")
    template = load_template("templates/email_template.txt")

    report = []
    base_time = datetime.now()

    for i, (_, contact) in enumerate(contacts.iterrows()):
        for _, reminder in reminders.iterrows():

            message = personalize(
                template,
                contact["name"],
                reminder["message"]
            )

            status = send_email(
                contact["email"],
                reminder["subject"],
                message
            )

            log(f"{contact['email']} → {status}")

            report.append({
                "email": contact["email"],
                "status": status,
                "time": base_time + timedelta(minutes=i*10)
            })

    df = pd.DataFrame(report)

    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/report.csv", index=False)

    generate_charts(df)

    print("✅ Emails Processed + Professional Graphs Generated")