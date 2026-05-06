# 📧 Email Automation & Reminder System

A Python-based system that automates sending emails and reminders using CSV data, templates, and scheduling logic. It also generates analytics and visual reports to track email performance.

---

## 🚀 Project Overview

This project simulates a real-world **email automation system** used by companies for:

* 📅 Reminder notifications
* 📨 Bulk email sending
* 🔁 Follow-ups
* 📊 Email analytics

It reads contacts and reminders from CSV files, personalizes messages using templates, and generates insightful visual reports.

---

## 🎯 Problem Statement

Manual email communication is:

* Time-consuming
* Error-prone
* Hard to track

This system automates the entire workflow:

> Contact list → Message template → Email sending → Status tracking → Analytics

---

## 💡 Features

* 📄 Load contacts from CSV
* 📝 Dynamic email template personalization
* ⚙️ Simulated email sending (Dry Run mode)
* 📊 Automatic report generation
* 📈 Visual analytics using charts
* 📁 Clean modular structure

---

## 🛠 Tech Stack

* Python
* Pandas
* Matplotlib
* CSV Handling
* Logging

---

## 📁 Project Structure

```
Email-Automation-Reminder-System/
│
├── data/
│   ├── contacts.csv
│   └── reminders.csv
│
├── templates/
│   └── email_template.txt
│
├── src/
│   ├── config.py
│   ├── email_service.py
│   ├── scheduler.py
│   ├── utils.py
│   └── logger.py
│
├── images/
│   ├── report_chart.png
│   ├── emails_per_user.png
│   ├── time_distribution.png
│   └── status_pie.png
│
├── docs/
│   └── architecture.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup


### Install dependencies

```
pip install -r requirements.txt
```

### Run the project

```
python main.py
```

---

## 📊 Output & Visualizations

After running the project, the following graphs are generated:

### 📈 Email Status Report

![Report Chart](images/report_chart.png)

---

### 📊 Emails per User

![Emails per User](images/emails_per_user.png)

---

### 📉 Email Traffic Patterns

![Time Distribution](images/time_distribution.png)

---

### 🥧 Status Distribution

![Status Pie](images/status_pie.png)

---

## 🧠 How It Works

1. Load contacts and reminders from CSV
2. Read email template
3. Personalize message for each user
4. Simulate email sending
5. Store results in DataFrame
6. Generate CSV report
7. Create visual analytics

---

## 🌍 Real-World Applications

* 📚 Education (class reminders)
* 💼 HR (interview scheduling)
* 💰 Finance (payment reminders)
* 📢 Marketing (email campaigns)
* 🛠 Operations (task alerts)

---

## 📌 Learning Outcomes

* Data handling with Pandas
* File handling (CSV, TXT)
* Automation using Python
* Visualization using Matplotlib
* Modular project design
* GitHub project structuring

---

## 👩‍💻 Author

**Ananya Jain**

---

## ⭐ Future Improvements

* Real email sending via SMTP
* Scheduling with cron/jobs
* Web dashboard (Streamlit/FastAPI)
* Database integration
* User authentication

---

## 📌 Note

This project uses simulated email sending for safety and demonstration purposes.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
