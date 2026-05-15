# Этот файл содержит описание функций, которые будут обрабатывать запросы и возвращать ответы. Каждая функция представляет собой view, которая принимает объект запроса и возвращает объект ответа. Django использует эти функции для обработки запросов и взаимодействия с данными в базе данных через модели. В этих функциях можно использовать различные методы для получения данных из запроса, взаимодействия с базой данных и формирования ответа.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import ModelOne
import json
from django.views.decorators.csrf import csrf_exempt

def create_user1(request, name, password): # request - это объект запроса, который содержит ВСЮ информацию о ней. name и password - это аргументы, которые мы получаем из URL-адреса. Они передаются в функцию автоматически благодаря определению пути в urls.py.
    user =  ModelOne.objects.create(name=name, password=password) # Создает новый объект и отправляет SQL запрос INSERT с указанными аргументами
    return HttpResponse(f"User {user.name} created") # Возвращает HTTP-ответ в виде строки

@csrf_exempt # Для отключения CSRF(Cross-Site Request Forgery) protection для текущего view. Нужен только для raw views
def create_user2(request):
    if request.method == "POST":
        data = json.loads(request.body) # Преобразует тело запроса из JSON в Python объект(словарь)
        # user = ModelOne.objects.create(**data)
        # return JsonResponse(user.to_json(), status=201)
        name = data.get("name") # Получить значение по ключу в словаре
        password = data.get("password")

        # user = ModelOne.objects.create( # Альтернативный способ
        #     name=data.get("name"),
        #     password=data.get("password")
        # )

        user = ModelOne(name=name, password=password)
        user.save() # То же самое как user =  ModelOne.objects.create(name=name, password=password)

        return JsonResponse({"name": name}) # 


def get_users(request):
    users =  ModelOne.objects.all() # Возвращает все объекты из модели в виде QuerySet
    data = list(users.values())
    # data = list(users.values('id', 'name', 'password')) # явное указание полей
    # return JsonResponse({"users": data}, safe=False) # более надежный способ это упаковать список в объект
    return JsonResponse(data, safe=False) # safe=False - указывать чтобы django не проверяла эти данные на безопасность
    # return render(request, "blog/users.html", {"users": users})

    # Альтернатива
    # users =  ModelOne.objects.all().values()
    # return JsonResponse({"users": list(users)}, safe=False)


def get_user(request, name):
    # user =  ModelOne.objects.get(name=name) # Возвращает ровно один объект модели(ошибку если больше 1 или 0). Можно преобразовать в словарь вручную
    user =  ModelOne.objects.filter(name=name).values().first() # метод filter() возвращает QuerySet, а values() превращает в словарь(работает только с QuerySet), затем first() возвращает первый словарь
    # user = get_object_or_404(ModelOne, name=name) # Лучше использовать этот вариант в случае если объект может отсутствовать(но все равно надо преобразовать в словарь вручную)
    # data = { # Преобразует объект в словарь вручную
    #     "id": user.id,
    #     "name": user.name,
    #     "password": user.password,
    # }
    # return JsonResponse(data)
    if not user:
        return JsonResponse({"error": "User not found"}, status=404)
    return JsonResponse(user)
    # return HttpResponse(f"User {user.name}")
    # return render(request, "blog/user.html", {"user": user}) # Последний аргумент это контекстный словарь для передачи данных в шаблон


# def change_user(request, id, name):
#     user = get_object_or_404(ModelOne, id=id)
#     user.name = name
#     user.save()
#     return HttpResponse(f"User {user.name} changed")

# def get_user_by_id(request, id):
#     user = get_object_or_404(ModelOne, id=id)
#     data = {
#         "name": user.name,
#         "password": user.password
#     }
#     return JsonResponse(data)



# View - a function that returns a response



# Create your views here.

# Request:

# request.method      # GET / POST
# request.GET         # query параметры
# request.POST        # данные формы
# request.headers     # заголовки
# request.user        # пользователь


# Response:

# HttpResponse       # Обычная строка
# JsonResponse       # JSON
# render()           # HTML-файл
# redirect()         # Перенаправление

