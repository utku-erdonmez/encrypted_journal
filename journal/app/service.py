import random
from datetime import datetime
from app.storage import save_data

def build_entry(text):
    dt = datetime.now()
    return {
        "id": str(random.randint(100000, 999999)),
        "date": dt.strftime("%Y-%m-%d"),
        "time": dt.strftime("%H:%M"),
        "text": text
    }

def new_entry(data, password, text):
    entry = build_entry(text)
    data["entries"].append(entry)
    save_data(data, password)

def get_random_entry(data):
    if not data["entries"]:
        return None
    return random.choice(data["entries"])

def search_entries(data, query):
    q = query.lower()
    return [
        e for e in data["entries"]
        if q in e["text"].lower()
    ]

def get_entries(data):
    return data["entries"]