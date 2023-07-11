from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from products.models import *
from .serializers import *


class UserDetail(RetrieveAPIView):
    """
        Detail of User for Customers
    """
    serializer_class = UserSerializerCustomers
    lookup_field = 'email'
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return User.objects.filter(email=self.request.user.email)


class ProductList(ListAPIView):
    """
        List of User Products for Customers
    """
    serializer_class = ProductSerializerCustomers
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Product.objects.filter(email=self.request.user.email).all()


class ProductDetail(RetrieveAPIView):
    """
        Detail of Product for Customers
    """
    serializer_class = ProductSerializerCustomers
    lookup_field = "serial__serial"
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Product.objects.filter(email=self.request.user.email).first()
