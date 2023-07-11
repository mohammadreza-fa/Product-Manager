from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.db import models
import json


class User(AbstractBaseUser):
    """
        User Model
    """
    ROLES = (
        ('manager', 'manager'),
        ('distributor', 'distributor'),
        ('customer', 'customer')
    )
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=True)
    role = models.CharField(choices=ROLES, default='customer', max_length=15)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.role}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
