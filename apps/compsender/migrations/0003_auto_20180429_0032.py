# Generated by Django 2.0.4 on 2018-04-29 00:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('compsender', '0002_tipocomprobante_codigo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.RemoveField(
            model_name='comprobante',
            name='description',
        ),
        migrations.AddField(
            model_name='comprobante',
            name='cae',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='cuit_emisor',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='comprobante',
            name='numero_comprobante',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
