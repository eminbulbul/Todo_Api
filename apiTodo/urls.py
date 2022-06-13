from django.urls import path
from .views import home, hello_world, todoList,todoCreate


urlpatterns = [
    path('', home),
    path('hello/', hello_world),
    path('todolist/', todoList),
    path('todocreate/', todoCreate),
]
