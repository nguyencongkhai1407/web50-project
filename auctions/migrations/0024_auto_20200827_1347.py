# Generated by Django 3.1 on 2020-08-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20200827_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closed_listing',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
