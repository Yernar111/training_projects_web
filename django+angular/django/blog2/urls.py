# При использовании DRF можно использовать DefaultRouter для автоматической генерации маршрутов для ViewSet, что упрощает процесс создания API. 
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import OneApiView, OneViewSet

# from rest_framework.authtoken.views import obtain_auth_token # view для получения токена при обычной аутентификации
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # view для получения и обновления JWT

router = DefaultRouter() # Объект роутера.
router.register('users', OneViewSet, basename='users1') # Регистрируем роутер. Автоматический формирует маршруты с префиксом users для всех CRUD в ViewSet
urlpatterns = router.urls # (экспорт маршрутов в django) Получаем список маршрутов, которые были сгенерированы роутером. Этот список можно использовать в основном файле urls.py для включения маршрутов приложения. Например, path('api/', include('blog2.urls')) - это позволит использовать все маршруты, сгенерированные роутером, с префиксом api/.

# При аутентификации нужно прописать дополнительный маршрут для получения токена доступа
urlpatterns += [
    # path('api/token/', obtain_auth_token), # При отправке POST запроса на этот маршрут с правильными данными супер пользователя будет возвращаться токен доступа для этого пользователя(чтобы сработало необходимо создать супер пользователя в терминале)
    path('protected/<int:id>/', OneApiView.as_view()), # get/1 запрос
    path('protected/', OneApiView.as_view()), # get и post запросы. as_view() нужен для того чтобы превратить класс в функцию, которая может обрабатывать HTTP запросы. Этот метод создает экземпляр класса и вызывает соответствующий метод (get, post, put, delete) в зависимости от типа HTTP запроса.

    # добавляем кастомные маршруты для получения данных и аутентификации, используя APIView и JWT токены.
    # path('protected/custom/', OneApiView.as_view(get=OneApiView.custom)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Эндпоинт для получения access и refresh токенов при отправке POST запроса с правильными данными супер пользователя
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Эндпоинт для получения нового access токена при отправке POST запроса с правильным refresh токеном

]

# После регистрации роутер создаст маршруты. В данном случае:
# GET users/
# POST users/
# GET users/1/
# PUT users/1/
# PATCH users/1/
# DELETE users/1/

# Access токен - это токен, который используется для аутентификации при каждом запросе к защищенным маршрутам. Он имеет короткий срок действия (обычно 5-15 минут) и должен быть включен в заголовок Authorization каждого запроса.
# Refresh токен - это токен, который используется для получения нового access токена после истечения срока действия текущего access токена. Он имеет более длительный срок действия (обычно несколько дней или недель) и должен быть хранится в безопасном месте на клиенте. Когда access токен истекает, клиент может отправить refresh токен на эндпоинт обновления токена, чтобы получить новый access токен без необходимости повторной аутентификации пользователя.