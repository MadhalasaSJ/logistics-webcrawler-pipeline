# Logistics Webcrawler Pipeline

This project implements an automated data pipeline that crawls logistics-related websites, extracts relevant information, and stores the data in AWS S3. It leverages Apache Airflow for orchestration, Docker for containerization, and Python-based crawlers for data extraction.

## 🚀 Features

- **Modular Crawlers**: Custom Python scripts located in the `crawlers/` directory to scrape data from various logistics websites.
- **Airflow DAGs**: Defined in the `airflow_dags/` directory to schedule and manage crawling tasks.
- **AWS S3 Integration**: Utilizes the `s3_utils/` module to upload and manage scraped data in AWS S3 buckets.
- **News API Integration**: Fetches the latest logistics news using the `news_api/` module.
- **Dockerized Setup**: Includes a `Dockerfile` for easy deployment and environment consistency.

## 📁 Project Structure

├── airflow_dags/ # Airflow DAG definitions

├── crawlers/ # Web crawling scripts

├── news_api/ # Modules to fetch news data

├── s3_utils/ # AWS S3 utility functions

├── Dockerfile # Docker configuration

├── requirements.txt # Python dependencies

├── design_doc.md # Project design documentation

└── README.md # Project overview

## 🛠️ Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MadhalasaSJ/logistics-webcrawler-pipeline.git
   cd logistics-webcrawler-pipeline
   
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. **Configure AWS Credentials**:
   
    Ensure your AWS credentials are set up to allow access to S3. This can be done by configuring the ~/.aws/credentials file or setting environment variables.

6. **Run Airflow**:
    Initialize and start Airflow to schedule and manage your DAGs.

7. **Execute Crawlers**:
    Run the crawler scripts as defined in the Airflow DAGs or manually for testing purposes.
   

# 📄 Documentation

- For a detailed overview of the system architecture, data flow, and design decisions, refer to the design_doc.md file.

📌 Notes
- Ensure that all necessary environment variables and configurations are set before running the pipeline.

- Regularly monitor the Airflow UI to track the status of your DAGs and tasks.

