from django.db import models

class CsvData(models.Model):
    # Define your model fields based on your CSV structure
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    # Add more fields as needed

    def __str__(self):
        return f'{self.column1} - {self.column2}'

class csv_db(models.Model):  # Corrected model name to follow Python naming conventions
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    family = models.CharField(max_length=255)
    StudentNumber = models.IntegerField()  # Renamed to follow Python naming conventions
    birthplace = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.family} - {self.StudentNumber} - {self.birthplace} - {self.email}'
