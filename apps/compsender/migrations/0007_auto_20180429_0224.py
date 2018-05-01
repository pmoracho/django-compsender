# Generated by Django 2.0.4 on 2018-04-29 02:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compsender', '0006_auto_20180429_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='punto_venta',
            field=models.IntegerField(blank=True, max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_punto_venta', message='El punto de venta debe ser un número de 1 a 9999', regex='[0-9]{4}')]),
        ),
    ]
