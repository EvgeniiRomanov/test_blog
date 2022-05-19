from django.contrib import admin

from .models import Note

@admin.register(Note)               # добавляем модель Note в админку
class NoteAdmin(admin.ModelAdmin):
    ...
# Register your models here.
