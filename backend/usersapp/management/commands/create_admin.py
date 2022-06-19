from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = get_user_model()
        try:
            super_user.objects.create_superuser('Admin', 'mail@pochta.ru', 'Der_P@rol111')
            print("Суперпользователь успешно создан.")
        except Exception as e:
            print(f"Ошибка {e} при создании суперпользователя")
