from django import forms
from .models import CsvData
from .models import csv_db

class CsvDataForm(forms.ModelForm):
    class Meta:
        model = CsvData
        fields = ['column1', 'column2']  # Add more fields as needed

class CsvDBForm(forms.ModelForm):
    class Meta:
        model = csv_db
        fields = ['id', 'birthplace', 'StudentNumber', 'family', 'name', 'email']
