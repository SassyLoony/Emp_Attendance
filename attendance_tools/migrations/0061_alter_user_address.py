# Generated by Django 4.0.6 on 2022-08-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0060_rename_name_location_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
    ]
