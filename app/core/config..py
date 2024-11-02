import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "RAG Project"
    MONGODB_URI: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
