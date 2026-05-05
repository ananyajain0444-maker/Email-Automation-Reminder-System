import schedule
import time
from datetime import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt

from src.utils import load_contacts, load_reminders, load_template, personalize
from src.email_service import send_email


# 🔥 IMAGE GENERATION FUNCTION (4 PERFECT IMAGES)
def generate_charts(df):
    os.makedirs("images", exist_ok=True)

    # 1️⃣ Bar Chart: Success vs Failed
    status_count = df["status"].value_counts()
    plt.figure(figsize=(6, 4))
    status_count.plot(kind="bar")
    plt.title("Email Status Report")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("images/report_chart.png", dpi=300)
    plt.close()

    # 2️⃣ Emails per User
    user_count = df["email"].value_counts()
    plt.figure(figsize=(6, 4))
    user_count.plot(kind="bar")
    plt.title("Emails Sent per User")
    plt.xlabel("User")
    plt.ylabel("Emails Count")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("images/emails_per_user.png", dpi=300)
    plt.close()

    # 3️⃣ Time Distribution (FIXED - NO CUT ISSUE)
    df["time"] = pd.to_datetime(df["time"])
    df["time_group"] = df["time"].dt.strftime("%H:%M")

    time_count = df["time_group"].value_counts().sort_index()

    plt.figure(figsize=(10, 5))
    time_count.plot(kind="line", marker='o')

    plt.title("Emails Over Time")
    plt.xlabel("Time (HH:MM)")
    plt.ylabel("Count")

    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("images/time_distribution.png", dpi=300)
    plt.close()

    # 4️⃣ Pie Chart (Status Distribution)
    plt.figure(figsize=(5, 5))
    status_count.plot(kind="pie", autopct='%1.1f%%')
    plt.title("Email Status Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("images/status_pie.png", dpi=300)
    plt.close()


# 📧 MAIN PROCESS FUNCTION
def process_emails():
    contacts = load_contacts("data/contacts.csv")
    reminders = load_reminders("data/reminders.csv")
    template = load_template("templates/email_template.txt")

    report = []

    for _, contact in contacts.iterrows():
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

            report.append({
                "email": contact["email"],
                "status": status,
                "time": datetime.now()
            })

    df = pd.DataFrame(report)

    # Save report
    os.makedirs("outputs", exist_ok=True)
    df.to_csv("outputs/report.csv", index=False)

    # 🔥 Generate all charts
    generate_charts(df)

    print("✅ Emails Processed, Report & 4 Images Generated")


# ⏰ SCHEDULER
def start_scheduler():
    # Run every 1 minute (demo)
    schedule.every(1).minutes.do(process_emails)

    print("🚀 Scheduler Started...")

    while True:
        schedule.run_pending()
        time.sleep(1)