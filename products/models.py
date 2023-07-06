from django.db import models
from users.models import User


class Products(models.Model):
    name = models.CharField(max_length=55)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    comment = models.TextField()
    registrant = models.ForeignKey(User, on_delete=models.CASCADE)
    serial = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class EmailTemplate(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    template = models.TextField()

    def __str__(self):
        return f'{self.product} | Template'

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'