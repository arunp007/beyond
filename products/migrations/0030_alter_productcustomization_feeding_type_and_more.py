# Generated by Django 4.0.1 on 2024-04-03 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_productcustomization_delete_customization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcustomization',
            name='feeding_type',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcustomization',
            name='nighty_length',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productcustomization',
            name='sleeve_type',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productcustomization',
            name='zip_type',
            field=models.TextField(max_length=100),
        ),
    ]
