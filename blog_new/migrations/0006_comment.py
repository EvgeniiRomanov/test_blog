# Generated by Django 4.0.4 on 2022-05-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_new', '0005_note_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
