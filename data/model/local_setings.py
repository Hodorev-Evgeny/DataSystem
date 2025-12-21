import os
from dotenv import load_dotenv


load_dotenv()

settings = {
    'pguser': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'pgdatabase': os.getenv('DB_NAME'),
    'url': os.getenv('DB_URL'),
}