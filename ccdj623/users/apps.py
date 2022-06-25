from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "ccdj623.users"
    verbose_name = "Users"
    label = 'user'
    def ready(self):
        try:
            from ssa412 import users
        except ImportError:
            pass
