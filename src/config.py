from dotenv import load_dotenv
from os import getenv


load_dotenv()

TOKEN = getenv("TOKEN")
OWNER_ID = getenv("OWNER_ID")
DATABASE = getenv("DATABASE")
MONGO_HOST = getenv("MONGO_HOST")
MONGO_PORT = getenv("MONGO_PORT")
MONGO_DATABASE = getenv("MONGO_DATABASE")
