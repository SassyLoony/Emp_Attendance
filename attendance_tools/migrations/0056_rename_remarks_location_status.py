# Generated by Django 4.0.6 on 2022-08-23 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0055_remove_leave_apply_current_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='remarks',
            new_name='status',
        ),
    ]
