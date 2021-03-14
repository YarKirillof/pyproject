from django.contrib.auth.models import User
from django.db import models
from mainapp.models import Casting
from my_project import settings



# Create your models here.
class Order(models.Model):
    casting = models.ForeignKey(Casting, verbose_name='Кастинг', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Актер', on_delete=models.CASCADE)
    hired = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)
