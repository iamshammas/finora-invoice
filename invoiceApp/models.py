from django.db import models
# Create your models here.

class Invoice(models.Model):
    customer_name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.customer_name
    
class InvoiceItem(models.Model):
    
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=350)
    qty = models.IntegerField()
    unit_price = models.IntegerField()
    total_amount = models.IntegerField(blank=True)
    dates = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args, **kwargs):
        self.total_amount = self.qty * self.unit_price
        super().save(*args, **kwargs)
        grand_tot = 0
        for item in self.invoice.invoiceitem_set.all():
            if item.total_amount:
                grand_tot += item.total_amount
        self.invoice.grand_total = grand_tot
        self.invoice.save()