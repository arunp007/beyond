# Generated by Django 4.0.1 on 2024-04-04 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_alter_quantity_quantity_alter_size_size'),
        ('accounts', '0016_productcustomization_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='size_variant',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='Quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.quantity'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.size'),
        ),
    ]
