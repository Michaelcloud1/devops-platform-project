import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "Platform API")
    VERSION = os.getenv("APP_VERSION", "1.0.0")
    ENVIRONMENT = os.getenv("APP_ENV", "development")