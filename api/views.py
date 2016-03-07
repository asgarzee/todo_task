from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Task
from .serializers import TaskSerializers


# Create your views here.

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     model = Task
#     serializer_class = TaskSerializers

class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class TaskDetail(generics.RetrieveAPIView):
#     model = Task
#     serializer_class = TaskSerializers
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         queryset = Task.objects.filter(pk=pk)
#         return queryset
