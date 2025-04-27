from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Default arguments for the tasks
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'logistics_webcrawler_pipeline',
    default_args=default_args,
    description='Pipeline to crawl logistics websites + News API and upload to S3',
    schedule_interval='@daily',    # Runs once a day
    start_date=days_ago(1),
    catchup=False,
) as dag:

    # Website crawler tasks
    crawl_gnosisfreight = BashOperator(
        task_id='crawl_gnosisfreight',
        bash_command='./crawlers/gnosisfreight.py',
    )

    crawl_freightwaves = BashOperator(
        task_id='crawl_freightwaves',
        bash_command='./crawlers/freightwaves.py',
    )

    crawl_g2 = BashOperator(
        task_id='crawl_g2',
        bash_command='./crawlers/g2.py',
    )

    crawl_leadiq = BashOperator(
        task_id='crawl_leadiq',
        bash_command='./crawlers/leadiq.py',
    )

    crawl_logistics_of_logistics = BashOperator(
        task_id='crawl_logistics_of_logistics',
        bash_command='./crawlers/logofglog.py',
    )

    crawl_marketsandmarkets = BashOperator(
        task_id='crawl_marketsandmarkets',
        bash_command='./crawlers/marketsandmarkets.py',
    )

    # News API task
    fetch_newsapi = BashOperator(
        task_id='fetch_newsapi',
        bash_command='./news_api/fetch_newsapi.py',
    )

    # S3 upload task
    upload_all_data = BashOperator(
        task_id='upload_all_data',
        bash_command='/s3_utils/upload_all.py',
    )

    # Define task order - Task dependencies
    [
        crawl_gnosisfreight,
        crawl_freightwaves,
        crawl_g2,
        crawl_leadiq,
        crawl_logistics_of_logistics,
        crawl_marketsandmarkets,
        fetch_newsapi,
    ] >> upload_all_data
