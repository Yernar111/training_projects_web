# Модели данных, которые будут использоваться в базе данных. SQLAlchemy позволяет описывать структуру таблиц и их связи с помощью классов и атрибутов. Эти модели будут использоваться для создания таблиц в базе данных и для взаимодействия с данными через ORM (Object-Relational Mapping).
from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True) # является обязательным полем
    name = Column(String)
    password = Column(Integer, unique=True)

