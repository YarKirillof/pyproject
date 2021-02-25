# Generated by Django 3.1.6 on 2021-02-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casting',
            name='fee',
        ),
        migrations.RemoveField(
            model_name='casting',
            name='slug',
        ),
        migrations.AlterField(
            model_name='casting',
            name='description',
            field=models.TextField(blank=True, verbose_name='Требования'),
        ),
        migrations.AlterField(
            model_name='casting',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
