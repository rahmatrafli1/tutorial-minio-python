import os
from minio import Minio
from minio.commonconfig import CopySource
from dotenv import load_dotenv

load_dotenv()

# Pengaturan Koneksi MinIO
minio_client = Minio(
    os.getenv('LOCAL_MINIO'),
    access_key=os.getenv('ACCESS_KEY_MINIO'),
    secret_key=os.getenv('SECRET_KEY_MINIO'),
    secure=False
)

source_bucket = "bucket-tujuan"

# Get list of objects in the source bucket
objects = '/txt/file_tujuan.txt'

# Delete an objects in the source bucket
source_object = objects
print(source_object)
minio_client.remove_object(bucket_name=source_bucket, object_name=source_object)

print(f"Delete objects in the bucket {source_bucket} is Successfully!")