# Generated by Django 2.1.5 on 2019-01-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egresos', '0007_auto_20190110_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='xml',
            field=models.FileField(blank=True, null=True, upload_to='factruras/'),
        ),
    ]
