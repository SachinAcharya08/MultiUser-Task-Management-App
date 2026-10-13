from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Tasks
from .serializers import TasksSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class TasksViewsets(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def list(self,request):
        qs=Tasks.objects.all()
        paginator=PageNumberPagination()
        paginator.page_size=2
        paginated_qs=paginator.paginate_queryset(qs,request)
        serializer=TasksSerializers(paginated_qs,many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def retrieve(self,request,pk=None):
        qs=Tasks.objects.all()
        task=get_object_or_404(qs,pk=pk)
        serializer=TasksSerializers(task)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=TasksSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def update(self,request,pk=None):
        qs=Tasks.objects.all()
        task=get_object_or_404(qs,pk=pk)
        serializer=TasksSerializers(task,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def partial_update(self,request,pk=None):
        qs=Tasks.objects.all()
        task=get_object_or_404(qs,pk=pk)
        serializer=TasksSerializers(task,data=request.data, partial=True)
        return Response(serializer.data,status=status.HTTP_206_PARTIAL_CONTENT)

    def destroy(self,request,pk=None):
        qs=Tasks.objects.all()
        task=get_object_or_404(qs,pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

