# Generated by Django 2.1.5 on 2019-09-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0017_auto_20190909_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepto',
            name='descuento_maximo',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='precio_venta_base',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
