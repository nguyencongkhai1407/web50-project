# Generated by Django 3.1 on 2020-08-26 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_remove_watchlist_bid_list_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
