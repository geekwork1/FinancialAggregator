from django.core.management.base import BaseCommand
from usersapp.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            User.objects.create(
                username='Admin',
                password='Der_P@rol111',
                email='mail@pochta.ru',
                is_superuser=True,
                is_active=True,
                is_staff=True
            )
            print("Суперпользователь успешно создан.")
        except Exception as e:
            print(f"Ошибка {e} при создании суперпользователя")
