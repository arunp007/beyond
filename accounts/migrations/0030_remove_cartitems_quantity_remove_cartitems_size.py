# Generated by Django 4.0.1 on 2024-04-09 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_variant'),
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
