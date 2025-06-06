import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TOKEN")
MAX_FILE_SIZE_MB = 5
SUPPORTED_EXTENSIONS = {'.txt', '.doc', '.docx', '.xlsx'}