from pathlib import Path
from typing import List, Union

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = "FinPulse"
    APP_ENV: str = "development"
    APP_DEBUG: bool = True

    NEWSAPI_KEY: str = ""
    GROQ_API_KEY: str = ""

    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC_RAW_NEWS: str = "raw-news"
    KAFKA_TOPIC_ENRICHED_NEWS: str = "enriched-news"
    KAFKA_CONSUMER_GROUP: str = "finpulse-consumers"

    REDIS_URL: str = "redis://localhost:6379/0"

    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: int = 8001
    CHROMA_COLLECTION_NAME: str = "finpulse-news"

    BACKEND_CORS_ORIGINS: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: Union[str, List[str]]) -> List[str]:
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        if isinstance(value, list):
            return value
        return []


settings = Settings()
