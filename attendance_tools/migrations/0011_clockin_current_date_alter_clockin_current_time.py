# Generated by Django 4.0.6 on 2022-07-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0010_alter_clockin_current_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='clockin',
            name='current_date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='clockin',
            name='current_time',
            field=models.CharField(default='', max_length=50),
        ),
    ]
