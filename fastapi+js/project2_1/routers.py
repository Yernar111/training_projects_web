# URL адреса
from fastapi import APIRouter, Depends, HTTPException
from schemas import ModelOne
from database import get_db
import crud

router1 = APIRouter()

# Test routes
@router1.get("/a") # Декоратор. Когда пользователь обращается к этому URL адресу вызывается функция
def one():
    return {"a": "one", "b": "two"} # Возвращает словарь который преобразуется в JSON

@router1.get("/b/{param1}/{param2}") # Path parameter. Для HTTP-метода GET лучше использовать query или path параметры(чтобы было тело запроса) 
def two(param1: int, param2: str):    
    return {"c": param1, "d": param2}

@router1.get("/c") # Query parameter. В URL адрес надо написать ?key=value&key=value (для двух параметров). Например, http://127.0.0.1:8000/three?id=1&name=abcd
def three(param1: int, param2: str):
    return {"e": param1, "f": param2}



# Real routes
# эндпоинт для создания пользователя. Метод POST используется для создания ресурса. В данном случае ресурсом является пользователь. В теле запроса передается JSON объект который преобразуется в модель ModelOne. Функция create_user принимает этот объект и выполняет операцию создания пользователя в базе данных. Результат операции возвращается клиенту.
@router1.post("/create_user")
def create_user(user: ModelOne, cur = Depends(get_db)): # get_db является функцией зависимостью, она вызывается до выполнения эндпоинта и передает результат аргументу
    return crud.create_user(cur=cur, user=user) # Возвращаем выполненную операцию клиенту 

@router1.get("/get_users")
def get_users(cur = Depends(get_db)):
    return crud.get_users(cur)

@router1.get("/get_user/{name}")
def get_user(name: str, cur = Depends(get_db)):
    user = crud.get_user(cur, name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



# @router1.get("/get_users", response_model=list[ModelOne]) # response_model позволяет указать тип данных возвращаемого значения(в данном случае список моделей ModelOne)
# def get_users(cur = Depends(get_db)):
#     return crud.get_users(cur)

