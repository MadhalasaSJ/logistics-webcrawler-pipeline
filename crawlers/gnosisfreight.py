# crawlers/gnosisfreight.py

import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import logging
import watchtower  # make sure you installed it: pip install watchtower

# Set up logging
logger = logging.getLogger("gnosisfreight-crawler")
logger.setLevel(logging.INFO)

# CloudWatch Log Group Name
log_group_name = "logistics-webcrawler-logs"
logger.addHandler(watchtower.CloudWatchLogHandler(log_group=log_group_name))

def crawl_gnosis():
    url = "https://www.gnosisfreight.com"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        today = datetime.today().strftime('%Y-%m-%d')

        raw_path = f"data/raw/gnosisfreight/{today}"
        processed_path = f"data/processed/gnosisfreight/{today}"

        os.makedirs(raw_path, exist_ok=True)
        os.makedirs(processed_path, exist_ok=True)

        with open(f"{raw_path}/page.html", "w", encoding='utf-8') as f:
            f.write(response.text)

        with open(f"{processed_path}/page.txt", "w", encoding='utf-8') as f:
            f.write(text)

        logger.info(f"Successfully crawled and saved Gnosis Freight on {today}")
        print("Crawled and saved gnosisfreight.com ✅")
    else:
        logger.error(f"Failed to fetch {url} - Status code: {response.status_code}")
        print(f"Failed to fetch {url} ❌")

if __name__ == "__main__":
    crawl_gnosis()
