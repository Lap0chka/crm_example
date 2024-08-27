import csv
import openpyxl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from crm.forms import DbDownloadForm


def download_excel(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    return sheet.iter_rows(min_row=2, values_only=True)

def download_csv(file):
    file_data = file.read().decode("utf-8")
    csv_data = csv.reader(file_data.splitlines())
    next(csv_data)
    return csv_data

@login_required
def db_download(request):
    if request.method == 'POST':
        form = DbDownloadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            if file.name.endswith(('.xls', '.xlsx')):
                data = download_excel(file)
            elif file.name.endswith(('.csv')):
                data = download_csv(file)
            else:
                messages.error(request, 'File type not supported')
                return redirect(reverse('crm:download'))
            for row in data:
                print(row)
    else:
        form = DbDownloadForm()
    return render(request, 'crm/db/db_download.html', {'form': form})



