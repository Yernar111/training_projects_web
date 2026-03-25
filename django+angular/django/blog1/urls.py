# Надо самостоятельно создать urls.py внутри app
from django.urls import path
# import views
from . import views

urlpatterns = [
    path("create_user/<str:name>/<int:password>", views.create_user1), # Плохой вариант, так как пароль передается через URL
    path("create_user/", views.create_user2), # Более надежный вариант
    path("get_users/", views.get_users),
    path("get_user/<str:name>/", views.get_user),
    # path("get_user/<int:id>", views.get_user, name="user1"), # name нужен для шаблонов и редиректов
]


# <int:id>     → число
# <str:name>   → строка
# <slug:slug>  → slug (my-post)
# <uuid:id>    → UUID