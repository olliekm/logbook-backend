from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Centralized settings
class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

settings = Settings()
