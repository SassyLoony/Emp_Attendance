# Generated by Django 4.0.6 on 2022-08-23 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0054_timesheet_rejected_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave_apply',
            name='current_time',
        ),
        migrations.AddField(
            model_name='leave_apply',
            name='leave_apply_time',
            field=models.CharField(default='', max_length=50),
        ),
    ]
