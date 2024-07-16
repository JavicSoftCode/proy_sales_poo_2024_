# Generated by Django 4.2.12 on 2024-07-12 10:15

import datetime
from django.db import migrations, models
import proy_sales.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_product_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 11, 10, 15, 18, 94919, tzinfo=datetime.timezone.utc), validators=[proy_sales.utils.validate_expiration_date], verbose_name='Caducidad'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='issue_date',
            field=models.DateTimeField(db_index=True, validators=[proy_sales.utils.get_current_datetime], verbose_name='Fecha Emision'),
        ),
    ]
