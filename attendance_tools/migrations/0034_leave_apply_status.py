# Generated by Django 4.0.6 on 2022-08-01 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0033_rename_current_date_user_clock_in_curr_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_apply',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
