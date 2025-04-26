# s3_utils/uploader.py

import boto3
import os

def upload_directory(local_dir, bucket, s3_prefix):
    s3 = boto3.client('s3')
    
    for root, dirs, files in os.walk(local_dir):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, local_dir)
            s3_path = os.path.join(s3_prefix, relative_path).replace("\\", "/")

            print(f"Uploading {local_path} to s3://{bucket}/{s3_path}")
            s3.upload_file(local_path, bucket, s3_path)
