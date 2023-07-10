from django.contrib import admin
from .models import Product, EmailTemplate, Serial, Property

admin.site.register(Product)
admin.site.register(Serial)
admin.site.register(Property)
admin.site.register(EmailTemplate)