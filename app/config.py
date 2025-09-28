import os.path
from pathlib import Path

from pydantic_settings import SettingsConfigDict, BaseSettings
from loguru import logger

class Settings(BaseSettings):

    FORMAT_LOG: str = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    LOG_ROTATION: str = "10 MB"

    VOICE_PATH: Path = Path(__file__).parent / "voice.wav"

    # model_config = SettingsConfigDict(
    #     env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    # )

settings = Settings()

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")
logger.add(
    log_file_path,
    format=settings.FORMAT_LOG,
    level="INFO",
    rotation=settings.LOG_ROTATION
)