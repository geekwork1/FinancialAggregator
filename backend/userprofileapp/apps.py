from django.apps import AppConfig


class userprofileappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userprofileapp'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import userprofileapp.signals