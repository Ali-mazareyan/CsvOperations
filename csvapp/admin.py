from django.contrib import admin
from .models import csv_db
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class YourModelResource(resources.ModelResource):
    class Meta:
        model = csv_db

class YourModelAdmin(ImportExportModelAdmin):
    resource_class = YourModelResource

# Register your model with the ImportExportModelAdmin
admin.site.register(csv_db, YourModelAdmin)
