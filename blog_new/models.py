from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name="Текст")
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    # update_at1 = models.EmailField(default='', verbose_name='Email')