# Generated by Django 4.0.5 on 2022-07-01 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='double',
            name='datetime',
        ),
        migrations.AddField(
            model_name='double',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 1, 14, 40, 12, 320358), null=True),
        ),
    ]