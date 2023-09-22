from rest_framework import generics, viewsets
from django.shortcuts import render
from todoapp import models
from .serializers import TasksSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TasksSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = TasksSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = TasksSerializer


def todoappView(request):
    return render(request, 'todolist.html')
