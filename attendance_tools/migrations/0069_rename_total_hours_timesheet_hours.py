# Generated by Django 4.0.6 on 2022-08-29 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0068_rename_hours_timesheet_total_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='total_hours',
            new_name='hours',
        ),
    ]