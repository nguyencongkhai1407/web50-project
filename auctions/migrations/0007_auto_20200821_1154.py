# Generated by Django 3.1 on 2020-08-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20200820_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_list',
            name='url',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='media'),
        ),
    ]
