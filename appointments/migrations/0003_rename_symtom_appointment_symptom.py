# Generated by Django 5.0.7 on 2024-10-06 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_alter_appointment_appointment_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='symtom',
            new_name='symptom',
        ),
    ]
