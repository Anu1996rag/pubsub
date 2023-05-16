from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    public_api_url: str = Field(..., env="PUBLIC_API_URL")
    public_api_endpoint: str = Field(..., env="PUBLIC_API_ENDPOINT")

    redis_channel: str = Field(..., env="REDIS_CHANNEL")

    # publisher creds
    publisher_url: str = Field(..., env="PUBLISHER_URL")
    publisher_port: str = Field(..., env="PUBLISHER_PORT")
    publisher_redis_url: str = Field(..., env="PUBLISHER_REDIS_URL")
    publisher_redis_port: str = Field(..., env="PUBLISHER_REDIS_PORT")

    # subscriber creds
    subscriber_url: str = Field(..., env="SUBSCRIBER_URL")
    subscriber_port: str = Field(..., env="SUBSCRIBER_PORT")
    subscriber_redis_url: str = Field(..., env="SUBSCRIBER_REDIS_URL")
    subscriber_redis_port: str = Field(..., env="SUBSCRIBER_REDIS_PORT")

    class Config:
        env_file = '.env'

settings = Settings()