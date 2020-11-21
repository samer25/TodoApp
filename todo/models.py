from django.db import models


# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=200, blank=False)
    is_done = models.BooleanField(default=False)
