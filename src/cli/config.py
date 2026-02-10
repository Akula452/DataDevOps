"""Environment and configuration management."""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


class Config:
    """Configuration class for different environments."""

    def __init__(self, env: Optional[str] = None):
        """Initialize configuration.
        
        Args:
            env: Environment name (dev, test, prod). Defaults to ENV variable or 'dev'.
        """
        self.env = env or os.getenv("ENVIRONMENT", "dev")
        self._load_env_file()
        self._set_config()

    def _load_env_file(self) -> None:
        """Load environment-specific .env file."""
        env_file = Path(__file__).parent.parent.parent / f".env.{self.env}"
        if env_file.exists():
            load_dotenv(env_file)
        else:
            load_dotenv()  # Load default .env if exists

    def _set_config(self) -> None:
        """Set configuration based on environment."""
        self.debug = self.env in ["dev", "test"]
        self.log_level = os.getenv("LOG_LEVEL", "INFO" if self.env == "prod" else "DEBUG")
        self.api_base_url = os.getenv("API_BASE_URL", "http://localhost:8000")
        self.timeout = int(os.getenv("REQUEST_TIMEOUT", "30"))
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))

    def __repr__(self) -> str:
        """String representation."""
        return f"Config(env={self.env}, debug={self.debug}, log_level={self.log_level})"


# Global config instance
config = None


def get_config(env: Optional[str] = None) -> Config:
    """Get or create global config instance."""
    global config
    if config is None or env:
        config = Config(env)
    return config
