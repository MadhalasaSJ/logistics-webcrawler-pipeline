# s3_utils/upload_newsapi.py

from uploader import upload_directory

if __name__ == "__main__":
    upload_directory(
        local_dir='data',
        bucket='logic-crawler-bucket',  # your real bucket
        s3_prefix='newsapi'
    )