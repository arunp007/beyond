# Generated by Django 4.0.1 on 2024-04-04 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0013_remove_cartitems_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCustomization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nighty_length', models.TextField(max_length=50)),
                ('sleeve_type', models.TextField(max_length=100)),
                ('feeding_type', models.TextField(max_length=100)),
                ('zip_type', models.TextField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customization', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
