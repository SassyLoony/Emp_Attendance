# Generated by Django 4.0.6 on 2022-09-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0070_alter_timesheet_rejected_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='overall_work_hours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=50)),
                ('date', models.CharField(default='', max_length=50)),
                ('hours', models.CharField(default='', max_length=50)),
                ('note1', models.CharField(default='', max_length=50)),
                ('note2', models.CharField(default='', max_length=50)),
                ('note3', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
