# Generated by Django 4.0.1 on 2024-04-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_remove_product_quantity_remove_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='quantity',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
