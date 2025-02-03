from dotenv import load_dotenv
import os

load_dotenv()  # takes environment variables from .env and loads it to your environment - you can access the same using os.getenv
print(os.getenv('NEW_ENV_VARIABLE'))