from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from products.models import *
from users.models import User


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


class ProductSerializersDistributor(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('product_id', 'created', 'updated')