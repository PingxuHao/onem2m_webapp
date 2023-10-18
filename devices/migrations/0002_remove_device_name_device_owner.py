# Generated by Django 4.2.5 on 2023-09-17 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]