from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from todo.models import Todo as TodoModel
from todo.serializers import TodoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def todo_list(request):
    pass


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = TodoModel.objects.get(pk=pk)
    except TodoModel.DoesNotExist:
        return JsonResponse(
            {'message': f'This todo {pk} is not exist!'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    pass


@api_view(['GET'])
def todo_list_completed(request):
    pass