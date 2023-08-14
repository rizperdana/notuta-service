from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.TextField(blank=True, default='')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
