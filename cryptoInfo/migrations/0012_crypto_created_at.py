# Generated by Django 3.0.6 on 2020-05-16 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoInfo', '0011_auto_20200516_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
