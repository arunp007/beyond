# Generated by Django 4.0.1 on 2024-04-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_product_quantity_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
