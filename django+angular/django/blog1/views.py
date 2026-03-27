# Файл для обработки запросов из файла urls
# Принимает HTTP request и возвращает response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import ModelOne
import json
from django.views.decorators.csrf import csrf_exempt

def create_user1(request, name, password): # request - это объект, который содержит ВСЮ информацию о запросе
    user =  ModelOne.objects.create(name=name, password=password) # Создает новый объект и отправляет SQL запрос INSERT с указанными аргументами
    return HttpResponse(f"User {user.name} created") # Возвращает HTTP-ответ в виде строки

@csrf_exempt # Для отключения CSRF для текущего view
def create_user2(request):
    if request.method == "POST":
        data = json.loads(request.body) # Преобразует тело запроса из JSON в Python объект(словарь)
        name = data.get("name") # Получить значение по ключу в словаре
        password = data.get("password")

        user =  ModelOne(name=name, password=password)
        user.save() # То же самое как user =  ModelOne.objects.create(name=name, password=password)

        return JsonResponse({"name": name}) # 


def get_users(request):
    users =  ModelOne.objects.all() # Возвращает все объекты из модели в виде QuerySet
    data = list(users.values())
    return JsonResponse(data, safe=False) # safe=False - указывать чтобы django не проверяла эти данные на безопасность
    # return render(request, "blog/users.html", {"users": users})


def get_user(request, name):
    # user =  ModelOne.objects.get(name=name) # Возвращает один объект модели. Можно преобразовать в словарь вручную
    user =  ModelOne.objects.filter(name=name).values().first() # метод filter() возвращает QuerySet, а values() превращает словарь(работает только с QuerySet), затем first() возвращает первый словарь
    # user = get_object_or_404(ModelOne, name=name) # Лучше использовать этот вариант в случае если объект может отсутствовать
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


def change_user(request, id, name):
    user = get_object_or_404(ModelOne, id=id)
    user.name = name
    user.save()
    return HttpResponse(f"User {user.name} changed")

def get_user_json(request, id):
    user = get_object_or_404(ModelOne, id=id)
    data = {
        "name": user.name,
        "password": user.password
    }
    return JsonResponse(data)


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
# render()            # HTML-файл
# redirect()          # Перенаправление