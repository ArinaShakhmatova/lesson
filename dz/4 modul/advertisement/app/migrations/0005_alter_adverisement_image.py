# Generated by Django 4.2.3 on 2023-08-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_adverisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adverisement',
            name='image',
            field=models.ImageField(upload_to='advertisement/', verbose_name='Изображение'),
        ),
    ]
