from django.shortcuts import render

def homepage(request):
    context = {
        'customers_count': 5,
        'appointments_count': 10,
    }
    return render(request, 'main/homepage.html', context)

def customers(request):
    context = {
        'customers': [],
        'total_customers': 0,
        'page_title': 'Customer Management'
    }
    return render(request, 'main/customers.html', context)

def appointments(request):
    context = {
        'appointments': [],
        'total_appointments': 0,
        'page_title': 'Appointments Management'
    }
    return render(request, 'main/appointments.html', context)

def services(request):
    context = {
        'services': [],
        'total_services': 0,
        'avg_price': 50,
        'page_title': 'Services & Pricing'
    }
    return render(request, 'main/services.html', context)
def project(request):
	context ={
	   'page_title':'About the Project'	
	}
	return render(request,'main/project.html', context)
