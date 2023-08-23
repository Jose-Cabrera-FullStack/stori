from django.apps import AppConfig


class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Change this to the name of your app and every reference to app_name in this folder
    name = 'app_name'
