from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('customers/', views.customers, name='customers'),
    path('appointments/', views.appointments, name='appointments'),
    path('services/', views.services, name='services'),
    path('project/',views.project,name='project'),
]
