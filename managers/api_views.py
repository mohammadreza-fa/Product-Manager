from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from product_manager.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from datetime import datetime
from users.models import User
from .serializers import *


class UserCreate(CreateAPIView):
    """
        Create User by Managers
    """
    serializer_class = UserSerializerManager


class UserList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()


class UserUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'


class UserDetail(RetrieveAPIView):
    """
        Detail of User for Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'


class UserDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'


class ProductCreate(CreateAPIView):
    """
        Create User by Managers
    """
    serializer_class = ProductSerializerManager

    def perform_create(self, serializer):
        return serializer.save(product_id=(randint(000, 999)), registrant=self.request.user)


class ProductList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()


class ProductUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial'


class ProductDetail(RetrieveAPIView):
    """
        Detail of User for Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial'


class ProductDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial'


class SerialList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()


class SerialUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()
    lookup_field = 'serial'


class SerialDetail(DestroyModelMixin, RetrieveAPIView):
    """
        Detail of User for Managers
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializerManager
    lookup_field = "serial__serial"

    def retrieve(self, request, *args, **kwargs):
        print(self.request.META.get('REMOTE_ADDR'))
        print(self.request.META.get('HTTP_USER_AGENT'))
        instance = self.get_object()
        instance.serial.usage += 1
        instance.serial.save()
        serializer = self.get_serializer(instance)
        print(self.request.META)
        if instance.serial.usage >= 5:
            instance.serial.delete()
        return Response(serializer.data)


class SerialDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()
    lookup_field = 'serial'


class PropertyCreate(CreateAPIView):
    """
        Create Property by Managers
    """
    serializer_class = PropertySerializersManagers


class PropertyList(ListAPIView):
    """
        List of all Properties for Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()


class PropertyListPaid(ListAPIView):
    """
        List of Paid Properties for Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.filter(status='paid').all()


class PropertyListUnpaid(ListAPIView):
    """
        List of Unpaid Properties for Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.filter(status='unpaid').all()


class PropertyUpdate(RetrieveUpdateAPIView):
    """
        Update Property with Serial by Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'id'


class PropertyDetail(RetrieveAPIView):
    """
        Detail of Property with Serial by Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'id'


class PropertyDestroy(RetrieveDestroyAPIView):
    """
        Destroy Property with Serial by Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'id'


class PropertyUpdateSerial(RetrieveUpdateAPIView):
    """
        Update Property with Serial by Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'serial__serial'


class PropertyDetailSerial(RetrieveAPIView):
    """
        Detail of Property with Serial for Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'serial__serial'


class PropertyDestroySerial(RetrieveDestroyAPIView):
    """
        Destroy Property with Serial by Managers
    """
    serializer_class = PropertySerializersManagers
    queryset = Property.objects.all()
    lookup_field = 'serial__serial'


class EmailCreate(CreateAPIView):
    serializer_class = EmailSerializersManagers

    def create(self, request, *args, **kwargs):
        msg = EmailMessage()
        msg['Subject'] = f"{self.request.data['subject']}"
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = f"{self.request.data['email']}"
        msg.set_content(f'{self.request.data["text"]}')
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PAASWORD)
            server.send_message(msg)
            return Response({'messages': 'ایمیل ارسال شد'})



class ProductEmailCreate(CreateAPIView):
    serializer_class = EmailSerializersManagers

    def create(self, request, *args, **kwargs):
        product = Product.objects.filter(product_id=self.request.query_params.get('product_id'))
        data = EmailSerializersManagers()
