from rest_framework import serializers
from OrderItem.models import OrderItem
from Product.api.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product','product_id' ,'quantity']