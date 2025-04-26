# crawlers/leadiq.py

import os
import logging
from datetime import datetime
from bs4 import BeautifulSoup
import watchtower
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger("leadiq-crawler")
logger.setLevel(logging.INFO)
log_group_name = "logistics-webcrawler-logs"
logger.addHandler(watchtower.CloudWatchLogHandler(log_group=log_group_name))

def crawl_leadiq():
    url = "https://leadiq.com/c/gnosis-freight/5fcf6529a856d346f831079f"
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    today = datetime.today().strftime('%Y-%m-%d')

    raw_path = f"data/raw/leadiq/{today}"
    processed_path = f"data/processed/leadiq/{today}"

    os.makedirs(raw_path, exist_ok=True)
    os.makedirs(processed_path, exist_ok=True)

    with open(f"{raw_path}/page.html", "w", encoding='utf-8') as f:
        f.write(html)

    with open(f"{processed_path}/page.txt", "w", encoding='utf-8') as f:
        f.write(text)

    driver.quit()
    logger.info(f"Successfully crawled and saved LeadIQ on {today}")
    print("Crawled and saved leadiq.com ✅")

if __name__ == "__main__":
    crawl_leadiq()
