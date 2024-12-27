from django.apps import AppConfig

## Es para configurar la app de ESTA APP

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
