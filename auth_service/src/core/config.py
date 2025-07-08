import os

from dotenv import load_dotenv

load_dotenv()

AUTH_SERVICE_PORT = os.getenv("AUTH_SERVICE_PORT")
# Database
DB_SCHEMA = os.getenv("DB_SCHEMA")
DATABASE_URL = os.getenv("DATABASE_URL")