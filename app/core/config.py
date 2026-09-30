from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ai_provider: str = ""
    ai_api_key: str = ""
    ai_model: str = ""
    jarvis_name: str = "JARVIS"
    jarvis_language: str = "en"
    jarvis_timezone: str = "Africa/Addis_Ababa"
    max_tool_calls: int = 8
    max_agent_steps: int = 12
    tool_timeout_seconds: int = 30
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
