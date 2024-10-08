# Generated by Django 4.2 on 2024-07-22 17:59

import datetime
from django.db import migrations, models
import proy_sales.utils


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_expiration_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productprice',
            options={'ordering': ('issue_date',), 'verbose_name': 'Precio Producto', 'verbose_name_plural': 'Precios Productos'},
        ),
        migrations.AlterField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 21, 17, 59, 16, 706601, tzinfo=datetime.timezone.utc), validators=[proy_sales.utils.validate_expiration_date], verbose_name='Caducidad'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='observaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Observacion'),
        ),
    ]
