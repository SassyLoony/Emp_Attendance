# Generated by Django 4.0.6 on 2022-07-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0014_rename_clock_out_clockout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clockout',
            old_name='clock_out_time',
            new_name='clockout_time',
        ),
    ]
