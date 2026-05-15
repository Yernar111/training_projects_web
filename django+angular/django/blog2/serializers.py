# Этот файл содержит описание сериализаторов, которые будут использоваться для преобразования данных между различными форматами. Сериализаторы позволяют преобразовывать данные из формата Python в формат JSON и обратно, что облегчает обмен данными между сервером и клиентом. В этом файле можно определить различные классы сериализаторов для различных моделей и полей, а также методы для валидации данных.
from rest_framework import serializers
from .models import ModelOne

# Классы для сериализации
class ModelOneSerializer(serializers.ModelSerializer): # ModelSerializer автоматический создает поля на основе модели
    class Meta:
        model = ModelOne # Для какой модели строится serializer
        fields = '__all__' # Для каких полей модели строится serializer(в данном случае все поля)
        # fields = ["id", "name"] # Альтернатива если конкретные поля


    def validate_password(self, value): # Пример метода для валидации конкретного поля модели. Он должен начинаться с validate_ и затем имя поля, которое мы хотим валидировать.
        if len(value) > 20:
            raise serializers.ValidationError("Value length can't be more than 20")
        return value
    
    def validate(self, data): # Пример метода для валидации нескольких полей модели одновременно. Он должен быть назван validate и принимать весь словарь данных, который мы хотим валидировать.
        if data["password"] == data["name"]:
            raise serializers.ValidationError("Name and password must be different")
        return data

# class ModelOneSerializer1(serializers.Serializer): # Serializer поля определеляются вручную(в данном случае делает то же самое и класс выше)
#     name = serializers.CharField()
#     password = serializers.CharField(write_only=True)
