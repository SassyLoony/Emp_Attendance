# Generated by Django 4.0.6 on 2022-08-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0044_alter_timesheet_posting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='posting_date',
            field=models.DateField(blank=True, default=''),
        ),
    ]
