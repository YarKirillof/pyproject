from django.db import models
from my_project import settings


# Create your models here.

class Casting(models.Model):
    title = models.CharField(max_length=255, null=True,  verbose_name='Наименование')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True,  verbose_name='Категория')
    height = models.CharField(max_length=255, null=True,  verbose_name='Рост')
    size = models.CharField(max_length=255, null=True,  verbose_name='Размер_одежды')
    sizeshoe = models.CharField(max_length=255, null=True,  verbose_name='Размер_обуви')
    place = models.CharField(max_length=255, null=True,  verbose_name='Адрес_локации')
    date = models.CharField(max_length=255, null=True,  verbose_name='Дата')
    time = models.CharField(max_length=255, null=True,  verbose_name='Время')
    hour = models.CharField(max_length=255, null=True,  verbose_name='Время_занятости')
    image = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    description = models.TextField(verbose_name='Требования', null=True, blank=True)
    fee = models.CharField(max_length=255, null=True,  verbose_name='Ставка')

    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
