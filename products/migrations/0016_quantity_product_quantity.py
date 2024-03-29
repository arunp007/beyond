# Generated by Django 4.0.1 on 2024-03-09 05:47

from django.db import migrations, models
import products.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_rename_sizevariant_size_remove_product_size_variant_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name=products.models.Quantity),
        ),
    ]
