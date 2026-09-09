import random
import time

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from storage import load_posted, save_posted
from urllib.parse import urlparse

def crawl_jobs(keyword, location, isRemote=False, pages=3):
    url = (
        "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search"
    )
    ua = UserAgent()

    all_jobs = []

    for page in range(pages):
        start = page*10

        params = [
            ("keywords", keyword),
            ("location", location),

            # Experience Level
            # 1 = Internship, 2 = Entry Level
            ("f_E", "1"),
            ("f_E", "2"),

            # Job Type
            # F = Fulltime, I = Internship
            ("f_JT", "F"),
            ("f_JT", "I"),

            # Date Posted : Last 24 Hours
            ("f_TPR", "r86400"),

            # Pagination
            ("start", start)
        ]

        if isRemote:
            # Work Type : Remote (2)
            params.append(("f_WT", "2"))

        headers = {
            "User-Agent": ua.random,
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.linkedin.com/jobs",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }

        response = requests.get(
            url,
            params=params,
            headers=headers
        )

        if response.status_code == 429:
            print("Rate limited. Waiting...")
            time.sleep(120)
            requests.get(
                url,
                params=params,
                headers=headers
            )

        response.raise_for_status()
        jobs = parse_jobs(response.text)
        all_jobs.extend(jobs)
    return all_jobs

def parse_jobs(html):
    posted = load_posted()
    new_posted = set(posted)

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    jobs = []
    for item in soup.select("li"):
        title = item.select_one(
            ".base-search-card__title"
        )
        company = item.select_one(
            ".base-search-card__subtitle"
        )
        location = item.select_one(
            ".job-search-card__location"
        )
        link = item.select_one(
            ".base-card__full-link"
        )
        url = normalize_url(str(link["href"] if link else ""))
        date_element = item.select_one("time")
        date = date_element.get("datetime") if date_element else None

        if not title:
            continue

        if url in posted:
            continue

        jobs.append({
            "title": title.text.strip(),
            "company": company.text.strip(),
            "location": location.text.strip() if location else "",
            "date_posted": date,
            "url": url
        })

        new_posted.add(url)

    save_posted(new_posted)
    return jobs

def normalize_url(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

def remove_duplicates(jobs):
    seen = set()
    unique = []

    for job in jobs:
        if job["url"] in seen:
            continue
        seen.add(job["url"])
        unique.append(job)

    return unique

def fetch_jobs(keywords, locations,  is_remote=False):
    all_jobs = []

    for keyword in keywords:
        for location in locations:
            print(f"Crawling {keyword} in {location}")

            jobs = crawl_jobs(keyword, location, isRemote=False)
            all_jobs.extend(jobs)
            time.sleep(random.uniform(2, 5))
        if is_remote:
                jobs = crawl_jobs(keyword, location, isRemote=True)
                all_jobs.extend(jobs)
                time.sleep(random.uniform(2, 5))

    return remove_duplicates(all_jobs)
