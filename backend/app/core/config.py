from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    app_name: str = Field(default="Mini-Agent Backend")
    environment: str = Field(default="development")

    # Networking
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)
    cors_origins: str = Field(default="*")  # comma-separated

    # Database
    database_url: Optional[str] = Field(default=None)

    # LLM
    openai_api_key: Optional[str] = Field(default=None)
    openai_model: str = Field(default="gpt-4o-mini")
    ollama_base_url: Optional[str] = Field(default=None)
    ollama_model: str = Field(default="llama3.1")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()  # Singleton-style settings instance

