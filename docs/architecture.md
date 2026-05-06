# 🏗️ System Architecture

## 📌 Overview
The Email Automation & Reminder System automates sending emails using CSV data, templates, and processing logic.

---

## 🔄 Workflow

Contacts CSV + Reminders CSV  
↓  
Load Data (Pandas)  
↓  
Email Template Processing  
↓  
Message Personalization  
↓  
Email Sending (Simulated)  
↓  
Status Logging  
↓  
Report Generation (CSV)  
↓  
Visualization (Charts)

---

## 🧩 Components

### Data Layer
- contacts.csv
- reminders.csv

### Template Engine
- email_template.txt
- Uses {{name}}, {{message}}

### Email Service
- Simulates sending
- Returns SUCCESS / FAILED

### Scheduler
- Processes emails
- Stores results

### Logging
- Tracks activity

### Reporting
- Generates report.csv

### Visualization
- report_chart.png
- emails_per_user.png
- time_distribution.png
- status_pie.png

---

## ⚙️ Design
- Modular
- Easy to extend

---

## 🚀 Future Scope
- SMTP email sending
- Database integration
- Dashboard