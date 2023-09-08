from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


# Create your views here.
def homepage(request):
    return render(request, 'dashboard.html')


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        if queryset is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(queryset, many=False)
        return Response(serializer.data)
