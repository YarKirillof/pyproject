from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fio = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    height = models.CharField(max_length=10, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)
    shoe = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    pass_data = models.CharField(max_length=9, null=True, blank=True)
    # photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    # @receiver(post_save, sender=User)
    # def save_or_create_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     else:
    #         try:
    #             instance.profile.save()
    #         except ObjectDoesNotExist:
    #             Profile.objects.create(user=instance)
    def __str__(self):
        return self.user.username
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
#


