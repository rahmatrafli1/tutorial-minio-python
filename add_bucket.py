from minio import Minio
from minio.error import S3Error
import os
from dotenv import load_dotenv

load_dotenv()

def add_bucket():
    # Pengaturan Koneksi MinIO
    minio_client = Minio(
        os.getenv('LOCAL_MINIO'),
        access_key=os.getenv('ACCESS_KEY_MINIO'),
        secret_key=os.getenv('SECRET_KEY_MINIO'),
        secure=False
    )

    # bucket sumber dan tujuan
    sumber_bucket = "bucket-sumber"
    tujuan_bucket = "bucket-tujuan"

    # Cek Bucket sumber dan Bucket tujuan apakah sudah dibuat apa belum?
    found1 = minio_client.bucket_exists(sumber_bucket)
    found2 = minio_client.bucket_exists(tujuan_bucket)
    if not found1 and not found2:
        minio_client.make_bucket(sumber_bucket)
        minio_client.make_bucket(tujuan_bucket)

    print("Bucket has been created!")

if __name__ == "__main__":
    try:
        add_bucket()
    except S3Error as exc:
        print("error occurred.", exc)