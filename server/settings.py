from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000

    db_user: str = 'denisdarahan'
    db_password: str = '1'
    db_name: str = 'minesweeper'
    db_host: str = '127.0.0.1'

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(_env_file='server/.env', _env_file_encoding='utf-8')
