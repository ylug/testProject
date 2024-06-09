from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователей с ролью - admin'''

    def handle(self, *args, **options):
        # Staff_1
        user = User.objects.create(
            email='vadim228@gmail.com',
            first_name='Vadim',
            last_name='Alvirov',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('vadim29081999')
        user.save()

        # Staff_2
        user = User.objects.create(
            email='13god244Gmail.ru',
            first_name='Sasha',
            last_name='Volnich',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('godgodgod13')
        user.save()
