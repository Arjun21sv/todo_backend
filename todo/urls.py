from django.urls import path
from .views import api_root, TodoListCreateAPIView

urlpatterns = [
    path('', api_root, name='api-root'),
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list'),
]
