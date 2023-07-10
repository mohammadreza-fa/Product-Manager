from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from users.models import User
from products.models import *
from .serializers import *


class UserCreate(CreateAPIView):
    """
        Create User by Distributors
    """
    serializer_class = UserSerializerDistributor


class UserList(ListAPIView):
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()


class UserUpdate(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()
    lookup_field = 'email'


class UserDetail(RetrieveAPIView):
    """
        Detail of User for Distributors
    """
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()
    lookup_field = 'email'


class ProductCreate(CreateAPIView):
    """
        Create User by Distributors
    """
    serializer_class = ProductSerializersDistributor


class ProductList(ListAPIView):
    serializer_class = ProductSerializersDistributor
    queryset = Product.objects.filter()


class ProductDistributorList(ListAPIView):
    """
        List of products created by the distributor
    """
    serializer_class = ProductSerializersDistributor

    def get_queryset(self):
        return Product.objects.filter(registrant_id=self.request.user.id)


class ProductUpdate(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = ProductSerializersDistributor
    lookup_field = 'email'

    def get_queryset(self):
        return Product.objects.filter(registrant_id=self.request.user.id)


class ProductDestroy(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = ProductSerializersDistributor
    lookup_field = 'email'

    def get_queryset(self):
        return Product.objects.filter(registrant_id=self.request.user.id)


class ProductDetail(ListAPIView):
    """
        Detail of User for Distributors
    """
    serializer_class = ProductSerializersDistributor

    def get_queryset(self):
        serial = self.request.query_params.get('serial')
        return Product.objects.filter(serial__serial=serial)


