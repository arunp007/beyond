# Generated by Django 4.0.1 on 2024-04-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_quantity_quantity_alter_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='quantity',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
