# Generated by Django 5.0.6 on 2024-05-21 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('established_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='car_images/')),
                ('petrol_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], default='Petrol', max_length=10)),
                ('car_type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Truck', 'Truck'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Hatchback', 'Hatchback'), ('Van', 'Van'), ('Wagon', 'Wagon')], default='Sedan', max_length=12)),
                ('gear_type', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=10)),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.brandmodel')),
            ],
        ),
        migrations.AddField(
            model_name='brandmodel',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.manufacturer'),
        ),
    ]