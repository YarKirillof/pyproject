# Generated by Django 3.1.6 on 2021-02-24 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0003_auto_20210220_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casting',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casting',
            name='category',
            field=models.CharField(max_length=255, null=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='date',
            field=models.CharField(max_length=255, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Требования'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='fee',
            field=models.CharField(max_length=255, null=True, verbose_name='Ставка'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='height',
            field=models.CharField(max_length=255, null=True, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='hour',
            field=models.CharField(max_length=255, null=True, verbose_name='Время_занятости'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='place',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес_локации'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='size',
            field=models.CharField(max_length=255, null=True, verbose_name='Размер_одежды'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='sizeshoe',
            field=models.CharField(max_length=255, null=True, verbose_name='Размер_обуви'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='time',
            field=models.CharField(max_length=255, null=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Наименование'),
        ),
    ]
