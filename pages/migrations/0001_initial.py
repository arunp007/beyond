# Generated by Django 4.0.1 on 2024-04-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
