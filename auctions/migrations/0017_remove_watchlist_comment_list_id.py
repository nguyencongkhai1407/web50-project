# Generated by Django 3.1 on 2020-08-26 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='comment_list_id',
        ),
    ]
