from django.urls import path
from invoiceApp import views
from .views import InvoiceDashboard,CreateCustomer

urlpatterns = [
    path('',InvoiceDashboard.as_view()),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('api/v1/user/create/',CreateCustomer.as_view())
]
