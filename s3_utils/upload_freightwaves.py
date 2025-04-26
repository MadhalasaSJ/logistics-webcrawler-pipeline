from uploader import upload_directory

if __name__ == "__main__":
    upload_directory(
        local_dir='./crawlers/data',  # This is your local folder containing raw + processed
        bucket='logic-crawler-bucket',  # 🔥 Replace with your real S3 bucket
        s3_prefix='freightwaves'  
    )