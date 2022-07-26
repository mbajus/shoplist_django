# Generated by Django 4.0.6 on 2022-07-19 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoplist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shoplist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='shop',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='unit',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
