from django.contrib import admin

from django_drf_playground.apps.to_do_list.models import Task
from django_drf_playground.apps.to_do_list.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "identifier"]
    search_fields = ("id", "name", "identifier")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "user"]
    search_fields = ("id", "title", "user", "status")
