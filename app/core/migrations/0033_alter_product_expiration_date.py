# Generated by Django 4.2.12 on 2024-07-12 19:42

import datetime
from django.db import migrations, models
import proy_sales.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_product_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 19, 42, 51, 852834, tzinfo=datetime.timezone.utc), validators=[proy_sales.utils.validate_expiration_date], verbose_name='Caducidad'),
        ),
    ]
