# Generated by Django 4.0.6 on 2022-07-16 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0007_user_address_user_date_of_birth_user_job_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='clockin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_time', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
