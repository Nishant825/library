from django.core.management.base import BaseCommand
from django.conf import settings
import subprocess

class Command(BaseCommand):
    help = 'Start Celery worker'

    def handle(self, *args, **options):
        celery_command = f'celery -A {settings.CELERY_APP} worker --loglevel=info'

        # Start Celery worker
        subprocess.Popen(celery_command, shell=True)
        self.stdout.write(self.style.SUCCESS('Celery worker started successfully.'))