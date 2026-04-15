 # Модели данных, которые будут использоваться в запросах и ответах(валидация и конвертирования объектов в JSON и обратно автоматический)
from pydantic import BaseModel

class ModelOne(BaseModel):
    name: str
    password: int
