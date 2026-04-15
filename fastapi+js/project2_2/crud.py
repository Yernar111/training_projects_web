from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.ModelOne): # параметр db является сессией БД, которая передается из эндпоинта через зависимость. Параметр user является объектом модели ModelOne, который передается из эндпоинта в виде JSON объекта и преобразуется в модель ModelOne
    db_user = models.Users(**user.model_dump()) # Создаем объект модели Users, передавая в нее данные из объекта user. Метод model_dump() преобразует модель Pydantic в словарь, который можно распаковать с помощью ** для передачи аргументов в конструктор модели SQLAlchemy
    db.add(db_user) # добавляем объект в сессию БД
    db.commit() # сохраняем
    db.refresh(db_user) # обновляем объект db_user, чтобы получить его id, который был сгенерирован при сохранении в БД. Метод refresh() обновляет объект из базы данных, чтобы он содержал все актуальные данные, включая сгенерированные поля, такие как id.
    return db_user


def get_users(db: Session): # Получаем всех пользователей из БД. Метод query() позволяет выполнять запросы к базе данных, а метод all() возвращает все результаты запроса в виде списка объектов модели Users.
    return db.query(models.Users).all()

def get_user(db: Session, name: str):
    return db.query(models.Users).filter(models.Users.name == name).first()