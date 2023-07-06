from django.contrib import admin
from .models import Products, EmailTemplate

admin.site.register(Products)
admin.site.register(EmailTemplate)