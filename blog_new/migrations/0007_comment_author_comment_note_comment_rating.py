# Generated by Django 4.0.4 on 2022-05-24 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_new', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='note',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog_new.note'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(choices=[(0, 'Без оценки'), (1, 'Ужасно'), (2, 'Плохо'), (3, 'Удовлетворительно'), (4, 'Хорошо'), (5, 'Отлично')], default=0, verbose_name='Оценка'),
        ),
    ]
