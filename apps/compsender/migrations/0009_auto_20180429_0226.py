# Generated by Django 2.0.4 on 2018-04-29 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compsender', '0008_auto_20180429_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobante',
            name='importe_gravado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='importe_no_gravado',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='importe_otros_impuestos',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='iva_10_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='iva_21',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='iva_27',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='iva_2_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='comprobante',
            name='iva_5',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
    ]
