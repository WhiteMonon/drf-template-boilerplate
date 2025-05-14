from rest_framework import viewsets , status
from rest_framework.response import Response
from rest_framework.decorators import action
from Customer.models import Customer
from Customer.api.serializers import CustomerSerializer
from Order.models import Order
from Order.api.serializers import OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.action == 'orders':
            return OrderSerializer
        return super().get_serializer_class()
    
    @action(detail=True, methods=['get'], url_path='orders')
    def orders(self, request, pk=None):
        """
        Lấy danh sách đơn hàng của một khách hàng cụ thể
        """
        try:
            customer = self.get_object()
            orders = Order.objects.filter(customer=customer)
            serializer = self.get_serializer(orders, many=True)
            return Response(serializer.data)
        except Customer.DoesNotExist:
            return Response(
                {"error": "Không tìm thấy khách hàng"},
                status=status.HTTP_404_NOT_FOUND
            )