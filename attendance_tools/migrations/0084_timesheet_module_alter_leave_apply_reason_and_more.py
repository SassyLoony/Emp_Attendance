# Generated by Django 4.0.6 on 2023-01-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0083_rename_date_overall_work_hours_dates'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='module',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='leave_apply',
            name='reason',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='leave_apply',
            name='rejected_reason',
            field=models.CharField(default='', max_length=255),
        ),
    ]
