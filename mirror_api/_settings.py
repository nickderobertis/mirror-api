from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    status_code: int = 200

    class Config:
        env_prefix = "MIRROR_API_"
