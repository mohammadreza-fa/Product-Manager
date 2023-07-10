from django.contrib.auth.models import Group
from django.contrib import admin
from .models import User, Log

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Log)