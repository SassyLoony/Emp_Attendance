# Generated by Django 4.0.6 on 2022-08-21 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0052_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timesheet',
            old_name='user',
            new_name='username',
        ),
    ]
