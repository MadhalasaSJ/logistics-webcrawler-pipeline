from s3_utils.uploader import upload_directory

if __name__ == "__main__":
    upload_directory(
        local_dir='data',
        bucket='logic-crawler-bucket',
        s3_prefix='daily_pipeline'   # upload entire structure
    )