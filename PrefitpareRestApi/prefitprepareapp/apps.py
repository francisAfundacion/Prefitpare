from django.apps import AppConfig

class PrefitprepareappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prefitprepareapp'

    def ready(self):
        import prefitprepareapp.signals