# Подключение к БД
from config import load_config
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db():
    config = load_config()
    with psycopg2.connect(**config, cursor_factory=RealDictCursor) as conn: # Используем 'with', чтобы не писать close() вручную. RealDictCursor позволяет возвращать словарь(а не кортеж) при операциях по типу cur.fetchone()
        with conn.cursor() as cur:
            yield cur # Если не было ошибок conn.commit() выполнится автоматически при выходе из with, иначе выполнится Rollback


# Способ если использовать .env для подключения к базе данных
# from .config import settings

# def get_db():
#     # Собираем словарь параметров для коннекта
#     connection_params = {
#         "dbname": settings.db_name,
#         "user": settings.db_user,
#         "password": settings.db_password,
#         "host": settings.db_host,
#         "port": settings.db_port
#     }
    
#     with psycopg2.connect(**connection_params, cursor_factory=RealDictCursor) as conn:
#         with conn.cursor() as cur:
#             yield cur


# Старый способ
# def get_db():
#     config  = load_config()
#     conn=psycopg2.connect(**config, cursor_factory=RealDictCursor) # RealDictCursor позволяет возвращать словарь(а не список) при операциях по типу cur.fetchone()
#     cur=conn.cursor()
#     try:
#         yield cur
#         conn.commit()
#     except:
#         conn.rollback()
#         raise
#     finally:
#         cur.close()
#         conn.close()