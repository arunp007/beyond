# Generated by Django 4.0.1 on 2024-03-03 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_fake_price_product_dummy_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_size',
        ),
    ]
