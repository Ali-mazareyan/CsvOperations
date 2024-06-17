import csv
from .models import csv_db


def load_data_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the header row if it exists
        next(csv_reader, None)

        for row in csv_reader:
            # Create an instance of your model and save it to the database
            csv_db.objects.create(column1=row[0], column2=row[1])
            # Add similar lines for other columns

# Replace 'your_file.csv' with the actual path to your CSV file
load_data_from_csv('/static/cvsapp/data.csv')