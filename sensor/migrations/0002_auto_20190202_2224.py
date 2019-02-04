# Generated by Django 2.1.5 on 2019-02-02 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humidity',
            old_name='date',
            new_name='Date_and_Time',
        ),
        migrations.RenameField(
            model_name='humidity',
            old_name='id_sensor',
            new_name='SensorID',
        ),
        migrations.RenameField(
            model_name='humidity',
            old_name='value',
            new_name='Value',
        ),
        migrations.RenameField(
            model_name='temperature',
            old_name='date',
            new_name='Date_and_Time',
        ),
        migrations.RenameField(
            model_name='temperature',
            old_name='id_sensor',
            new_name='SensorID',
        ),
        migrations.RenameField(
            model_name='temperature',
            old_name='value',
            new_name='Value',
        ),
        migrations.RemoveField(
            model_name='humidity',
            name='name',
        ),
        migrations.RemoveField(
            model_name='temperature',
            name='name',
        ),
    ]