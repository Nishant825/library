from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime

class Command(BaseCommand):
    fake = Faker()
    help = 'Make demo users'

    def add_arguments(self, parser):
        parser.add_argument('--add', type=int, help='for adding users')
        parser.add_argument('--delete', type=int, help='for deleted users')

    def handle(self, *args, **options):
        add_user = options['add']
        delete_user = options['delete']
        if add_user:
            for _ in range(add_user):
                time_val = str(datetime.now()).split('.')[-1][:5]
                first_name = self.fake.first_name()
                username = first_name + time_val
                try:
                    User.objects.create(first_name=first_name, last_name=self.fake.last_name(),
                        email=self.fake.email(), username=username, password="Nishant#2796")
                    self.stdout.write(self.style.SUCCESS(f'User Recieved: {add_user} and created user is {username}'))
                except Exception as err:
                    self.stdout.write(self.style.SUCCESS(f'User not created: recieved error  {str(err)} and created s'))
            self.stdout.write(self.style.SUCCESS(f'{add_user} users created successfully'))

        if delete_user:
                deleted_user = User.objects.all().order_by('-id')[:delete_user]
                for user in deleted_user:
                    user.delete()
                    self.stdout.write(self.style.SUCCESS(f'{user.username} deleted successfully'))
                self.stdout.write(self.style.SUCCESS(f'{delete_user} user deleted successfully'))