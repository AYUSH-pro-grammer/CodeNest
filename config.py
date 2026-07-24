import os

from dotenv import load_dotenv


load_dotenv()


APP_NAME = os.getenv("APP_NAME", "CodeNest")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///codenest.db",
)

DEV_MODE = os.getenv(
    "DEV_MODE",
    "true",
).lower() == "true"