from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'

    print("HELLOOOOO")


    def ready(self):
        import users.signals
