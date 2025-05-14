from django.db import models
from Customer.models import Customer

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)