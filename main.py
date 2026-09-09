from datetime import datetime

from discord import send_message
from crawler import fetch_jobs

SKIP = [
    # sales / business
    # "sales",
    # "business development",
    # "account",
    # "marketing",
    # "customer",
    # "customer service",
    # "solution",

    # non IT engineer
    # "maintenance",
    # "manufacturing",
    # "mechanical",
    # "electrical",
    # "civil",
    # "structural",
    # "project",
    # "construction",
    # "field",
    # "cost control",

    # operational
    # "operator",
    # "technician",
    # "officer",
    # "sourcing",
    # "purchasing",
    # "audit",
    # "auditor",
    # "legal",
    # "economics",
    # "researcher",

    # seniority
    "manager",
    "director",
    "head",
    "lead",
    "principal",
    "senior"
]

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
        "UI/UX",
    ],
    [
        "Indonesia"
    ],
    is_remote=True
)

today = datetime.now().strftime("%Y-%m-%d")

messages_list = []
messages_list.append(f"""```text
╔════════════════════════════════════════════════════
║                  📌 JOB UPDATE
╠════════════════════════════════════════════════════
║ 📅 Tanggal: {today}
║ jobs from the last 24 hours.
║
║ 🌏 Indonesia
║ 💻 Software Engineer • Backend • Fullstack
║    • Frontend • Data Engineer • DevOps • QA
║    •  UI/UX
║ 🎓 Internship & Entry Level
║
║ ℹ️ Note:
║ Mungkin ga akurat. Kindly check each job details
║ ya gengs.
╚════════════════════════════════════════════════════
```""")

for job in jobs:
    title = job["title"].lower()
    if any(keyword in title for keyword in SKIP):
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

def chunk_list(items, chunk_size):
    for i in range(0, len(items), chunk_size):
        yield items[i:i + chunk_size]

for batch in chunk_list(messages_list, 5):
    final_message = "".join(batch)
    send_message(final_message)
