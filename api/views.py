from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
# from rest_framework import serializers
from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializers


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

# Create your views here.

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     model = Task
#     serializer_class = TaskSerializers

# class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class TaskDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class TaskDetail(generics.RetrieveAPIView):
#     model = Task
#     serializer_class = TaskSerializers
#
#     def get_queryset(self):
#         pk = self.kwargs['pk']
#         queryset = Task.objects.filter(pk=pk)
#         return queryset
