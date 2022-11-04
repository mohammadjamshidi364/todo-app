from django.contrib import admin

from .models import TodoItem , Workspace


admin.site.register(TodoItem)

admin.site.register(Workspace)