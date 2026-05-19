import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "super_secret_key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_SERVICE_KEY: str = os.getenv("SUPABASE_SERVICE_KEY")

settings = Settings()