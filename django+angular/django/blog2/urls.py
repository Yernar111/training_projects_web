# При использовании DRF упрощается содержимое файла urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import OneApiView, OneViewSet

from rest_framework.authtoken.views import obtain_auth_token # Вью для получения токена

router = DefaultRouter() # Объект роутера. Автоматический формирует маршруты(чтобы не писать вручную)
router.register('users', OneViewSet, basename='users1') # Регистрируем роутер(маршрут с префиксом users, вызывающий OneViewSet, с определенными basename users1(необязательно)).

urlpatterns = router.urls # Экспортируем маршруты в django

# При аутентификации нужно прописать дополнительный маршрут для получения токена доступа
urlpatterns += [
    path('api/token/', obtain_auth_token), # При отправке POST запроса на этот маршрут с правильными данными супер пользователя будет возвращаться токен доступа для этого пользователя
    path('protected/<int:id>/', OneApiView.as_view()), # get запрос
    path('protected/', OneApiView.as_view()), # as_view() метод который преобразует класс в view функцию
]

# После регистрации роутер создаст маршруты. В данном случае:
# GET users/
# POST users/
# GET users/1/
# PUT users/1/
# PATCH users/1/
# DELETE users/1/