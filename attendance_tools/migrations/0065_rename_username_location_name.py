# Generated by Django 4.0.6 on 2022-08-29 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0064_remove_attendance_mail_table_current_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='username',
            new_name='name',
        ),
    ]
