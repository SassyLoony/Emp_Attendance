# Generated by Django 4.0.6 on 2022-07-18 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0013_clock_out_remove_clockin_clock_out_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clock_out',
            new_name='clockout',
        ),
    ]
