# Generated by Django 4.0.1 on 2024-03-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_product_size_variant_product_size_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
        migrations.AddField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='products.SizeVariant'),
        ),
    ]
