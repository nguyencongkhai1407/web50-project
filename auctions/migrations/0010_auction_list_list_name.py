# Generated by Django 3.1 on 2020-08-22 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200821_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_list',
            name='list_name',
            field=models.CharField(default='', max_length=64),
        ),
    ]
