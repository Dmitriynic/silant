# Generated by Django 4.1.6 on 2023-02-21 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_alter_car_drive_axle_model_alter_car_engine_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='drive_axle_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.driveaxlemodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.enginemodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='steerable_bridge_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.steerablebridgemodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='technique_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.techniquemodel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.transmissionmodel'),
        ),
    ]
