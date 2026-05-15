# При использовании DRF (который позволяет создавать API) логика обработки запросов и взаимодействия с данными в базе данных реализуется в классе ViewSet или APIView, который находится в файле views.py. В этом файле можно определить различные классы для различных моделей и маршрутов, а также методы для обработки различных типов HTTP-запросов (GET, POST, PUT, DELETE). В этих методах можно использовать различные функции и методы для получения данных из запроса, взаимодействия с базой данных и формирования ответа.
# DRF предоставляет множество встроенных классов и функций, которые облегчают процесс создания API и позволяют быстро разрабатывать функциональные приложения.
from rest_framework.viewsets import ModelViewSet
from .models import ModelOne
from .serializers import ModelOneSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view, permission_classes

class OneViewSet(ModelViewSet): # Класс наследует ModelViewSet. Это позволяет автоматически создавать все CRUD методы для модели, которая указана в queryset. ModelViewSet - это класс, который предоставляет полный набор действий для работы с моделью, включая создание, чтение, обновление и удаление объектов. Он автоматически обрабатывает HTTP-запросы и выполняет соответствующие действия на основе типа запроса (GET, POST, PUT, DELETE). 
    queryset = ModelOne.objects.all() 
    serializer_class = ModelOneSerializer # Указывает какой сериализатор использовать для преобразования данных модели в JSON и обратно. Сериализатор определяет, какие поля модели будут включены в JSON и как они будут валидироваться при получении данных от клиента.

    # Кастомный метод для нестандартной логики(в данном случае бесполезный, так как повторяет retrieve)
    @action(detail=True, methods=['get'], url_path='custom') # Декоратор для создания кастомного маршрута. detail=True означает что этот маршрут будет работать с конкретным объектом модели(то есть будет принимать id в URL-адресе), methods=['get'] означает что этот маршрут будет обрабатывать только GET запросы, url_path='custom' означает что этот маршрут будет доступен по адресу /users/{id}/custom/
    def custom(self, request, pk=None): # pk=None это id полученный из URL-адреса(pk-primary key)
        a = self.get_object() # Метод get_object() автоматически получает объект модели на основе pk из URL-адреса. Он использует queryset, указанный в классе, для поиска объекта модели с соответствующим pk. Если объект не найден, он возвращает ошибку 404. Этот метод удобен для получения конкретного объекта модели в методах класса, таких как retrieve(), update() и destroy(), а также в кастомных методах, таких как этот.
        # serializer = ModelOneSerializer(a)
        b = ModelOne.objects.filter(id=a.id) # имеет смысл только если ищем связанные объекты из другой модели
        serializer = ModelOneSerializer(b, many=True) # Сериализация в JSON(в данном случае объекты ModelOne, many=True означает сериализацию сразу нескольких объектов и поэтому возвращает массив словарей)
        return Response(serializer.data) # Response работает только внутри APIView(для raw views надо использовать JsonResponse)
        # return Response({"a": 1})




# Class-based view для аутентификации.
class OneApiView(APIView): # Класс наследует APIView. Это позволяет писать CRUD методы вручную, подходит для масштабируемости
    permission_classes = [IsAuthenticated] # Защищенный эндпойнт. Разрешаем доступ к этому API только аутентифицированным пользователям. То есть только пользователи с токеном доступа смогут обращаться к методам этого класса через HTTP-запросы(для этого надо первым делом получить токен, отправив POST запрос на /api/token/)

    # def get_object(self, id):
    #     return ModelOne.objects.get(pk=id)

    def get(self, request, id=None): # Благодаря наследованию APIView при HTTP GET запросе автоматический вызывается этот метод(то же самое с остальными методами)
        if id:
            a = get_object_or_404(ModelOne, pk=id)
            serializer = ModelOneSerializer(a)
            return Response(serializer.data)
        
        b = ModelOne.objects.all()
        serializer = ModelOneSerializer(b, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ModelOneSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, id): 
    #     a = self.get_object(id) 
    #     a.delete() 
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # def custom(self, request):
    #     ...


from rest_framework import mixins
from rest_framework import generics


# Mixins - это классы, которые предоставляют определенные методы для работы с данными, такие как list(), create(), retrieve(), update() и destroy(). Они могут быть использованы вместе с GenericAPIView для создания классов представлений, которые поддерживают определенные действия. Например, ListModelMixin предоставляет метод list() для получения списка объектов модели, а CreateModelMixin предоставляет метод create() для создания нового объекта модели. Использование миксинов позволяет создавать более гибкие и переиспользуемые классы представлений, которые могут поддерживать только те действия, которые необходимы для конкретного случая использования.
class ModelOneListCreateDetailView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView): 
    queryset = ModelOne.objects.all()
    serializer_class = ModelOneSerializer

    def get(self, request, *args, **kwargs): # Метод для обработки HTTP GET запросов. Он проверяет, есть ли в URL-адресе параметр pk (который обычно используется для указания конкретного объекта модели). Если pk присутствует, он вызывает метод retrieve() из RetrieveModelMixin для получения конкретного объекта модели. Если pk отсутствует, он вызывает метод list() из ListModelMixin для получения списка всех объектов модели. Это позволяет одному методу get() обрабатывать как запросы на получение списка объектов, так и запросы на получение конкретного объекта, в зависимости от наличия параметра pk в URL-адресе.
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs) # Вызывает RetrieveModelMixin
        return self.list(request, *args, **kwargs)         # Вызывает ListModelMixin

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)       # Вызывает CreateModelMixin

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)       # Вызывает UpdateModelMixin

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)      # Вызывает DestroyModelMixin


# Concrete Generic View Classes(full-crud) - это классы, которые предоставляют выбранный набор действий для работы с моделью, включая создание, чтение, обновление и удаление объектов. Они автоматически обрабатывают HTTP-запросы и выполняют соответствующие действия на основе типа запроса (GET, POST, PUT, DELETE). Например, ListCreateAPIView предоставляет методы для получения списка объектов модели и создания нового объекта модели, а RetrieveUpdateDestroyAPIView предоставляет методы для получения конкретного объекта модели, обновления его данных и удаления его из базы данных. Использование этих классов позволяет быстро создавать функциональные представления для работы с данными модели без необходимости писать много кода вручную.
class ModelOneListCreateView(generics.ListCreateAPIView): # GET и POST
    queryset = ModelOne.objects.all()
    serializer_class = ModelOneSerializer

class ModelOneDetailView(generics.RetrieveUpdateDestroyAPIView):      # GET(id), UPDATE И DELETE
    queryset = ModelOne.objects.all()
    serializer_class = ModelOneSerializer

# Отличия между ModelViewSet, APIView, Mixins и Concrete Generic View Classes:
# ModelViewSet - предоставляет полный набор действий для работы с моделью, включая создание, чтение, обновление и удаление объектов. Он автоматически обрабатывает HTTP-запросы и выполняет соответствующие действия на основе типа запроса (GET, POST, PUT, DELETE). Он также позволяет создавать кастомные методы для нестандартной логики.
# APIView - позволяет писать CRUD методы вручную, подходит для масштабируемости. Он не предоставляет автоматическую обработку HTTP-запросов и требует ручного определения методов для каждого типа запроса (GET, POST, PUT, DELETE). Он также позволяет создавать кастомные методы для нестандартной логики.
# Mixins - предоставляют определенные методы для работы с данными, такие как list(), create(), retrieve(), update() и destroy(). Они могут быть использованы вместе с GenericAPIView для создания классов представлений, которые поддерживают определенные действия. Использование миксинов позволяет создавать более гибкие и переиспользуемые классы представлений, которые могут поддерживать только те действия, которые необходимы для конкретного случая использования.
# Concrete Generic View Classes - предоставляют выбранный набор действий для работы с моделью, включая создание, чтение, обновление и удаление объектов. Они автоматически обрабатывают HTTP-запросы и выполняют соответствующие действия на основе типа запроса (GET, POST, PUT, DELETE). Использование этих классов позволяет быстро создавать функциональные представления для работы с данными модели без необходимости писать много кода вручную.

# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer): # метод для добавления дополнительной логики при сохранении объекта модели. Он вызывается при сохранении нового объекта модели и позволяет выполнять дополнительные действия, такие как установка владельца объекта на текущего аутентифицированного пользователя. В данном случае, при сохранении нового продукта, мы устанавливаем его владельцем текущего пользователя, который отправил запрос на создание продукта. Это обеспечивает связь между продуктом и пользователем, который его создал.
#         serializer.save(owner=self.request.user)



@api_view(['GET', 'POST']) # Декоратор для указания разрешенных HTTP методов для function based view. CSRF protection отключается автоматически для этих методов, так как они не изменяют данные на сервере
@permission_classes([IsAuthenticated])
def user(request, id):
    if request.method == 'GET':
        user = get_object_or_404(ModelOne, id=id)
        serializer = ModelOneSerializer(user)
        return Response(serializer.data) # Response работает только внутри APIView(для function based view надо использовать JsonResponse)
    
    elif request.method == 'POST':
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