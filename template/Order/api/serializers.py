from rest_framework import serializers
from Order.models import Order
from OrderItem.api.serilazers import OrderItemSerializer
from OrderItem.models import OrderItem

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_items','created_at']

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'customer' , 'order_items']

class OrderCreateSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id','customer' , 'order_items']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        if not order_items_data:
            raise serializers.ValidationError("Order must have at least one order item.")
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
