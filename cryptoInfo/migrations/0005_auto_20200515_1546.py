# Generated by Django 3.0.6 on 2020-05-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptoInfo', '0004_auto_20200515_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crypto',
            name='urlToImage',
            field=models.URLField(blank=True, null=True),
        ),
    ]
