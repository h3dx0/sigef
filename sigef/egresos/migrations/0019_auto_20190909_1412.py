# Generated by Django 2.1.5 on 2019-09-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0018_auto_20190909_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepto',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='importe',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='concepto',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
