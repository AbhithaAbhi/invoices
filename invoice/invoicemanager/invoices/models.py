from django.db import models

# Create your models here.

class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer_name}"


class InvoiceDetail(models.Model):
    invoices = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.description