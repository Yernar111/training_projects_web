 # Модели данных, которые будут использоваться в запросах и ответах. А также для валидации(конвертирования в нужный тип)
from pydantic import BaseModel

class ModelOne(BaseModel):
    name: str
    password: int
