# Generated by Django 4.1.6 on 2023-02-21 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_maintenance_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='delivery_adress',
            new_name='delivery_address',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='engine_serial_driver',
            new_name='engine_serial_number',
        ),
    ]
