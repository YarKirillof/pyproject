from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(AbstractUser):
    first_name = None
    last_name = None
    fio = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    shoe = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pass_data = models.CharField(max_length=10, null=True, blank=True)
    photo = models.ImageField(blank=True, upload_to='media/')

    class Meta:
        ordering = ['fio']



