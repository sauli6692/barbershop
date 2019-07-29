from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from employees.choices import USER_TYPE_STAFF

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin'):
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='qwerty123',
                type=USER_TYPE_STAFF
            )
            self.stdout.write('Admin user created.')
        else:
            self.stdout.write('Admin user already exists.')
