# Generated by Django 4.0.6 on 2022-09-03 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0071_overall_work_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='overall_work_hours',
            old_name='note1',
            new_name='location',
        ),
    ]
