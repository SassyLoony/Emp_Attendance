# Generated by Django 4.0.6 on 2022-08-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0038_user_acc_no_user_blood_group_user_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='current_time',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='image',
            name='user_current_date',
            field=models.CharField(default='', max_length=50),
        ),
    ]
