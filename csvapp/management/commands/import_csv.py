# csvapp/management/commands/import_csv.py
from django.core.management.base import BaseCommand
from csvapp.models import csv_db
import csv

class Command(BaseCommand):
    help = 'Import data from CSV file into CsvDB model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row

                for row in reader:
                    if len(row) == 5:
                        id, name, age, email, city = row
                        csv_db.objects.create(id=id, name=name, age=age, email=email, city=city)
                    else:
                        self.stderr.write(self.style.ERROR(f'Skipping invalid row: {row}'))

            self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {csv_file_path}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {e}'))
