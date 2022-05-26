from django.db import models
from django.utils.translation import gettext_lazy as _ # для шаблонов с именами
from django.contrib.auth.models import User #для оформления пользователей

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name="Текст")
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    # email = models.EmailField(default='', verbose_name='Email')
    # author = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)     # удаляем все записи пользователя
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):   # отображение запись объекта в читаемой форме
        return f"Запись №{self.id}"

    class Meta:   # украшения по именам для модели, что бы отображалась по рус
        verbose_name = _('Запись')
        verbose_name_plural = _('Записи')


class Comment(models.Model):
    """Комментарии и оценки статьй"""
    class Ratings(models.IntegerChoices):
        WITHOUT_RATING = 0, _('Без оценки')
        TERRIBLE = 1, _("Ужасно")
        BADLY = 2, _("Плохо")
        FINE = 3, _("Удовлетворительно")
        GOOD = 4, _("Хорошо")
        EXCELLENT = 5, _("Отлично")

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name="Запись")
    #note1 =
    rating = models.IntegerField(default=Ratings.WITHOUT_RATING, choices=Ratings.choices, verbose_name="Оценка")

    def __str__(self):
        return f"{self.get_rating_display()}: {self.author}"

    class Meta:   # украшения по именам для модели, что бы отображалась по рус
        verbose_name = _("Комментарий")
        verbose_name_plural = _('Комментарии')