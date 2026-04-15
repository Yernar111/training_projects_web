from pydantic import BaseModel

class ModelOne(BaseModel):
    id: int | None = None
    name: str
    password: int
