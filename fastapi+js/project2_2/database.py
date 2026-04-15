from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Talgar558_@localhost:5432/project111_database"
engine = create_engine(settings.db_url) # Создаем движок для подключения к базе данных. Движок управляет соединениями с базой данных и выполняет SQL-запросы. Параметр db_url содержит URL подключения к базе данных, который формируется на основе параметров из .env файла.
SessionLocal = sessionmaker(bind=engine) # Создаем класс SessionLocal, который будет использоваться для создания сессий подключения к базе данных. Параметр bind указывает на движок, который будет использоваться для подключения к базе данных. Сессия позволяет выполнять операции с базой данных, такие как добавление, удаление и изменение данных, а также выполнение SQL-запросов.

Base = declarative_base()

# Зависимость для получения сессии БД в эндпоинтах
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()