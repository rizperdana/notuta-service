from rest_framework import serializers
from todo.models import Todo as TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = (
            'title',
            'description',
            'completed',
            'created_at',
            'updated_at',
        )