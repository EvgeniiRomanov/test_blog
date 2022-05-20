from django.contrib import admin

from .models import Note

@admin.register(Note)               # добавляем модель Note в админку
class NoteAdmin(admin.ModelAdmin):   # наследуем весь костяк из admin.ModelAdmin

# отображение полей в списке в указанном порядке
    list_display = ('title', 'id', 'public', 'create_at', 'update_at')

# отвечает за отображение полей. Группировака поля в режиме редактирования
    fields = (('title', 'public'), 'message', 'create_at', 'update_at')

# если поле в модели не редактируемое (create_at), то помещаем сюда, если хотим его отображать
    readonly_fields = ('create_at', 'update_at')

# поля по которым искать
    search_fields = ['title', 'message']    # [=title] поиск точного совпадения

# фильтр справа
    list_filter = ['public']