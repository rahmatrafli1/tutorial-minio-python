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

source_bucket = "sumber-bucket"
destination_bucket = "bucket-sumber"

found = minio_client.bucket_exists(destination_bucket)
if not found:
    minio_client.make_bucket(destination_bucket)

# Get list of objects in the source bucket
objects = minio_client.list_objects(source_bucket, None)

# Copy each object to the destination bucket
for obj in objects:
    source_object = obj.object_name
    destination_object = source_object # You can modify the destination object name if needed
    minio_client.copy_object(bucket_name=destination_bucket, object_name=destination_object, source=CopySource(source_bucket, destination_object))
    minio_client.remove_object(bucket_name=source_bucket, object_name=destination_object)

minio_client.remove_bucket(bucket_name=source_bucket)

print(f"All objects copied from {source_bucket} to {destination_bucket}")