from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "priority",
    ]


admin.site.register(Task, TaskAdmin)
