# Generated by Django 4.0.6 on 2022-09-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0076_timesheet_leadname'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign_lead',
            name='lead_empid',
            field=models.CharField(default='', max_length=150),
        ),
    ]
