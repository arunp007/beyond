# Generated by Django 4.0.1 on 2024-03-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=True),
        ),
    ]
