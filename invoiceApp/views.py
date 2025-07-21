from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
# from .models import InvoiceItem
from .serializers import InvoiceSerializers,InvoiceItem,InvoiceNameSerializers,Invoice
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
# Create your views here.

def index(request):
    return redirect('dashboard')

def dashboard(request):
    invoice = Invoice.objects.all()
    context = {
        invoice:'invoice'
    }
    return render(request,'dashboard.html',context)

class InvoiceDashboard(APIView):
    invoicess = InvoiceItem.objects.all()
    def get(self,request):
        serializer = InvoiceSerializers(self.invoicess,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CreateCustomer(APIView):
    def get(self,request):
        name = Invoice.objects.all()
        serializer = InvoiceNameSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = InvoiceNameSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)