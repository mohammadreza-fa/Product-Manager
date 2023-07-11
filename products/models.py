from django.core.files.base import ContentFile
from django.dispatch import receiver
from users.models import User
from django.db import models


class EmailTemplate(models.Model):
    template = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Serial(models.Model):
    serial = models.CharField(max_length=25, unique=True)
    usage = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.serial


class Product(models.Model):
    product_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=25, null=False, blank=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.CharField(max_length=13, null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, null=True, blank=True)
    registrant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} | {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Property(models.Model):
    STATUS = (
        ('paid', 'paid'),
        ('unpaid', 'unpaid')
    )
    name = models.CharField(max_length=55, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    distributor_share = models.PositiveIntegerField()
    developer_share = models.PositiveIntegerField()
    paid = models.PositiveIntegerField(default=0)
    status = models.CharField(choices=STATUS, max_length=6, default='unpaid')
    notes = models.TextField()

    def debt(self):
        return self.product.price - self.paid

    def dev_share(self):
        return (self.product.price * self.developer_share) / 100

    def dist_share(self):
        return (self.product.price * self.distributor_share) / 100


class Email(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='EmailProduct')

    def __str__(self):
        return f'{self.product.name} | {self.product.email}'

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'