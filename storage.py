import json
import os

POSTED_FILE = "posted.json"

def load_posted():
    if not os.path.exists(POSTED_FILE):
        with open(POSTED_FILE, "w") as f:
            json.dump([], f)
        return set()

    with open(POSTED_FILE) as f:
        return set(json.load(f))

def save_posted(posted):
    with open(POSTED_FILE, "w") as f:
        json.dump(list(posted), f)