import os
from minio import Minio
from minio.error import S3Error
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

# bucket sumber dan tujuan
sumber_bucket = "bucket-sumber"
tujuan_bucket = "bucket-tujuan"

nama_sumber_file_bucket = "/txt/file_tujuan.txt"
nama_tujuan_file_bucket = "/txt/file_tujuan.txt"
copy_nama_tujuan_file = "/txt/file_tujuan.txt"

def copy_file_object(minio_client, sumber_bucket, nama_sumber_file_bucket, tujuan_bucket, nama_tujuan_file_bucket):
    # Cek Bucket sumber dan Bucket tujuan apakah sudah dibuat apa belum?
    found1 = minio_client.bucket_exists(sumber_bucket)
    found2 = minio_client.bucket_exists(tujuan_bucket)
    if not found1 and not found2:
        minio_client.make_bucket(sumber_bucket)
        minio_client.make_bucket(tujuan_bucket)

    if nama_tujuan_file_bucket == nama_sumber_file_bucket:
        # Move file ke MinIO client
        minio_client.copy_object(tujuan_bucket, copy_nama_tujuan_file, CopySource(sumber_bucket, nama_sumber_file_bucket))
        minio_client.remove_object(sumber_bucket, nama_sumber_file_bucket)

    print(f"File {copy_nama_tujuan_file} has been moved!")

if __name__ == "__main__":
    try:
        copy_file_object(minio_client, sumber_bucket, nama_sumber_file_bucket, tujuan_bucket, nama_tujuan_file_bucket)
    except S3Error as exc:
        print("error occurred.", exc)