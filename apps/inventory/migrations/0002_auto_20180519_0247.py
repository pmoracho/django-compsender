# Generated by Django 2.0.5 on 2018-05-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulo',
            name='grupo',
        ),
        migrations.AddField(
            model_name='aplicacion',
            name='grupo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
