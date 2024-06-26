# Generated by Django 4.0.1 on 2024-04-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0050_variant_remove_quantity_quantity_remove_size_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='quantity',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')]),
        ),
        migrations.AlterField(
            model_name='variant',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL'), ('XXXXL', 'XXXXL')], max_length=10),
        ),
    ]
