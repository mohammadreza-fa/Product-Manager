from product_manager.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from django.contrib.auth.hashers import make_password
from email.message import EmailMessage
from rest_framework import serializers
from products.models import *
from users.models import User
from datetime import datetime
from random import randint
import smtplib


class UserSerializerDistributor(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def create(self, validated_data):
        password = make_password(validated_data['password'])
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            password=password
        )
        return user


class ProductSerializerDistributor(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        date = datetime.now().strftime('%d%m%y')
        serial = Serial.objects.create(serial=f"{validated_data['product_id']}-{date}-{randint(0000, 9999)}-{randint(0000, 9999)}")
        product = Product.objects.create(
            product_id=validated_data['product_id'],
            name=validated_data['name'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            price=validated_data['price'],
            comment=validated_data['comment'],
            template=validated_data['template'],
            registrant=validated_data['registrant'],
            serial=serial
        )
        template = product.template.template

        with open(f'Serials/{product.first_name} {product.last_name}.txt', 'w') as file:

            if '{first_name}' in template:
                template = template.replace('{first_name}', product.first_name)
            if '{last_name}' in template:
                template = template.replace('{last_name}', product.last_name)
            if '{email}' in template:
                template = template.replace('{email}', product.email)
            if '{phone_number}' in template:
                template = template.replace('{phone_number}', product.phone_number)
            if '{serial}' in template:
                template = template.replace('{serial}', product.serial.serial)
            if '{price}' in template:
                template = template.replace('{price}', product.price)
            if '{product_name}' in template:
                template = template.replace('{product_name}', product.name)
            if '{registrant}' in template:
                template = template.replace('{registrant}', product.registrant.last_name)
            if '{comment}' in template:
                template = template.replace('{comment}', product.comment)

            email_content = template
            file.write(email_content)

            subject = product.name
            to = product.email
            msg = EmailMessage()
            msg['Subject'] = f"{subject}"
            msg['From'] = EMAIL_HOST_USER
            msg['To'] = f"{to}"
            msg.set_content(f'{template}')
            with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
                server.login(EMAIL_HOST_USER, EMAIL_HOST_PAASWORD)
                server.send_message(msg)

        return product


class PropertySerializerDistributor(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class EmailSerializerDistributor(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'