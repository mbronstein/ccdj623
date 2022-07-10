from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "wip.accounts"
    verbose_name = "Accounts"
    label = 'accounts'

    # def ready(self):
    #     try:
    #         from ssa412 import users
    #     except ImportError:
    #         pass
