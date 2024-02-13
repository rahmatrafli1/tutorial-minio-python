import os
from minio import Minio
from dotenv import load_dotenv

load_dotenv()

# Pengaturan Koneksi MinIO
minio_client = Minio(
    os.getenv('LOCAL_MINIO'),
    access_key=os.getenv('ACCESS_KEY_MINIO'),
    secret_key=os.getenv('SECRET_KEY_MINIO'),
    secure=False
)

source_bucket = ["bucket-sumber", "bucket-tujuan"]

for bucket in source_bucket:
    minio_client.remove_bucket(bucket)
    print(f"Bucket {source_bucket} removed successfully.")