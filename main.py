import os
from datetime import datetime
import requests
from discord import send_message
from crawler import fetch_jobs

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def chunk_list(items, chunk_size):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

def classify_job(title) -> bool:
    prompt = f"""
You are a job classifier.

Classify whether this job title matches:
- Tech related roles (software engineer, quality assurance, security, devops)
- Entry level / junior / internship only
- NOT senior, lead, manager, director, head, principal

Return ONLY:
true
or
false

Job title:
{title}
"""

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "google/gemma-4-26b-a4b-it:free",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0,
            "max_tokens": 2
        }
    )

    result = response.json()
    answer = result["choices"][0]["message"]["content"].strip().lower()
    return answer == "true"

jobs = fetch_jobs(
    [
        "Software Engineer",
        "Backend Engineer",
        "Backend Developer",
        "Full Stack Developer",
        "Frontend Developer",
        "QA Engineer",
        "Quality Assurance Engineer",
        "Data Engineer",
        "Machine Learning Engineer",
        "DevOps Engineer",
        "Cloud Engineer",
    ],
    [
        "Indonesia",
    ],
    is_remote=True
)

today = datetime.now().strftime("%Y-%m-%d")

messages_list = []
messages_list.append(f"""```text
╔════════════════════════════════════════════════════
║                  📌 JOB UPDATE
╠════════════════════════════════════════════════════
║ 📅 Date: {today}
║ These are jobs from the last 24 hours.
║
║ 🌏 Indonesia
║ 💻 Software Engineer • Backend • Fullstack
║    • Frontend • Data Engineer • DevOps • QA
║ 🎓 Internship & Entry Level
║
║ ℹ️ Note:
║ Mungkin ga akurat. Kindly check each job details
║ ya gengs.
╚════════════════════════════════════════════════════
```""")

for job in jobs:
    title = job["title"].lower()
    if not classify_job(title):
        continue
    message = f"""
 **{job["title"]}**

🏢 {job["company"]}
📍 {job["location"]}
🕑 Posted on {job["date_posted"]}

🔗 Linkedin URL : {job["url"]}
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    messages_list.append(message)

for batch in chunk_list(messages_list, 5):
    final_message = "".join(batch)
    send_message(final_message)
