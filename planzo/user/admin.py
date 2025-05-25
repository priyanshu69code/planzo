from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import UserProfile, UserPrefrences

User = get_user_model()

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserPrefrences)


# Register your models here.
