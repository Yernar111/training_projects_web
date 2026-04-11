# При использовании DRF упрощается содержимое файла views.py
from rest_framework.viewsets import ModelViewSet
from .models import ModelOne
from .serializers import ModelOneSerializer

from rest_framework.decorators import APIView, action
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class OneViewSet(ModelViewSet): # Класс наследует ModelViewSet. Это позволяет не писать вручную CRUD методы.
    queryset = ModelOne.objects.all()
    serializer_class = ModelOneSerializer # Указываем класс сериализатора
    @action(detail=True, methods=['get'], url_path='custom') # detail=True конкретный URL-адрес, methods=['get'] разрешенные методы, url_path кастомный путь
    def custom(self, request, pk=None): # pk=None это id полученный из URL-адреса(pk-primary key)
        a = self.get_object() # Получение объекта текущей модели на основе pk(иначе вернет 404)
        b = ModelOne.objects.filter(id=a)
        serializer = ModelOneSerializer(b, many=True) # Сериализация в JSON(в данном случае объекты ModelOne, many=True означает сериализацию сразу нескольких объектов и поэтому возвращает массив словарей)
        return Response(serializer.data)
        # return Response({"a": 1})


# Class-based view для аутентификации.
class OneApiView(APIView): # Класс наследует APIView. Это позволяет писать CRUD методы вручную, подходит для масштабируемости

    permission_classes = [IsAuthenticated] # Разрешаем доступ к этому API только аутентифицированным пользователям. То есть только пользователи с токеном доступа смогут обращаться к методам этого класса через HTTP-запросы(для этого надо первым делом получить токен, отправив POST запрос на /api/token/)
    def get_object(self, id): # Вспомогательный метод для получения объекта по id.
        a = ModelOne.objects.get(id=id)
        if not a:
            return None
        return a
    
    def get(self, request, id): # Благодаря наследованию APIView при HTTP GET запросе автоматический вызывается этот метод(то же самое с остальными методами)
        a = self.get_object(id)
        if not a:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ModelOneSerializer(a)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ModelOneSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Список CRUD методов реализованных в ModelViewSet:

# list() - GET /users/
# retrieve() - GET /users/{id}/
# create() - POST /users/
# update() - PUT /users/{id}/
# destroy() - DELETE /users/{id}/