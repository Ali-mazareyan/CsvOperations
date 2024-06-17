import csv
from django.shortcuts import render
from django.http import JsonResponse
from .models import csv_db
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CsvDBForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView

def main(request):
    return render(request, 'csvapp/index.html')

def search(request):
    if request.method == 'POST':
        # Perform search in the CsvDB model
        search_term = request.POST.get('searchInput', '').lower()
        search_results = csv_db.objects.filter(
            Q(name__icontains=search_term) |
            Q(family__icontains=search_term) |
            Q(StudentNumber__icontains=search_term) |
            Q(birthplace__icontains=search_term) |
            Q(email__icontains=search_term) 
        )

        # Convert QuerySet to a list of dictionaries
        search_results_dict = [model_to_dict(result) for result in search_results]

        # Save search results to a CSV file
        result_csv_path = 'csvapp/static/cvsapp/search_results.csv'
        with open(result_csv_path, mode='w', newline='') as result_file:
            csv_writer = csv.writer(result_file)
            csv_writer.writerow(search_results_dict[0].keys())  # Write header
            csv_writer.writerows(result.values() for result in search_results_dict)  # Write data rows

        # Output search results as JSON and send to the browser
        response = JsonResponse(search_results_dict, safe=False)

        # Add a custom header to the response for downloading the CSV file
        response['Content-Disposition'] = 'attachment; filename="search_results.csv"'

        return response

    return render(request, 'csvapp/search.html')

def all_data(request):
    try:
        all_data = csv_db.objects.all()
    except csv_db.DoesNotExist:
        all_data = []

    return render(request, 'csvapp/all_data.html', {'all_data': all_data})

def add_record(request):
    if request.method == 'POST':
        form = CsvDBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_data')
    else:
        form = CsvDBForm()

    return render(request, 'csvapp/add_record.html', {'form': form})

def edit_record(request, record_id):
    record = get_object_or_404(csv_db, pk=record_id)
    form = CsvDBForm(instance=record)

    if request.method == 'POST':
        form = CsvDBForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            # Redirect with a success parameter
            return HttpResponseRedirect(reverse('edit_record', args=[record_id]) + '?success=true')

    return render(request, 'csvapp/edit_record.html', {'form': form, 'record_id': record_id})

def delete_record(request, record_id):
    record = get_object_or_404(csv_db, pk=record_id)

    if request.method == 'POST':
        record.delete()
        return HttpResponseRedirect(reverse('all_data'))

    return render(request, 'csvapp/delete_record.html', {'record': record, 'record_id': record_id})

class UserDetailView(DetailView):
    model = csv_db
    template_name = 'csvapp/delete_record.html'
    context_object_name = 'user_details'