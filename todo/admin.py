from django.contrib import admin

# Register your models here.
from todo.models import TodoList

admin.site.register(TodoList)
