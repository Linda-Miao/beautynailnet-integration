# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection

def homepage(request):
    # Get some sample data for the homepage
    customers_count = Customer.objects.count() if 'Customer' in globals() 
else 0
    appointments_count = Appointment.objects.count() if 'Appointment' in 
globals() else 0
    
    context = {
        'customers_count': customers_count,
        'appointments_count': appointments_count,
    }
    return render(request, 'main/homepage.html', context)

def customers(request):
    customers_list = Customer.objects.all()
    context = {
        'customers': customers_list,
        'total_customers': customers_list.count(),
        'page_title': 'Customer Management'
    }
    return render(request, 'main/customers.html', context)

def appointments(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                a.APPOINTMENT_ID,
                a.APPOINTMENT_DATE,
                a.APPOINTMENT_TIME,
                a.STATUS,
                c.FIRST_NAME,
                c.LAST_NAME,
                c.PHONE_NUMBER,
                s.FIRST_NAME,
                s.LAST_NAME,
                a.TOTAL_COST
            FROM APPOINTMENT a
            JOIN CUSTOMER c ON a.CUSTOMER_ID = c.CUSTOMER_ID
            JOIN STAFF s ON a.STAFF_ID = s.STAFF_ID
            ORDER BY a.APPOINTMENT_DATE DESC
        """)
        appointments_data = cursor.fetchall()
    
    context = {
        'appointments': appointments_data,
        'total_appointments': len(appointments_data),
        'page_title': 'Appointments Management'
    }
    return render(request, 'main/appointments.html', context)

def services(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                SERVICE_ID,
                SERVICE_NAME,
                DESCRIPTION,
                DURATION,
                PRICE,
                CATEGORY
            FROM SERVICE
            ORDER BY CATEGORY, SERVICE_NAME
        """)
        services_data = cursor.fetchall()
    
    total_services = len(services_data)
    avg_price = sum(service[4] for service in services_data) / 
total_services if total_services > 0 else 0
    
    context = {
        'services': services_data,
        'total_services': total_services,
        'avg_price': avg_price,
        'page_title': 'Services & Pricing'
    }
    return render(request, 'main/services.html', context)
