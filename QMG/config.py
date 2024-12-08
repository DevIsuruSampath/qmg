from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DOWNLOAD_PATH = "./downloads"

# Ensure download path exists
os.makedirs(DOWNLOAD_PATH, exist_ok=True)
