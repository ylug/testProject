from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователей с ролью - user'''

    def handle(self, *args, **options):
        # User_1
        user = User.objects.create(
            email='petya222@mail.ru',
            first_name='Vania',
            last_name='Poroch',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('vanaiii')
        user.save()

        # User_2
        user = User.objects.create(
            email='erreww@mail.ru',
            first_name='Nadir',
            last_name='Timkanov',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('kalokol3333')
        user.save()

        # User_3
        user = User.objects.create(
            email='wwweeewww@mail.ru',
            first_name='Artem',
            last_name='Adilti',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('333test444')
        user.save()
