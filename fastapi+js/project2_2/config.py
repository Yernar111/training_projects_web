from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): # Параметры для подключения к БД. Эти параметры будут загружаться из .env файла при запуске приложения
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    
    model_config = SettingsConfigDict(env_file="database.env")
    @property # метод для получения URL подключения к БД
    def db_url(self):
        return (
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()