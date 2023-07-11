from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView
from product_manager.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from permissions import IsManagerOrDistributorUser
from email.message import EmailMessage
from users.models import User
from products.models import *
from .serializers import *
import smtplib


class UserCreate(CreateAPIView):
    """
        Create User by Distributors
    """
    serializer_class = UserSerializerDistributor
    permission_classes = [IsManagerOrDistributorUser, ]


class UserList(ListAPIView):
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()
    permission_classes = [IsManagerOrDistributorUser, ]


class UserUpdate(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()
    lookup_field = 'email'
    permission_classes = [IsManagerOrDistributorUser, ]


class UserDetail(RetrieveAPIView):
    """
        Detail of User for Distributors
    """
    serializer_class = UserSerializerDistributor
    queryset = User.objects.filter(role='customer').all()
    lookup_field = 'email'
    permission_classes = [IsManagerOrDistributorUser, ]


class ProductCreate(CreateAPIView):
    """
        Create User by Distributors
    """
    serializer_class = ProductSerializerDistributor
    permission_classes = [IsManagerOrDistributorUser, ]

    def perform_create(self, serializer):
        return serializer.save(product_id=(randint(000, 999)), registrant=self.request.user)


class ProductList(ListAPIView):
    serializer_class = ProductSerializerDistributor
    permission_classes = [IsManagerOrDistributorUser, ]

    def get_queryset(self):
        return Product.objects.filter(registrant__email=self.request.user.email)


class ProductDistributorList(ListAPIView):
    """
        List of products created by the distributor
    """
    serializer_class = ProductSerializerDistributor
    permission_classes = [IsManagerOrDistributorUser, ]

    def get_queryset(self):
        return Product.objects.filter(registrant__email=self.request.user.email)


class ProductUpdate(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = ProductSerializerDistributor
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerOrDistributorUser, ]

    def get_queryset(self):
        return Product.objects.filter(registrant__email=self.request.user.email)


class ProductDestroy(RetrieveUpdateAPIView):
    """
        Update User by Distributors
    """
    serializer_class = ProductSerializerDistributor
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerOrDistributorUser, ]

    def get_queryset(self):
        return Product.objects.filter(registrant__email=self.request.user.email)


class ProductDetail(RetrieveAPIView):
    """
        Detail of User with serial for Distributors
    """
    serializer_class = ProductSerializerDistributor
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerOrDistributorUser, ]

    def get_queryset(self):
        return Product.objects.filter(registrant__email=self.request.user.email)


class PropertyList(ListAPIView):
    """
        List of products created by the distributor
    """
    serializer_class = PropertySerializerDistributor
    queryset = Property.objects.all()
    permission_classes = [IsManagerOrDistributorUser, ]


class PropertyDetail(RetrieveAPIView):
    """
        Detail of User with serial for Distributors
    """
    serializer_class = PropertySerializerDistributor
    queryset = Property.objects.all()
    lookup_field = 'serial__serial'
    permission_classes = [IsManagerOrDistributorUser, ]


class EmailCreate(CreateAPIView):
    serializer_class = EmailSerializerDistributor
    permission_classes = [IsManagerOrDistributorUser, ]

    def create(self, request, *args, **kwargs):
        data = EmailSerializersManagers(data=self.request.data)
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
