import os

from dotenv import load_dotenv

load_dotenv()

AUTH_SERVICE_PORT = os.getenv("AUTH_SERVICE_PORT")
DB_SCHEMA = os.getenv("DB_SCHEMA")