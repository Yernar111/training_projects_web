# Точка входа, подключение роутера
# В этом проекте SQL пишется вручную с использованием SQLAlchemy
from fastapi import FastAPI
from routers import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router1, prefix="/users", tags=["Users"]) # Подключение роутера. prefix позволяет указать общий префикс для всех эндпоинтов в этом роутере. tags позволяет указать теги для группировки эндпоинтов в документации Swagger UI

@app.get("/")
def root():
    return {"status": "ok"}
