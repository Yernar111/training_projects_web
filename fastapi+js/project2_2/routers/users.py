from fastapi import APIRouter, Depends, HTTPException
from schemas import ModelOne
from database import get_db
import crud, schemas

from sqlalchemy.orm import Session

router1 = APIRouter()

@router1.post("/", response_model=schemas.ModelOne) # response_model позволяет указать тип данных возвращаемого значения(в данном случае модель ModelOne)
def create_user(user: schemas.ModelOne, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@router1.get("/", response_model=list[schemas.ModelOne])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router1.get("/{name}", response_model=schemas.ModelOne)
def get_user(name: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# @router1.post("/create_user")
# def create_user(user: ModelOne, cur = Depends(get_db)):
#     return crud.create_user(cur=cur, user=user)

# @router1.get("/get_users")
# def get_users(cur = Depends(get_db)):
#     return crud.get_users(cur)

# @router1.get("/get_user/{name}")
# def get_user(name: str, cur = Depends(get_db)):
#     user = crud.get_user(cur, name)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user