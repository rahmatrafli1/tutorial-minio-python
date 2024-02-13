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

source_bucket = "bucket-sumber"

# Get list of objects in the source bucket
objects = minio_client.list_objects(source_bucket, None)

# Delete all objects in the source bucket
for obj in objects:
    source_object = obj.object_name
    minio_client.remove_object(bucket_name=source_bucket, object_name=source_object)

print(f"Delete all objects in the bucket {source_bucket} is Successfully!")