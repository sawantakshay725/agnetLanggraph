import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Centralized configuration for the supply chain intelligence system.
    Reads from environment variables with sensible defaults.
    """

    # Database
    DB_PATH: str = os.getenv("DB_PATH", "data/supply_chain.db")

    # API Keys
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY")
    DEEPSEEK_API_KEY: Optional[str] = os.getenv("DEEPSEEK_API_KEY")

    # Forecasting defaults
    DEFAULT_FORECAST_HORIZON: int = int(os.getenv("DEFAULT_FORECAST_HORIZON", 30))

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Feature flags
    ENABLE_ANALYTICS: bool = os.getenv("ENABLE_ANALYTICS", "true").lower() == "true"
    ENABLE_FORECASTING: bool = os.getenv("ENABLE_FORECASTING", "true").lower() == "true"


def get_config() -> Config:
    """
    Returns a Config object with all settings.
    """
    return Config()
