from rest_framework import serializers
from products.models import *
from users.models import User


class UserSerializerCustomers(serializers.ModelSerializer):
    """
        User Serializer for Customers
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class ProductSerializerCustomers(serializers.ModelSerializer):
    """
        Product Serializer for Customers
    """
    class Meta:
        model = Product
        exclude = ('product_id', 'created', 'updated', 'template')
