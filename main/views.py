from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def homepage(request):
    # Get some sample data for the homepage
    customers_count = Customer.objects.count() if 'Customer' in globals() else 0
    appointments_count = Appointment.objects.count() if 'Appointment' in globals() else 0
    
    context = {
        'customers_count': customers_count,
        'appointments_count': appointments_count,
    }
    return render(request, 'main/homepage.html', context)

def customers(request):
    customers = Customer.objects.all()[:10] if 'Customer' in globals() else []
    return render(request, 'main/customers.html', {'customers': customers})

