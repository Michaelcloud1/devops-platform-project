import os

class Config:
    APP_NAME = "Platform API"
    VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("APP_ENV", "development")