import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now get the NewsAPI key
NEWS_API_KEY = os.getenv("News_API")

def fetch_and_save_news():
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q=logistics OR supply chain&"
        f"sortBy=publishedAt&"
        f"language=en&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        today = datetime.today().strftime('%Y-%m-%d')

        raw_dir = f"data/raw/newsapi/{today}"
        processed_dir = f"data/processed/newsapi/{today}"

        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)

        # Save raw JSON
        with open(f"{raw_dir}/news.json", "w", encoding="utf-8") as f:
            json.dump(news_data, f, indent=2)

        # Save processed text
        articles = news_data.get("articles", [])
        with open(f"{processed_dir}/news.txt", "w", encoding="utf-8") as f:
            for article in articles:
                f.write(f"Title: {article['title']}\n")
                f.write(f"Description: {article['description']}\n")
                f.write(f"URL: {article['url']}\n")
                f.write("="*50 + "\n\n")

        print("News data fetched and saved locally ✅")
    else:
        print(f"Failed to fetch news - Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_and_save_news()
