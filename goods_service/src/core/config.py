import os
from dotenv import load_dotenv

load_dotenv()
# Database
DATABASE_URL = os.environ.get("DATABASE_URL")
# Service envs
PORT = int(os.environ.get("PORT"))
# MinIO
MINIO_API_PORT = os.environ.get("MINIO_API_PORT")
MINIO_HOST = os.environ.get("MINIO_HOST")
MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY")
MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY")
USE_HTTPS = os.environ.get("USE_HTTPS").lower() in ('true', '1', 't')
