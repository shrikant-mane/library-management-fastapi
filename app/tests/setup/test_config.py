from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

TEST_BASE_DIR = Path(__file__).resolve().parents[3]

class Settings(BaseSettings):
    TEST_DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=TEST_BASE_DIR / ".test_env",
    )

settings = Settings()

