# Generated by Django 4.0.1 on 2024-04-06 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_alter_cartitems_quantity_alter_cartitems_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cartitems',
            name='size',
        ),
    ]
