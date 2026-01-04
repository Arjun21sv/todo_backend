from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView

from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        "todos": request.build_absolute_uri("todos/")
    })


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
