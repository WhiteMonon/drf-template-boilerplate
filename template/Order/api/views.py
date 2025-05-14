from rest_framework import viewsets
from rest_framework.response import Response
from Order.models import Order
from Order.api.serializers import OrderSerializer , OrderDetailSerializer , OrderCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class OrderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing order instances.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        return super().get_serializer_class()
    
    @swagger_auto_schema(
        operation_summary="Get all orders",
        operation_description="This endpoint returns a list of all orders.",
        responses={
            200: openapi.Response(
                description="A list of orders",
                schema=OrderSerializer(many=True)
            )
        }
    )
    def list(self, request, *args, **kwargs):
        """
        List all orders.
        """

        return super().list(request, *args, **kwargs)
    
