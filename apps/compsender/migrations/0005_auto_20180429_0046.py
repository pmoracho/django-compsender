# Generated by Django 2.0.4 on 2018-04-29 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compsender', '0004_auto_20180429_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='importe_gravado',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='importe_otros_impuestos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='importe_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='iva_10_5',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='iva_21',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='iva_27',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='iva_2_5',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comprobante',
            name='iva_5',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=15),
            preserve_default=False,
        ),
    ]
