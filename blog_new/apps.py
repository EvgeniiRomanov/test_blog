from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogNewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_new'

    verbose_name = _('блоГГГ')   # rename app name
