# Generated by Django 5.0.7 on 2024-10-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_remove_department_slug'),
        ('doctors', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='doctors',
            field=models.ManyToManyField(blank=True, null=True, related_name='departments', to='doctors.doctor'),
        ),
        migrations.AlterField(
            model_name='department',
            name='staffs',
            field=models.ManyToManyField(blank=True, null=True, related_name='departments', to='staffs.staff'),
        ),
    ]
