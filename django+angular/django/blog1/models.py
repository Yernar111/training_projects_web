# Для описания таблицы из базы данных(следует после обработки запроса в view)
from django.db import models 

# По умолчанию таблица сама создается из модели(в данном случае с названием blog1/modelone). 
class ModelOne(models.Model): # Модель таблицы в базе данных. Существующая таблица обязательно должна иметь столбец Primary Key(например, id). А если использовать модель для создания новой таблицы в БД, то столбец id будет создан автоматически
    name = models.CharField(max_length=20, db_column="name") # Объект столбца таблицы которое будет использоваться в модели(в данном случае с типом varhcar(100))
    password = models.IntegerField(db_column="password") # Последний аргумент для указания имени столбца в таблице которая соответствует текущему полю в модели, если же имена совпадают или таблица создается по новой, то последний аргумент не обязателен

    class Meta: # Класс Meta позволяет предотвратить создание таблицы по новой
        db_table = "users1" # Чтобы указать название таблицы с которой взаимодействует модель
        managed = False # Чтобы не бе создавать таблицу по новой, а работать с существующей

# One-to-One
class ModelTwo(models.Model):
    name = models.OneToOneField(ModelOne, on_delete=models.CASCADE)
    age = models.IntegerField()

# One-to-many
class ModelThree(models.Model):
    name = models.ForeignKey(ModelOne, on_delete=models.CASCADE)
    email = models.EmailField()

# Many-to-Many
class ModelFour(models.Model):
    name = models.ManyToManyField(ModelOne)
    address = models.CharField(max_length=20)

# Create your models here.
