# Serializer - файл который используется в DRF подходе для превращения объектов моделей в JSON и обратно автоматический(вместо того чтобы прописывать это вручную)
# Также используется для валидации
from rest_framework import serializers
from .models import ModelOne

class ModelOneSerializer(serializers.ModelSerializer): # Класс для сериализации
    class Meta:
        model = ModelOne # Для какой модели строится serializer
        fields = '__all__' # Для каких полей модели строится serializer(в данном случае все поля)
        # fields = ["id", "name"] # Альтернатива если конкретные поля


    def validate_password(self, value): # Пример метода для валидации(с названием конкретного поля password)
        if len(value) > 20:
            raise serializers.ValidationError("Value length can't be more than 20")
        return value
    
    def validate(self, data): # Пример метода для валидации(со всеми полями модели)
        if data["password"] == data.get("password"):
            raise serializers.ValidationError("Name and password must be different")
        return data

