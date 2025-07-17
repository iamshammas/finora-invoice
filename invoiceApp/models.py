from django.db import models

# Create your models here.

class Invoice(models.Model):
    customer_name = models.CharField(max_length=150)
    date = models.DateTimeField()

    def __str__(self):
        return self.customer_name
    
class InvoiceItem(models.Model):
    name = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=350)
    qty = models.IntegerField()
    unit_price = models.IntegerField()
    total_amount = models.IntegerField()
    grand_total = models.IntegerField()