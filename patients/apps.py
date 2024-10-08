from django.apps import AppConfig


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'
    # Import the signals.py in apps.py: You need to tell Django to import the signals.py file when your app is ready so that the signal gets registered.
    def ready(self):
        import patients.signals