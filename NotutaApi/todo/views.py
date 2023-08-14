from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from todo.models import Todo as TodoModel
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoSerializer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(
                todo_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            todo_serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    elif request.method == 'GET':
        todos = TodoModel.objects.all()
        title = request.GET.get('title', None)
        
        if title is not None:
            todos = todos.filter(title__icontains=title)
        
        todo_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(
            todo_serializer.data, safe=False
        )


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = TodoModel.objects.get(pk=pk)
    except TodoModel.DoesNotExist:
        return JsonResponse(
            {'message': f'This todo {pk} is not exist!'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        todo_serializer = TodoSerializer(todo)
        return JsonResponse(todo_serializer.data)
    
    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoSerializer(
            todo, data=todo_data
        )
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data)
        return JsonResponse(
            todo_serializer.errors,
            status=status.HTTP_404_NOT_FOUND
        )
    
    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse(
            {'message': 'Todo was deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
    

@api_view(['GET'])
def todo_list_completed(request):
    todos = TodoModel.objects.filter(completed=True)

    if request.method == 'GET':
        todo_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(
            todo_serializer.data,
            safe=False
        )