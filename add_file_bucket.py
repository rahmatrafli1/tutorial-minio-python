from minio import Minio
from minio.error import S3Error
import os
from dotenv import load_dotenv

load_dotenv()

def add_file():
    # Pengaturan Koneksi MinIO
    minio_client = Minio(
        os.getenv('LOCAL_MINIO'),
        access_key=os.getenv('ACCESS_KEY_MINIO'),
        secret_key=os.getenv('SECRET_KEY_MINIO'),
        secure=False
    )

    # Nama file tujuan
    nama_folder = "/home/diginsight/Documents/Minio/Copy Object/txt"

    tujuan_file = f"/{nama_folder}/file_tujuan.txt"

    # bucket sumber
    sumber_bucket = "bucket-sumber"

    nama_tujuan_file_bucket = "/txt/file_tujuan.txt"

    # Upload file ke MinIO client
    minio_client.fput_object(
        sumber_bucket, nama_tujuan_file_bucket, tujuan_file 
    )
    print("File upload has been uploaded!")

if __name__ == "__main__":
    try:
        add_file()
    except S3Error as exc:
        print("error occurred.", exc)