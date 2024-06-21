from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "markets"
    oauth_token_secret: str = "wtvr"


settings = Settings()  # type: ignore






