# Generated by Django 4.2.12 on 2024-07-10 09:01

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_product_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='productprice',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='productprice',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 9, 9, 1, 44, 335966, tzinfo=datetime.timezone.utc), verbose_name='Caducidad'),
        ),
    ]
