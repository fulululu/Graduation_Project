# Generated by Django 2.0.3 on 2018-04-08 10:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20180408_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CREATETIME',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 4, 8, 10, 4, 25, 263344, tzinfo=utc)),
            preserve_default=False,
        ),
    ]