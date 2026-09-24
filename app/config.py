from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    use_azure_openai: bool = False
    azure_openai_endpoint: str = ""
    azure_openai_api_key: str = ""
    azure_openai_api_version: str = ""
    azure_openai_chat_deployment: str = ""
    azure_openai_embedding_deployment: str = ""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
