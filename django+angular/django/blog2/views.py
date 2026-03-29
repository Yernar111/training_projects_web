# При использовании DRF упрощается содержимое файла views.py
from rest_framework.viewsets import ModelViewSet
from .models import ModelOne
from .serializers import ModelOneSerializer

class OneViewSet(ModelViewSet): # Класс наследует ModelViewSet. Это позволяет не писать вручную CRUD методы.
    queryset = ModelOne.objects.all()
    serializer_class = ModelOneSerializer

# Список CRUD методов реализованных в ModelViewSet:

# list() - GET /users/
# retrieve() - GET /users/{id}/
# create() - POST /users/
# update() - PUT /users/{id}/
# destroy() - DELETE /users/{id}/