# Generated by Django 4.0.1 on 2024-03-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_remove_product_size_variant_product_size_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
