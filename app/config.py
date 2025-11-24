from environs import Env
from dataclasses import dataclass


@dataclass
class Settings:
    debug: bool
    database_url: str
    secret_key: str
    port: int


def load_settings() -> Settings:
    env = Env()
    env.read_env()

    return Settings(
        debug=env.bool("debug"),
        database_url=env.str("database_url"),
        secret_key=env.str("secret_key"),
        port=env.int("port")
    )


settings = load_settings()

