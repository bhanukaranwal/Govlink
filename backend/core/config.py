from pydantic_settings import BaseSettings
from typing import List
import yaml


class Settings(BaseSettings):
    PROJECT_NAME: str = "GovLink"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    DATABASE_URL: str
    REDIS_URL: str
    
    USAJOBS_API_KEY: str = ""
    USAJOBS_USER_AGENT: str = ""
    
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    HUGGINGFACE_TOKEN: str = ""
    OPENAI_API_KEY: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


config = load_config()
