# Generated by Django 4.0.6 on 2022-10-18 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_bid_date_alter_comment_user_alter_listing_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='User',
        ),
        migrations.AlterField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 23, 32, 54, 956483)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 18, 23, 32, 54, 955489)),
        ),
    ]