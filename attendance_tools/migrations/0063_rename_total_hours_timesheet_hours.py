# Generated by Django 4.0.6 on 2022-08-27 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0062_rename_hours_timesheet_total_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='total_hours',
            new_name='hours',
        ),
    ]
