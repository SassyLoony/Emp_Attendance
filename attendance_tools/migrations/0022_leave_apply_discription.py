# Generated by Django 4.0.6 on 2022-07-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0021_leave_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_apply',
            name='discription',
            field=models.CharField(default='', max_length=50),
        ),
    ]
