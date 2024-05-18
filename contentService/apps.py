from django.apps import AppConfig


class ContentserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contentService'

    def ready(self):
        import contentService.signals