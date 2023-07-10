from rest_framework import serializers
from datetime import datetime
from users.models import User
from products.models import *
from random import randint


class UserSerializerManager(serializers.ModelSerializer):
    """
        User Serializer for Managers
    """
    class Meta:
        model = User
        fields = '__all__'

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


class ProductSerializerManager(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        date = datetime.now().strftime('%d%m%y')
        serial = Serial.objects.create(serial=f"{validated_data['product_id']}-{date}-{randint(1000, 9999)}-{randint(1000, 9999)}")
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
        with open(f'Serials/{product.first_name} {product.last_name}.txt', 'w') as file:
            template = product.template.template
            # email_content = template.format(product.first_name, product.last_name, product.serial, product.first_name, product.last_name, product.email)
            email_content2 = template.replace('{first_name}', product.first_name).replace('{last_name}', product.last_name).replace('{serial}', serial.serial).replace('{email}', product.email)
            file.write(email_content2)

        return product


class SerialSerializerManagers(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = '__all__'


class PropertySerializersManagers(serializers.ModelSerializer):
    dev_share = serializers.ReadOnlyField()
    dist_share = serializers.ReadOnlyField()
    debt = serializers.ReadOnlyField()

    class Meta:
        model = Property
        fields = '__all__'


class EmailSerializersManagers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'