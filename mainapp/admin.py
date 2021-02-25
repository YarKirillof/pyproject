from django.contrib import admin
from .models import Casting
from accounts.models import Profile




admin.site.register(Casting)
admin.site.register(Profile)
