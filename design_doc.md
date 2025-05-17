# Design Document: Logistics Webcrawler Pipeline

## 🧩 Overview

This document outlines the system architecture, key components, and data flow of the Logistics Webcrawler Pipeline. The goal of the project is to automate the collection of logistics-related data from various online sources and store the processed information in AWS S3 for further analysis or downstream applications.

---

## 🏗️ Architecture Components

### 1. **Crawlers**
- Located in the `crawlers/` directory.
- Custom scripts written in Python using libraries like `requests`, `BeautifulSoup`, or `Selenium` depending on the target website.
- Responsible for extracting structured or semi-structured data from logistics websites.

### 2. **Airflow DAGs**
- DAGs in `airflow_dags/` schedule the crawling tasks.
- Each DAG can execute one or multiple crawlers, depending on the site's complexity and update frequency.
- DAGs can also handle post-processing or validation steps before uploading to AWS.

### 3. **News API Integration**
- `news_api/` contains modules that fetch the latest logistics and supply chain news using external APIs (e.g., NewsAPI.org).
- Helpful for adding real-time news insights alongside crawled data.

### 4. **AWS S3 Utility**
- `s3_utils/` provides functions to upload JSON, CSV, or raw HTML/text data to S3 buckets.
- Ensures durable and scalable storage of crawled datasets.

### 5. **Docker**
- The entire project is containerized using a `Dockerfile`.
- Enables seamless deployment and consistent environments across machines.

---

## 🔄 Data Flow

1. **Trigger**: Airflow DAG is triggered (either manually or on schedule).
2. **Crawling**: The selected crawler scripts scrape websites and collect data.
3. **Preprocessing**: Data may be cleaned, transformed, or validated locally.
4. **Upload**: Clean data is uploaded to a specific AWS S3 bucket/folder.
5. **Log & Monitor**: Airflow logs task status and any errors; results are visible via the Airflow UI.

---

## 🧪 Testing Strategy

- Unit tests can be added to ensure each crawler returns data in the expected format.
- DAGs can be run in a test mode to simulate scheduling.
- Mock S3 uploads can validate AWS integration without real writes.

---

## 📝 Future Improvements

- Add database integration (e.g., PostgreSQL or DynamoDB) for structured data querying.
- Enable email or Slack notifications from Airflow on task failures.
- Add retry logic for flaky websites in crawler scripts.
- Use headless browsers or advanced tools (e.g., Playwright) for JavaScript-heavy sites.

---

## 📌 Author & Repository

- GitHub: [https://github.com/MadhalasaSJ/logistics-webcrawler-pipeline](https://github.com/MadhalasaSJ/logistics-webcrawler-pipeline)
