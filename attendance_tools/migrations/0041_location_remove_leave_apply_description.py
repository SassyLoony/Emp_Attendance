# Generated by Django 4.0.6 on 2022-08-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tools', '0040_timesheet_timesheet_option_val'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('lat', models.CharField(default='', max_length=150)),
                ('lon', models.CharField(default='', max_length=150)),
                ('remarks', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='leave_apply',
            name='description',
        ),
    ]
