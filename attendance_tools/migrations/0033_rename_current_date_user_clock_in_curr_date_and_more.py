# Generated by Django 4.0.6 on 2022-07-30 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0032_rename_current_date_now_user_clock_in_current_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_clock_in',
            old_name='current_date',
            new_name='curr_date',
        ),
        migrations.RenameField(
            model_name='user_clock_in',
            old_name='current_time',
            new_name='curr_time',
        ),
    ]