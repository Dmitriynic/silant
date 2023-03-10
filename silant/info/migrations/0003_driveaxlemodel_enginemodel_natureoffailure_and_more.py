# Generated by Django 4.1.6 on 2023-02-20 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_directory2_alter_directory_feature_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriveAxleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NatureOfFailure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SteerableBridgeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TechniqueModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.car'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.car'),
        ),
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
        migrations.AlterField(
            model_name='complaint',
            name='order_note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.natureoffailure'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='recovery_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.recoverymethod'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.typeofmaintenance'),
        ),
        migrations.DeleteModel(
            name='Directory',
        ),
        migrations.DeleteModel(
            name='Directory2',
        ),
    ]
