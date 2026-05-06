import pandas as pd

def load_contacts(path):
    return pd.read_csv(path)

def load_reminders(path):
    return pd.read_csv(path)

def load_template(path):
    with open(path, "r") as f:
        return f.read()

def personalize(template, name, message):
    return template.replace("{{name}}", name).replace("{{message}}", message)