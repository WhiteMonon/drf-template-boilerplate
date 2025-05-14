from django.db import models
from Order.models import Order
from Product.models import Product

# Create your models here.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def _str__(self):
        return f"{self.product.name} - {self.quantity}"