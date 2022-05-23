from asyncio.base_tasks import _task_get_stack
from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)