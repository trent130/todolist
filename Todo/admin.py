from django.contrib import admin
from .models import TodoItem, UserProfile
# Register your models here.

admin.site.register(TodoItem)
admin.site.register(UserProfile)
