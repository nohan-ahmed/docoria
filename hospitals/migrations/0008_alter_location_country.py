# Generated by Django 5.0.7 on 2024-10-04 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('hospitals', '0007_alter_hospital_cover_img_alter_hospital_doctors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country'),
        ),
    ]
