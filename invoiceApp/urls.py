from django.urls import path
from invoiceApp import views

urlpatterns = [
    path('',views.index)
]
