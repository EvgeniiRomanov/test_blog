from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User #для оформления пользователей

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name="Текст")
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    # email = models.EmailField(default='', verbose_name='Email')

    author = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)     # удаляем все записи пользователя

    def __str__(self):   # отображение запись объекта в читаемой форме
        return f"Запись №{self.id}"


    class Meta:   # украшения по именам для модели, что бы отображалась по рус
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')


class Comment(models.Model):
    """Комментарии и оценки статьй"""