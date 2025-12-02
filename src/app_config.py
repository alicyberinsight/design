from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    rabbitmq_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
