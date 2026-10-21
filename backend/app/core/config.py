from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    groq_api_key: str = ""
    llm_model: str = "openai/gpt-oss-120b"
    frontend_origin: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=ROOT_DIR / ".env", extra="ignore", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()
