# Generated by Django 4.0.1 on 2024-04-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_alter_quantity_quantity_alter_size_size'),
        ('accounts', '0020_remove_cartitems_size_variant_cartitems_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='quantity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.quantity'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.size'),
        ),
    ]
