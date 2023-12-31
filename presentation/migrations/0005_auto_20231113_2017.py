# Generated by Django 3.2.23 on 2023-11-13 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presentation', '0004_auto_20231113_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='context',
            field=models.TextField(default='Add your review', max_length=200),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Add your name', max_length=200),
        ),
    ]
