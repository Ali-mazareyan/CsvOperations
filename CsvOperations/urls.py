# urls.py
from django.contrib import admin
from django.urls import path
from django.urls import path
from csvapp.views import main, search, all_data, add_record, edit_record, delete_record
from csvapp.views import UserDetailView

urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('search/', search, name='search'),
    path('all_data/', all_data, name='all_data'),
    path('add_record/', add_record, name='add_record'),  # URL for adding a record
    path('edit_record/<int:record_id>/', edit_record, name='edit_record'),  # URL for editing a record
    path('delete_record/<int:pk>/', UserDetailView.as_view(), name='delete_record'),  # URL for deleting a record
]
