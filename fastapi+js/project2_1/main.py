# Точка входа, подключение роутера
# В этом проекте SQL пишется вручную без использования SQLAlchemy
# Dependecies это функции или объекты, которые позволяют получать доступ к базе данных. Функция зависимость вызывается перед выполнением эндпоинта
from fastapi import FastAPI
import routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Пример разрешенного источника (frontend)
    "http://127.0.0.1:8000",  # Пример разрешенного источника (backend)
    "http://localhost:8000",  # Пример разрешенного источника (backend)
    "http://localhost:8080",  # Пример разрешенного источника (backend)
    "http://127.0.0.1:5500"
]

# Для получения запросов с разных адресов(В том числе подключения frontend)
app.add_middleware( # CORS(Cross-Origin Resource Sharing)
    CORSMiddleware,
    allow_origins=origins, # Все источники
    allow_credentials=True,
    allow_methods=["*"], # Все методы
    allow_headers=["*"], # Все заголовки
)

app.include_router(routers.router1)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)