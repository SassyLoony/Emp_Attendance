# Generated by Django 4.0.6 on 2022-08-17 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0042_alter_timesheet_posting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='posting_date',
            field=models.DateTimeField(default=datetime.date(2022, 8, 17)),
        ),
    ]
