from django.contrib import admin
from .models import UserProfile,users

admin.site.register(UserProfile)
admin.site.register(users)