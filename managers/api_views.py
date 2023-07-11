from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from product_manager.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response
from email.message import EmailMessage
from permissions import IsManagerUser
from datetime import datetime
from users.models import User
from products.models import *
from .serializers import *
import smtplib


class UserCreate(CreateAPIView):
    """
        Create User by Managers
    """
    serializer_class = UserSerializerManager
    permission_classes = [IsManagerUser, ]


class UserList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    permission_classes = [IsManagerUser, ]


class UserUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'
    permission_classes = [IsManagerUser, ]


class UserDetail(RetrieveAPIView):
    """
        Detail of User for Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'
    permission_classes = [IsManagerUser, ]


class UserDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = UserSerializerManager
    queryset = User.objects.all()
    lookup_field = 'email'
    permission_classes = [IsManagerUser, ]


class ProductCreate(CreateAPIView):
    """
        Create User by Managers
    """
    serializer_class = ProductSerializerManager
    permission_classes = [IsManagerUser, ]

    def perform_create(self, serializer):
        return serializer.save(product_id=(randint(000, 999)), registrant=self.request.user)


class ProductList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    permission_classes = [IsManagerUser, ]


class ProductUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerUser, ]


class ProductDetail(RetrieveAPIView):
    """
        Detail of User for Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerUser, ]


class ProductDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = ProductSerializerManager
    queryset = Product.objects.all()
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerUser, ]


class SerialList(ListAPIView):
    """
        List of User for Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()
    permission_classes = [IsManagerUser, ]


class SerialUpdate(RetrieveUpdateAPIView):
    """
        Update User by Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()
    lookup_field = 'serial'
    permission_classes = [IsManagerUser, ]


class SerialDetail(DestroyModelMixin, RetrieveAPIView):
    """
        Detail of User for Managers
    """
    queryset = Serial.objects.all()
    serializer_class = SerialSerializerManagers
    lookup_field = "serial"
    permission_classes = [IsManagerUser, ]


class SerialDestroy(RetrieveDestroyAPIView):
    """
        Destroy User by Managers
    """
    serializer_class = SerialSerializerManagers
    queryset = Serial.objects.all()
    lookup_field = 'serial'
    permission_classes = [IsManagerUser, ]


class PropertyCreate(CreateAPIView):
    """
        Create Property by Managers
    """
    serializer_class = PropertySerializerManagers
    permission_classes = [IsManagerUser, ]


class PropertyList(ListAPIView):
    """
        List of all Properties for Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.all()
    permission_classes = [IsManagerUser, ]


class PropertyListPaid(ListAPIView):
    """
        List of Paid Properties for Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.filter(status='paid').all()
    permission_classes = [IsManagerUser, ]


class PropertyListUnpaid(ListAPIView):
    """
        List of Unpaid Properties for Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.filter(status='unpaid').all()
    permission_classes = [IsManagerUser, ]


class PropertyUpdate(RetrieveUpdateAPIView):
    """
        Update Property with Serial by Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class PropertyDetail(RetrieveAPIView):
    """
        Detail of Property with Serial by Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class PropertyDestroy(RetrieveDestroyAPIView):
    """
        Destroy Property with Serial by Managers
    """
    serializer_class = PropertySerializerManagers
    queryset = Property.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class EmailCreate(CreateAPIView):
    serializer_class = EmailSerializerManagers
    permission_classes = [IsManagerUser, ]

    def create(self, request, *args, **kwargs):
        data = EmailSerializerManagers(data=self.request.data)
        if data.is_valid():
            data.save()
            text = data.instance.product.template.template
            if '{first_name}' in text:
                text = text.replace('{first_name}', data.instance.product.first_name)
            if '{last_name}' in text:
                text = text.replace('{last_name}', data.instance.product.last_name)
            if '{email}' in text:
                text = text.replace('{email}', data.instance.product.email)
            if '{phone_number}' in text:
                text = text.replace('{phone_number}', data.instance.product.phone_number)
            if '{serial}' in text:
                text = text.replace('{serial}', data.instance.product.serial.serial)
            if '{price}' in text:
                text = text.replace('{price}', data.instance.product.price)
            if '{product_name}' in text:
                text = text.replace('{product_name}', data.instance.product.name)
            if '{registrant}' in text:
                text = text.replace('{registrant}', data.instance.product.registrant.last_name)
            if '{comment}' in text:
                text = text.replace('{comment}', data.instance.product.comment)

            subject = data.instance.product.name
            to = data.instance.product.email
            msg = EmailMessage()
            msg['Subject'] = f"{subject}"
            msg['From'] = EMAIL_HOST_USER
            msg['To'] = f"{to}"
            msg.set_content(f'{text}')
            with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PAASWORD)
                server.send_message(msg)
                return Response({'messages': 'ایمیل ارسال شد'})
        else:
            return Response(data.errors)


class EmailList(ListAPIView):
    serializer_class = EmailSerializerManagers
    queryset = Email.objects.all()
    permission_classes = [IsManagerUser, ]


class EmailTemplateList(ListAPIView):
    """
        List of Unpaid Properties for Managers
    """
    serializer_class = EmailTemplateSerializerManager
    queryset = EmailTemplate.objects.all()
    permission_classes = [IsManagerUser, ]


class EmailTemplateUpdate(RetrieveUpdateAPIView):
    """
        Update Email Template with id by Managers
    """
    serializer_class = EmailTemplateSerializerManager
    queryset = EmailTemplate.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class EmailTemplateDetail(RetrieveAPIView):
    """
        Detail of Email Template with id by Managers
    """
    serializer_class = EmailTemplateSerializerManager
    queryset = EmailTemplate.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class EmailTemplateDestroy(RetrieveDestroyAPIView):
    """
        Destroy Email Template with id by Managers
    """
    serializer_class = EmailTemplateSerializerManager
    queryset = EmailTemplate.objects.all()
    lookup_field = 'id'
    permission_classes = [IsManagerUser, ]


class EmailTemplateCreate(CreateAPIView):
    """
        Create Email Template by Managers
    """
    serializer_class = EmailTemplateSerializerManager
    permission_classes = [IsManagerUser, ]