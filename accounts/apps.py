from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'


class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import accounts.signals
