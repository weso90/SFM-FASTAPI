from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Simple Family Manager"
    DATABASE_URL: str = "sqlite:///./family_manager.db"

    class Config:
        case_sensitive = True

settings = Settings()