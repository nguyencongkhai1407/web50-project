# Generated by Django 3.1 on 2020-08-28 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20200828_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
