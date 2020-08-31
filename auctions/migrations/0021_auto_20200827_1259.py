# Generated by Django 3.1 on 2020-08-27 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_closed_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='closed_listing',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='closed_listing',
            name='winner_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
