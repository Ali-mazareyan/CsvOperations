from django.core.management.base import BaseCommand
from csvapp.models import csv_db

class Command(BaseCommand):
    help = 'Delete all records from CsvDB model'

    def handle(self, *args, **kwargs):
        csv_db.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All records deleted successfully.'))