# При использовании DRF упрощается содержимое файла urls.py
from rest_framework.routers import DefaultRouter
from .views import OneViewSet 

router = DefaultRouter() # Объект роутера. Автоматический формирует маршруты(чтобы не писать вручную)
router.register('users', OneViewSet, basename='users1') # Регистрируем роутер(маршрут с префиксом users, вызывающий OneViewSet, с определенными basename users1(необязательно)).

urlpatterns = router.urls # Экспортируем маршруты в django

# После регистрации роутер создаст маршруты. В данном случае:
# GET users/
# POST users/
# GET users/1/
# PUT users/1/
# PATCH users/1/
# DELETE users/1/