from django.contrib.auth.models import Group
from django.contrib import admin
from .models import User

admin.site.unregister(Group)
admin.site.register(User)