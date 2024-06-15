#Contains configuration for the app. This file is used to configure some of the application-specific settings

from django.apps import AppConfig

class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'
