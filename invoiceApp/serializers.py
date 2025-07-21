from rest_framework import serializers
from .models import InvoiceItem,Invoice


class InvoiceNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
    invoice = InvoiceNameSerializers()
    class Meta:
        model = InvoiceItem
        fields = '__all__'